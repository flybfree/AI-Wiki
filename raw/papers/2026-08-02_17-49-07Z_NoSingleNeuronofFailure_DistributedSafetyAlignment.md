---
title: No Single Neuron of Failure: Distributed Safety Alignment Against White-Box Attacks
published: 2026-08-02T17:49:07Z
authors: Simiao Xie, Chuancheng Shi, Shangze Li, Wenhua Wu, Fei Shen, Ying Zhou, Zhiyong Wang, Tat-Seng Chua
url: http://arxiv.org/abs/2608.01414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# No Single Neuron of Failure: Distributed Safety Alignment Against White-Box Attacks

## Abstract
With the rapid release of open-weight large foundation models, safety threats are shifting from black-box jailbreaks to neuron-level white-box attacks that directly identify and manipulate safety-related neurons. Existing alignment methods often investigate the safety behavior on a small number of neurons, creating fragile single point of failure with limited redundancy. To address this issue, we propose distributed safety alignment (DSA), which redundantly encodes safety capabilities across multiple computational neurons, ensuring that the model maintains its safety baseline even when critical safety neurons are disrupted. Specifically, we localize the intervention to the inputs of the down-projection layers in language-side feed-forward networks and treat each feature coordinate as the activation of an individual neuron. DSA then combines neuron activations with loss gradients to compute a direction-aware first-order Taylor score that globally identifies the neurons that contribute most to the current refusal behavior of the model. Finally, targeted disruption via deterministic masking and stochastic dropout is coupled, forcing the model to abandon narrow safety neurons and redundantly encode safety behavior across multiple compensatory neurons. Extensive experiments show that DSA substantially improves robustness against white-box neuron-level safety attacks while preserving the model's general language and multimodal utility.

## Metadata
- **Published**: 2026-08-02T17:49:07Z
- **Authors**: Simiao Xie, Chuancheng Shi, Shangze Li, Wenhua Wu, Fei Shen, Ying Zhou, Zhiyong Wang, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01414v1)