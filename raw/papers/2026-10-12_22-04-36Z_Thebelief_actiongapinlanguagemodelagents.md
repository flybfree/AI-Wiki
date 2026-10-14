---
title: The belief-action gap in language model agents
published: 2026-10-12T22:04:36Z
authors: Ayse Sila Okcu, Weisheng Wang, Tongmeng Xie, Niall Dalton, Angelos Nalmpantis, Raghu Arghal, Mario Giulianelli
url: http://arxiv.org/abs/2610.17444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The belief-action gap in language model agents

## Abstract
Language model (LM) agents can fail for different reasons, requiring different explanations and interventions. We study how state beliefs, action values, and action preferences interact as LM agents reason and commit to decisions in text-rendered grid worlds. We estimate task-relevant beliefs using report-based and representation-based probes, and action values using inverse reinforcement learning. We find that task-relevant state and value information is often represented more reliably than it is reflected in behaviour. Tracking action preferences throughout reasoning further shows that decisions sharpen around a commitment point and reported belief uncertainty decreases near commitment, although individual belief changes do not consistently explain shifts in action preference. Finally, forced actions follow reasoning prefixes from other decisions when transplanted, whereas the tested reasoning-window activation edits provide limited control over the action. Together, these results suggest that some failures arise not from missing task-relevant information, but from how available information is translated into action. Our measurements distinguish information availability from belief-action consistency without by themselves identifying the cause of each failure. Our code is available at: https://anonymous.4open.science/r/belief-action-gap-F745/

## Metadata
- **Published**: 2026-10-12T22:04:36Z
- **Authors**: Ayse Sila Okcu, Weisheng Wang, Tongmeng Xie, Niall Dalton, Angelos Nalmpantis, Raghu Arghal, Mario Giulianelli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17444v1)