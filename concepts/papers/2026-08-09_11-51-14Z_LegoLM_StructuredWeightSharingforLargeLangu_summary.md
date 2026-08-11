# Summary: 2026-08-09_11-51-14Z_LegoLM_StructuredWeightSharingforLargeLanguageMode.md
Saved: 2026-08-10 23:17
Source: 2026-08-09_11-51-14Z_LegoLM_StructuredWeightSharingforLargeLanguageMode.md
Model: None

---

## Summary
LegoLM introduces a structured weight‑sharing scheme that tackles two specific failure modes of traditional global quantization in large language models: a linear mismatch penalty for low‑dimensional vector blocks and an accumulation of outlier weights beyond the Lloyd‑Max decision threshold. By applying three data‑free adaptations — scalar‑block encoding, percentile‑selective replacement, and boundary‑layer protection — LegoLM achieves high compression ratios while keeping perplexity loss minimal. The approach is validated across GPT‑2 small (124 M) and Mistral‑7B, demonstrating superior performance compared with conventional 8‑bit post‑training quantization.

## Key Contributions
- [Finding 1] Distributional mismatch: for vector blocks of dimension d ≤ 2, heterogeneous weight scales create a penalty that grows linearly with d, causing perplexity in the millions.
- [Finding 2] Outlier dominance: scalar blocks contain ~1/K weights beyond the outermost Lloyd‑Max threshold that cannot be represented by any centroid, leading to catastrophic quality loss across layers.
- [Finding 3] Full replacement at K=128 degrades GPT‑2 small by only +23% but catastrophically degrades Mistral‑7B by +1,134,279%; selective replacement at p=99% rescues both models to under +15%.

## Methodology
The authors systematically analyzed why global weight sharing fails, identifying the two failure modes and proposing three data‑free adaptations. They encoded scalar blocks with a single representative value, selected outlier weights verbatim using percentile thresholds, and protected the first and last transformer layers from extreme compression. The framework is applied without retraining or fine‑tuning.

## Results
On Mistral‑7B LegoLM reaches 4.41× compression with only +0.03% perplexity degradation, outperforming PTQ‑8bit in both quality and ratio; at 2.67× it degrades by –0.02%. At 5.12× compression it preserves accuracy within noise. Full replacement at K=128 worsens GPT‑2 small by +23% but Mistral‑7B by +1,134,279%; selective replacement keeps both under +15%. An ablation shows that adding selective replacement to per‑layer K‑means yields near‑lossless quality, matching LegoLM within 0.02%.

## Significance
Structured weight sharing enables high compression ratios without sacrificing model utility, offering a practical path for efficient deployment of large language models in resource‑constrained settings.

## Related Concepts
global weight sharing, Lloyd‑Max decision threshold, outlier dominance, percentile‑selective replacement, boundary‑layer protection, K‑means quantization, perplexity degradation.
