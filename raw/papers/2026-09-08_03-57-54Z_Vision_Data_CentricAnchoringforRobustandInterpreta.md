---
title: Vision: Data-Centric Anchoring for Robust and Interpretable Agentic AI
published: 2026-09-08T03:57:54Z
authors: Arun Vignesh Malarkkan, Xinyuan Wang, Yanjie Fu
url: http://arxiv.org/abs/2609.08216v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vision: Data-Centric Anchoring for Robust and Interpretable Agentic AI

## Abstract
Agentic AI systems built on large language models fail in two persistent ways that scaling does not fix: they break under distribution shift, and they cannot explain the decisions they make. We argue these are co-symptoms of one structural deficiency in the data lifecycle that governs how agents are trained, evaluated, and deployed. Observational interaction logs record what an agent did, not what it would have done otherwise. They encode spurious correlations without controlled variation, so they lack the counterfactual structure needed to separate causal signal from coincidence or to validate an explanation. No model-centric method can recover invariances the data never contained. We present Data-Centric Anchoring: robustness and interpretability should be engineered into the data environment, not extracted from models after training. Our central contribution is the Data-Centric Agentic Loop, a four-stage framework of Curate, Augment, Constrain, and Attribute. The ordering is structural, not stylistic. Curation precedes augmentation because generative models amplify whatever bias they are trained on. Augmentation precedes constraint because invariance objectives are vacuous without variation across environments to be invariant to. Attribution closes the loop, converting observed failures into targeted data interventions for the next iteration. Each stage manufactures the preconditions of the next, which makes the loop self-correcting rather than merely sequential. We ground the framework in a failure-driven taxonomy that links four core failure modes to the data lifecycle: spurious feature reliance, distribution-shift fragility, uncertainty miscalibration, and explanation unfaithfulness. We close with the limits of this approach and the open problems that stand between it and practical deployment at scale.

## Metadata
- **Published**: 2026-09-08T03:57:54Z
- **Authors**: Arun Vignesh Malarkkan, Xinyuan Wang, Yanjie Fu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08216v1)