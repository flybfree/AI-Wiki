title: Agent Architecture Evolution (ReAct → ToT → Reflexion → Multi-Agent)
date: 2026-05-09
tags: [agent-architecture, evolution, prompting-patterns, reasoning-patterns, tool-use, agentic]

# Agent Architecture Evolution

This entry maps the full evolution of agent reasoning architectures, from early single-pass approaches through modern multi-step, tool-using, self-reflecting workflows.

## Architecture Timeline

### 1. Single-Pass Reasoning (2022)

**CoT **(Chain of Thought, Wei et al.)
- Input reasoning steps into prompt as few-shot examples
- LLMs follow these steps to produce final answer
- Requires manual prompt engineering

**Zero-shot-CoT **(Kojima, 2022)
- Uses trigger sentences like "think step by step"
- No manual prompt engineering of examples
- Less accurate than few-shot CoT

### 2. Multi-Reasoning: Tree + Graph (2023)

**ToT — Tree of Thoughts **(Yao et al., 2023)
- Generates plans using tree-like reasoning structure
- Each node = intermediate reasoning step
- Uses BFS or DFS to explore reasoning paths
- LLM evaluates intermediate steps to select next path
- Queries LLM **multiple times** (per exploration node)
- More expensive than CoT but better for strategic lookahead

**GoT — Graph of Thoughts **(Khot et al., 2023)
- Extends ToT tree to **directed acyclic graph**
- Allows merging of intermediate paths
- More powerful than tree for problems with convergent reasoning
- Supports evaluation + aggregation operators

**AoT — Algorithm of Thoughts **(Hao et al., 2023)
- Incorporates algorithmic examples into prompts
- Needs only **one or a few** LLM queries
- More efficient than ToT/GoT for algorithmic problems
- Uses domain-specific algorithmic thinking

### 3. Reasoning + Acting Integration (ReAct Era)

**ReAct **(Yao et al., 2022)
- Interleaves reasoning **(thought) with action (act)**
- Pattern: `Thought → Action → Observation → Thought → Action...`
- Reasoning guides actions, actions ground reasoning
- Synergistic: each component makes the other more effective

**ReWOO **(Srinivas et al., 2023)
- **Separates planning from execution**
- Agent first generates complete plan, then **executes all actions independently**, combines observations
- Uses "WOO" (Worker Only Once) paradigm for efficiency
- Supports parallel action execution
- More efficient than ReAct for parallelizable tasks

**HuggingGPT **(Shao et al., 2023)
- Decomposes task into sub-goals
- Routes to models on HuggingFace for each sub-goal
- Uses GPT-4 as Task Router/manager
- Demonstrates LLMs as orchestrators of external tool APIs

### 4. Self-Reflection & Adaptation (2023)

**Reflexion **(Shinn et al., 2023)
- Combines natural language feedback with persistent memory
- Agent produces action → receives critic feedback → adjusts via refinement
- Uses short-term sliding window + long-term persistent storage
- **Verbal reinforcement learning**: LLM provides critique, not scalar
- Improves planning through detailed natural language feedback

### 5. Multi-Agent Orchestration Frameworks (2023)

**AutoGPT **(2023)
- First popular autonomous agent framework
- Fully automated goal setting, task decomposition, cycle through tasks
- Pioneered "fully autonomous" agents

**ChatDev **(2023)
- Multi-agent simulated software company
- Multiple LLM agents with different roles
- Sequential workflow from requirements to deployment

**CrewAI **(2023)
- Role-based multi-agent orchestration
- Define agents with roles, goals, and backstories
- Sequential or parallel task execution

**DSPy **(Khattam et al., 2023)
- Compiles declarative LLM applications
- Programmatic specification → optimized prompts/fine-tuning
- No manual prompting required

**LangGraph **(2023, LangChain)
- Stateful, multi-participant agent orchestration
- Graph-based workflows with **persistent state**
- Built on LangChain ecosystem

**AutoGen **(Microsoft, 2023)
- Multi-agent conversation framework
- Different agent types: conversable, human, code interpreter
- Group chat, code generation, sequential patterns

## Architecture Comparison Matrix

| Architecture | Reasoning | Acting | Self-Reflect | Parallel | Multi-Agent |
|---|---|---|---|---|---|
| CoT | ✓ | | | | |
| ToT | ✓✓✓ | | | ✓ (search) | |
| GoT | ✓✓✓✓ | | | ✓ (merge) | |
| ReAct | ✓✓ | ✓✓ | ✓ (implicit) | | |
| ReWOO | ✓✓ | ✓✓✓ | | ✓✓ (parallel) | |
| Reflexion | ✓✓ | ✓ | ✓✓ | | |
| AutoGPT | ✓✓✓ | ✓✓✓✓ | ✓ | | ✓ (implicit) |
| CrewAI | | ✓✓✓ | | ✓✓✓ | ✓✓✓ |
| DSPy | ✓✓✓ | ✓✓ | | ✓ | |
| LangGraph | ✓✓ | ✓✓✓ | | ✓✓✓ | ✓✓✓ |

## Design Patterns

1. **Thought + Action + Observation** (ReAct pattern)
2. **Plan → Execute → Observe** (ReWOO pattern)  
3. **Tree/Graph of Thoughts** (ToT + GoT)
4. **Reflection + Memory + Self-Correction** (Reflexion)
5. **Task Decomposition → API Routing** (HuggingGPT)
6. **Multi-Agent Orchestration** (CrewAI, AutoGen, etc.)

## Key Insights

1. **CoT/Zero-shot-CoT** = basic reasoning, no execution
2. **ToT/GoT** = strategic lookahead, more expensive
3. **ReAct** = synergistic reasoning + action, underlies all modern agents
4. **ReWOO** = most efficient for parallelizable tasks (decoupled plan+execute)
5. **Reflexion** = self-improvement via verbal critique
6. **HuggingGPT** = LLM as orchestrator of API ecosystem
7. **Multi-agent frameworks** = production-ready patterns for complex workflows

## Cross-References
- ReAct paper: [[ReAct: Synergizing Reasoning and Acting in Language Models]]
- LLM-Agent-Survey (2308.11432)
- CourseDesigner Lesson 13: Agents and Agentic Workflows
