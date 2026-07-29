---
title: CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification
published: 2026-07-27T20:09:05Z
authors: Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada
url: http://arxiv.org/abs/2607.25045v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CogEEGAgent: Toward Autonomous Cognitive EEG Analysis with Grounded Execution and Selection-Aware Verification

## Abstract
Electroencephalography (EEG) analysis in cognitive studies requires specialized expertise and involves many defensible choices over contrasts, channels, time windows, and statistical tests. LLM agents can translate varied natural-language questions into analysis choices, offering a flexible interface for automation. Yet fluent reports alone cannot establish that an agent selected the requested analysis or evaluated a confirmatory claim independently of adaptive search. We present CogEEGAgent, a cognitive-EEG analysis agent grounded in MNE-Python. Its EEG-specific scientific harness separates semantic from scientific authority. The LLM interprets intent and proposes registered analyses, while deterministic components validate typed contracts, control confirmation access, and authorize evidence-bound release. On a prespecified routing benchmark, CogEEGAgent maps language to registered analyses more accurately than a matched deterministic router, while matched preflight makes both systems abstain whenever required. In an externally model-authored, outcome-blind campaign, the complete system releases supported analyses with participant-disjoint confirmation and blocks prespecified capability hazards and lifecycle-reuse requests. Policy stress testing shows that held-out confirmation curbs false positives from uncorrected adaptive search. Together, these studies establish bounded autonomy and an auditable automation framework for cognitive-EEG workflows. More broadly, they show how scientific agents can combine flexible language understanding with fail-closed control over inference and release.

## Metadata
- **Published**: 2026-07-27T20:09:05Z
- **Authors**: Dengzhe Hou, Lingyu Jiang, Fangzhou Lin, Kazunori D Yamada
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25045v1)