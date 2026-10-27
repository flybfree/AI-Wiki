---
title: CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems
published: 2026-10-26T09:25:38Z
authors: Yujia Zheng, Tianhao Li, Shangzhi Xu, Yuekai Huang, Ziyou Jiang, Zhaoyang Li, Yuyao Ge, Junran Peng, Mingyang Li
url: http://arxiv.org/abs/2610.35082v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoSA: The Conflict of Skills Attack in Real-World LLM Agent Ecosystems

## Abstract
Agent Skills allow LLM agents to combine reusable capabilities, but checking each Skill in isolation cannot rule out policy violations when they are composed. We term such failures Conflict of Skills (CoS): artifacts or assessment signals produced for one purpose may be reused downstream without preserving the restrictions or authorization needed for their new use. Using controlled executions of publicly available Skills and matched single-Skill controls, we identify four recurring mechanisms behind CoS. Building on these findings, we introduce the Conflict of Skills Attack (CoSA), which adds locally admitted Skills to an existing pool to supply missing business operations (capability supplementation) or reshape artifact exchange, decision reuse, and target/action bindings (relationship reshaping). CoSA leaves existing Skills and runtime permissions unchanged. To evaluate this threat under autonomous Skill selection, we introduce CoSA-Bench, built from real-world Skills and controlled services, with 288 tasks across recruiting, finance, IT, and business, covering data leakage, unauthorized state modification, and unsafe execution. Across five LLMs and three agent harnesses, additions capped at 5% of each original pool raise the policy-violation rate from 35.02% to 58.45%, an increase of 23.43 percentage points. Trace analysis links compliant-to-violating transitions to cross-Skill dependencies involving the additions. Finally, we develop a lightweight harness-level guard that checks information flow and authorization before consequential actions. On OpenClaw recruiting tasks across five models, the guard reduces violations from 65.28% to 6.67%, while policy-compliant task completion on matched benign controls changes from 66.67% to 65.00%.

## Metadata
- **Published**: 2026-10-26T09:25:38Z
- **Authors**: Yujia Zheng, Tianhao Li, Shangzhi Xu, Yuekai Huang, Ziyou Jiang, Zhaoyang Li, Yuyao Ge, Junran Peng, Mingyang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35082v1)