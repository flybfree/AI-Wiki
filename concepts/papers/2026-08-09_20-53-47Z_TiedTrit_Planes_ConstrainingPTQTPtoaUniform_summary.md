# Summary: 2026-08-09_20-53-47Z_TiedTrit_Planes_ConstrainingPTQTPtoaUniformNine_Le.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_20-53-47Z_TiedTrit_Planes_ConstrainingPTQTPtoaUniformNine_Le.md
Model: None

---

## Summary  
The paper introduces **Tied Trit‑Planes**, a novel approach that forces the PTQTP (Post‑Training Quantization of Tensor Parallelism) weight decomposition into a single, uniform nine‑level quantizer by tying the two ternary planes to a fixed scale ratio. This constraint eliminates the need for separate per‑group scales and enables the two trit planes to fold losslessly into one 4‑bit code plane. The resulting representation is persistent across disk, expert cache, and kernel input, allowing SSD‑streamed mixture‑of‑experts serving with identical byte blocks on CPU‑SIMD hardware. The authors demonstrate that this tied formulation matches the official DeepSeek‑V4‑Flash‑0731 API while delivering faster decode times and smaller model files without detectable fidelity loss at small evaluation scales.

## Key Contributions  
- [Finding 1] **Uniform nine‑level quantizer**: By tying the two ternary planes to a fixed three‑to‑one scale ratio, PTQTP collapses into a single balanced‑ternary identity that can be represented with exactly nine quantization levels.  
- [Finding 2] **Persistent folded format**: The two trit planes are concatenated into one 4‑bit code plane (4.0625 bits per weight), which is stored identically on disk, in the expert cache, and as kernel input, enabling seamless SSD streaming.  
- [Finding 3] **Benchmark match with Q4_K baseline**: On DeepSeek‑V4‑Flash‑0731 (284 B‑A13B MoE), the tied model achieves identical serving scores to the official API on most fixtures and matches a 4.5‑bit Q4_K benchmark, while being 6.7 % faster in decode and 9 % smaller in file size.

## Methodology  
The authors start from the standard PTQTP decomposition of LLM weight matrices into two ternary planes with independent per‑group scales. They then impose a hard constraint that the scale ratio between the two planes is exactly three, which mathematically forces both planes to share the same identity matrix and thus merge into a single nine‑level quantizer. This merged representation is folded into a 4‑bit code plane (two trit bits plus a scaling bit). The resulting byte layout is identical across all storage layers—disk blocks, expert cache entries, and kernel input registers—allowing a single integer dot pass to read the weight block. The method is implemented with trunk‑ternarization ladders that progressively fold higher‑precision intermediate values into the final 4‑bit code while preserving lossless reconstruction for the MoE routing.

## Results  
Experiments were conducted on a 64 GB laptop using DeepSeek‑V4‑Flash‑0731’s MXFP4 expert weights and SSD‑streamed experts. The tied model was compared to a 4.5‑bit Q4_K baseline with an expert‑lossless anchor arm as control. On five fixtures, the tied model matched the official serving API at step 0 (Q4_K: 4/5) and captured 12 of 14 continuation steps (11/14). MMLU scores were 86 vs. 84 on a 100‑item subset, decode latency was reduced by 6.7 %, and model file size shrank by 9 %. No fidelity difference was observed at these small evaluation sizes; any per‑fixture discrepancy traced to a single near‑tie cell. Theoretical analysis showed higher weight‑reconstruction error and worse perplexity, indicating a dissociation between proxy metrics (speed, size) and reference fidelity.

## Significance  
This work bridges the gap between theoretical quantization constraints and practical serving performance, showing that imposing a simple scale ratio can yield a uniform, persistent 4‑bit representation without sacrificing serving quality. By eliminating per‑group scales and enabling identical byte blocks across storage layers, it reduces memory bandwidth, speeds up decode, and shrinks model size—critical advantages for edge deployment of MoE models.

## Related Concepts  
- PTQTP (Post‑Training Quantization of Tensor Parallelism)  
- Uniform nine‑level quantizer / balanced ternary identity  
- Trit planes and folding into a 4‑bit code plane  
- Persistent serving format with identical disk, cache, and kernel input blocks  
- SSD streaming for mixture‑of‑experts weights  
- CPU‑SIMD kernels (aarch64/x86‑64)  
- Trunk‑ternarization ladder for lossless folding
