---
title: Tutorial -- How to Build an AI Agent Framework from Scratch
date: 2026-06-08
type: tutorial
tags: [agent-framework, implementation, tutorial, harness, agentic-loop, tool-design]
---

# Tutorial: Building an AI Agent Framework from Scratch

This tutorial walks through designing and implementing an agent framework -- the infrastructure that wraps an LLM and lets it act autonomously. We draw on Anthropic's "Building Effective Agents" research, the "Code as Agent Harness" survey, the "Is Grep All You Need?" study, and practical patterns from AutoGen, CrewAI, LangGraph, and DSPy.

---

## 1. What You Are Building

An agent framework is the **harness** around a language model. It manages:

- The agentic query loop (the runtime core)
- Context assembly and compaction
- Tool discovery, definition, and dispatch
- Permission gates and safety checks
- Memory (short-term and long-term)
- Stopping conditions and error recovery
- Logging and observability

The key insight from recent research: **the harness matters as much as the model**. A good prompt alone is not enough; the execution environment, safety model, context policy, and recovery strategy are equally important.

---

## 2. Understanding the Agentic Query Loop

The agentic query loop is the runtime core of every agent. It is a simple ReAct-style while-loop:

```
while not stopped:
    context = assemble_context()
    response = model.call(context)
    if response contains tool calls:
        results = execute_tools(response.tools)
        context = append(context, results)
    else:
        return response
```

The loop itself is not the hard part. The hard part is making it reliable under:

- **Token pressure** -- the conversation grows; you must compact context before each call
- **Tool failures** -- tools can error, timeout, or return unexpected output
- **Permission constraints** -- not all tool calls should be allowed unconditionally
- **Infinite loops** -- the model can get stuck retrying the same failed action

### Stopping Conditions

Define clear rules for when the loop ends:

- No more tool calls in the response (model says it is done)
- Maximum iteration count reached (safety limit)
- Context window overflow (force stop and compact)
- Explicit abort signal from user or system
- Tool execution returns a "terminal" result (e.g., file written, API call succeeded)

---

## 3. The Building Blocks

### 3.1 The Augmented LLM

Every agent starts with an LLM enhanced with three capabilities:

1. **Retrieval** -- the ability to pull relevant information from outside the model's training data (RAG, search, file read)
2. **Tools** -- the ability to call external functions (code execution, API calls, file operations)
3. **Memory** -- the ability to retain information across turns

These are not optional extras. They are the foundation. Without them, you have a chatbot, not an agent.

### 3.2 Tool Design (Agent-Computer Interface)

Tools are your agent's hands. Poor tool design is the most common cause of agent failure.

**Tool definition structure:**

```python
class Tool:
    name: str           # unique identifier
    description: str    # what the tool does (model reads this to decide when to use it)
    parameters: dict    # JSON Schema defining required/optional arguments
    examples: list      # example invocations (helps model understand usage)
    edge_cases: list    # when NOT to use this tool
    return_format: str  # how results are returned (text, JSON, file path, etc.)
```

**Tool design principles:**

- Give the model enough tokens to "think" before it writes itself into a corner
- Keep the format close to what the model has seen naturally on the internet
- Avoid formatting overhead (no manual line counting, no complex string escaping)
- Put yourself in the model's shoes -- is it obvious how to use this tool?
- Poka-yoke your tools -- make it harder to make mistakes (e.g., require absolute paths over relative)
- Test how the model uses your tools; iterate on mistakes

### 3.3 Memory Architecture

Agents need two types of memory:

**Short-term (working memory):**
- Current plan and task list
- Recent tool results
- Conversation history (compacted, not raw)
- Current state of the task

**Long-term (persistent memory):**
- User preferences and style
- Past task outcomes and lessons learned
- Knowledge base entries
- Configuration and context that persists across sessions

Memory management is a core engineering challenge. The model's context window is limited; you must decide what to keep, what to summarize, and what to discard.

---

## 4. Workflow Patterns

Before building an autonomous agent, consider whether a simpler workflow pattern suffices. Anthropic identifies five patterns, ordered by complexity:

### 4.1 Prompt Chaining (Simplest)

Decompose a task into a fixed sequence of LLM calls. Each call processes the output of the previous one.

