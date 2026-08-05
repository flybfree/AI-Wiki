---
title: "Ornith 1.0: Self-Scaffolding Agentic Coding Models"
tags: ["agentic-coding", "self-improving", "open-source", "DeepReinforce"]
created: 2026-07-07
updated: 2026-07-07
source: https://deep-reinforce.com/ornith_1_0.html, https://github.com/deepreinforce-ai/Ornith-1
---

# Ornith 1.0: Self-Scaffolding Agentic Coding Models

**Sources**: [DeepReinforce](https://deep-reinforce.com/ornith_1_0.html), [GitHub](https://github.com/deepreinforce-ai/Ornith-1)

## Overview

Ornith 1.0 is a family of open-source agentic coding models developed by DeepReinforce AI that introduces **self-scaffolding** — a self-improving training framework where the model learns not only to solve tasks but also to construct the scaffolds (search trajectories, planning structures) that guide those solutions.

Unlike standard coding models that just generate code, Ornith 1.0 jointly optimizes both the scaffold and the resulting solution, discovering better search trajectories and generating higher-quality outputs through reinforcement learning.

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Self-Improving-AI-Loops.md|Self-Improving AI Loops]] — 2 title terms overlap; shared tags: opensource; 10 backlinks
- [[concepts/llm-models/2026-07-10_OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 3 backlinks; 4 summary/topic terms overlap
- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]] — 1 title term overlap; 433 backlinks; 3 summary/topic terms overlap

## Core Innovation: Self-Scaffolding

The key breakthrough is treating **workflow construction as the main training target**:

- **Traditional approach**: Model generates a solution directly
- **Ornith approach**: Model learns to generate both the scaffold (planning structure) AND the solution rollouts that follow from it
- **Result**: The model autonomously improves its own execution framework — AI optimizes "the way to write code" itself, not just the code

This represents a paradigm shift where the agent doesn't just produce outputs but continuously refines its own problem-solving methodology.

## Model Family

Ornith 1.0 releases four sizes across dense and mixture-of-experts (MoE) architectures:

| Size | Type | Parameters |
|------|------|------------|
| **9B** | Dense | 9 billion |
| **31B** | Dense | 31 billion |
| **35B** | MoE | 35 billion (active) |
| **397B** | MoE | 397 billion (total) |

All models are built on pretrained Gemma 4 and Qwen 3.5 foundations, then fine-tuned with the self-scaffolding framework.

## Benchmark Performance

Ornith 1.0 achieved state-of-the-art results among fully open-source systems on major agentic coding benchmarks:

### Key Results
- **SWE-Bench Verified**: 82.4 (397B model) — highest score for any fully open-source system
- **Terminal-Bench 2.1**: Leading open-source performance
- **ClawEval**: Top-tier results
- **NL2Repo**: Strong performance

### Comparison to Commercial Models
- Matches or exceeds **Claude Opus 4.7** on several headline benchmarks
- The 397B model leads comparable open-weight models on agentic coding suites
- While Claude Opus 4.8 and GLM-5.2-744B still top some columns, Ornith closes the gap significantly

## Integration with Agent Frameworks

Ornith 1.0 exposes an **OpenAI-compatible endpoint with tool calling**, enabling seamless integration with standard agent frameworks:

**Works out of the box with**:
- Claude Code
- OpenHands
- OpenClaw
- Hermes Agent

This means you can deploy Ornith as a model provider in existing agent ecosystems without custom adapters.

## Local Deployment

### Hardware Requirements
- **9B/31B dense models**: Can run on consumer hardware with sufficient VRAM
- **35B/397B MoE models**: Require enterprise-grade GPU clusters or cloud inference

### Setup Path
1. Pull model from Hugging Face collection: `deepreinforce-ai/Ornith-10`
2. Deploy via standard OpenAI-compatible serving (vLLM, TGI, etc.)
3. Configure agent framework to use Ornith endpoint
4. Enable tool calling for agentic capabilities

### Quantization Options
Models available in various quantization formats for efficient local deployment.

## Why It Matters

Ornith 1.0 represents a significant step forward in **agentic coding**:

1. **Self-improvement**: The model gets better at its own methodology over time
2. **Open source**: MIT licensed, accessible to the community
3. **Performance**: Competes with top commercial models on coding tasks
4. **Integration**: Works with existing agent frameworks immediately
5. **Scalability**: Range from 9B (local) to 397B (enterprise)

## Practical Applications

- **Autonomous code generation** for complex projects
- **Multi-step debugging** and problem-solving across systems
- **Workflow optimization** where the agent improves its own approach
- **Research and development** of agentic AI systems
- **Production deployment** as a coding assistant backend

## Related Resources

- [Ornith 1.0 Deep Dive](https://www.communeify.com/en/blog/ornith-1-0-ai-agent-coding-framework-analysis/) — Analysis of self-scaffolding technology and anti-cheating mechanisms
- [Benchmark Results Page](https://ornith.site/benchmarks/) — Detailed scores across all benchmarks
- [GitHub Repository](https://github.com/hermannheringer/Ornith) — Implementation details and usage examples

---

*This article will be updated as new benchmark results and capabilities are released.*