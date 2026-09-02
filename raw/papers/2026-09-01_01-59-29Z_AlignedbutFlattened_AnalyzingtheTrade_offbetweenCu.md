---
title: Aligned but Flattened: Analyzing the Trade-off between Cultural Alignment and Diversity in LLMs
published: 2026-09-01T01:59:29Z
authors: Jingshen Zhang, Shaoyang Xu, Wenxuan Zhang
url: http://arxiv.org/abs/2609.00565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aligned but Flattened: Analyzing the Trade-off between Cultural Alignment and Diversity in LLMs

## Abstract
Cultural fine-tuning has become the de facto paradigm for building culture-aware large language models (LLMs), yet existing optimization exclusively for alignment scores provides an incomplete portrait of cultural fidelity by systematically obscuring inherent cultural diversity. This unidimensional evaluation lens prompts a fundamental question: do models genuinely perceive distinct cultural nuances, or do they merely memorize dominant cultural values? To address this, we propose a synergistic evaluation framework that jointly formalizes cultural alignment and diversity. Through extensive benchmarking of six mainstream LLMs on the World Values Survey, this framework uncovers a systematic and critical trade-off: the pursuit of cultural alignment consistently incurs an acute expense of diversity, leading to severe "cultural flattening." Investigating this behavioral shift, we demonstrate that these superficial alignment gains stem from models artificially anchoring to dominant majorities, converging onto a monolithic response pattern that wipes out the heterogeneous distributions inherent to human groups. Crucially, our mechanistic analysis suggests that this diversity collapse is not merely a behavioral anomaly but more likely a structural consequence of the low-rank bias inherent in neural network optimization. Therefore, our findings expose the limitations of current post-training paradigms and call for a shift toward alignment objectives that preserve cross-cultural pluralism.

## Metadata
- **Published**: 2026-09-01T01:59:29Z
- **Authors**: Jingshen Zhang, Shaoyang Xu, Wenxuan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00565v1)