# Summary: 2026-08-10_07-47-57Z_GoverningtheKVCache_PreventingTimingSide_ChannelLe.md
Saved: 2026-08-10 23:56
Source: 2026-08-10_07-47-57Z_GoverningtheKVCache_PreventingTimingSide_ChannelLe.md
Model: None

---

## Summary  
The paper investigates how the key‑value (KV) cache, a core optimization for LLM inference, can be exploited as a timing side channel that allows an adversary to reconstruct another tenant’s private prompt. It introduces KVGov, a governance layer that cryptographically isolates each principal’s cache keys and mitigates three known attack families—PROMPTPEEK, EarlyBird, and InputSnatch—while preserving most of the caching efficiency. The authors also provide theoretical analyses showing when the defense is effective and how it behaves under realistic tenant heterogeneity.

## Key Contributions  
- [Finding 1] KVGov introduces a per‑principal salt σₚ = HMAC_K(secret, principal_id) that seeds the block‑hash chain, making cache keys cryptographically disjoint across tenants.  
- [Finding 2] An ablation study (N=1000 trials, deterministic judges) isolates σₚ as both necessary and sufficient for preventing reconstruction attacks.  
- [Finding 3] The evolutionary stability analysis reveals a tipping point of ~31.6 % adversary prevalence below which global caching remains stable.

## Methodology  
The authors model the cache‑hit latency as a function of principal identity, then embed σₚ at the boundary where prompts diverge rather than at the root of the hash chain. They simulate both vLLM and llama.cpp on real hardware (Qwen2.5‑7B‑Instruct, NVIDIA A100) to measure gate‑verified cold/cached TTFT ratios and compare them with a baseline without isolation.

## Results  
On Qwen2.5‑7B‑Instruct the defense reduces the cold‑to‑cached transition time from 0.22 × baseline, confirming that timing leakage is exploitable at production scale. The simulation calibrated to these measurements shows a 12.6 % reduction in adversary expected utility and an estimated 93 % retention of prefix‑cache benefit with no cross‑principal signal.

## Significance  
By decoupling cache keys per tenant, KVGov mitigates a previously unaddressed side channel that could compromise privacy in shared LLM environments. The theoretical stability analysis provides guidance for system designers on when isolation is sufficient and how heterogeneous workloads affect performance.

## Related Concepts  
- Key‑value (KV) cache  
- Timing side channel  
- Multi‑tenant inference  
- HMAC sealing / salt generation  
- Stackelberg water‑filling scheduler  
- Evolutionary stability analysis
