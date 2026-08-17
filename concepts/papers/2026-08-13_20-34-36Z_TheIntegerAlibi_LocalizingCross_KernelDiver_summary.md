# Summary: 2026-08-13_20-34-36Z_TheIntegerAlibi_LocalizingCross_KernelDivergencein.md
Saved: 2026-08-16 21:30
Source: 2026-08-13_20-34-36Z_TheIntegerAlibi_LocalizingCross_KernelDivergencein.md
Model: None

---

## Summary  
This paper investigates why two GPU kernels that implement the same scaled INT8 GEMM interface in vLLM can produce divergent outputs for the same model, prompts, and hardware. By fixing all external factors except the linear‑layer kernel (CUTLASS vs. Triton) and analyzing a 1.7B Qwen3 checkpoint, the authors demonstrate that the integer accumulator is exact under power‑of‑two scaling, so any discrepancy must arise from later scale application or output rounding. The study also shows that these differences are localized to specific layers and tokens, with flip risk concentrated at small logit margins. Providing a reproducible “integer alibi” protocol enables concrete checks for kernel interchangeability.

## Key Contributions  
- [Finding 1] Under verified no‑overflow INT8 bounds, the integer accumulator is exact and order‑independent; differences cannot stem from accumulation but only from subsequent scaling or rounding.  
- [Finding 2] Bit‑identical outputs are observed for all layers when using power‑of‑two scales (196/196 and 252/252 matched predictions), confirming the “integer alibi” holds across the model’s depth.  
- [Finding 3] The divergence manifests as at most one bfloat16 spacing per output, and cross‑implementation FP8 GEMM shows a larger effect that grows with reduction depth.

## Methodology  
The authors held the Qwen3 checkpoint, prompts, hardware, inference engine, decoding, and quantization configuration constant while swapping only the INT8 linear kernel (CUTLASS vs. Triton). They executed cold restarts to ensure reproducibility, recorded outputs for 196‑layer and 252‑layer models, and compared them across multiple runs. To isolate the source of divergence, they applied a probe checkpoint that re‑introduced the original kernel, restoring end‑to‑end bitwise agreement. Additionally, teacher‑forced replay was used to map token flips to logit margins, enabling statistical analysis with ROC‑AUC.

## Results  
No sequence matched between kernels across 8/8, 16/16, and 64/64 comparison sets, yet the observed differences never exceeded one bfloat16 spacing. The “integer alibi” was confirmed by checking that all linear layers produced identical accumulator values under power‑of‑two scales. Per‑layer predictions from the probe checkpoint matched the original kernel for 8/8 and 16/16 sequences, indicating localized divergence. Cross‑implementation FP8 GEMM exhibited a prevalence of differences proportional to reduction depth, while INT8 differences remained at parts per million.

## Significance  
This work clarifies that integer quantization does not guarantee bitwise consistency across different kernels; the true source is post‑accumulator operations. By establishing a reproducible “integer alibi” protocol and linking flip risk to logit margins, it provides a concrete framework for evaluating kernel interchangeability in large language models.

## Related Concepts  
- INT8 GEMM quantization  
- Kernel interchangeability testing  
- Integer accumulator exactness under power‑of‑two scaling  
- Output rounding and bfloat16 spacing  
- Teacher‑forced replay and logit margin analysis
