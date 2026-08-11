# Summary: 2026-08-10_13-28-23Z_FromSweeptoSeam_InterleavedCross_BlockPost_Trainin.md
Saved: 2026-08-10 23:50
Source: 2026-08-10_13-28-23Z_FromSweeptoSeam_InterleavedCross_BlockPost_Trainin.md
Model: None

---

## Summary  
The paper tackles the problem of compressing large language models to two bits or fewer using block‑wise post‑training quantization (PTQ). Existing matched sequential baselines move a fixed two‑block window through the network only once, so errors introduced early are never revisited. The authors introduce Interleaved Cross‑Block Quantization (ICBQ), which revisits each boundary pair between consecutive chunks twice—once at the end of one chunk and again at the start of the next—to mitigate this limitation while preserving the original two‑block objective and reusing existing calibration inputs.

## Key Contributions  
- ICBQ revisits every seam pair twice, refining the same boundary across adjacent blocks.  
- A depth‑wise upper‑bound analysis shows that repeated seam refinement multiplies the propagated error term but leaves a residual bounded independently of network depth, guaranteeing finite perplexity even when the baseline degrades severely.  
- The method reduces ternary‑quantization perplexity relative to the matched Sequential CBQ baseline and can be applied to 3‑bit and 2‑bit GPTQ configurations.

## Methodology  
The authors modify an existing block‑wise PTQ pipeline by inserting an interleaved scheduling step that processes each boundary pair twice. The moving window still spans two consecutive Transformer blocks, but the seam is evaluated at both ends of the chunk. Calibration inputs remain unchanged, and the local two‑block objective is retained. Under assumptions of local contraction (error does not accumulate beyond a constant) and smoothness (error propagation is bounded), the authors derive an analytical bound that separates the depth‑dependent propagated term from a residual term.

## Results  
Experiments on several large language models demonstrate that ICBQ achieves lower perplexity than the matched Sequential CBQ baseline. In configurations where the baseline exhibits severe degradation, ICBQ yields finite perplexity instead of exploding values. The approach also works with 3‑bit and 2‑bit GPTQ quantizations, confirming its scalability to extreme bit depths.

## Significance  
By revisiting seam pairs, ICBQ mitigates the “sweep” effect that plagues fixed two‑block PTQ, enabling more reliable compression without sacrificing model quality. This opens the door to compressing LLMs to two bits or fewer while preserving inference performance, a crucial step for deploying models on resource‑constrained hardware.

## Related Concepts  
- Block‑wise post‑training quantization (PTQ)  
- Cross‑block reconstruction within a moving window  
- Seam refinement / interleaved scheduling  
- Ternary and 2‑bit GPTQ quantization  
- Perplexity as a metric of quantization quality  
- Depth‑wise error bound analysis