```
Step 1: LLM generates outline
    -> Gate: validate outline meets criteria
Step 2: LLM writes document from outline
    -> Gate: validate document completeness
Step 3: LLM reviews and revises
```

**When to use:** Tasks that can be cleanly decomposed into fixed subtasks. Trade latency for accuracy.

### 4.2 Routing

Classify input and direct to specialized followup.

```
Input -> Classifier -> Specialized Prompt A
          -> Specialized Prompt B
          -> Specialized Prompt C
```

**When to use:** Complex tasks with distinct categories that are better handled separately.

### 4.3 Parallelization

Run independent subtasks in parallel, then aggregate results.

```
Subtask A --\
Subtask B --- -> Aggregate -> Final Output
Subtask C --/
```

**When to use:** Speed (sectioning) or confidence (voting). For complex tasks, separate LLM calls perform better than one call handling everything.

### 4.4 Orchestrator-Workers

A central LLM dynamically breaks down tasks, delegates to workers, and synthesizes results.

```
Orchestrator LLM
    -> Worker A: Task X
    -> Worker B: Task Y
    -> Worker C: Task Z
    <- Synthesize results <-
```

**When to use:** Complex tasks where you cannot predict the subtasks needed. Flexibility over pre-defined paths.

### 4.5 Evaluator-Optimizer (Most Complex)

One LLM generates a response; another evaluates and provides feedback in a loop.

```
Generator -> Output -> Evaluator -> Feedback -> Generator -> ...
```

**When to use:** Clear evaluation criteria + measurable improvement from iteration. Analogous to a human writer's revision process.

---

## 5. Building the Framework

### 5.1 Project Structure

```
agent-framework/
├── core/
│   ├── agent.py          # Main agent class with query loop
│   ├── context.py        # Context assembly and compaction
│   ├── memory.py         # Short-term and long-term memory
│   └── harness.py        # Safety, permissions, logging
├── tools/
│   ├── registry.py       # Tool registration and discovery
│   ├── base.py           # Base tool class
│   └── builtins/         # Built-in tools
│       ├── file_ops.py
│       ├── code_exec.py
│       ├── search.py
│       └── web.py
├── workflows/
│   ├── chaining.py       # Prompt chaining workflow
│   ├── routing.py        # Routing workflow
│   ├── parallel.py       # Parallelization workflow
│   ├── orchestrator.py   # Orchestrator-workers workflow
│   └── evaluator.py      # Evaluator-optimizer workflow
├── models/
│   ├── base.py           # Model interface
│   └── providers/        # Provider implementations
│       ├── anthropic.py
│       ├── openai.py
│       └── local.py
├── config.yaml           # Agent configuration
└── tests/
    ├── test_agent.py
    ├── test_tools.py
    └── test_workflows.py
```

### 5.2 Core Agent Implementation

The agent class is the entry point. It manages the query loop:

```python
class Agent:
    def __init__(self, config):
        self.model = ModelProvider(config.model)
        self.tools = ToolRegistry(config.tools)
        self.memory = MemoryManager(config.memory)
        self.harness = AgentHarness(config.safety)
        self.context = ContextManager(config.context)
        self.max_iterations = config.max_iterations
        self.callbacks = config.callbacks

    def run(self, goal: str) -> str:
        """Main entry point: run the agentic query loop."""
        iteration = 0
        self.context.add({"role": "user", "content": goal})

        while iteration < self.max_iterations:
            iteration += 1

            # 1. Assemble and compact context
            context = self.context.assemble()

            # 2. Check stopping conditions
            if self._should_stop(context):
                break

            # 3. Get model response
            response = self.model.generate(
                messages=context.messages,
                tools=self.tools.get_definitions(),
            )

            # 4. Process response
            if response.tool_calls:
                results = self._execute_tools(response.tool_calls)
                self.context.add_tool_results(results)
            else:
                # No more tool calls -- model is done
                return response.content

        return self._handle_timeout()

    def _execute_tools(self, tool_calls):
        """Execute tool calls with safety checks."""
        results = []
        for call in tool_calls:
            # Safety: check permissions
            if not self.harness.check_permission(call.tool_name, call.args):
                results.append({
                    "tool": call.tool_name,
                    "result": "PERMISSION_DENIED",
                    "error": "Tool call was blocked by safety policy"
                })
                continue

            # Execute the tool
            try:
                result = self.tools.execute(call.tool_name, call.args)
                results.append({
                    "tool": call.tool_name,
                    "result": result,
                    "error": None
                })
            except Exception as e:
                results.append({
                    "tool": call.tool_name,
                    "result": None,
                    "error": str(e)
                })
        return results
```

