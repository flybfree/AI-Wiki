---
title: Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems
url: http://arxiv.org/abs/2610.31553v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_16-57-01Z_ContestableAgentsforDataGovernance_RecordingHumanS.md
generated_at: 2026-10-22 22:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "contestable governance," a framework in which specialist LLM-based agents generate scored, cited arguments for disputed metadata decisions, and a human steward can accept, reject, modify, or add arguments before any decision is committed to a governance record. The authors demonstrate the pattern through two HVAC use cases—point classification using Brick Schema labels and a warranty failure-mode decision linking claim fields, telemetry, and service notes—showing how structured and unstructured operational data can be governed through a single auditable workflow rather than siloed pipelines.

## Key Takeaways
- Contestable governance replaces perfunctory human approval with a structured review workflow: agents produce scored, cited arguments for uncertain metadata proposals, and a steward must explicitly accept, reject, modify, or add arguments before commit, ensuring the governance record retains the evidence, interventions, and final outcome rather than a bare sign-off.
- A triage path reserves full argumentation and multi-agent debate only for uncertain proposals, while simpler cases still require review before commit, balancing computational cost against the need to prevent unreviewed AI-generated errors from propagating into downstream operational systems such as telemetry dashboards and transaction logs.
- A versioned domain glossary supplies model-specific terms and acronym definitions to the agents, and a precedent gate controls which verified decisions become reusable reference points, preventing drift in classification labels (e.g., Brick Schema class labels for HVAC points) and ensuring that warranty failure-mode decisions remain traceable to revisioned service bulletins and inspection reports.

## Context
Industrial data governance has long treated structured telemetry and unstructured documents as separate domains, relying on a small cadre of domain experts to classify, link, and document them. As LLM-based agents enter these pipelines, the field lacks a principled mechanism for recording what a human reviewer actually verified, creating audit gaps that regulators and downstream consumers cannot close. This paper addresses that gap by formalizing a human-in-the-loop argumentation protocol that makes stewardship explicit, auditable, and versioned across both structured and unstructured systems.

## Implications
For practitioners in facilities management, manufacturing, and asset-intensive industries, the framework offers a concrete path to deploy AI-assisted metadata governance without surrendering accountability: every decision carries a traceable chain of agent arguments, human interventions, and precedent gates. For the broader AI governance community, the contestable-agent pattern suggests that transparency and contestability—not merely model accuracy—should be first-class design requirements in any system where AI proposals touch operational records, compliance obligations, or safety-critical classifications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31553v1)
