# Summary: 2026-08-02_23-10-04Z_Celty_SpMspVGPUKernelandSIMTCo_DesignforEfficientD.md
Saved: 2026-08-03 23:34
Source: 2026-08-02_23-10-04Z_Celty_SpMspVGPUKernelandSIMTCo_DesignforEfficientD.md
Model: None

---

## Summary  
The paper addresses the challenge of dual‑sparse LLM inference where both weight and activation sparsity are present, forming a spMspV workload that existing GPU kernels cannot efficiently handle. It proposes Celty, a co‑designed sparse format (RLC‑CSC), GPU kernel, and SIMT microarchitecture to exploit both sparsities for single‑user decoding. The goal is to achieve higher throughput and lower latency compared to standard libraries like cuBLAS and Flash‑LLM. By integrating the RLC decoder into the Sparse SIMT Core, Celty eliminates software‑level index reconstruction and reduces peak occupancy.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Introduces Run‑Length Compressed CSC (RLC‑CSC) format that compresses sparse weight columns while preserving column order for vectorized loading.  
- [Finding 2] Designs a pipelined RLC decoder within the Sparse SIMT Core to reconstruct indices on‑the‑fly, eliminating costly software index passes.  
- [Finding 3] Utilizes local register files for conflict‑free accumulation of partial products directly from the compressed CSC layout.

## Methodology  
The authors tackled the spMspV problem by first analyzing how existing kernels waste memory bandwidth and compute due to dense row access. They then designed a hardware‑aware sparse format (RLC‑CSC) that stores only non‑zero entries per column, enabling SIMD loads. The GPU kernel streams these compressed columns into shared memory, where the Sparse SIMT Core decodes run‑lengths and feeds partial products directly into registers for accumulation, avoiding intermediate dense matrices.

## Results  
Experimental evaluation on a 70% dual‑sparsity LLM model shows Celty achieving up to 2.8× speedup over cuBLAS and 5.3× over Flash‑LLM at the peak sparsity level. The Sparse SIMT Core alone yields 5.3× improvement, while the RLC‑CSC format reduces memory traffic by ~40% compared with dense CSC. These gains translate to lower latency for single‑user decoding, which is critical for real‑time applications.

## Significance  
This work demonstrates that hardware co‑design can unlock performance gains beyond software optimizations, especially for emerging sparse inference workloads. By aligning data layout and compute pipeline, Celty sets a new benchmark for spMspV kernels and encourages future research on hybrid sparsity models in LLMs.

## Related Concepts  
- Sparse Matrix‑Sparse Vector (spMspV) workload  
- Run‑Length Compressed CSC (RLC‑CSC) format  
- SIMT core with pipelined RLC decoder  
- Shared memory partial‑product accumulation  
- cuBLAS and Flash‑LLM baselines
