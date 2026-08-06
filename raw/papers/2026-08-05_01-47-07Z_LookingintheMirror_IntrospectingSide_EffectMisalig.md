---
title: Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning
published: 2026-08-05T01:47:07Z
authors: Kotaro Yoshida, Laura Gomezjurado Gonzalez, Yukinori Yamamoto, Yuji Naraki, Ryotaro Shimizu, Wenya Wang
url: http://arxiv.org/abs/2608.04347v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning

## Abstract
Fine-tuning enables a source model to acquire desired capabilities and behaviors in a target domain while retaining much of its general-purpose competence. However, this adaptation process can also degrade alignment properties that were present in the source model. Recent work has shown that large language models can be trained using LoRA-based modules known as introspection adapters (IAs) to describe behavioral changes induced by fine-tuning. However, existing studies primarily consider settings in which the model is fine-tuned on datasets explicitly designed to implant a specific behavior and is then asked to explain the implanted behavior. This differs from practical deployment scenarios, where the central concern is often side-effect misalignment: unintended degradation of alignment caused by fine-tuning on tasks that are not obviously related to safety or alignment. To bridge this gap, we formulate a novel problem setting called \emph{side-effect introspection}, in which the target of introspection is not a behavior explicitly implanted through fine-tuning, but rather alignment shifts that emerge as unintended side effects, and we construct a dataset for this setting. Furthermore, to enhance sensitivity to internal model changes, we propose the Delta-Aware Introspection Adapter (DAIA), a novel mechanism designed to explicitly process both base-model activations and activation differences induced by fine-tuning. Our empirical evaluation shows that introspection learning generalizes to unseen fine-tuned models and safety categories, and that DAIA consistently outperforms existing introspection adapters.

## Metadata
- **Published**: 2026-08-05T01:47:07Z
- **Authors**: Kotaro Yoshida, Laura Gomezjurado Gonzalez, Yukinori Yamamoto, Yuji Naraki, Ryotaro Shimizu, Wenya Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04347v1)