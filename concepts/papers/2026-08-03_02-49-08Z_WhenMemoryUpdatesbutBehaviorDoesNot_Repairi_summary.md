# Summary: 2026-08-03_02-49-08Z_WhenMemoryUpdatesbutBehaviorDoesNot_RepairingImpli.md
Saved: 2026-08-03 23:17
Source: 2026-08-03_02-49-08Z_WhenMemoryUpdatesbutBehaviorDoesNot_RepairingImpli.md
Model: None

---

## Summary  
The paper tackles the implicit policy adaptation (IPA) gap that occurs when a memory‑augmented agent retains outdated stored state while its generated response does not reflect the update, leading to suboptimal performance on benchmark tasks such as STALE. It identifies draft‑anchored verification as a structural cause of this gap and introduces StateAuditor, an audit system that inspects provenance from stored state to draft rather than checking only what is said in the draft. The solution creates candidate old‑to‑new transitions using timestamped evidence, pins each quotation deterministically to a single entry, and only allows verified chronologically newer evidence to trigger repair actions. Experiments on STALE show a clear improvement in VTA scores, while a matched control demonstrates that the gain is largely due to the transition machinery rather than added context.

## Key Contributions  
- [Finding 1] The IPA gap stems from draft‑anchored verification that cannot detect unstated stale dependencies because it looks only at what is said.  
- [Finding 2] StateAuditor audits stored state to draft, generating candidate transitions from timestamped evidence and deterministically pinning quotations to single entries for provenance validation.  
- [Finding 3] On STALE the pipeline raises VTA by +5.0 points (95 % CI [+2.9, +7.2]), whereas a matched control shows only a +0.6 increase, indicating that the benefit is driven by the transition machinery rather than generic memory augmentation.

## Methodology  
The authors designed StateAuditor as a two‑step process: first, they generate candidate old‑to‑new transitions from timestamped evidence present in the draft response; second, deterministic code validates that each quotation is linked to exactly one stored entry and that the new evidence is genuinely newer than the old. Only those verified transitions are permitted to initiate repair actions, thereby repairing implicit stale dependencies without altering the overall structure of agent behavior.

## Results  
On STALE’s full protocol (400 scenarios, 50‑session histories) the pipeline yields VTA = .736 versus .686 for the predecessor model, a paired gain of +5.0 points with a 95 % confidence interval [+2.9, +7.2]. A third‑party judge reproduces this result (.738 vs. .680). On HorizonBench, using a gold‑derived structured store, the pipeline improves user‑clustered preference accuracy (p < 0.01); however, a matched control shows that most of the gain originates from the draft‑side audit itself. A harder authored lifecycle set yields no improvement, bounding the claim while preventing false invalidation.

## Significance  
Repairing implicit stale dependencies can boost personalized agent performance when memory updates are not reflected in generated behavior, offering a targeted repair mechanism that does not require generic memory augmentation. The work demonstrates that provenance‑based auditing and deterministic transition validation can close the IPA gap on benchmark tasks where agents retain outdated state.

## Related Concepts  
Implicit policy adaptation (IPA), draft‑anchored verification, provenance checking, chronological validation, state auditor, VTA, HorizonBench, gold‑derived structured store.
