# Summary: 2026-08-10_13-28-23Z_FromSweeptoSeam_InterleavedCross_BlockPost_Trainin.md
Saved: 2026-08-11 00:09
Source: 2026-08-10_13-28-23Z_FromSweeptoSeam_InterleavedCross_BlockPost_Trainin.md
Model: None

---

## Summary  
The paper tackles the challenge of compressing large language models to two bits or fewer using block‑wise post‑training quantization, a technique that has become increasingly feasible. In the fixed two‑block setting, errors introduced early in the sweep are never revisited, leading to severe degradation. To address this limitation, the authors introduce Interleaved Cross‑Block Quantization (ICBQ), which revisits each seam pair between consecutive chunks twice, thereby improving reconstruction quality and preserving the local two‑block objective while reusing existing calibration inputs.

## Key Contributions  
- ICBQ revisits each boundary pair twice to mitigate early error propagation.  
- The authors derive a depth‑wise upper‑bound showing that repeated seam refinement multiplies only the propagated term, while the residual remains bounded independently of network depth.  
- Empirically, ICBQ reduces ternary‑quantization perplexity relative to the matched Sequential CBQ baseline and yields finite perplexity in configurations where the baseline degrades severely; it also works with 3‑bit and 2‑bit GPTQ.

## Methodology  
The authors modify the standard block‑wise PTQ pipeline by keeping the local two‑block objective unchanged and reusing the calibration inputs of existing pipelines. Their scheduling change schedules each seam pair to be refined at the end of one chunk and again at the start of the next, creating an interleaved “sweep” that revisits boundaries twice without altering the core quantization steps.

## Results  
Experiments show that ICBQ consistently lowers ternary‑quantization perplexity compared with the Sequential CBQ baseline. In cases where the baseline exhibits severe degradation, ICBQ produces finite perplexity, indicating a more stable reconstruction. The method also supports 3‑bit and 2‑bit GPTQ quantizations, demonstrating robustness across different precision levels.

## Significance  
ICBQ provides a practical solution to error accumulation in block‑wise quantization, enabling reliable two‑bit compression for large language models. By revisiting seam pairs, it improves the quality of ultra‑low‑precision models and opens the door to more efficient deployment without sacrificing performance.

## Related Concepts  
- Block‑wise post‑training quantization  
- Cross‑block reconstruction within a moving window  
- Seam pair refinement  
- Ternary (3‑bit) and 2‑bit GPTQ  
- Perplexity as a metric of quantization quality  
- Depth‑wise analysis of error propagation
