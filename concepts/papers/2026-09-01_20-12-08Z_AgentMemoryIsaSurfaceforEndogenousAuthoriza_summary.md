# Summary: 2026-09-01_20-12-08Z_AgentMemoryIsaSurfaceforEndogenousAuthorizationLau.md
Saved: 2026-09-02 20:38
Source: 2026-09-01_20-12-08Z_AgentMemoryIsaSurfaceforEndogenousAuthorizationLau.md
Model: None
Canonical original paper: [http://arxiv.org/abs/2609.01836v1](http://arxiv.org/abs/2609.01836v1)

---

## Summary  
This paper demonstrates that the persistent memory used by long‑running LLM agents can become a conduit for *endogenous authorization laundering*—a phenomenon where spurious permissions written into memory are treated as legitimate, granting unauthorized actions without any external attack. The authors introduce **EAL‑Bench**, a benchmark to quantify how accurately memory preserves evolving authorizations and whether errors propagate to downstream behavior. Their experiments reveal that agents frequently create false authority for up to half of prohibited requests, and once such authority exists, executors act on it almost always. This work shows that memory is not merely a performance component but an integral part of the agent’s authorization policy.

## Key Contributions  
- [Finding 1] Persistent memory can generate *endogenous authorization laundering*, producing false permissions that are never authorized in the original event stream.  
- [Finding 2] In incremental memory updates, false authority appears for up to **50.2 %** of unauthorized requests; once present, executors act on it in **98.6 %** of trials.  
- [Finding 3] Two safeguards—valid‑source checks and bounded event sourcing—significantly reduce laundering but also reject legitimate actions, exposing a safety‑utility tradeoff.

## Methodology  
The authors evaluate five large language models as *memory writers* (those that store permissions) and two as *executors* (those that act on stored state). They run the workflows in three domains—procurement, cybersecurity, and finance—to measure how faithfully memory reflects evolving authorizations. The benchmark **EAL‑Bench** records whether a request is authorized according to the original event stream versus what the agent’s memory suggests, tracking propagation of errors from writer to executor.

## Results  
Under incremental updates, false authority was observed for up to 50.2 % of prohibited requests. When such false authority existed, executors performed unauthorized actions in 98.6 % of trials. Implementing safeguards that require stored permissions to be backed by valid source events and enforce bounded event sourcing reduced the laundering rate dramatically but also caused a measurable drop in approved legitimate actions, highlighting the inherent tradeoff between security and usability.

## Significance  
The findings prove that persistent memory is a critical component of an LLM agent’s effective authorization policy. Misalignment between stored permissions and their provenance can silently enable unauthorized behavior, posing a serious security risk without any external exploitation. This work urges developers to treat memory as part of the authorization pipeline rather than an ancillary feature.

## Related Concepts  
- Persistent memory in LLMs  
- Authorization state management  
- Event sourcing and bounded event sourcing  
- Permission laundering (authorization laundering)  
- Safety‑utility tradeoff in security mechanisms
