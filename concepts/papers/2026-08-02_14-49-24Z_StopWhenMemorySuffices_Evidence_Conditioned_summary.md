# Summary: 2026-08-02_14-49-24Z_StopWhenMemorySuffices_Evidence_ConditionedProgres.md
Saved: 2026-08-03 23:27
Source: 2026-08-02_14-49-24Z_StopWhenMemorySuffices_Evidence_ConditionedProgres.md
Model: None

---

## Summary  
The paper tackles the challenge of balancing answer quality with inference latency in long‑horizon LLM agents by proposing a memory system that can terminate early when its stored evidence is sufficient. It introduces Router‑Mem, an evidence‑conditioned progressive execution framework that combines a cheap retrieval prefix with a lightweight sufficiency router to decide whether one token is enough for the current query. The approach is trained using evidence‑level supervision and distills rationale‑conditioned representations to improve decision accuracy. Experiments demonstrate that this system can achieve strong scores while cutting average inference time substantially compared with full memory execution.

## Key Contributions  
- **Finding 1:** Router‑Mem can deliver high answer quality (55.17 % on AMA‑Bench, 38.77 % on BEAM) without incurring the latency of exhaustive memory traversal.  
- **Finding 2:** Evidence‑level supervision combined with rationale‑conditioned representation distillation enables a single‑token decision that reliably predicts sufficiency.  
- **Finding 3:** The progressive execution reduces average inference time by 27.3 % on AMA‑Bench and 25.5 % on BEAM relative to full memory execution.

## Methodology  
Router‑Mem first extracts a shared low‑cost retrieval prefix that gathers relevant evidence from the agent’s history. This evidence is fed into a lightweight sufficiency router, which outputs a binary signal indicating whether early termination is safe. If the router predicts insufficiency, the system expands memory blocks by reusing additional retrieval hits and performs deeper analysis and aggregation. The training objective aligns the router output with human‑annotated evidence quality, while representation distillation transfers reasoning from full‑memory reasoning to the router’s decision layer.

## Results  
On AMA‑Bench, Router‑Mem scores 55.17 % with a 27.3 % reduction in average inference time compared with full memory execution; on BEAM it scores 38.77 % with a 25.5 % latency cut. These gains are achieved across multiple benchmarks, confirming that the progressive strategy yields both quality and efficiency improvements.

## Significance  
By decoupling evidence retrieval from exhaustive search, Router‑Mem addresses a core bottleneck in persistent LLM agents: the trade‑off between memory cost and response speed. The framework offers a scalable path toward adaptive intelligence where agents can store histories without prohibitive latency, enabling real‑world applications such as multi‑turn dialogue and long‑term planning.

## Related Concepts  
evidence‑conditioned progressive execution; sufficiency router; memory block expansion; retrieval prefix; evidence‑level supervision; rationale‑conditioned representation distillation.
