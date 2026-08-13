---
title: High-Order Liquid Evidence Encoding for Gradual GNSS Spoofing Detection in Autonomous Driving
published: 2026-08-12T08:30:17Z
authors: Muhammad Ayub Sabir, Junbiao Pang, Fatima Ashraf
url: http://arxiv.org/abs/2608.11790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# High-Order Liquid Evidence Encoding for Gradual GNSS Spoofing Detection in Autonomous Driving

## Abstract
Accurate Global Navigation Satellite System (GNSS)-based localization is essential for safe and reliable autonomous driving. However, spoofing attacks can manipulate vehicle position estimates. Continuous and subtle attacks are particularly difficult to detect because individual GNSS observations may remain plausible while the inconsistency between GNSS-implied displacement and onboard vehicle motion gradually increases. Existing methods often rely on static vehicle-behavior features or a single residual signal and do not explicitly model this evolution. To address this problem, we propose a causal high-order liquid evidence framework for GNSS spoofing detection. The method first constructs a physics-guided GNSS--motion inconsistency residual by comparing GNSS-implied displacement with onboard-motion-derived displacement. It then forms separate evidence streams for the residual level and its first- and second-order discrete variations, with relevant contextual cues selected according to the evidence order. Each stream is processed by a separate adaptive liquid encoder, and the resulting temporal states are hierarchically coupled to predict spoofing at the window endpoint using only current and past observations. Experiments on three subsets of the real-world AV-GPS dataset show that the proposed method achieves the highest F1-scores among the evaluated temporal models on Dataset~1 and Dataset~3, reaching 0.9535 and 0.9777, respectively. On Dataset~3, it detects both labeled normal-to-attack transitions within four sampling steps. Code and datasets are publicly available at: https://github.com/pangjunbiao/GNSS_Spoofing.git.

## Metadata
- **Published**: 2026-08-12T08:30:17Z
- **Authors**: Muhammad Ayub Sabir, Junbiao Pang, Fatima Ashraf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11790v1)