---
title: ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation
published: 2026-10-06T22:06:17Z
authors: Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal, Tanner Sorensen, Justin Chiu, Alessandro Di Bari, Neha Gupta, Andreas Stolcke
url: http://arxiv.org/abs/2610.09163v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ToolRACER: A Robust Agentic Conversation Emulation Resource for Agent Training and Evaluation

## Abstract
Task-oriented conversational agents remain fragile under real world conversation scenarios as they rarely follow a predictable script, especially when users exhibit non-cooperative behavior. Existing function-calling benchmarks often emphasize successful, cooperative interactions and underrepresent adversarial conversation trajectories, thereby limiting the training resources available for developing robust agents. We present ToolRACER, a synthetic data generation pipeline that coordinates user, assistant and tool emulation models to generate and validated multi-turn interactions between a user and an agent. Using \sysn, we construct ToolRACERBench a robust multi-turn conversation benchmark spanning six domains, ranging over 55 varied personas, generating a validated corpus of 5.6K conversation trajectories, with approximately 66\% of conversations containing failure-prone conversation scenarios. We inject adversarial behaviors, producing validated conversational interaction trajectories that capture realistic, robust scenarios. We evaluate models trained on ToolRACERBench against internal benchmarks, as well as on function calling benchmarks such as $τ^2$-bench, BFCLv3 and ACEBench to evaluate agentic accuracy and robustness. Models trained on ToolRACERBench improve end to end agentic accuracy across $τ^2$-bench and ACEBench, demonstrating significant gains when mixed with in-domain dataset in small language models for agent capability tasks.

## Metadata
- **Published**: 2026-10-06T22:06:17Z
- **Authors**: Arkajyoti Chakraborty, Aryan Tayal, Ishika Agarwal, Tanner Sorensen, Justin Chiu, Alessandro Di Bari, Neha Gupta, Andreas Stolcke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09163v1)