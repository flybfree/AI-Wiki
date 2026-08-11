# Summary: 2026-08-10_07-47-57Z_GoverningtheKVCache_PreventingTimingSide_ChannelLe.md
Saved: 2026-08-10 23:40
Source: 2026-08-10_07-47-57Z_GoverningtheKVCache_PreventingTimingSide_ChannelLe.md
Model: None

---

## Summary  
The paper addresses timing side‑channel leakage in multi‑tenant LLM inference caused by shared key‑value (KV) caches, where an adversary can reconstruct a tenant’s private prompt by probing cache‑hit latency. It introduces KVGov, a governance layer that cryptographically isolates each principal’s cache using HMAC salts and a Stackelberg water‑filling scheduler to reduce the attacker’s expected utility. The solution preserves most of the caching efficiency while preventing reconstruction attacks across all known families (PROMPTPEEK, EarlyBird, InputSnatch). This work demonstrates both theoretical analysis and real‑hardware validation.

## Key Contributions  
- Finding 1: KVGov provides a per‑principal salt σp = HMAC_K(secret, principal_id) that makes cache keys cryptographically disjoint across tenants.  
- Finding 2: The Stackelberg water‑filling audit scheduler (ORIGAMI) reduces the adversary’s expected utility by ~12.6% under realistic tenant heterogeneity (Gini 0.63).  
- Finding 3: Evolutionary stability analysis shows a tipping point below which global caching remains stable, with a prevalence threshold of ~31.6%.

## Methodology  
The authors model the cache‑hit latency as a timing channel and formulate it as an adversarial utility maximization problem. They design KVGov to inject salts only at the boundary where prompts diverge, preserving prefix reuse benefits. The scheduler ORIGAMI dynamically balances caching and security by allocating resources based on principal priority. Experiments are run in simulation calibrated to hardware measurements.

## Results  
On Qwen2.5‑7B‑Instruct with vLLM 0.26.0 on NVIDIA A100, the gate‑verified cold/cached TTFT ratio is 0.22, confirming exploitability. KVGov’s simulation shows a 93% retention of prefix‑cache benefit and eliminates cross‑principal leakage. Independent replication on llama.cpp via Apple Metal yields a TTFT ratio of 0.093.

## Significance  
This work bridges cache efficiency and security in multi‑tenant LLM services, offering a practical governance mechanism that can be integrated into existing inference pipelines without sacrificing throughput.

## Related Concepts  
- KV Cache (key‑value memory for prefix reuse)  
- Timing side channel  
- Multi‑tenant isolation  
- HMAC cryptographic salt  
- Stackelberg water‑filling scheduler  
- Evolutionary stability analysis
