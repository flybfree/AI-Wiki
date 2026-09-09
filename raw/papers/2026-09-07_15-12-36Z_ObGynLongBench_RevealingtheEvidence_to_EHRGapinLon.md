---
title: ObGynLongBench: Revealing the Evidence-to-EHR Gap in Longitudinal EHR Decision-Making
published: 2026-09-07T15:12:36Z
authors: Jun Xiang, Zhijie Bao, Rong Hu, Kaizhou Qin, Wei Chen, Zhongyu Wei
url: http://arxiv.org/abs/2609.07601v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ObGynLongBench: Revealing the Evidence-to-EHR Gap in Longitudinal EHR Decision-Making

## Abstract
The application of large language models (LLMs) to personalized medical assistants has garnered growing interest. However, existing medical benchmarks largely rely on static question answering with pre-selected evidence, leaving unclear whether LLMs can make reliable clinical decisions from real longitudinal electronic health records (EHRs). To bridge this gap, we introduce ObGynLongBench, a rule-grounded long-context EHR benchmark for obstetric and gynecologic decision-making, comprising 1,500 clinical decision-point cases from 976 real pregnancy EHR histories and traceable rules. Each case is anchored to a patient, a pregnancy-timeline point, and a pre-decision information boundary, enabling Evidence-only, Visit-level EHR, and History-level EHR evaluation. Evaluating 17 LLMs reveals a substantial Evidence-to-EHR Gap: models perform well when evidence is directly provided, but accuracy drops when evidence must be extracted from same-day records or full pre-decision EHR histories. Further analyses identify evidence utilization as a key bottleneck: performance decreases with longer EHR contexts and more complex evidence requirements, and earlier failures often predict later failures within the same patient history. Finally, active-search agents perform best among EHR access strategies, highlighting patient-specific evidence utilization as a central challenge for reliable personalized medical assistants. Resources are available at https://github.com/xiangjun2003/ObgynLongbench.

## Metadata
- **Published**: 2026-09-07T15:12:36Z
- **Authors**: Jun Xiang, Zhijie Bao, Rong Hu, Kaizhou Qin, Wei Chen, Zhongyu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07601v1)