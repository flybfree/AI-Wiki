# Summary: 2026-08-09_11-51-14Z_LegoLM_StructuredWeightSharingforLargeLanguageMode.md
Saved: 2026-08-10 23:20
Source: 2026-08-09_11-51-14Z_LegoLM_StructuredWeightSharingforLargeLanguageMode.md
Model: None

---

## Summary  
The paper introduces LegoLM, a data‑free compression technique that mitigates two specific failure modes of global weight sharing in large language models: a linear‑in‑d distortion for low‑dimensional vector blocks and an accumulation of unrepresentable outlier weights. By applying three systematic adaptations—scalar‑block encoding, percentile‑selective replacement, and boundary‑layer protection—the authors achieve high compression ratios while preserving model quality. Experiments on GPT‑2 small (124 M) and Mistral‑7B show that LegoLM reaches 4.41× compression with only a +0.03% perplexity increase and 2.67× compression with negligible degradation, outperforming conventional PTQ‑8bit methods. The approach also scales to larger models, where selective replacement prevents catastrophic loss of performance.

## Key Contributions  
- Finding 1: Distributional mismatch for vector blocks of dimension d ≤ 2 causes a linear‑in‑d penalty that cannot be resolved by increasing K, leading to high perplexity.  
- Finding 2: For scalar blocks, about 1/K weights fall beyond the outermost Lloyd‑Max decision threshold and are unrepresentable as centroids, causing cumulative quality loss.  
- Finding 3: LegoLM resolves both issues with three data‑free adaptations: scalar‑block encoding, percentile‑selective replacement of outliers, and boundary‑layer protection for first/last transformer blocks.

## Methodology  
The authors conduct a systematic study of global weight sharing by analyzing why it fails in practice. They identify the two failure modes described above and design three complementary fixes that do not require additional training data. The framework is evaluated through controlled experiments on GPT‑2 small (124 M) and Mistral‑7B, measuring compression ratio, perplexity degradation, and downstream accuracy. An ablation study isolates the impact of selective replacement, confirming it as the dominant quality‑preserving mechanism.

## Results  
At K=64 with 99% percentile selection, LegoLM achieves 5.12× compression on LAMBADA while preserving accuracy within noise, exceeding PTQ‑8bit’s ratio. On GPT‑2 small, full replacement at K=128 degrades perplexity by only +23%, whereas selective replacement keeps it under +15%. The ablation shows that adding selective replacement to per‑layer K‑means yields near‑lossless quality, matching LegoLM within 0.02% loss.

## Significance  
LegoLM demonstrates that high‑quality compression is possible without sacrificing model performance, especially for large models where outlier dominance becomes severe. By eliminating the linear distortion and preserving outliers selectively, it surpasses PTQ‑8bit in both compression ratio and accuracy, offering a practical path toward more efficient deployment of LLMs.

## Related Concepts  
- Global weight sharing  
- Transformer layers  
- Lloyd‑Max decision threshold  
- Centroid representation  
- Outlier dominance  
- Percentile‑selective replacement  
- Boundary‑layer protection  
- K‑means quantization  
- Perplexity degradation  
- Compression ratio
