# Summary: 2026-07-26_15-26-00Z_FormallyVerifiedSynthesizableFloating_PointDataTyp.md
Saved: 2026-07-27 22:42
Source: 2026-07-26_15-26-00Z_FormallyVerifiedSynthesizableFloating_PointDataTyp.md
Model: None

---

## Summary  
The paper presents a fully verified, synthesizable representation of IEEE‑754 binary32 (FP32) and bfloat16 (BF16) arithmetic in the ARCH HDL language model. It proves that every operator—comparisons, conversions, addition/subtraction, multiplication, and fused multiply‑add (FMA)—maps to a single bit‑vector intermediate representation while generating three equivalent artifacts: SystemVerilog code, an SMT‑LIB model, and a Lean 4 proof model. The verification is split between exhaustive SAT‑based checks for multiplier‑free operators and a sound Lean proof of correct rounding for the multiplier‑bearing FMA/FP32 mul. Physical implementation on Nangate45 shows that the exact‑wide FMA’s 470‑bit datapath can be replaced by a pipelined 98‑bit guard/round/sticky pipeline without loss of correctness.

## Key Contributions  
- [Finding 1] A unified bit‑vector IR and three syntactically linked artifacts (SystemVerilog, SMT‑LIB, Lean) that stay structurally identical across all operators.  
- [Finding 2] Exhaustive equivalence proofs for multiplier‑free operators using the SMT‑LIB FloatingPoint theory; correct rounding proofs for FMA/FP32 mul via Lean without SAT solving of multiplier equivalence.  
- [Finding 3] A bounded 98‑bit datapath that pipelines to 268 MHz on Nangate45, proven bit‑identical to the exact‑wide reference over all 2⁹⁶ inputs.

## Methodology  
The authors first encode each operator against a canonical bit‑vector IR, then synthesize three representations: SystemVerilog for hardware synthesis, an SMT‑LIB model for automated verification, and a Lean 4 proof script that directly mirrors the IR. Verification is performed via a Yosys‑to‑SMT miter to check structural equivalence, followed by exhaustive SAT solving for operators lacking multipliers and a sound Lean proof for those involving multipliers. The FMA’s datapath is reengineered as a guard/round/sticky pipeline; correctness is verified in Lean over the full input space.

## Results  
Theoretical results: 24 operators are structurally equivalent across artifacts; multiplier‑free operators are provably equivalent to SMT‑LIB theory for all 2⁶⁴ inputs; FMA/FP32 mul are correctly rounded for all exact dyadic values via Lean. Experimental results: the pipelined 98‑bit FMA runs at 268 MHz on Nangate45, matching the exact‑wide implementation’s performance and rounding behavior.

## Significance  
This work bridges formal verification and hardware synthesis in a language model context, enabling trustworthy floating‑point arithmetic without sacrificing throughput. By proving correctness at the bit level and providing a pipelined, synthesizable FMA, it addresses a longstanding bottleneck in low‑latency AI accelerators.

## Related Concepts  
IEEE‑754 binary32, bfloat16, ARCH HDL, SystemVerilog, SMT‑LIB, Lean 4, correct rounding, fused multiply‑add (FMA), guard/round/sticky datapath, pipelining, Nangate45.
