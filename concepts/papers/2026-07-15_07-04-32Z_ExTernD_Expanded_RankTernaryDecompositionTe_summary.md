# Summary: 2026-07-15_07-04-32Z_ExTernD_Expanded_RankTernaryDecompositionTernaryLL.md
Saved: 2026-07-23 23:43
Source: 2026-07-15_07-04-32Z_ExTernD_Expanded_RankTernaryDecompositionTernaryLL.md
Model: None

---

## Summary  
ExTernD proposes an expanded‑rank ternary decomposition for low‑bit quantized large language models that can achieve bf16‑level accuracy despite using only {-1,0,+1} factors. By deliberately increasing the inner rank beyond full matrix rank (μ > 1) and adjusting a sparsity threshold τ, the method corrects quantization errors introduced by earlier low‑rank components, allowing the residual error to shrink monotonically toward zero. This continuous scaling enables the model’s perplexity to approach any desired accuracy level rather than being limited to discrete bit‑width bands. The work demonstrates that ternary PTQ can match or exceed conventional Q4_K/Q5_K performance on several 4B‑parameter models.

## Key Contributions  
- [Finding 1] An expanded‑rank factorization A ≈ B·diag(D)·C with B, C ternary and D real, where the inner rank k = μ min(m,n) > min(m,n) corrects errors of lower‑rank components.  
- [Finding 2] The residual error decreases monotonically as μ grows, allowing it to be driven below any ε > 0, thus achieving bf16 accuracy arbitrarily closely.  
- [Finding 3] Memory and compute scale continuously depend on μ while factor sparsity follows a threshold τ, delivering exact accuracy targets instead of rounding to the next bit‑width.

## Methodology  
The authors decompose each weight matrix A into three parts: B (m × k) and C (k × n) are ternary matrices containing only -1, 0, +1; D is a real scale vector of length k. The decomposition is performed by first selecting μ to control the inner rank, then applying a sparsity threshold τ to zero out sub‑components that would otherwise increase error. The resulting factors are stored with minimal memory overhead because many entries remain zero, and the compute cost scales linearly with μ.

## Results  
On Gemma‑4‑E2B and Qwen3.5‑4B, ExTernD reaches 5.2–5.5 effective bits per word (effective bpw) at Q4_K levels, comparable to conventional Q4_K/Q5_K. A full conversion of Qwen3.5‑4B with μ = 3 yields a wikitext‑2 perplexity of 10.10, only 3.2% higher than the bf16 baseline (9.78), placing it near the Q4_K/Q5_K band (~5.7 effective bpw). The method’s error residual is shown to drop below any ε > 0 as μ increases.

## Significance  
ExTernD proves that ternary quantization can surpass fixed‑bit accuracy limits by exploiting an expanded rank, offering a path toward truly continuous precision control in LLMs without sacrificing memory or compute efficiency. This could enable more accurate inference on edge devices where bf16 is the target but full fp32 storage is prohibitive.

## Related Concepts  
- Ternary decomposition (B, C ∈ {‑1,0,+1})  
- Post‑training quantization (PTQ) for LLMs  
- Effective bits per word (effective bpw)  
- Inner rank expansion and sparsity thresholds  
- Perplexity as a metric of language model quality