### 5.3 Tool Registry

The tool registry manages tool discovery and execution:

```python
class ToolRegistry:
    def __init__(self):
        self._tools = {}

    def register(self, tool: Tool):
        self._tools[tool.name] = tool

    def get_definitions(self) -> list:
        """Return JSON Schema definitions for all tools (for the LLM)."""
        return [tool.to_openai_format() for tool in self._tools.values()]

    def execute(self, name: str, args: dict) -> str:
        """Execute a tool by name."""
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")
        return self._tools[name].execute(args)

    def list_available(self) -> list:
        """Return list of available tool names and descriptions."""
        return [f"{t.name}: {t.description}" for t in self._tools.values()]
```

### 5.4 Context Management

Context management is critical. The conversation grows with each iteration; you must compact it before it exceeds the model's context window.

```python
class ContextManager:
    def __init__(self, max_tokens, compaction_threshold):
        self.max_tokens = max_tokens
        self.compaction_threshold = compaction_threshold
        self.messages = []
        self.working_memory = {}  # Short-term: plan, state, notes

    def add(self, message: dict):
        self.messages.append(message)
        self._maybe_compact()

    def add_tool_results(self, results: list):
        for r in results:
            content = f"Tool: {r['tool']}\nResult: {r['result']}\n"
            if r['error']:
                content += f"Error: {r['error']}\n"
            self.add({"role": "assistant", "content": content})

    def assemble(self) -> dict:
        """Return context ready for model call."""
        return {
            "messages": self.messages,
            "working_memory": self.working_memory,
            "available_tools": self._get_tool_list(),
        }

    def _maybe_compact(self):
        """Compact context if approaching token limit."""
        current_tokens = self._count_tokens()
        if current_tokens > self.compaction_threshold:
            self._compact()

    def _compact(self):
        """Summarize older messages to free tokens."""
        # Strategy: keep recent messages, summarize older ones
        # This is where you implement your compaction strategy
        pass
```

### 5.5 Safety Harness

The safety harness is what makes the difference between a demo and a reliable product:

```python
class AgentHarness:
    def __init__(self, config):
        self.permissions = config.permissions  # {tool_name: allowed}
        self.sandbox = config.sandbox           # Whether to sandbox execution
        self.approval_required = config.approval  # List of tools requiring approval
        self.audit_log = []

    def check_permission(self, tool_name: str, args: dict) -> bool:
        """Check if this tool call is allowed."""
        if tool_name in self.approval_required:
            # Require human approval
            return self._request_approval(tool_name, args)

        if tool_name not in self.permissions:
            return False

        return self.permissions[tool_name]

    def log_action(self, action: dict):
        """Log all agent actions for audit."""
        self.audit_log.append({
            "timestamp": datetime.now().isoformat(),
            **action
        })

    def _request_approval(self, tool_name, args):
        # This would interface with a human approval system
        # For now, return False (block)
        return False
```

---

## 6. Workflow Implementations

### 6.1 Prompt Chaining

```python
class PromptChainingWorkflow:
    def __init__(self, steps: list):
        """
        steps: list of {
            "prompt": str,
            "tools": [tool_names],
            "gate": callable,  # validation function
            "model": str,      # which model to use
        }
        """
        self.steps = steps
        self.state = {}

    def run(self, initial_input: str) -> str:
        current = initial_input
        for i, step in enumerate(self.steps):
            # Execute step
            result = self._execute_step(step, current)

            # Run gate (validation)
            if step.get("gate") and not step["gate"](result):
                raise ValueError(f"Gate failed at step {i}: {result}")

            self.state[f"step_{i}"] = result
            current = result

        return current

    def _execute_step(self, step, input_text):
        # Use the agent with specific tools and prompt
        agent = Agent(config={
            "model": step.get("model", "default"),
            "tools": step.get("tools", []),
        })
        return agent.run(f"{step['prompt']}\n\nInput: {input_text}")
```

