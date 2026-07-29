# Summary: 2026-07-28_00-46-34Z_CondPSE_APolynomial_FilteredStructuralEncoderwithC.md
Saved: 2026-07-28 22:27
Source: 2026-07-28_00-46-34Z_CondPSE_APolynomial_FilteredStructuralEncoderwithC.md
Model: None

---

## Summary  
CondPSE introduces a learned positional‑structural encoder that injects topology‑derived signals into graph neural networks via a polynomial filter bank and FiLM‑style conditional modulation, thereby overcoming the limitations of 1‑WL bounded message passing. The encoder is pretrained to reconstruct both node‑level positional/structural targets and global invariants, after which it is frozen for use as an input encoding across downstream tasks. Experiments on synthetic structural‑discrimination benchmarks show a dramatic boost in CSL (42.9 % → 97.3 %) and EXP (68.3 % → 99.9 %) accuracy relative to the prior GPSE baseline, while real molecular property prediction yields only modest gains. The work demonstrates that strong synthetic structural discrimination can translate into downstream performance when integrated with appropriate message‑passing or attention backbones.

## Key Contributions  
- [Finding 1] CondPSE achieves state‑of‑the‑art accuracy on both CSL and EXP tasks, surpassing GPSE by >50 % points.  
- [Finding 2] The polynomial filter bank is the primary driver of improvement; ablation studies confirm its necessity for the gain.  
- [Finding 3] Conditional FiLM modulation conditioned on cross‑filter, local messages, and graph‑level signals refines the structural response without requiring additional training.

## Methodology  
CondPSE builds upon Positional‑Structural Encodings (PSE) by applying a learnable polynomial filter bank to standard Gaussian node probes. The filtered outputs are then processed through FiLM‑style modulation that is conditioned on three sources: cross‑filter interactions, local message‑passing results, and global graph invariants. During pretraining, the encoder learns to reconstruct both node‑level positional/structural targets and a set of graph‑level invariants; after pretraining it is frozen and injected as an input encoding into downstream models such as hybrid local‑message‑passing or global‑attention backbones.

## Results  
On synthetic benchmarks, CondPSE lifts CSL accuracy from 42.9 % to 97.3 % and EXP accuracy from 68.3 % to 99.9 %, compared with GPSE’s baseline of ~50 % and ~70 % respectively. Ablation experiments show that removing the polynomial filter bank drops performance back toward GPSE levels, confirming its central role. When used with a hybrid local‑message‑passing/global‑attention backbone on real ZINC molecular data, CondPSE matches GPSE’s performance but does not consistently outperform it; no ordering emerges across multiple backbone configurations.

## Significance  
CondPSE bridges the gap between theoretical structural information and practical downstream utility by providing a reusable, frozen encoder that captures topology‑specific signals. Its success on synthetic tasks highlights how learned PSE can improve graph representation, yet its real‑world gains are modest, underscoring the importance of task‑specific integration and potential label mismatches.

## Related Concepts  
- Positional‑Structural Encodings (PSE)  
- Graph Neural Networks with 1‑WL test limits  
- GPSE (Graph‑Pre‑trained Structural Encoder)  
- FiLM modulation for conditional conditioning  
- Polynomial filter banks in graph processing  
- Message passing and global attention architectures  
- Structural discrimination benchmarks (CSL, EXP)
