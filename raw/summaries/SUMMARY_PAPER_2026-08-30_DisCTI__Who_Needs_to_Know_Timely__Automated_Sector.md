---
title: DisCTI: Who Needs to Know Timely? Automated Sector-Aware Cyber Threat Intelligence Dissemination
url: http://arxiv.org/abs/2608.27967v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_06-22-48Z_DisCTI_WhoNeedstoKnowTimely_AutomatedSector_AwareC.md
generated_at: 2026-08-30 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an automated method for delivering cyber threat intelligence to specific sectors in a timely manner. By treating sector mapping as a multilabel classification task, the authors use a BERT model trained on STIX-formatted events from 872 labeled incidents. The system achieves a macro‑averaged F1 score of 0.89, indicating that 94.5 % of individual sector assignments are correct.

## Key Takeaways
- A deep learning approach can map CTI events to sectors with high accuracy, reducing manual curation effort.
- The model’s performance is measured by a macro‑averaged F1 score of 0.89 and a Hamming loss of 0.055 on the custom dataset.
- Embedding sector‑specific threat knowledge into BERT improves classification beyond generic models.

## Context
This work extends AI applications in cybersecurity by integrating domain expertise with transformer architectures, demonstrating how specialized data labeling can enhance model relevance. It aligns with broader efforts to automate information flow and reduce analyst overload through automated classification pipelines.

## Implications
Practitioners can deploy sector‑aware CTI dissemination to protect critical infrastructure faster and more efficiently. The approach lowers the barrier for organizations lacking dedicated analysts while maintaining high precision in threat targeting.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27967v1)
