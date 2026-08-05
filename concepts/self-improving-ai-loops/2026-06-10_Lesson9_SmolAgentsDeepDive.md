---
title: "Lesson 9 — SmolAgents Deep Dive: Code-First Agents from Hugging Face"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 9
tags: [smolagents, code-agents, huggingface, tool-calling, secure-execution]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 9: SmolAgents Deep Dive — Code-First Agents from Hugging Face



**Source**: [Original Article](http://localhost:11434)

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson1_ParadigmShift.md|Lesson 1 — The Paradigm Shift: From Prompting to Loops]] — 2 title terms overlap, 7 topic terms overlap, same area: home
- [[concepts/ai-foundations/ai-ml-foundations-lesson-13-agents-and-agentic-workflows.md|AI/ML Foundations Lesson 13 - Agents and Agentic Workflows]] — 2 title terms overlap, 7 topic terms overlap, same area: home
- [[concepts/ai-foundations/ai-ml-foundations-lesson-04-supervised-learning-learning-from-labels.md|AI/ML Foundations Lesson 04 - Supervised Learning: Learning from Labels]] — 2 title terms overlap, 7 topic terms overlap, same area: home

## Core Idea

**SmolAgents** is a Hugging Face library (~1,000 lines of code) that lets agents write their own actions as **Python code** instead of JSON tool calls. This is the key differentiator: code is a better language for expressing computer actions than JSON because it has composability, object management, generality, and representation in LLM training data.

> "We crafted our code languages specifically to express the actions performed by a computer. If JSON snippets were a better way, this package would have been written in JSON snippets."

## Architecture: CodeAgent vs ToolCallingAgent

SmolAgents provides two agent types based on how actions are specified:

### CodeAgent (Default) — Writes Actions as Python Code

The agent generates Python code snippets to perform actions and solve tasks. Code is executed in a local or sandboxed Python interpreter.

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(model_id="anthropic/claude-sonnet-4-20250514")
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

result = agent.run("Analyze this dataset and find correlations")
```

**Strengths:**
- **Highly expressive:** Complex logic, control flow, tool chaining, looping
- **Flexible:** No need to predefine every possible action — dynamically compose operations
- **Emergent reasoning:** Ideal for multi-step problems with dynamic logic
- **Object management:** Store tool outputs in variables, pass between steps naturally

**Limitations:**
- Risk of errors (syntax errors, exceptions in generated code)
- Less predictable — more prone to unexpected outputs
- Requires secure execution environment

### ToolCallingAgent — Writes Actions as JSON

The agent outputs structured JSON tool calls (OpenAI API format). No code execution — just structured tool invocations.

```python
from smolagents import ToolCallingAgent, WebSearchTool

agent = ToolCallingAgent(tools=[WebSearchTool()], model=model)
result = agent.run("Search for the latest AI research on LLM reasoning")
```

**Strengths:**
- **Reliable:** Less prone to hallucination, structured and validated output
- **Safe:** Arguments strictly validated, no arbitrary code execution
- **Interoperable:** Easy to map to external APIs or services

**Limitations:**
- **Low expressivity:** Can't combine or transform results dynamically
- **Inflexible:** Must define all possible actions in advance
- **No code synthesis:** Limited to predefined tool capabilities

### When to Use Which

| Use CodeAgent when... | Use ToolCallingAgent when... |
|----------------------|------------------------------|
| You need reasoning, chaining, or dynamic composition | You have simple, atomic tools (API calls, document fetches) |
| Tools are functions that can be combined | You want high reliability and clear validation |
| Your agent is a problem solver or programmer | Your agent is like a dispatcher or controller |
| You need complex logic or control flow | You need to map to external APIs |

## Installation and Setup

### Install with Toolkit

```bash
pip install "smolagents[toolkit]"
```

### Minimal Agent (3 Lines)

```python
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel()  # Free Hugging Face inference
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
result = agent.run("What is the 118th Fibonacci number?")
```

### Model Backend Options

SmolAgents is **model-agnostic** — supports any LLM through multiple backends:

#### Hugging Face Inference Providers (Free)

```python
from smolagents import CodeAgent, InferenceClientModel

