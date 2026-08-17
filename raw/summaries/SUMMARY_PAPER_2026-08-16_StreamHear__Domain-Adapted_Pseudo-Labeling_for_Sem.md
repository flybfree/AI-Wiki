---
title: StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition
url: http://arxiv.org/abs/2608.13717v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_19-23-02Z_StreamHear_Domain_AdaptedPseudo_LabelingforSemi_Su.md
generated_at: 2026-08-16 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
StreamHear is a semi‑supervised streaming ASR method that adapts a pretrained student using an offline teacher and pseudo‑labels from unlabeled data. The pipeline combines teacher fine‑tuning, dynamic‑programming realignment to fix chunk placement, and training on the mixture of labeled and pseudo‑labeled audio. Experiments show consistent gains over supervised fine‑tuning and close performance to the offline teacher across multiple domains.

## Key Takeaways
- StreamHear generates pseudo‑labels from unlabeled audio by fine‑tuning an offline transducer teacher on a small labeled set, enabling semi‑supervised learning where labeled data is scarce. 
- The dynamic‑programming realignment step uses an ASR hypothesis anchor to correct word placement at the chunk level, improving alignment without additional supervision. 
- The method outperforms traditional supervised student fine‑tuning and narrows the gap to the offline teacher across financial calls, read speech, and phone‑quality dialogue datasets.

## Context
The paper addresses a persistent challenge in streaming ASR: domain shift between source and target audio where labeled data is expensive but unlabeled data plentiful. By leveraging pseudo‑labeling and realignment, StreamHear demonstrates that semi‑supervised strategies can rival fully supervised approaches without massive label collection.

## Implications
For practitioners, StreamHear offers a practical path to improve streaming ASR systems with limited labeled resources, reducing costs of annotation while maintaining high accuracy. Industry adoption could streamline deployment pipelines, especially in domains like finance and mobile assistants where continuous unlabeled speech streams are available but labeling is costly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13717v1)
