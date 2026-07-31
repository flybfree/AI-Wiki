# Summary: 2026-07-29_23-46-23Z_ThreatForest_Multi_AgentAttackTreeGenerationwithPl.md
Saved: 2026-07-30 20:24
Source: 2026-07-29_23-46-23Z_ThreatForest_Multi_AgentAttackTreeGenerationwithPl.md
Model: None

---

## Summary
ThreatForest is a multi-agent system designed to automatically generate structured attack trees from source code repositories and map each attack step to adversary tactics, techniques, and procedures (TTPs) across multiple frameworks such as MITRE ATT&CK, CAPEC, and cloud‑specific matrices. It synthesizes evidence‑based mitigations throughout the pipeline. The authors decompose threat modeling into a deterministic multi‑stage agent workflow with human‑in‑the‑loop validation points. A key finding is that the embedding stage for TTP mapping dominates accuracy performance.

## Key Contributions
- ThreatForest is the first end‑to‑end system that converts a code repository into TTP‑mapped attack trees with evidence‑based mitigations across multiple adversary frameworks.
- The embedding‑based cosine similarity step is identified as the dominant bottleneck in overall accuracy, while other pipeline components have minimal impact.
- A controlled single‑call baseline demonstrates that doubling defensibility comes from improving the embedding encoder rather than the multi‑agent architecture.

## Methodology
The authors approached the problem by designing a multi‑stage agent pipeline: repository analysis, context refinement, threat generation, parallel attack‑tree construction with TTP mapping and mitigation synthesis, and report generation. The workflow is represented as a directed graph with deterministic verification gates, bounded retries, and three human‑in‑the‑loop validation points. A domain‑specific sentence transformer maps each attack step to candidate techniques using cosine similarity.

## Results
Panel measurements on seven application domains yield quality scores of 0.63–0.68 for threat statements, attack trees, and mitigations, but only 0.29 for embedding‑only TTP mapping, indicating a stable gap across all domains that isolates the binding constraint. A single‑call baseline on the same model more than doubles defensibility, confirming that the limitation lies in the embedding encoder rather than the multi‑agent design.

## Significance
Threat modeling remains essential yet labor‑intensive for cloud‑native architectures; ThreatForest automates end‑to‑end generation and mapping, dramatically reducing manual effort. The system provides a reusable benchmarking framework for evaluating similar tools. By isolating the embedding bottleneck, it guides future research on more accurate TTP representations.

## Related Concepts
threat modeling, attack trees, TTP (MITRE ATT&CK, CAPEC), multi‑agent system, embedding similarity, cosine similarity, mitigation synthesis, human‑in‑the‑loop validation, directed graph pipeline, adversarial verification.
