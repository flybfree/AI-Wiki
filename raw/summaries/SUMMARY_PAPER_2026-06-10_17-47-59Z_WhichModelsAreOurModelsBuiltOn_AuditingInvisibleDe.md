---

title: Which Models Are Our Models Built On? Auditing Invisible Dependencies in Modern LLMs
url: http://arxiv.org/abs/2606.12385v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_17-47-59Z_WhichModelsAreOurModelsBuiltOn_AuditingInvisibleDe.md
generated_at: "2026-06-11 10:56"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces ModSleuth, an agentic system that reconstructs LLM dependency graphs from public artifacts using source‑grounded evidence. It recovers 1,060 verified dependencies across four releases and shows complex multi‑hop relationships.

## Key Takeaways
- The primary challenge is not extracting information but defining what counts as a dependency and reconciling inconsistent artifact references.
- ModSleuth distinguishes direct from indirect dependencies using operation‑centered relationships to model heterogeneous pipeline roles.
- It resolves artifact identities across names, versions, and repositories, revealing multi‑hop license obligations and discrepancies between released and training‑time artifacts.

## Context
Modern LLM development relies on a web of external models that generate data, filter corpora, and guide decisions. This hidden ecosystem makes it hard to trace the full chain of influences and compliance requirements.

## Implications
Understanding these dependencies is crucial for auditing licensing, ensuring reproducibility, and preventing unintended model misuse. Practitioners can use ModSleuth to build transparent pipelines and mitigate regulatory risk.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12385v1)
