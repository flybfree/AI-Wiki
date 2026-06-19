---

title: SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning
url: http://arxiv.org/abs/2604.23747v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-26_14-53-48Z_SFT_then_RLOutperformsMixed_PolicyMethodsforLLMRea.md
generated_at: "2026-06-11 10:28"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper investigates why mixed-policy optimization methods for large language model reasoning often underperform the standard supervised fine-tuning followed by reinforcement learning pipeline. It identifies two bugs in popular frameworks — a DeepSpeed optimizer issue that discards micro‑batches and an OpenRLHF loss aggregation error — which degrade SFT performance. After correcting these issues, SFT‑then‑RL surpasses all mixed‑policy approaches on math benchmarks.

## Key Takeaways
- The DeepSpeed CPU‑offloaded optimizer bug silently drops intermediate micro‑batches during gradient accumulation, causing a large portion of the performance gap.
- OpenRLHF’s loss aggregation bug incorrectly weights per‑mini‑batch losses, adding a smaller but still detrimental effect.
- Even with only 50 reinforcement learning steps, SFT‑then‑RL outperforms mixed‑policy methods on math benchmarks while using fewer FLOPs.

## Context
Mixed‑policy optimization seeks to blend supervised and reinforcement signals to improve LLM reasoning. However, many recent implementations suffer from hidden implementation flaws that obscure their true efficacy compared to simpler pipelines.

## Implications
Practitioners should verify optimizer settings and loss aggregation logic before adopting mixed‑policy methods. This paper provides a clear diagnostic framework, encouraging more robust evaluation of RLHF techniques in the field.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.23747v1)
