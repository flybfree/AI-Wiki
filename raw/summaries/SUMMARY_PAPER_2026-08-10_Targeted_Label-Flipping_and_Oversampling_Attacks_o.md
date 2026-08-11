---
title: Targeted Label-Flipping and Oversampling Attacks on Federated Conditional GANs
url: http://arxiv.org/abs/2608.09314v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-56-50Z_TargetedLabel_FlippingandOversamplingAttacksonFede.md
generated_at: 2026-08-10 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper examines label flipping attacks on federated conditional GANs and an oversampling variant that upweights poisoned samples. It provides theoretical analysis showing linear semantic damage with quadratic deviation from true distribution. Experiments on FEMNIST, MNIST, CIFAR10 confirm the attack’s effectiveness.

## Key Takeaways
- Label flipping attacks can redirect generation for a target label to a source class by altering local training data.
- Oversampling amplifies poisoning influence leading to measurable Kullback-Leibler divergence between clean and poisoned conditional distributions.
- The semantic impact scales linearly with poisoning strength while distribution deviation grows quadratically, making detection harder.

## Context
Federated learning enables collaborative model training across decentralized devices. GANs are vulnerable because the global generator is updated based on aggregated local models. Attacks that manipulate label information undermine trust in federated systems.

## Implications
Practitioners must adopt robust evaluation metrics beyond labels to detect distribution shifts. The paper highlights the need for defenses that protect against adversarial poisoning in distributed generative models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09314v1)
