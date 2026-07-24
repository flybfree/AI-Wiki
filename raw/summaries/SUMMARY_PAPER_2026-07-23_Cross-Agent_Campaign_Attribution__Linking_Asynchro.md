---
title: Cross-Agent Campaign Attribution: Linking Asynchronous Attacks Across LLM Agents
url: http://arxiv.org/abs/2607.18826v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_08-01-51Z_Cross_AgentCampaignAttribution_LinkingAsynchronous.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a method for linking attacks that occur across multiple LLM agents without sharing runtime state or attacker identity. It proposes Asynchronous Attribution Fingerprint Vectors which score similarity between sessions using proxy‑observable cues such as tool use, timing and prompt residue. Experiments on the SCD‑v1 benchmark show the approach achieves high pairwise AUC while simpler detectors perform near chance.

## Key Takeaways
- The framework links asynchronous campaigns across independent agents by measuring structural and stylometric residues from each session.
- Pairwise similarity scores derived from A2FV outperform per‑session detectors that rely only on local judgments.
- Timing information is retained as a diagnostic channel but does not dominate the signal.

## Context
LLM agent security research often evaluates defenses in isolation, treating each interaction as independent. This limits detection of coordinated attacks that span multiple agents and runtimes. The need for cross‑agent attribution arises from real‑world deployments where adversaries can orchestrate campaigns without a central oracle.

## Implications
For practitioners, the paper provides a lightweight proxy‑side protocol that can be integrated into existing guardrail pipelines. It highlights the importance of capturing non‑oracle cues across sessions to improve campaign detection in dynamic AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18826v1)
