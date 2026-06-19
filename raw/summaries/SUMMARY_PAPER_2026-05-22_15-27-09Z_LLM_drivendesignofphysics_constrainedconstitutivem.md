---

title: "LLM-driven design of physics-constrained constitutive models: two agents are better than one"
url: http://arxiv.org/abs/2605.23754v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-22_15-27-09Z_LLM_drivendesignofphysics_constrainedconstitutivem.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces a multi‑agent system where an LLM Creator proposes constitutive models and an Inspector agent checks them against nine physical constraints, improving model validity from 91% to 100% for Claude Opus while preserving accuracy. The approach works with different LLMs (Claude Opus 4.7 and Kimi K2.5) across materials like brain tissue and rubber.

## Key Takeaways
- Adding an Inspector agent raises the share of exported models that satisfy all physical constraints from 91% to a perfect 100% for Claude Opus, while increasing it from 37% to 56% for Kimi.  
- The combined pipeline maintains near‑baseline accuracy and shows strong generalization to unseen loading paths.  
- Separating generation from inspection creates a trustworthy process that can be applied to any material or model type.

## Context
The paper addresses the challenge of generating physics‑aware models using LLMs, which traditionally lack systematic verification against fundamental laws. By integrating an inspector component, the method bridges the gap between rapid model creation and rigorous scientific validation, reflecting broader trends toward automated, reliable AI‑driven engineering workflows.

## Implications
For researchers and industry practitioners, this work offers a scalable framework that can be deployed across various domains without manual constraint checking, accelerating material modeling and enabling trustworthy deployment of LLM‑generated constitutive models in practice.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.23754v1)
