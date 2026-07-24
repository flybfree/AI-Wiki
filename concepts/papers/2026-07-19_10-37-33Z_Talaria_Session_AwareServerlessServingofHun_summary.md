# Summary: 2026-07-19_10-37-33Z_Talaria_Session_AwareServerlessServingofHundred_Bi.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_10-37-33Z_Talaria_Session_AwareServerlessServingofHundred_Bi.md
Model: None

---

## Summary  
Talaria tackles the challenge of serverless multi‑model LLM serving where a single user session repeatedly invokes different models across short tool gaps, carrying a long reusable KV prefix that must remain contiguous for high performance. The paper proposes a session‑aware router that jointly decides model placement and admission, optimizing for model residency, KV locality, instance pressure, and soft reservations to minimize the session completion time (SCT). By treating session continuity as the primary scheduling metric, Talaria avoids the latency penalties caused by independent request scheduling.

## Key Contributions  
- [Finding 1] The introduction of a joint placement‑and‑admission decision framework that treats session continuity as the central optimization goal.  
- [Finding 2] Implementation of session‑prefill (SP), which admits budget‑eligible continuations before the active model slot closes, preventing unnecessary round delays.  
- [Finding 3] Design of an instance‑local substrate that stabilizes HBM addresses and stages weights across model switches to preserve KV locality.

## Methodology  
The authors first analyze existing serverless systems that schedule each request independently, leading to high SCT for long sessions with large models and extensive KV. Their approach introduces a router that ranks placements based on three factors: (1) model residency—ensuring the heavy weights of >100B‑parameter models fit within the instance; (2) KV locality—maintaining stable HBM addresses so the long prefix does not need reconstruction or movement; and (3) instance pressure—balancing GPU availability. Soft reservations allocate a portion of the admission budget to anticipate returns, while session‑prefill pre‑admits continuations before the slot expires. An instance‑local substrate keeps HBM addresses constant across model switches and stages weights in a buffer for rapid reintegration.

## Results  
On a single TP=8 server, Talaria replayed 30 SWE‑Bench model sessions (960 calls) using three models each exceeding 100B parameters. Compared with an otherwise identical round scheduler that lacked SP, host‑KV restoration, and D2D staging, Talaria reduces the p50 SCT from 1000 s to 189 s and the p95 SCT from 2296 s to 867 s, delivering speedups of 5.3× and 2.6× respectively.

## Significance  
By making session continuity a core scheduling criterion, Talaria dramatically improves user experience for serverless LLM services handling massive models and long‑range KV contexts, reducing latency and resource waste while preserving model quality.

## Related Concepts  
Serverless multi‑model serving, GPU pool multiplexing, KV locality, instance admission budget, soft reservations, session prefill, HBM address stability, D2D staging, round‑based scheduling.
