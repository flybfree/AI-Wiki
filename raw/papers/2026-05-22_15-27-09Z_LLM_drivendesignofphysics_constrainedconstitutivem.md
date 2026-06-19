---

title: 'LLM-driven design of physics-constrained constitutive models: two agents are better than one'
published: "2026-05-22T15:27:09Z"
authors: Marius Tacke, Matthias Busch, Kian Abdolazizi, Jonas Eichinger, Kevin Linka, Roland Aydin, Christian Cyron
url: http://arxiv.org/abs/2605.23754v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# LLM-driven design of physics-constrained constitutive models: two agents are better than one



**Source**: [Original Paper](http://arxiv.org/abs/2605.23754v1)
## Abstract
Developing constitutive models that capture how materials deform under load traditionally requires years of specialized expertise in continuum mechanics, machine learning, and scientific programming. Large language models (LLMs) have recently been shown to lower this barrier by generating constitutive models on demand, but existing single-agent pipelines lack systematic checks that the resulting models respect fundamental physical laws. To close this gap, we introduce the first multi-agent LLM-driven approach for constitutive model generation: a Creator agent proposes a model tailored to the data, while an Inspector agent critically audits each proposal against nine physical constraints and returns it for refinement whenever a violation is detected. We demonstrate this concept with constitutive artificial neural networks (CANNs) and benchmark it on brain tissue, experimental rubber, and synthetic rubber, using two different LLM backbones (Claude Opus 4.7 and Kimi K2.5). Adding the Inspector raises the share of exported models that truly satisfy all physical constraints from 91% to a perfect 100% for Opus and from 37% to 56% for Kimi, while preserving near-baseline accuracy and remarkable generalization to unseen loading paths. In combination, the generated models are physically valid, highly accurate, and extrapolate reliably beyond the training data - properties that together make them directly usable in practice. Separating generation from inspection thus turns LLM-driven constitutive modeling into a genuinely trustworthy process. The paradigm is deliberately technique-agnostic and scales automatically with advances in LLM capability, opening a promising path toward automated, physics-aware model discovery.

## Metadata
- **Published**: 2026-05-22T15:27:09Z
- **Authors**: Marius Tacke, Matthias Busch, Kian Abdolazizi, Jonas Eichinger, Kevin Linka, Roland Aydin, Christian Cyron
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23754v1)