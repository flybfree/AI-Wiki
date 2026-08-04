# Summary: 2026-08-01_01-59-12Z_TheGate_NottheCache_GateProvenanceBoundstheClosed_.md
Saved: 2026-08-03 23:50
Source: 2026-08-01_01-59-12Z_TheGate_NottheCache_GateProvenanceBoundstheClosed_.md
Model: None

---

## Summary  
The paper investigates why token‑skipping in vision‑language‑action (VLA) models can degrade performance when the skip decision is derived from a previously accelerated forward pass. By showing that the two underlying mechanisms—reuse and deletion—interact with gate provenance, the authors demonstrate that self‑harvested gates cause hidden collapses that are invisible to downstream detectors. Their contribution is an “actuation‑slack refresh” technique that injects a clean dense pass between control steps, preserving both speed and reliability.

## Key Contributions  
- [Finding 1] The gate’s provenance—whether it comes from a fresh dense forward or from the model’s own accelerated history—determines closed‑loop reliability; token skipping alone does not cause failure.  
- [Finding 2] When the gate is harvested from prior acceleration, both reuse and deletion mechanisms amplify errors across control steps, leading to measurable performance drops that detectors miss.  
- [Finding 3] An unconditional “actuation‑slack refresh”—a dense pass run while the robot executes its current chunk off the critical path—restores a clean gate and fresh KV base, recovering accuracy to near‑dense levels.

## Methodology  
The authors compare two token‑skipping mechanisms (reuse and deletion) on identical episodes under three gate sources: a dense 1.00 pass, reuse of a self‑harvested gate, and deletion of the same gate. They measure collapse rates at a skip ratio of 0.9 on LIBERO‑Object, finding severe degradation only when the gate is self‑generated (0.68 under reuse, 0.31 under deletion) versus the pristine dense baseline (1.00). The hidden nature of the failure is confirmed by action‑level detectors that remain unaffected.

## Results  
The actuation‑slack refresh recovers performance to 0.98 at skip ratio 0.9 while maintaining the speed advantage of token skipping. Integrated into state‑of‑the‑art caching and pruning across four LIBERO suites and four SIMPLER tasks, latency drops 18–22 % below dense execution. The experiments confirm that gate provenance, not the skipping mechanism itself, governs reliability.

## Significance  
Closed‑loop VLA training‑free acceleration must preserve a clean gate signal; otherwise hidden degradation accumulates silently. By decoupling speed from gate contamination through an unconditional refresh, the paper enables high‑throughput VLA agents without sacrificing task success, a critical step for real‑world robotics.

## Related Concepts  
Token skipping, closed‑loop reinforcement learning, VLA models, KV cache, gate signal provenance, caching strategies, pruning techniques.
