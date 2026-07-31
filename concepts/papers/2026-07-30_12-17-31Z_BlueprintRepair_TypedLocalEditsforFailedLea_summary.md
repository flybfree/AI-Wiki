# Summary: 2026-07-30_12-17-31Z_BlueprintRepair_TypedLocalEditsforFailedLeanProofB.md
Saved: 2026-07-30 21:49
Source: 2026-07-30_12-17-31Z_BlueprintRepair_TypedLocalEditsforFailedLeanProofB.md
Model: None

---

## Summary  
The paper introduces **BlueprintRepair**, a repair interface that enables an LLM to fix failed Lean proof blueprints by applying ten schema‑checked, typed local edits. Each edit explicitly names the node it modifies, guaranteeing that the target theorem remains unchanged while only its surrounding statements are altered. The authors also create **BlueprintTrace**, a benchmark of 142 controlled failure cases with complete repair trajectories for comparison. By evaluating three different repair strategies—typed local edits, exact source patches, and full module rewrites—they demonstrate how typed edits achieve the best cost‑efficiency within token limits.

## Key Contributions  
- [Finding 1] BlueprintRepair provides a typed local edit framework that preserves theorem nodes while allowing the model to correct erroneous proof blueprints.  
- [Finding 2] The authors construct **BlueprintTrace**, a benchmark of 142 controlled failures with recorded accepted and rejected repair trajectories, enabling systematic comparison.  
- [Finding 3] Typed edits are the cheapest per solved state among the three interfaces (patching is 1.30× more expensive than rewriting), and they reach near‑final coverage within 10 000 tokens per task.

## Methodology  
The proof blueprint is modeled as a dependency graph of formal statements; each repair operation must declare its target node, ensuring that only the intended local change is applied. The system validates every edit against Lean’s schema and requires that all lemmas used by the repaired theorem be explicitly referenced. To assess performance, the authors run three interfaces—typed edits, exact source patches, and complete module rewrites—under matched source code, feedback, model, and budget conditions, one episode per state in BlueprintTrace.

## Results  
With **DeepSeek‑V4‑Flash**, all three repair methods solve almost the same number of localized failures. Typed repair is the least costly (patching 1.30× more expensive than rewriting), while complete rewrites are the most expensive (2.06×). Within a budget of 10 000 completion tokens per task, typed edits achieve almost all final coverage, whereas the free‑form interfaces lag significantly. A second model, **Qwen3.6‑Flash**, solves fewer states but still keeps typed repair cheapest and outperforms it on proof‑authoring states.

## Significance  
These findings show that structured, locally scoped edits can dramatically reduce token consumption compared to wholesale rewrites or patching, making LLM‑based theorem proving more scalable and cost‑effective. By limiting the scope of changes to a single node and requiring explicit dependencies, BlueprintRepair improves robustness while preserving proof integrity.

## Related Concepts  
- Lean proof blueprints (dependency graphs)  
- Schema‑checked local edits  
- Repair interfaces for LLM systems  
- BlueprintTrace benchmark with controlled failures  
- Typed vs. exact source patches  
- Complete module rewrites  
- Completion token budgeting  
- Proof‑authoring states
