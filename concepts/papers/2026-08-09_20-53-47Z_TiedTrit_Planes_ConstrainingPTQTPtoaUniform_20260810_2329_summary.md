# Summary: 2026-08-09_20-53-47Z_TiedTrit_Planes_ConstrainingPTQTPtoaUniformNine_Le.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_20-53-47Z_TiedTrit_Planes_ConstrainingPTQTPtoaUniformNine_Le.md
Model: None

---

## Summary  
The paper introduces “Tied Trit‑Planes,” a novel quantization strategy that forces the two ternary planes of PTQTP to share a fixed three‑to‑one scale ratio, thereby collapsing them into a single uniform nine‑level (balanced‑ternary) quantizer. By enforcing this identity as a hard constraint inside the solver, the authors achieve a persistent serving representation where disk storage, expert‑cache memory, and kernel input all consist of identical 4.0625‑bit/weight blocks that are consumed in one integer dot pass. This conjunction—ratio‑3 nine‑level code, CPU‑SIMD kernels, SSD‑streamed experts, and a single persistent byte format—has never been combined before. The approach is applied to the DeepSeek‑V4‑Flash‑0731 Mixture‑of‑Experts model, yielding performance that matches the official serving API on most fixtures while delivering faster decode and smaller model files.

## Key Contributions  
- [Folding lossless into a uniform nine‑level quantizer via scale ratio constraint] The authors first prove that tying the two per‑group scales to a three‑to‑one ratio yields a balanced‑ternary identity, eliminating any residual scaling error.  
- [Persistent serving representation with identical 4.0625‑bit/weight blocks] They define a single persistent byte format that simultaneously serves as disk storage, expert‑cache memory, and kernel input, enabling lossless folding into one integer dot pass.  
- [First solver constraint on the balanced‑ternary identity] This work is the first to impose the nine‑level identity directly within PTQTP’s optimization loop, rather than treating it as a post‑hoc assumption.

## Methodology  
The authors start from the standard PTQTP decomposition of LLM weight matrices into two ternary planes with independent per‑group scales. They then add a hard constraint that the product of the two scale factors equals three, which mathematically forces the two planes to map onto the same nine‑level balanced‑ternary code. The resulting 4.0625‑bit/weight blocks are written once to disk and cached in experts, and both the kernel input and the output of the integer dot pass share these bytes. CPU‑SIMD kernels (aarch64/x86‑64) perform a single pass over the persistent data, eliminating redundant reads/writes. The model DeepSeek‑V4‑Flash‑0731 is quantized from its released MXFP4 expert weights and streamed via SSD under this format.

## Results  
Experiments on a 64 GB laptop compare the tied model against a baseline Q4_K (4.5‑bit) quantization. At step 0, the tied model matches the official serving API on 5/5 fixtures, while at captured continuation steps it scores 12/14, versus 4/5 and 11/14 for Q4_K. On a 100‑item MMLU subset, the tied model achieves 86 vs. 84 accuracy, decodes 6.7 % faster, and occupies 9 % less disk space. No fidelity difference is detected at these small evaluation sizes; any observed discrepancies trace to a single near‑tie cell. The tied quantization exhibits higher weight‑reconstruction error and worse perplexity, indicating a dissociation between proxy metrics (speed, size) and reference fidelity.

## Significance  
This work bridges quantization efficiency with serving infrastructure by providing a unified persistent format that eliminates the need for multiple passes over memory. It demonstrates that imposing mathematical identities can improve both performance and storage without sacrificing model quality at small scales, offering a template for future mixed‑expert deployments where latency and bandwidth are critical.

## Related Concepts  
- PTQTP (Post‑Training Quantization with Two Ternary Planes)  
- Balanced ternary / nine‑level quantizer  
- Persistent serving representation  
- Mixture‑of‑Experts (MoE) model quantization  
- SSD streaming of expert weights  
- CPU‑SIMD integer dot kernels
