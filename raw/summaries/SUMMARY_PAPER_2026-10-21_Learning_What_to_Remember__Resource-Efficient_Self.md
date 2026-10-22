---
title: Learning What to Remember: Resource-Efficient Self-Improvement for Lifelong Agents
url: http://arxiv.org/abs/2610.26453v2
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-19_14-09-45Z_LearningWhattoRemember_Resource_EfficientSelf_Impr.md
generated_at: 2026-10-21 23:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces TokenWorth, a lightweight feedback-driven memory adaptation framework designed to help self-improving lifelong agents learn which past experiences are actually worth reusing under strict resource constraints. The authors demonstrate that simply accumulating more experience does not guarantee better decisions, and that effective self-improvement depends on learning what is worth remembering rather than storing everything. TokenWorth achieves the highest task success rate while consuming the fewest output tokens across multiple LifelongAgentBench environments and deployment settings.

## Key Takeaways
- The paper identifies a fundamental challenge in resource-constrained lifelong learning: existing memory-augmented agent methods often provide limited benefits over simple retrieval or even no-memory baselines when generation, interaction, and memory resources are jointly constrained. Retrieving an ineffective experience can consume scarce computational resources and actively hinder downstream task execution, making indiscriminate memory use counterproductive.
- TokenWorth operates as a query-dependent memory worth estimation mechanism that learns from sparse execution feedback without updating the backbone model. It uses the learned worth scores to guide both experience retrieval decisions and bounded memory management, enabling the agent to continually adapt its reuse strategy over time. This design keeps the approach lightweight and deployable without expensive model fine-tuning.
- Empirical evaluation across three LifelongAgentBench environments and both local and API-based deployments shows that TokenWorth achieves the highest task success rate while using the fewest output tokens among all evaluated methods under specified resource budgets, demonstrating that selective memory use outperforms accumulation-based strategies.

## Context
This work sits at the intersection of lifelong learning, memory-augmented language agents, and resource-efficient AI deployment. As large language model agents are increasingly deployed in production settings with strict token budgets, latency constraints, and memory limits, the field has largely assumed that more stored experience leads to better performance. This paper challenges that assumption by showing that under realistic resource constraints, the bottleneck shifts from memory accumulation to memory selection, reframing a core design question in agent systems research.

## Implications
For practitioners building autonomous agents in production environments—such as customer service bots, coding assistants, or research agents—this work suggests that investing in memory selection and worth estimation mechanisms may yield far greater returns than simply expanding memory stores or retrieval pipelines. The finding that a lightweight, feedback-driven adaptation layer can outperform heavier memory systems under constrained budgets has practical significance for reducing inference costs and improving reliability in API-based deployments. More broadly, it signals a shift in the research agenda from "how to remember more" to "how to decide what to remember," which could influence the design of future agent architectures, memory management systems, and evaluation benchmarks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26453v2)
