---
title: ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping
url: http://arxiv.org/abs/2607.27528v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_23-46-23Z_ThreatForest_Multi_AgentAttackTreeGenerationwithPl.md
generated_at: 2026-07-30 20:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
ThreatForest is a multi‑agent system that turns a code repository into a structured attack tree, maps each step to adversary tactics, techniques, and procedures using pluggable frameworks such as MITRE ATT&CK, CAPEC, or cloud threat matrices, and produces evidence‑based mitigations. The authors demonstrate that the embedding stage, which assigns cosine similarity between attack steps and technique embeddings, is the dominant source of accuracy loss across seven application domains. Their evaluation shows panel scores of 0.63–0.68 for threat statements, attack trees, and mitigations, while TTP mapping alone scores only 0.29.

## Key Takeaways
- The embedding‑based cosine similarity step is the primary bottleneck in TTP mapping, limiting overall system accuracy despite a well‑designed pipeline.  
- ThreatForest’s multi‑stage agent architecture includes deterministic verification gates and three human‑in‑the‑loop validation points to ensure reliability.  
- A single‑call baseline on the same model can double defensibility, indicating that the limitation lies in the embedding encoder rather than the overall design.

## Context
This work addresses a longstanding challenge in secure software development: automating threat modeling for cloud‑native architectures where manual analysis is slow and expertise scarce. By leveraging large language models to generate attack trees and map them to standardized TTP frameworks, ThreatForest illustrates how AI can augment traditional security processes with scalable, reproducible outputs.

## Implications
For practitioners, ThreatForest offers a reusable framework that can be benchmarked against other AI‑driven threat modeling tools, highlighting the importance of embedding quality in downstream tasks. Industry adoption could accelerate risk assessment pipelines, reducing reliance on scarce security experts and enabling continuous integration of automated mitigations into development workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27528v1)