### 6.2 Orchestrator-Workers

```python
class OrchestratorWorkflow:
    def __init__(self, orchestrator_agent, worker_templates):
        self.orchestrator = orchestrator_agent
        self.worker_templates = worker_templates  # {name: agent_config}

    def run(self, task: str) -> str:
        # Step 1: Orchestrator decomposes the task
        plan = self.orchestrator.run(
            f"Break this task into subtasks and return a JSON plan:\n{task}"
        )

        # Step 2: Execute subtasks (in parallel if independent)
        results = self._execute_plan(plan, task)

        # Step 3: Synthesize results
        final = self.orchestrator.run(
            f"Synthesize these results into a final answer:\n{results}"
        )

        return final

    def _execute_plan(self, plan, original_task):
        # Parse plan JSON, execute workers, handle dependencies
        pass
```

---

## 7. Framework Selection Guide

| Need | Recommended Approach |
|------|---------------------|
| Simple tool use | Direct API calls + custom loop |
| Prompt chaining | Custom workflow (see 6.1) |
| Multi-agent conversation | AutoGen |
| Role-based multi-agent | CrewAI |
| Stateful graph workflows | LangGraph |
| Declarative LLM programs | DSPy |
| Quick prototype | Claude Agent SDK or Strands SDK |
| Production system | Custom harness with direct API calls |

**Key takeaway from Anthropic:** Start with direct API calls. Many patterns can be implemented in a few lines of code. Use frameworks only when you understand their internals and need their specific features.

---

## 8. Common Pitfalls

### 8.1 Tool Design Mistakes

- **Relative paths** -- models lose track of directory context. Always require absolute paths.
- **Complex formats** -- JSON-escaped code, line-counted diffs, custom serialization. These add overhead the model must handle.
- **Poor descriptions** -- the model can only use tools it understands. Tool descriptions are as important as the tool code itself.
- **Too many tools** -- models perform better with fewer, well-documented tools. Group related operations.

### 8.2 Context Management Mistakes

- **No compaction** -- the context grows unbounded until it overflows. Implement proactive compaction.
- **Lost working memory** -- the model forgets its own plan. Inject working memory into the prompt each iteration.
- **Over-summarization** -- compaction loses critical details. Summarize selectively, keeping tool results intact.

### 8.3 Safety Mistakes

- **No permission gates** -- the model can call any tool without restriction. Implement per-tool permissions.
- **No audit logging** -- you cannot debug what you cannot see. Log every tool call and result.
- **No approval workflow** -- destructive actions (delete, send, publish) should require human approval.
- **No timeout** -- agents can run forever. Set max iterations and time limits.

### 8.4 Architecture Mistakes

- **Over-engineering** -- start with the simplest pattern that works. Add complexity only when needed.
- **Framework lock-in** -- frameworks add abstraction layers that make debugging harder. Understand what's under the hood.
- **No evaluation** -- without measuring performance, you cannot know if changes improve or degrade the system.
- **Ignoring the ACI** -- spending more time on the prompt than on tool design is backwards. The tool interface is the agent's primary interaction surface.

---

## 9. Evaluation and Testing

### 9.1 What to Measure

- **Task success rate** -- does the agent complete the goal?
- **Tool usage accuracy** -- does it call the right tools with correct arguments?
- **Iteration count** -- how many turns does it take? (efficiency)
- **Error rate** -- how often does it hit tool failures or permission blocks?
- **Latency and cost** -- time and token usage per task
- **Human approval rate** -- how often does it need human intervention?

### 9.2 Testing Strategy

```
Unit tests:
  - Tool execution (mocked)
  - Context compaction
  - Permission checks
  - Stopping conditions

Integration tests:
  - Agent with real model calls (sandboxed)
  - Workflow patterns end-to-end
  - Tool interaction sequences

E2E tests:
  - Real tasks with evaluation criteria
  - Compare against human baseline
  - Measure success rate, cost, latency
```

---

## 10. Putting It All Together

Here is a minimal working agent:

