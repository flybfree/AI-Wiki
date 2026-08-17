# Summary: 2026-08-14_05-29-58Z_QUASAR_LoweringtheLossFloorofQuantization_AwareTra.md
Saved: 2026-08-16 21:40
Source: 2026-08-14_05-29-58Z_QUASAR_LoweringtheLossFloorofQuantization_AwareTra.md
Model: None

---

## Summary  
Quantization‑aware training (QAT) aims to keep model quality when moving inference to low‑bit formats, but the standard approach suffers from a high loss floor because it uses a single lossy reconstruction of full‑precision weights. QUASAR solves this by embedding lightweight, loss‑aware reconstructions into every training step, allowing the method to continuously lower the error and improve the final quantized model. The authors show that minimizing this reconstruction error is the only reconstruction‑dependent term in the QAT convergence bound, making it a principled optimization target.  

## Key Contributions  
- [Finding 1] QUASAR integrates online saliency estimates derived from exponential moving averages of squared gradients to guide clipping ranges and affine dequantizer fitting during training.  
- [Finding 2] The method continuously performs lightweight reconstruction at each step, avoiding the impractical multi‑epoch loss‑aware optimization used in prior second‑order PTQ techniques.  
- [Finding 3] QUASAR’s reconstruction error is identified as the sole term that directly controls the final quantized model’s loss, establishing it as a clear objective for QAT convergence.  

## Methodology  
The authors modify only the training loop: after computing gradients, they compute an online saliency estimate via exponential moving averages of squared gradients; this saliency is used to search over a small set of clipping ranges and fit affine dequantizers through weighted least squares. The reconstruction error computed from these dequantized weights is added to the standard QAT loss, enabling continuous improvement without freezing the model or incurring extra inference overhead.  

## Results  
Across Qwen3 and Llama‑3.1, QUASAR achieves the lowest held‑out KL divergence among competitive QAT methods at 2, 3, and 4 bits. At 3 bits it reduces KL by ≥10% and at 4 bits by ≥29%, while at 2 bits it improves average accuracy on eight tasks by 3.5–4.3 percentage points over strong QAT and PTQ baselines.  

## Significance  
By lowering the loss floor, QUASAR enables more reliable low‑bit inference with minimal additional cost, addressing a longstanding bottleneck in practical quantization for large language models. The continuous reconstruction approach makes high‑quality quantization feasible at scale without sacrificing training efficiency or requiring changes to deployment formats.  

## Related Concepts  
Quantization‑aware training (QAT), post‑training quantization (PTQ), loss‑aware reconstruction, exponential moving average saliency estimation, affine dequantizers, second‑order PTQ, KL divergence as a metric for model quality, integer quantization, NVFP4.
