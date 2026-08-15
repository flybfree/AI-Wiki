**Original paper:** [https://arxiv.org/abs/2608.12761v1](https://arxiv.org/abs/2608.12761v1)

# Summary: 2026-08-13_03-12-13Z_CorrectIsNotGoverned_ProvenanceIntegrityinAgenticW.md
Saved: 2026-08-13 22:36
Source: 2026-08-13_03-12-13Z_CorrectIsNotGoverned_ProvenanceIntegrityinAgenticW.md
Model: None

---

## Summary  
This paper argues that merely achieving the correct outcome is insufficient for institutional trust in agentic workflows; a work must be governed by inspectable provenance to guarantee authority, fact dependencies, and sound completion evidence. The authors introduce **Matrix**, a deterministic causal‑state layer that records these governance signals, verifies evidence, and can selectively invalidate affected tasks. Experiments compare governed versus direct workflows and demonstrate that while outcomes often match, only the governed path retains full evidential integrity and respects change constraints. A role‑separated transfer challenge further reveals that overly strict completeness contracts can block legitimate synthetic packets generated outside an authoring context.

## Key Contributions  
- [Finding 1] Governed execution is defined as work whose decisions, completion, and response to change are supported by inspectable provenance, distinguishing it from mere correctness.  
- [Finding 2] Matrix records authority and fact dependencies deterministically, enabling verification of completion evidence and selective invalidation of affected work.  
- [Finding 3] Governed workflows preserve governing evidence, refuse unsupported closure, limit recovery to dependent tasks, whereas direct workflows lack these safeguards.

## Methodology  
The authors approached the problem by constructing a deterministic causal‑state layer—Matrix—that captures every authority and fact relationship in an agentic workflow. The system logs provenance events, ties them to completion evidence, and enforces that any change must be traceable through this graph. Experiments were conducted in controlled settings where both governed and direct execution paths produced the same computational outcome, allowing a side‑by‑side comparison of governance fidelity.

## Results  
Across controlled comparisons, governed and direct workflows often reached identical outcomes; however, only the governed path consistently retained governing evidence, refused to close unsupported tasks, and limited recovery to dependent subtasks. The role‑separated transfer challenge showed that a deterministically enforced completeness contract could over‑block synthetic packets produced outside the authoring context, indicating an overly restrictive governance model.

## Significance  
These results do not prove Matrix improves accuracy; instead, they highlight its role as an institutional integrity layer that makes agentic work auditable and independently verifiable. By enforcing provenance, authority, and fact dependencies, the paper advances trustworthy AI systems where correctness alone is inadequate for compliance or accountability.

## Related Concepts  
- Provenance (traceability of data and decisions)  
- Authority and fact dependencies in causal graphs  
- Deterministic execution layers  
- Completion evidence verification  
- Synthetic packet generation  
- Completeness contracts  
- Agentic workflows
