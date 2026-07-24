# Summary: 2026-07-21_08-01-51Z_Cross_AgentCampaignAttribution_LinkingAsynchronous.md
Saved: 2026-07-24 00:53
Source: 2026-07-21_08-01-51Z_Cross_AgentCampaignAttribution_LinkingAsynchronous.md
Model: None

---

## Summary  
The paper tackles the problem of linking asynchronous attacks that occur across independent LLM‑agent sessions, where no shared runtime state or attacker identity is available. By introducing a lightweight proxy‑side reference protocol called Asynchronous Attribution Fingerprint Vectors (A²FV), it enables pairwise similarity scoring from observable tool‑use, timing, and prompt residue without relying on a central oracle. The authors also construct SCD‑v1, a controlled benchmark that simulates multi‑session campaigns while preserving privacy and non‑oracle conditions.

## Key Contributions  
- A²FV provides a lightweight proxy‑side reference protocol for scoring pairwise campaign similarity using tool‑use, timing, and prompt residue.  
- SCD‑v1 constructs a controlled persona‑matched benchmark with benign traffic, isolated attacks, multi‑session campaigns, matched non‑oracle evasion, and leakage audits to evaluate A²FV without an oracle.  
- Empirical results show A²FV achieves 0.82 pairwise AUC on SCD‑v1 while score‑only adaptations of per‑session detectors remain near chance.

## Methodology  
The authors formalize cross‑agent asynchronous campaign attribution as a problem of linking sessions from the same latent adversarial campaign without shared state, test‑time labels, or an attacker identity oracle. They define A²FV as a vector that encodes structural and stylometric residues together with timing information derived from proxy‑observable artifacts such as tool calls, timestamps, and leftover prompt text. SCD‑v1 is built by creating multiple personas, injecting benign traffic, isolated attacks, and multi‑session campaign traces, then auditing for leakage to ensure the evaluation remains non‑oracle.

## Results  
On the SCD‑v1 benchmark, A²FV attains a pairwise AUC of 0.82, indicating strong ability to differentiate campaigns. Adaptive detectors that rely only on per‑session scores perform at chance level, demonstrating that the signal is not captured by simple aggregations. Structural and stylometric residues dominate the score, while timing adds diagnostic value but does not become dominant alone. Crossed‑style controls reveal that the signal is partly style‑sensitive yet cannot be reduced to style alone. Static and dimension‑aware non‑oracle stress tests confirm that pairwise separability persists under controlled evasion.

## Significance  
These findings establish cross‑agent campaign attribution as a distinct evaluation layer for securing LLM agents in production environments, enabling detection of coordinated attacks across independent agents without compromising privacy or requiring an oracle. The approach provides a practical proxy‑side metric that can be integrated into existing guardrail pipelines to monitor multi‑session threats.

## Related Concepts  
Asynchronous Attribution Fingerprint Vectors (A²FV), pairwise AUC, SCD‑v1 benchmark, cross‑agent campaign attribution, guardrail leakage, structural and stylometric residue, timing diagnostics, non‑oracle evasion.
