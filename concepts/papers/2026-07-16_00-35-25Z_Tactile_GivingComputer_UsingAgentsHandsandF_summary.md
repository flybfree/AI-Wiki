# Summary: 2026-07-16_00-35-25Z_Tactile_GivingComputer_UsingAgentsHandsandFeet.md
Saved: 2026-07-23 23:44
Source: 2026-07-16_00-35-25Z_Tactile_GivingComputer_UsingAgentsHandsandFeet.md
Model: None

---

## Summary  
The paper introduces **Tactile**, an open‑source tool layer that gives computer‑using agents reliable “hands and feet” for desktop interaction by converting heterogeneous UI evidence into structured action‑grounded interface states. It replaces the brittle screen‑pixel clicking paradigm with a semantic observe‑ground‑act‑verify loop that prefers native actions, falls back to OCR‑grounded coordinates when visible text is best evidence, and records full provenance for replay and failure attribution. The authors demonstrate that adding Tactile improves success rates on macOSWorld tasks from 41.1 % to 50.0 % overall and from 45.2 % to 55.3 % on accessibility‑adapted tasks across multiple code agents.

## Key Contributions  
- [Finding 1] Tactile introduces a reusable execution substrate that maps heterogeneous UI evidence—OS accessibility semantics, OCR‑grounded text, and visual fallback regions—to structured target candidates with labels, roles, state, geometry, affordances, and verification cues.  
- [Finding 2] The system implements an observe‑ground‑act‑verify loop that prioritizes native semantic actions when available, uses OCR‑grounded coordinates as a fallback, and maintains full provenance for replay and failure attribution.  
- [Finding 3] Empirical evaluation shows consistent gains across Codex, Claude Code, OpenCode, and Goose on a 96‑task cross‑agent subset, raising overall success from 41.1 % to 50.0% and accessibility‑adapted success from 45.2 % to 55.3%.

## Methodology  
The authors approached the problem by analyzing how current agent interfaces treat UI as a single opaque screen layer, leading to loss of grounding and verification. They designed Tactile as middleware that parses OS‑level accessibility metadata (e.g., ARIA roles), extracts text via OCR with confidence scores, and identifies visual fallback regions. Each UI element is transformed into a compact target object containing actionable attributes. The loop observes the current state, grounds it to a target, acts using the most appropriate method, verifies outcome, and logs all steps for auditability.

## Results  
On macOSWorld‑style benchmark tasks, adding Tactile improves Codex Success@100 from 41.1 % to 50.0% overall and from 45.2 % to 55.3% on accessibility‑adapted tasks. A cross‑agent subset of 96 tasks shows similar improvements across all four models, indicating robust gains independent of the underlying language model.

## Significance  
This work demonstrates that reliable computer use is not solely a function of model strength but also of an execution substrate that exposes software actions as semantic, verifiable objects. By providing reproducible, auditable interfaces, Tactile reduces failure attribution ambiguity and enables debugging, which are critical for long‑term agent reliability in human‑in‑the‑loop settings.

## Related Concepts  
- Human‑computer interaction (HCI)  
- Accessibility semantics (ARIA, ATAG)  
- OCR‑grounded vision  
- Observe‑ground‑act‑verify loop  
- Agent execution substrate
