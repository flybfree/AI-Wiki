# Summary: 2026-08-07_12-36-52Z_NiyamAI_AnIntent_BoundAIAgentwithCryptographically.md
Saved: 2026-08-09 20:15
Source: 2026-08-07_12-36-52Z_NiyamAI_AnIntent_BoundAIAgentwithCryptographically.md
Model: None

---

## Summary  
The paper introduces **Niyam‑AI**, a framework that enforces safety constraints on autonomous LLM agents by making the enforcement mathematically provable through zero‑knowledge proofs. At runtime, an Intent Contract—committed via SHA‑256—lists permitted tools and constraints; every tool call is intercepted by an isolated Judge model, which generates a zk‑SNARK proof (EZKL) that third parties can verify without seeing the model’s weights. This approach eliminates reliance on opaque software checks and provides cryptographic guarantees that only authorized actions are taken. The contribution lies in combining intent‑bounded tool execution with verifiable guardrails, achieving higher safety than existing defenses while preserving performance.

## Key Contributions  
- **Intent Contract + zk‑SNARK Guardrail**: A SHA‑256‑committed Intent Contract defines allowed tools and constraints; each call is guarded by a zk‑SNARK proof generated via EZKL, enabling cryptographic verification.  
- **Performance‑aware Verification Pipeline**: The framework measures that proof generation adds ~2.3 s per approved action while verification takes ~50 ms, demonstrating that security overhead is acceptable for real‑world deployment.  
- **Empirical Superiority on Agent‑SafetyBench**: Niyam‑AI achieves an F1 score of 88.5% with a 1.1% false‑positive rate and outperforms NeMo Guardrails, Prompt Guard 2, and GPT‑OSS‑Safeguard in all paired tests (p < 0.0001).

## Methodology  
The authors approached the problem by first formalizing safety as an Intent Contract that is immutable after session start. They deployed an isolated Judge model to evaluate each tool call, and upon acceptance generated a zk‑SNARK proof using the EZKL library. The proof is sent to an external verifier; only if verification succeeds does the underlying LLM execute the action. This pipeline was evaluated on 2,000 real‑world scenarios from Agent‑SafetyBench, employing stratified cross‑validation and McNemar’s exact test for paired comparisons.

## Results  
The experimental results show that Niyam‑AI reaches an F1 score of **88.5 %** (bootstrap 95% CI: [85.19%, 91.88%]) with a low false‑positive rate of **1.1 %**. In head‑to‑head comparisons, Niyam‑AI wins **390** discordant scenarios against NeMo Guardrails (vs 20 losses), **115** vs Prompt Guard 2 (vs 13), and **384** vs GPT‑OSS‑Safeguard (vs 19). The paired test yields a p‑value < 0.0001 for each comparison, confirming statistically significant improvement.

## Significance  
By providing cryptographically verifiable guardrails, Niyam‑AI addresses the core vulnerability of autonomous LLM agents: hidden unsafe actions that cannot be proved to have been prevented. This work moves beyond opaque software filters toward trustworthy AI systems where stakeholders can audit compliance without exposing proprietary model weights, fostering adoption in high‑stakes domains such as finance and healthcare.

## Related Concepts  
- **Intent Contract**: A SHA‑256‑committed list of permitted tools and constraints.  
- **Zero‑Knowledge Proof (zk‑SNARK)**: A proof that a tool call complies with the Intent Contract without revealing the Judge model’s internal state.  
- **EZKL Library**: The implementation used to generate and verify the zk‑SNARK proofs.  
- **Agent‑SafetyBench**: A benchmark suite evaluating safety defenses across multiple LLM agents.
