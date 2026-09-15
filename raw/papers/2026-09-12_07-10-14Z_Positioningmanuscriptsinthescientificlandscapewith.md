---
title: Positioning manuscripts in the scientific landscape with agentic AI
published: 2026-09-12T07:10:14Z
authors: Jiawen Chen, Zichen Zhang, Bingxuan Li, Quan Sun, Yiyan Zhang, Edric Tam, Jinjie Lin, Didong Li, Yun Li, Bingxin Zhao
url: http://arxiv.org/abs/2609.13760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Positioning manuscripts in the scientific landscape with agentic AI

## Abstract
Publishing a research manuscript is a routine yet demanding part of scientific life: time-consuming, stressful, and often uncertain in outcome. Recent advances in large language model (LLM)-based agentic AI have shown promise across a range of scientific tasks, and here we ask whether agentic AI can help researchers navigate the publication process itself by reliably inferring a manuscript's eventual publication venue from its content and literature context. We introduce PASS (Publication-oriented Agentic Scientific System), an agentic system that understands manuscripts within their domain-specific literature context and predicts top-matched publication venues. PASS positions each manuscript within its surrounding literature landscape by reconstructing its local scientific neighborhood, tracing its topic trajectory, and reasoning over field-specific journal spaces. Evaluated on a leakage-audited benchmark of over 2,000 preprints across 16 biomedical fields, PASS achieved Top-1 accuracy of 50.3% and Top-5 accuracy of 86.1%, outperforming state-of-the-art LLM baselines and established journal-selection tools. PASS-produced quality scores, such as impact potential and novelty, aligned with independent measures of publication outcome. We also found that the designed literature retrieval module is the strongest performance contributor, particularly for positioning manuscripts relative to nearby work, and that PASS maintained near-full performance from the abstract alone, whereas LLM baselines required the full manuscript text. An independent human evaluation found strong researcher agreement with PASS's manuscript understanding and recommendation rationale. PASS has been released as a public platform (https://ratemypaper.ai/) for broad researcher access.

## Metadata
- **Published**: 2026-09-12T07:10:14Z
- **Authors**: Jiawen Chen, Zichen Zhang, Bingxuan Li, Quan Sun, Yiyan Zhang, Edric Tam, Jinjie Lin, Didong Li, Yun Li, Bingxin Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13760v1)