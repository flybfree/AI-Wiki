# Summary: 2026-07-26_11-39-49Z_DualityCert_Verifier_GatedLanguage_ModelRepairofBr.md
Saved: 2026-07-27 22:42
Source: 2026-07-26_11-39-49Z_DualityCert_Verifier_GatedLanguage_ModelRepairofBr.md
Model: None

---

## Summary  
The paper introduces DualityCert, a symbolic verifier that evaluates candidate Seiberg‑duality claims in four‑dimensional N=1 quiver gauge theories by checking t Hooft anomaly matching, R‑charge consistency, central‑charge agreement and a bounded chiral‑ring proxy. The verifier produces a “consistency certificate” that records which inconsistency tests failed rather than proving the claim true. DualityCert is then used as a repair environment for language‑model agents: each agent receives a deliberately broken duality statement and must edit it until the verifier certifies the revised version.  

## Key Contributions  
- [Finding 1] DualityCert provides a fast, symbolic verification pipeline that can be integrated into language‑model fine‑tuning loops to repair broken Seiberg‑duality claims.  
- [Finding 2] Verifier‑gated retry of language‑model repairs improves final success rates by +8.3 pp on deepseek‑chat and +7.1 pp on qwen‑plus compared with a single attempt, with the improvement statistically significant (Holm‑adjusted p < 0.002).  
- [Finding 3] Category‑level feedback from the verifier yields an additional +8.7 pp gain on qwen‑plus versus content‑free retries, while interpretable obligation identities add +6.4 pp; however, these benefits are not observed on deepseek‑chat.  

## Methodology  
The authors built DualityCert as a symbolic verifier that runs a suite of well‑defined tests on each candidate duality claim. The verification output is a binary certificate indicating whether any test failed. In the repair experiment, 145 broken claims were preregistered and presented to two large language models (deepseek‑chat and qwen‑plus). Agents could make up to eleven edits; strategies ranged from a single attempt to stop‑first policies versus multiple attempts with verification feedback. All per‑attempt logs, the benchmark data set and the verifier code are publicly released.  

## Results  
On deepseek‑chat, the verifier‑gated repair strategy improved success by 8.3 pp (p < 0.01). On qwen‑plus, it improved by 7.1 pp (p < 0.01). When a budget of eleven attempts was used, the stop‑first portfolio underperformed independent verifier‑filtered resampling by 10.3 pp on deepseek‑chat but outperformed it by 14.7 pp on qwen‑plus, reversing the ordering of the two policies across models. Category‑level feedback from DualityCert added +8.7 pp to qwen‑plus compared with content‑free retries and +6.4 pp versus interpretable obligation identities; no effect was seen on deepseek‑chat.  

## Significance  
These findings demonstrate that integrating a cheap, symbolic verification certificate into language‑model repair workflows can substantially boost the generation of correct Seiberg‑duality claims, with gains that depend on model architecture and feedback granularity. The work also highlights how lightweight verifier outputs can serve as actionable signals for fine‑tuning agents, opening avenues for automated scientific reasoning in quantum field theory.  

## Related Concepts  
Seiberg duality, t Hooft anomaly matching, R‑charge consistency, central charge matching, chiral ring proxy, language‑model fine‑tuning with verification constraints, preregistered benchmarking, symbolic certificate generation, stop‑first policy evaluation, interpretable obligation identities.
