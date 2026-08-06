---
title: Mind the Cap: Output-Budget Regimes Change the Measured Multilingual Reasoning Gap
url: http://arxiv.org/abs/2608.04160v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_19-18-41Z_MindtheCap_Output_BudgetRegimesChangetheMeasuredMu.md
generated_at: 2026-08-05 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how output‑token budgets affect multilingual reasoning performance across Qwen3‑8B and Llama‑3.1‑8B‑Instruct on the MGSM benchmark. It finds that the native‑vs‑translate gap varies dramatically with budget, can be reversed by length normalization at tight caps, and that freezing certain evaluation peaks does not reveal a true reasoning deficit.

## Key Takeaways
- The measured gap swings up to 57 points across different token budgets, showing it is largely driven by token‑budget constraints rather than intrinsic language ability.  
- Length normalization moves the gap by up to 38.9 points when the cap binds, and at tight caps this normalization can reverse which prompting strategy scores higher, indicating budget effects are strong.  
- A frozen test at a $B^*=1024 token budget fails to reject null hypotheses because native accuracy is already saturated there; above saturation the residual difference reflects strategy performance rather than a reasoning deficit.

## Context
Multilingual AI models are often evaluated under a single output‑cap, but languages require varying token lengths for comparable content. This hidden variable can bias gap measurements and mislead practitioners about model capabilities. Understanding how budget interacts with language‑specific demands is crucial for fair benchmarking.

## Implications
Researchers should treat the output cap as an independent experimental factor when reporting multilingual accuracy. Practitioners must consider budget constraints in model adaptation, such as vocabulary extensions, to close performance gaps without inflating reported scores.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04160v1)
