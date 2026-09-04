---
title: NeoRed: A Knowledge-Logic-Alignment Multimodal Large Language Model for Neonatal Respiratory Disease Diagnosis
published: 2026-09-03T08:24:38Z
authors: Yinan Liu, Hongtai Xia, Haoran Xu, Jiankang Hong, Jingkuan Song, Ye Luo
url: http://arxiv.org/abs/2609.03527v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeoRed: A Knowledge-Logic-Alignment Multimodal Large Language Model for Neonatal Respiratory Disease Diagnosis

## Abstract
Neonatal respiratory diseases are a major cause of neonatal morbidity and mortality, posing substantial challenges in clinical practice. Despite recent advances, existing Multimodal Large Language Models (MLLMs) face two key limitations in neonatal diagnosis: (1) domain gap arising from predominantly adult training data; (2) insufficient integration of multidimensional clinical context for accurate diagnosis. To address these challenges, we collect two real-world clinical datasets (NeoCXR and NeoCXR-EV) and propose NeoRed, to the best of our knowledge, the first MLLM tailored for neonatal respiratory disease, filling the gap in neonatal diagnostic reports generation. To enhance joint diagnosis from heterogeneous clinical context and chest X-rays, we design a novel Knowledge-Logic-Alignment (KLA) framework which constrains model behavior from three perspectives: 1) Knowledge Prior Injection (KPI) incorporates neonatologist-inspired diagnostic priors into multimodal representations, guiding disease-specific attention across modalities; 2) Diagnostic Logic Constraint (DLC) aligns the semantics of generated reports with multimodal diagnostic logic; and 3) Visual Semantic Alignment (VSA) establishes semantic correspondence between visual features and imaging conclusions. Extensive experiments demonstrate that NeoRed enables accurate neonatal diagnostic reports generation, achieving ROUGE-L of 53.29% and Clinical Efficacy F1 score of 65.19% on NeoCXR, outperforming existing MLLMs. NeoRed also preserves competitive report generation performance on adult benchmarks (MIMIC-CXR and IU-Xray). Datasets will be available upon application.

## Metadata
- **Published**: 2026-09-03T08:24:38Z
- **Authors**: Yinan Liu, Hongtai Xia, Haoran Xu, Jiankang Hong, Jingkuan Song, Ye Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03527v1)