---
title: Letting Models Manage Their Own Context: Where We Stand
url: http://arxiv.org/abs/2611.34147v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_10-44-04Z_LettingModelsManageTheirOwnContext_WhereWeStand.md
generated_at: 2026-11-26 21:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper investigates model-driven context management, in which an LLM decides itself when and what to compact through a context API, rather than relying on an agent harness to trigger compaction once the context window fills. The authors implemented this in nooa, NVIDIA's open-source agent harness, and compared it against harness-managed compaction across document research and machine learning engineering tasks at context budgets from 8K to 512K tokens. They find that models using the context API reach higher accuracy, often with fewer input tokens, especially at tight budgets, and that inference engines can further reduce the cost of these edits by reusing the KV cache of the unchanged suffix.

## Key Takeaways
- Model-driven compaction improves performance at tight budgets: GPT 6.1 nearly triples its score at a 32K budget on OfficeQA Pro v2, rising from 21% to 56%, while Kimi gains with up to 41% fewer input tokens.
- Behavior is highly model-dependent: models differ widely in how often they call the context API, how aggressively they compact, and when they begin compacting, and prompt changes shift that timing, so the strategy is not a uniform win across models.
- Inference-side optimization is possible: by reusing the KV cache of the unchanged suffix after a model-driven edit, the authors cut prefill compute by up to 15% per request with no measurable change in accuracy.

## Context
Agent harnesses today act as external context managers, summarizing history when the window fills, which treats context control as a fixed harness policy rather than a model capability. This paper reframes context management as something the model itself can learn and execute, situating the question at the intersection of agent design, prompting, and inference-system engineering. The comparison spans budgets from 8K to 512K tokens across document research and machine learning engineering, making it relevant to long-horizon agents that must operate under constrained or variable context windows.

## Implications
The results point toward a co-design frontier in which models are trained to manage their own context and inference engines are built to support KV cache editing, rather than treating context handling as a purely harness-side concern. For practitioners, model-driven compaction can deliver better accuracy per token at tight budgets, but the gains are not automatic: prompt design and model choice strongly affect when and how compaction happens, so evaluation should be done per model and per task. For systems builders, KV cache reuse after edits offers a low-risk way to reduce prefill cost without sacrificing accuracy, suggesting that context management and serving infrastructure should be optimized together.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34147v1)
