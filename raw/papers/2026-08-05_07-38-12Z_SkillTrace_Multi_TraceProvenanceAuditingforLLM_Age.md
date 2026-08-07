---
title: SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse
published: 2026-08-05T07:38:12Z
authors: Jialuo Chen, Minghe Wang, Lingqi Jiang, Jianan Ma, Xinhao Deng, Xiaohu Du, Ruixiao Lin, Yunhao Feng, Linkang Du, Jingyi Wang
url: http://arxiv.org/abs/2608.05204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillTrace: Multi-Trace Provenance Auditing for LLM-Agent Skill Reuse

## Abstract
LLM-agent ecosystems are rapidly growing around reusable skills: mixed-modality packages of metadata, natural-language instructions, code, tools, references, and operational workflows. As skills become marketplace artifacts, auditing their reuse is no longer the same problem as ordinary code clone detection. Existing detectors target single-modality source code or whole-package similarity, yet skill reuse evidence is distributed across authored text, implementation fragments, and operational structure. As a result, they can miss reuse that preserves only one part of a skill. We present SKILLTRACE, a multi-trace provenance auditing framework for LLM-agent skill reuse. SKILLTRACE extracts three provenance traces: Expression, Implementation, and Operational. It represents the Operational Trace as a Skill Operational Graph (SOG) that captures activation, procedure, and resource-flow structure. An LLM assists only the Operational-trace extraction, once at ingestion; at audit time SKILLTRACE compares cached traces deterministically, calibrates each trace against same-function strict negatives, and reports which trace supports a reuse decision. On SKILLTRACE-BENCH, with 820 transformed reuse positives over 100 marketplace anchors and 751 negative controls, SKILLTRACE achieves AUROC 0.938 and F1 0.898. A 36,446-skill wild audit further shows that trace-attributed evidence surfaces actionable reuse review queues beyond repository-level baselines.

## Metadata
- **Published**: 2026-08-05T07:38:12Z
- **Authors**: Jialuo Chen, Minghe Wang, Lingqi Jiang, Jianan Ma, Xinhao Deng, Xiaohu Du, Ruixiao Lin, Yunhao Feng, Linkang Du, Jingyi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05204v1)