---
title: F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill
url: http://arxiv.org/abs/2607.25637v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_12-17-53Z_F_AI_2R_WhoDidWhat_andWhoChecked_VerifiableAIProve.md
generated_at: 2026-07-28 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces F(AI)2R, a framework that embeds AI in the research workflow both as an authoring assistant and as a verifiable provenance checker. The authors demonstrate that by treating every artefact—including this own manuscript—as a machine‑readable object, they can record who did what and who verified it using PROV-O standards. Their work shows that the system can be automated into an executable skill that runs continuously on each push to a repository.

## Key Takeaways
- The framework creates a provenance graph for every AI‑assisted artefact, ensuring no claim is parentless and all verification rungs are granted only by humans.
- It extends PROV-O with a specific extension (aiprov) designed for AI‑in‑the‑loop workflows, making the provenance model portable across domains.
- The system integrates with CI pipelines so that every push triggers graph conformance checks, publishing the current build as part of the artefact’s lifecycle.

## Context
Current research often relies on AI to draft or edit papers but leaves no trace of how those decisions were made. Without a formal audit trail, it is impossible to confirm authenticity or trace back claims to their sources. This paper addresses that gap by proposing a standardized provenance model and an automated skill that can be applied beyond scholarly writing.

## Implications
For researchers, the framework provides confidence that AI contributions are documented and verifiable, supporting reproducibility and trust in AI‑augmented work. For industry, it offers a blueprint for auditable AI processes across product development, enabling compliance with emerging regulatory standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25637v1)