model = InferenceClientModel(
    model_id="meta-llama/Llama-4-Scout-256B",
    provider="together",  # or "sambanova", "hyperbolic", etc.
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

#### LiteLLM (100+ Providers)

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="anthropic/claude-sonnet-4-20250514",
    api_key=os.environ["ANTHROPIC_API_KEY"],
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

#### Ollama (Self-Hosted)

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/llama3.3",
    api_base="http://localhost:11434",
    api_key="YOUR_API_KEY",
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

#### LM Studio (Self-Hosted, Preferred)

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="lmstudio-community/Meta-Llama-3.3-70B-Instruct-Q4_K_M",
    api_base="http://localhost:1234",  # LM Studio default port
    api_key="lm-studio",  # LM Studio accepts any API key
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

#### transformers (Local GPU)

```python
from smolagents import CodeAgent, TransformersModel

model = TransformersModel(
    model_id="meta-llama/Llama-4-Scout-256B",
    max_new_tokens=4096,
    device_map="auto",
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

#### Azure OpenAI

```python
from smolagents import CodeAgent, AzureOpenAIModel

model = AzureOpenAIModel(
    model_id=os.environ["AZURE_OPENAI_MODEL"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
```

## Tools System

### Creating a Custom Tool

A tool is a class that wraps a function with metadata (name, description, input types, output type):

```python
from smolagents import Tool

class WeatherTool(Tool):
    name = "get_weather"
    description = "Returns current weather for a location."
    inputs = {
        "location": {
            "type": "string",
            "description": "City name, e.g. 'Paris, France'",
        },
        "unit": {
            "type": "string",
            "description": "Temperature unit: 'celsius' or 'fahrenheit'",
        },
    }
    output_type = "string"

    def forward(self, location: str, unit: str = "celsius") -> str:
        # Call your weather API here
        return f"Weather in {location}: 22°C, clear skies"

weather_tool = WeatherTool()
```

### The `@tool` Decorator (Simple Tools)

For simple tools, use the decorator — it auto-generates the class:

```python
from smolagents import tool

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web and return results.
    
    Args:
        query: The search query string.
        max_results: Maximum number of results to return (default 5).
    """
    import requests
    results = requests.get(f"https://html.duckduckgo.com/html/?q={query}").text
    return results[:2000]  # Truncate for context
```

### Sharing Tools to the Hub

```python
# Push to Hugging Face Hub
weather_tool.push_to_hub("your-username/weather-tool", token="YOUR_HF_TOKEN")

# Load from Hub (trust remote code — only load from trusted sources)
from smolagents import load_tool
loaded_tool = load_tool("your-username/weather-tool", trust_remote_code=True)
```

### Using MCP Server Tools

```python
from smolagents import MCPClient, CodeAgent
from mcp import StdioServerParameters

# Stdio-based MCP server
server_params = StdioServerParameters(
    command="uvx",
    args=["--quiet", "pubmedmcp@0.1.3"],
)

with MCPClient(server_params) as tools:
    agent = CodeAgent(tools=tools, model=model, add_base_tools=True)
    agent.run("Find recent research on Alzheimer's treatments.")
```

## The ReAct Loop Internals

All agents in SmolAgents are built on the `MultiStepAgent` class, which implements the ReAct framework (Reason + Act):

```
Initialization:
  1. System prompt → SystemPromptStep
  2. User query → TaskStep

While loop (ReAct):
  1. agent.write_memory_to_messages() → LLM-readable chat messages
  2. Send to model → get completion
  3. Parse completion → action (code snippet for CodeAgent, JSON for ToolCallingAgent)
  4. Execute action → log result to memory (ActionStep)
  5. Run step_callbacks (optional hooks for logging, monitoring)
  6. Repeat until task complete or max_steps reached
```

### Optional Planning Step

Agents can run periodic planning steps (no tool calls, just reflection):

```python
agent = CodeAgent(
    tools=[search_tool, image_tool],
    model=model,
    planning_interval=3,  # Plan every 3 steps
)
```

## Memory Management

### Replay Agent Runs

```python
result = agent.run("What's the 20th Fibonacci number?")
agent.replay()  # Replay the last run in a UI
```

### Access Memory Programmatically

```python
# System prompt
print(agent.memory.system_prompt.system_prompt)

# First task
task_step = agent.memory.steps[0]
print(task_step.task)

# All action steps with errors
for step in agent.memory.steps:
    if hasattr(step, 'error') and step.error:
        print(f"Step {step.step_number} errored: {step.error}")
```

### Dynamic Memory Modification via Callbacks

```python
def update_screenshot(memory_step, agent):
    """Remove old screenshots to save tokens."""
    latest = memory_step.step_number
    for prev in agent.memory.steps:
        if prev.step_number <= latest - 2:
            prev.observations_images = None  # Remove old images
    # Take new screenshot
    png_bytes = driver.get_screenshot_as_png()
    memory_step.observations_images = [png_bytes]

agent = CodeAgent(
    tools=[WebSearchTool(), go_back, search_item],
    model=model,
    step_callbacks=[update_screenshot],
    max_steps=20,
)
```

### Run One Step at a Time

```python
agent = CodeAgent(tools=[], model=model, verbosity_level=1)
agent.python_executor.send_tools({**agent.tools})

task = "Calculate the sum of primes below 100"
agent.memory.steps.append(TaskStep(task=task, task_images=[]))

final_answer = None
step_number = 1
while final_answer is None and step_number <= 10:
    memory_step = ActionStep(step_number=step_number, observations_images=[])
    final_answer = agent.step(memory_step)
    agent.memory.steps.append(memory_step)
    step_number += 1
```

## Security: Code Execution Safeguards

### Local Executor (Default)

SmolAgents rebuilds a secure `LocalPythonExecutor` from scratch:

- **Imports disallowed by default** — only explicitly authorized modules
- **Submodule access forbidden** — `import numpy` works but `numpy.random` needs separate authorization
- **Operation count capped** — prevents infinite loops
- **Only defined operations allowed** — undefined commands raise errors

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(model_id="anthropic/claude-sonnet-4-20250514")

# Authorize specific imports
agent = CodeAgent(
    tools=[],
    model=model,
    additional_authorized_imports=["requests", "bs4", "numpy"],
)
```

### Sandbox Execution Options

| Executor | Security | Setup Cost | Use Case |
|----------|----------|-----------|----------|
| **Local (default)** | Medium | None | Dev, trusted code |
| **Docker** | High | Docker installed | Production, untrusted code |
| **E2B** | High | API key | Cloud sandbox |
| **Blaxel** | High | API key + workspace | Cloud sandbox |
| **Modal** | High | API key | Cloud sandbox |

```python
# Docker sandbox
agent = CodeAgent(
    tools=[],
    model=model,
    executor_type="docker",  # Runs in Docker container
)

# E2B sandbox
agent = CodeAgent(
    tools=[],
    model=model,
    executor_type="e2b",  # Runs in E2B cloud sandbox
)
```

## Best Practices for Building Good Agents

### 1. Simplify the Workflow

> "The best agentic systems are the simplest."

- Reduce LLM calls as much as possible
- Group tools into unified functions (e.g., `get_spot_information()` calls both weather and distance APIs)
- Use deterministic logic instead of agentic decisions where possible

### 2. Improve Information Flow to the LLM

The LLM is like an intelligent robot trapped in a room — it only knows what you tell it.

- Make the task description crystal clear
- Log everything useful inside tools (especially errors)
- Provide detailed tool descriptions with input/output format examples

### 3. Use a Stronger LLM

> "In an agentic workflow, some errors are actual bugs, others are the LLM not reasoning properly."

- First debugging step: use a more powerful model
- Qwen2/5-72B, Llama 4 Scout, or Claude Sonnet 4 handle complex agentic tasks much better than smaller models

### 4. Provide Detailed Instructions

```python
agent = CodeAgent(
    tools=[search_tool, weather_tool],
    model=model,
    instructions="Always verify weather data with at least two sources before returning results.",
)
```

### 5. Use Planning for Complex Tasks

```python
agent = CodeAgent(
    tools=[search_tool, image_tool, db_query_tool],
    model=model,
    planning_interval=3,  # Agent reflects and replans every 3 steps
)
```

## CLI Interface

SmolAgents includes a CLI for quick agent runs:

```bash
# Run with direct prompt
smolagent "Plan a trip to Tokyo and Kyoto" \
  --model-type "InferenceClientModel" \
  --model-id "Qwen/Qwen3-Next-80B-A3B-Thinking" \
  --imports "pandas numpy" \
  --tools "web_search"

# Interactive mode (launches setup wizard)
smolagent
```

## Comparison with Other Frameworks

| Feature | SmolAgents | LangGraph | OpenDevin | Aider |
|---------|-----------|-----------|-----------|-------|
| **Code-first actions** | ✅ Yes | ❌ JSON/nodes | ✅ Yes | ✅ Yes |
| **Lines of code** | ~1,000 | 10,000+ | 50,000+ | 5,000+ |
| **Learning curve** | Low | Medium | High | Low |
| **Model flexibility** | 100+ via LiteLLM | 100+ via LiteLLM | 100+ via LiteLLM | 100+ via LiteLLM |
| **Sandboxed execution** | ✅ Docker/E2B/Blaxel | ❌ No | ✅ Browser-based | ❌ No |
| **Hub integration** | ✅ Push/pull tools & agents | ❌ No | ❌ No | ❌ No |
| **MCP support** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Self-correcting** | ✅ Planning steps | ✅ langgraph-reflection | ✅ Built-in | ✅ Skill-based |
| **Best for** | Minimalist code agents | Production workflows | Full-stack dev | CLI pair programming |

## When to Use SmolAgents

### Choose SmolAgents when:
- You want minimal abstraction (~1,000 lines vs 10,000+ in LangGraph)
- Code-first actions suit your use case (coding, data analysis, research)
- You need to share tools/agents to the Hugging Face Hub
- You want sandboxed code execution (Docker/E2B/Blaxel)
- You prefer full control over the loop logic
- You're building agents that write and execute their own code

### Choose LangGraph when:
- You need explicit state management with graphs
- Production workflows with visual debugging
- You need `langgraph-reflection` for self-correction
- Your team needs a visual workflow builder

### Choose OpenDevin when:
- Building full-stack applications autonomously
- You need browser automation + test-driven execution
- The task is a complex multi-step coding project

### Choose Aider when:
- You prefer CLI over GUI
- Working with local LLMs for coding
- You want skill-based self-improvement

## Key Takeaway

SmolAgents is the minimalist code-first agent library. It's ~1,000 lines of code, supports any LLM via LiteLLM, has built-in sandboxed execution, and lets you share tools/agents to the Hub. Use CodeAgent when you need expressive, dynamic logic. Use ToolCallingAgent when you need reliability and structured output. The model matters less than the feedback loop — SmolAgents gives you the simplest path to build that loop.

## Related Concepts
- [[Self-Improving AI Loops]]
- [[Harness Engineering]]
- [[Feedback Loop Engineering]]
- [[Agent Frameworks]]
- [[Model Version Brittleness]]
