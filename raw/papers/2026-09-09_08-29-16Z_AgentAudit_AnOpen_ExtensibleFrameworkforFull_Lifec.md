---
title: AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents
published: 2026-09-09T08:29:16Z
authors: Shrey Nag,  Sachita, Abhishek Kumar Singh, Lipi Goel, Rajeshwar Singh Janwar
url: http://arxiv.org/abs/2609.09875v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentAudit: An Open, Extensible Framework for Full-Lifecycle Trust Evaluation of AI Agents

## Abstract
Existing evaluation frameworks mostly assess only one part of AI agents, such as task completion (AgentBench) or security robustness (AgentDojo, ASB), rather than the complete pipeline of planning, tool selection, tool execution, memory and reasoning. Failures can occur at any stage, yet existing benchmarks rarely identify their precise source. AgentAudit evaluates the entire execution trace across ten capability, grounding, security and behavioural dimensions, namely instruction integrity, planner, memory, tool selection, tool invocation, tool correctness, alignment, tool faithfulness, security and execution integrity, combined with behavioural classification and failure attribution to pinpoint the exact stage responsible for an observed failure. AgentAudit can evaluate any LLM-based AI agent, since it attaches to the agent instead of replacing it. It reads only the recorded execution trace and does not interfere with how the agent runs, so it places no constraint on the agent's internal implementation. We evaluate five language models (OpenAI GPT-5, Claude Sonnet 5, Sarvam 105B, Llama 3.3 70B and Gemini 2.5 Flash) across nine capability and adversarial tasks. Claude Sonnet 5 and GPT-5 obtain the highest mean Composite Trust Scores (95.1 and 80.6 out of 100, respectively), while Sarvam 105B, Llama 3.3 70B and Gemini 2.5 Flash trail substantially (57.6, 45.7 and 22.6). All traces were scored by a single fixed judge model, which was itself one of the evaluated models, a limitation discussed in Section VII.E. More importantly, models with similar task-completion behaviour can diverge sharply in trustworthiness, as several non-frontier models are repeatedly classified Unsafe_Compliance on adversarial tasks rather than merely failing them, a distinction that pass/fail benchmarks cannot surface.

## Metadata
- **Published**: 2026-09-09T08:29:16Z
- **Authors**: Shrey Nag,  Sachita, Abhishek Kumar Singh, Lipi Goel, Rajeshwar Singh Janwar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09875v1)