```python
# agent.py
import json
from anthropic import Anthropic

class SimpleAgent:
    def __init__(self, api_key, model="claude-sonnet-4-20250514"):
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.messages = []
        self.tools = []
        self.max_iterations = 20

    def add_tool(self, name, description, parameters):
        self.tools.append({
            "name": name,
            "description": description,
            "input_schema": parameters,
        })

    def run(self, goal):
        self.messages = [{"role": "user", "content": goal}]

        for i in range(self.max_iterations):
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=self.messages,
                tools=self.tools,
            )

            # Check for tool use
            if response.stop_reason == "tool_use":
                for block in response.content:
                    if block.type == "tool_use":
                        # Execute the tool
                        result = self._execute_tool(block.name, block.input)

                        # Add to conversation
                        self.messages.append({
                            "role": "assistant",
                            "content": [block],
                        })
                        self.messages.append({
                            "role": "user",
                            "content": [
                                {
                                    "type": "tool_result",
                                    "tool_use_id": block.id,
                                    "content": result,
                                }
                            ],
                        })
            else:
                # Agent is done
                return response.content[0].text

        return "Max iterations reached"

    def _execute_tool(self, name, args):
        # Route to appropriate handler
        if name == "read_file":
            with open(args["path"], "r") as f:
                return f.read()
        elif name == "write_file":
            with open(args["path"], "w") as f:
                f.write(args["content"])
            return f"Written {len(args['content'])} bytes to {args['path']}"
        elif name == "run_code":
            import subprocess
            result = subprocess.run(
                ["python", "-c", args["code"]],
                capture_output=True, text=True, timeout=30
            )
            return f"stdout: {result.stdout}\nstderr: {result.stderr}"
        else:
            return f"Unknown tool: {name}"


# usage.py
agent = SimpleAgent(api_key="sk-ant-...")

# Define tools
agent.add_tool(
    name="read_file",
    description="Read the contents of a file",
    parameters={
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Absolute file path"},
        },
        "required": ["path"],
    },
)

agent.add_tool(
    name="write_file",
    description="Write content to a file. Creates the file if it does not exist.",
    parameters={
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Absolute file path"},
            "content": {"type": "string", "description": "File content"},
        },
        "required": ["path", "content"],
    },
)

agent.add_tool(
    name="run_code",
    description="Execute Python code and return the output",
    parameters={
        "type": "object",
        "properties": {
            "code": {"type": "string", "description": "Python code to execute"},
        },
        "required": ["code"],
    },
)

# Run the agent
result = agent.run(
    "Read the file /tmp/data.csv, count the number of rows, "
    "write a summary to /tmp/summary.txt, and tell me how many rows there are."
)
print(result)
```

---

## 11. Scaling Up

Once you have a working agent, consider these improvements:

1. **Multi-agent coordination** -- split complex tasks into specialized agents
2. **Persistent memory** -- store and retrieve knowledge across sessions
3. **Better context compaction** -- summarize older messages while preserving key information
4. **Human-in-the-loop** -- approval gates for sensitive actions
5. **Observability** -- structured logging, tracing, and metrics
6. **Evaluation harness** -- automated testing against benchmarks
7. **Plugin system** -- allow third-party tools without modifying core code

---

## 12. Key Takeaways

- The harness is as important as the model -- invest equally in both
- Start with the simplest pattern that works; add complexity only when needed
- Tool design (ACI) deserves as much effort as prompt engineering
- Memory management is a core engineering challenge, not an afterthought
- Safety, permissions, and audit logging are non-negotiable for production agents
- Measure everything -- you cannot improve what you do not measure
- Frameworks can help you start, but understand what's under the hood
- Agents add value for open-ended, multi-step tasks; workflows are better for predictable sequences

---

## Cross-References

- [[2026-06-08_BuildingEffectiveAgents_Anthropic]] -- Anthropic's principles and patterns
- [[2026-05-09_AutonomousAgentFrameworks]] -- Framework comparison (AutoGen, CrewAI, LangGraph, DSPy)
- [[2026-05-09_AgentArchitectureEvolution]] -- Architecture timeline (CoT -> ReAct -> Multi-Agent)
- [[Code as Agent Harness paper]] (2605.18747) -- Code as the operational substrate for agents
- [[Is Grep All You Need?]] (2605.15184) -- How retrieval strategy interacts with agent architecture
- Lesson 13: Agents and Agentic Workflows -- Concept-first overview for learners
