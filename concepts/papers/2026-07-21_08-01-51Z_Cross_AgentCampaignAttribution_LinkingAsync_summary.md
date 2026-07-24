# Summary: 2026-07-21_08-01-51Z_Cross_AgentCampaignAttribution_LinkingAsynchronous.md
Saved: 2026-07-24 00:33
Source: 2026-07-21_08-01-51Z_Cross_AgentCampaignAttribution_LinkingAsynchronous.md
Model: None

---

## Summary  
The paper tackles the problem of detecting coordinated adversarial campaigns that span multiple LLM‑agent sessions without a shared runtime state or attacker identity oracle. By formalizing *cross‑agent asynchronous campaign attribution*, it introduces a lightweight proxy‑side protocol called Asynchronous Attribution Fingerprint Vectors (A²FV) that scores pairwise similarity from observable tool‑use, timing, and prompt residue. The authors also construct the SCD‑v1 benchmark to evaluate this approach under realistic conditions of benign traffic, isolated attacks, multi‑session campaigns, and leakage audits. Their work shows that A²FV can reliably link sessions while conventional per‑session detectors fail.

## Key Contributions  
- [Finding 1] The authors formalize cross‑agent asynchronous campaign attribution as a distinct evaluation layer for LLM agents, enabling detection of coordinated attacks across independent runs without shared state or labels.  
- [Finding 2] They introduce Asynchronous Attribution Fingerprint Vectors (A²FV), a proxy‑observable reference protocol that computes pairwise similarity scores from tool‑use patterns, timing deltas, and prompt residues.  
- [Finding 3] The SCD‑v1 benchmark demonstrates A²FV achieving an AUC of 0.82 for campaign linking, whereas score‑only adaptations of per‑session detectors remain near chance.

## Methodology  
The authors approached the problem by first defining a formal model that treats each LLM session as a fragment of a larger adversarial campaign, even when sessions are executed in isolation. They designed A²FV to be implemented on the proxy side, extracting lightweight signals—such as which tools an agent calls, how long it takes, and leftover prompt text—that can be compared across sessions. To validate their framework, they built SCD‑v1: a controlled persona‑matched benchmark that includes benign traffic, isolated attacks, multi‑session campaigns, matched non‑oracle evasion attempts, and leakage audits. The evaluation measures how well A²FV scores separate paired campaign fragments while other methods degrade.

## Results  
On SCD‑v1, the pairwise AUC of A²FV is 0.82, indicating strong performance in linking sessions. Score‑only adaptations that rely solely on per‑session detectors achieve near‑chance accuracy (≈0.5), confirming that the signal is not captured by individual guardrail outputs. The strongest signals come from structural and stylometric residue—patterns in tool calls and prompt remnants—while timing provides a diagnostic channel for richer traces. Crossed‑style controls show the linkage is partly style‑sensitive but cannot be reduced to style alone. Static and dimension‑aware non‑oracle stress tests further confirm that pairwise separability persists under controlled evasion attempts.

## Significance  
This work establishes cross‑agent campaign attribution as a crucial layer for securing LLM agents in production environments where attacks may be distributed across multiple independent systems. By providing a reliable, lightweight proxy‑side method and a benchmark that captures real‑world fragmentation, the authors enable early detection of coordinated adversarial behavior without requiring shared state or attacker oracles.

## Related Concepts  
LLM‑agent defenses, guardrails, adversarial campaigns, asynchronous attacks, pairwise similarity scoring, stylometric analysis, timing traces, non‑oracle evasion, benchmarking frameworks.
