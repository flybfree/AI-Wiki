---
title: "Lesson 4 — Agent Frameworks: The Loop Engine"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 4
tags: [agent-frameworks, smolagents, langgraph, openhands, aider]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 4: Agent Frameworks — The Loop Engine



**Source**: [Original Article](http://localhost:4000/v1)
## Core Idea

Agent frameworks are the engines that run your loops. They handle the ReAct cycle (Reasoning → Acting → Observing), manage tool calls, and orchestrate the feedback loop. Each framework has a different philosophy — pick based on your use case.

## Framework Comparison

### SmolAgents (Hugging Face)
**Philosophy:** Minimal abstractions, code-first.
**Definition:** A minimalist agent library (~1,000 lines of code) where the agent writes its actions as code rather than tool calls.

**Key feature:** CodeAgent pattern — the agent writes Python code to perform actions instead of calling predefined tools. This is more flexible than tool-calling because the agent can compose operations dynamically.

```python
from smolagents import CodeAgent, HfApiModel

model = HfApiModel(model_id="meta-llama/Llama-4-Scout-256B")
agent = CodeAgent(
    tools=[],  # Start empty, agent writes its own code
    model=model,
    max_steps=10
)

result = agent.run("Analyze this dataset and find correlations")
```

**Best for:** Minimalist setups, developers who want full control, first-class code execution
**Self-hosted:** Yes, works with any OpenAI-compatible model via LiteLLM
**Pros:**
- ~1K lines of code — easy to understand and modify
- First-class code execution — agent writes and runs code
- Simple API, minimal abstraction overhead

**Cons:**
- Less built-in orchestration than LangGraph
- No visual workflow builder
- You manage the loop yourself

### LangGraph
**Philosophy:** State machine with explicit cycles.
**Definition:** A library for building stateful, multi-part applications with LLMs using directed graphs. Agents are nodes, transitions are edges, and loops are explicit cycles in the graph.

**Key feature:** `langgraph-reflection` package encodes self-correcting loops explicitly:
1. Main agent runs
2. Judge node runs a structured check
3. Graph loops until the judge returns nothing to critique

```python
from langgraph.graph import StateGraph, START, END
from langgraph_reflection import ReflectionNode

# Define the graph
workflow = StateGraph(AgentState)

# Agent node: does the work
workflow.add_node("agent", run_agent)

# Judge node: checks the work
workflow.add_node("judge", ReflectionNode())

# Cycle: agent → judge → agent (if judge finds issues)
workflow.add_conditional_edges(
    "judge",
    lambda state: "agent" if state.needs_fix else "end",
    {"agent": "agent", "end": END}
)

workflow.add_edge(START, "agent")
graph = workflow.compile()
```

**Best for:** Self-correcting loops, production workflows, explicit state management
**Self-hosted:** Yes, works with any model via LiteLLM
**Pros:**
- Explicit state management — you see exactly what the agent does
- `langgraph-reflection` for built-in self-correction
- Production-ready with observability
- Visual graph debugging

**Cons:**
- Steeper learning curve
- More code to set up
- Graph debugging can be complex

### OpenDevin / OpenHands
**Philosophy:** Autonomous coding agent.
**Definition:** An open-source platform for autonomous developer agents that can build full-stack applications.

**Key features:**
- Browser automation via Puppeteer
- Test-driven execution
- Git-aware context (reads git history, commits progress)
- Full-stack web app development

```bash
# Run OpenDevin in Docker
docker run -it -p 3000:3000 \
  -e LLM_API_KEY=sk-xxx \
  -e LLM_BASE_URL=http://localhost:4000/v1 \
  openhands/openhands
```

**Best for:** Full-stack development, complex multi-step projects, autonomous coding
**Self-hosted:** Yes, Docker-based
**Pros:**
- Full-stack agent with browser automation
- Git-aware — reads commit history, leaves progress notes
- Test-driven execution built in
- Production use cases (building real apps)

**Cons:**
- Heavy — requires Docker, significant resources
- More complex to configure
- Focused on coding (not general agentic tasks)

### Aider
**Philosophy:** CLI pair programming with local LLMs.
**Definition:** A CLI tool that lets you pair program with AI using local or cloud models. Git-aware, skill-based self-improvement.

**Key feature:** Skill-based self-improvement — agents update their own skills after runs. Aider agents read and write skill files that improve their behavior over time.

```bash
# Use Aider with local model via LiteLLM
export OPENAI_API_KEY=anything
export OPENAI_BASE_URL=http://localhost:4000/v1

aider --model openai/my-agent \
  --file doc/tickets/001.md \
  --yes-always \
  --commit-message "implement ticket"
```

**Best for:** CLI-first developers, local LLM coding, iterative improvement
**Self-hosted:** Yes, works with any OpenAI-compatible API
**Pros:**
- Simple CLI, no Docker needed
- Git-aware context
- Skill-based self-improvement
- Works great with Ralph loops

**Cons:**
- CLI-only (no GUI)
- Focused on coding (not general tasks)
- Less orchestration than LangGraph

## Pattern Comparison Matrix

| Framework | Loop Pattern | Best For | Learning Curve | Self-Hosted |
|-----------|-------------|----------|---------------|-------------|
| **SmolAgents** | CodeAgent writes code | Minimalist, full control | Low | Yes |
| **LangGraph** | State machine with cycles | Self-correcting loops, production | Medium | Yes |
| **OpenDevin** | Autonomous coding | Full-stack dev, complex projects | High | Yes |
| **Aider** | CLI pair programming | Local LLM coding, iterative | Low | Yes |
| **Ralph Loop** | `while true` bash loop | Simplest possible loop | None | Yes |

## When to Use Which

### Use SmolAgents when:
- You want minimal abstraction
- The agent needs to write and execute its own code dynamically
- You're comfortable managing the loop yourself

### Use LangGraph when:
- You need explicit self-correction (agent → judge → agent loop)
- Production workflows with observability
- Complex state management across multiple steps

### Use OpenDevin when:
- Building full-stack applications autonomously
- You need browser automation + test-driven execution
- The task is a complex multi-step coding project

### Use Aider when:
- You prefer CLI over GUI
- Working with local LLMs for coding
- You want skill-based self-improvement

### Use a Ralph Loop when:
- The task is simple and repetitive
- You want the simplest possible implementation
- You don't need complex state management

## The Ralph Loop: Still the Simplest Option

For many use cases, you don't need a framework at all:

```bash
#!/bin/bash
# Ralph loop with Aider + local LLM
export OPENAI_API_KEY=anything
export OPENAI_BASE_URL=http://localhost:4000/v1

while true; do
  aider --model openai/my-agent \
    --file doc/tickets/$(ls doc/tickets/ | head -1) \
    --yes-always \
    --no-auto-commit \
    --commit-message "implement ticket"
  
  if pytest tests/ -q; then
    mv doc/tickets/$(ls doc/tickets/ | head -1) doc/tickets/done/
    echo "✓ Ticket done"
  else
    echo "✗ Tests failed, retrying..."
    sleep 5
  fi
done
```

## Key Takeaway

Start with a Ralph loop (bash `while true`). When you need explicit state management, move to LangGraph. When you need code execution, use SmolAgents. When you're building full-stack apps, use OpenDevin. When you're coding locally, use Aider. The framework is less important than the feedback loop it enables.

## Related Concepts
- [[Self-Improving AI Loops]]
- [[Ralph Loops]]
- [[Feedback Loop Engineering]]
