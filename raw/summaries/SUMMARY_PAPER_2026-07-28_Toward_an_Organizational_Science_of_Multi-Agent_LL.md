---
title: Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm
url: http://arxiv.org/abs/2607.25446v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_08-35-21Z_TowardanOrganizationalScienceofMulti_AgentLLMSyste.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces IMACS, a framework that separates the three logical concerns of multi‑agent LLM systems—who is on the team, how members coordinate, and which algorithm fuses their work—into orthogonal layers. Controlled experiments demonstrate that accountability placement changes outcomes only when the collaboration protocol routes deliverables through the accountable agent, while an adaptive meta‑protocol called Adaptive Org Routing outperforms all fixed protocols by learning optimal choices online.

## Key Takeaways
- Organizational assignments can be independently swapped while keeping the same collaboration protocol intact.  
- Accountability placement influences outcomes exactly when the protocol routes the deliverable through that agent, revealing a direct link between accountability and results.  
- Adaptive Org Routing meta‑protocol selects the best protocol per task under an explicit quality‑cost tradeoff and outperforms every fixed protocol in controlled studies.

## Context
Multi‑agent frameworks built on large language models often treat organizational theory and algorithmic fusion as inseparable, limiting systematic study of each factor. This work decouples them, allowing researchers to isolate how role assignments affect performance without altering the underlying collaboration logic.

## Implications
The separation enables organizations to tailor team structures without re‑engineering algorithms, improving deployment flexibility across model families. Practitioners must view organizational design as a variable that can be validated or learned per binding, not hard‑coded, fostering more resilient and adaptive AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25446v1)
