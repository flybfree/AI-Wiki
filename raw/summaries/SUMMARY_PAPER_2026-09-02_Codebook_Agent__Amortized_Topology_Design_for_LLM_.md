---
title: Codebook Agent: Amortized Topology Design for LLM Multi-Agent Systems
url: http://arxiv.org/abs/2609.02264v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-10-22Z_CodebookAgent_AmortizedTopologyDesignforLLMMulti_A.md
generated_at: 2026-09-02 20:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Codebook Agent, a framework that compresses successful communication topologies into a query‑independent 16‑entry codebook and uses a reward‑weighted MLP to generate topology distributions. This approach achieves higher accuracy than existing methods while cutting token consumption by up to 33 % compared with the strongest prior.

## Key Takeaways
- Topology search collapses to only six distinct graphs even when the codebook capacity grows from eight to sixty‑four, limiting diversity.
- Edge count is negatively correlated with measured token usage (Pearson r ≈ -0.4), meaning sparser graphs increase inference cost rather than reduce it.
- A message‑passing scorer cannot rank candidates in regimes where agents share a profile because the scorer is adjacency‑invariant.

## Context
In large language model multi‑agent systems, the communication topology directly affects both accuracy and efficiency. Current designs treat topology generation as a conditional graph problem that often requires iterative search or runtime message passing, which can be costly for real‑time deployment.

## Implications
Codebook Agent enables faster, token‑efficient deployment of agent topologies without additional computation at inference time, offering practical benefits for scalable AI agents in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02264v1)
