---
title: ProPerAgent: Toward Memory-Driven Proactive Assistance
url: http://arxiv.org/abs/2610.22671v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_21-40-17Z_ProPerAgent_TowardMemory_DrivenProactiveAssistance.md
generated_at: 2026-10-18 20:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ProPerMem, a benchmark for memory-driven proactive assistance (MPA), which evaluates whether AI assistants can autonomously decide when to intervene based on long-horizon personal memories rather than simply answering a prompted query. The authors demonstrate that both content retrieval and timing of intervention are independently critical, and that existing systems fail dramatically when either is left to the model. They then propose ProPerAgent, a system combining a graph-organized memory store with a gating mechanism and reinforcement learning post-training, which substantially improves proactive intervention accuracy over all evaluated baselines.

## Key Takeaways
- The paper establishes a controlled ablation showing that GPT-5.3-Chat achieves 96% accuracy when both the correct evidence and the correct timing window are provided, but performance collapses to 38% when the model must choose its own timing, and further to 15% when it must also retrieve evidence from memory. This proves that content and timing are separately necessary and that failure in either dimension is catastrophic for proactive assistance.
- ProPerMem is a uniquely challenging benchmark pairing egocentric video with year-long, distractor-rich user memories averaging approximately 618,000 tokens, along with human-verified trigger windows and a joint scoring protocol for content and timing. Every baseline evaluated, including frontier models given summarized or retrieval-augmented memory, scores at most 15%, highlighting the gap between reactive QA and true proactive intervention.
- ProPerAgent lifts strict accuracy from below 10% to 37.5% on Qwen3.8-27B and 38% on GPT-5.3-Chat without any training, using a plug-and-play harness that surfaces memory from a graph-organized store and gates it down to what is worth interrupting for. A lightweight RL post-training stage further curbs early and repeated firing, reaching 42.4% accuracy, demonstrating that architectural design and targeted fine-tuning can close a large portion of the performance gap.

## Context
The broader AI landscape is shifting from reactive question-answering toward proactive, context-aware assistants that must decide autonomously when and whether to speak. Prior research in proactive assistance typically supplies the relevant fact directly in context, sidestepping the harder problem of mining evidence from long-horizon personal memory. This paper addresses that harder regime, which mirrors real-world deployment scenarios where assistants must sift through months or years of user history to identify a moment worth interrupting for. By formalizing the joint content-and-timing evaluation and showing that frontier models fail at 15% in this setting, the work exposes a fundamental capability gap in current LLM-based assistants.

## Implications
For practitioners building personal AI assistants, this work signals that retrieval-augmented generation alone is insufficient for proactive behavior; systems need explicit timing gates and memory organization structures to avoid both missed interventions and excessive, annoying interruptions. The graph-organized memory store and RL-based firing control in ProPerAgent offer a practical architectural blueprint that could be adapted to consumer assistants, health monitoring agents, or productivity tools that must act on long-term user context. The benchmark itself provides a rigorous evaluation standard that the field currently lacks, enabling more honest progress tracking as proactive assistants move from research prototypes to deployed products.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22671v1)
