# Summary: 2026-05-08_13-08-18Z_FutureValidityistheMissingStatistic_FromImpossibil.md
Saved: 2026-05-10 21:00
Source: 2026-05-08_13-08-18Z_FutureValidityistheMissingStatistic_FromImpossibil.md
Model: None

---


## Summary  
The paper demonstrates that current speculative decoding techniques—local vocabulary masking, Leviathan rejection, and rollback—produce samples from a locally projected distribution rather than the intended grammar‑conditional distribution. It introduces the future‑validity function Φ_t(y) as a missing correction statistic that would align the decoder’s output with the true grammar‑conditional law. By providing exact or approximate Φ, the authors show how to transform speculative decoding into a faithful sampling process. The work bridges an earlier impossibility result for grammar‑constrained generation with practical estimators for tractable grammars.

## Key Contributions  
- [Finding 1] Any speculative decoder that uses local mask access, Leviathan rejection, and rollback samples from the locally projected distribution μ^{proj} instead of the target grammar‑conditional distribution μ★.  
- [Finding 2] The future‑validity function Φ_t(y)=Pr_p[valid completion | y] is identified as the missing statistic; the desired output distribution is a Doob transform of the base model with h=Φ.  
- [Finding 3] Exact Φ yields an oracle decoder FVO‑Spec that samples exactly μ★, while approximate estimators (e.g., one‑step correction and exact dynamic programming) bound the total‑variation error; exact DP reduces TV by 97 % on Dyck grammars.

## Methodology  
The authors first formalize the gap between μ^{proj} and μ★, then define Φ_t(y) as a conditional probability of completing the masked token sequence to a valid parse. They propose an oracle decoder FVO‑Spec that uses exact Φ for perfect sampling. For real‑world grammars, they evaluate estimator hierarchies: a one‑step correction (OneStep) with minimal overhead, and exact dynamic programming on Dyck or finite JSON languages, which achieve near‑perfect fidelity.

## Results  
On Dyck grammars with Qwen3‑8B, the total‑variation gap between μ^{proj} and μ★ can reach 0.996. OneStep reduces this gap by 14 % while incurring less than 1 % additional throughput. Exact dynamic programming cuts the TV error to near zero (≈97 % reduction). Finite‑language correction for JSON languages attains numerical precision, eliminating remaining gaps.

## Significance  
By supplying the missing future‑validity statistic, the paper enables speculative decoding to respect grammatical constraints, improving user experience and model utility. The results provide concrete performance gains—sub‑1 % overhead with 97 % TV reduction—demonstrating that theoretical impossibility can be overcome for enumerable grammars.

## Related Concepts  
- Grammar‑conditional distribution μ★  
- Locally projected distribution μ^{proj}  
- Doob transform of a base model with h=Φ  
- Future‑validity function Φ_t(y)  
- Speculative decoding (local mask, Leviathan rejection, rollback)  
- Total variation distance between distributions  
- Dyck grammars and finite JSON languages  
- Oracle decoder FVO‑Spec  
- OneStep correction estimator  
- Exact dynamic programming for Φ estimation

[[2026-05-08_13-08-18Z_FutureValidityistheMissingStatistic_FromImpossibil.md]]