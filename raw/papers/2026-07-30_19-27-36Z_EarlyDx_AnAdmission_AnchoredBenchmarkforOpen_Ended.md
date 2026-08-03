---
title: EarlyDx: An Admission-Anchored Benchmark for Open-Ended Generation of Evidence-Supported ED-Encounter Diagnoses
published: 2026-07-30T19:27:36Z
authors: Jiahui Li, Ruili Fang, Zishuai Liu, Yutong Guo, Nan Yang, Wenzhan Song, Jin Lu, Fei Dou
url: http://arxiv.org/abs/2607.28788v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EarlyDx: An Admission-Anchored Benchmark for Open-Ended Generation of Evidence-Supported ED-Encounter Diagnoses

## Abstract
Clinical diagnosis at hospital admission must be made rapidly from limited, incomplete evidence. Existing diagnosis-prediction benchmarks are poorly suited to this setting: they restrict prediction to closed code sets, exclude free-text notes, and supervise with discharge diagnoses that incorporate the full inpatient course. We introduce EarlyDx, a large-scale benchmark for open-ended early diagnosis, built from 154,834 emergency department encounters in MIMIC-IV. Each encounter is restricted to records available at admission time $t_0$ and supervised by the diagnoses recorded during the ED encounter rather than at discharge. An LLM auditor further verifies every free-text label as supported, partially supported, or unsupported by that evidence; the primary evaluation scores only fully supported labels. Under a semantic LLM-as-judge protocol, no evaluated system --- frontier general, medical-specialized, or in-domain post-trained --- synthesizes admission-time evidence reliably. Zero-shot models score largely by extraction, recovering only 3-31% of diagnoses that must be inferred rather than read from the record; post-training raises inference-dependent recall to 56%, but a sizeable margin remains, and on time-critical conditions no system attains a clinician's balance of sensitivity and precision. We release the full construction and evaluation pipeline at here.

## Metadata
- **Published**: 2026-07-30T19:27:36Z
- **Authors**: Jiahui Li, Ruili Fang, Zishuai Liu, Yutong Guo, Nan Yang, Wenzhan Song, Jin Lu, Fei Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28788v1)