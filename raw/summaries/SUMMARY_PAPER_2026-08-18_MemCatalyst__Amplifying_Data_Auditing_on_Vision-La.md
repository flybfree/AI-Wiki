---
title: MemCatalyst: Amplifying Data Auditing on Vision-Language Models via Data Poisoning
url: http://arxiv.org/abs/2608.17722v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_12-46-52Z_MemCatalyst_AmplifyingDataAuditingonVision_Languag.md
generated_at: 2026-08-18 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MemCatalyst, a set of data poisoning tools designed to boost membership inference auditing on vision-language models by forcing the model to over-learn inconsistencies between images and text. Experiments show that with few poisoned samples the attack significantly raises MI AUC while leaving model performance unchanged. The approach proves transferable across different VLM architectures in black-box settings.

## Key Takeaways
- Poisoning Text (PT) and Poisoning Image (PI) create mismatched image-text pairs that make the model memorize contradictory features, increasing its vulnerability to membership queries.
- The attack requires only a minimal budget of poisoned samples yet yields a noticeable boost in MI AUC across five state-of-the-art audits.
- Results demonstrate negligible impact on the VLM’s overall performance, indicating that data poisoning can be used for auditing without degrading utility.

## Context
Vision-language models rely heavily on large internet datasets, making it challenging to trace unauthorized use of creators’ content. Membership inference attacks are emerging as a way to reveal such usage, but their effectiveness varies across model architectures and training regimes. This work addresses those variability issues by providing a systematic poisoning framework that works broadly.

## Implications
For data owners, MemCatalyst offers a practical means to detect when their visual assets have been used in training without consent. Practitioners can leverage the tool to protect intellectual property and privacy while keeping model performance intact, fostering trustworthy AI development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17722v1)
