---
title: From Triage to Impact: A Multi-Hop Reasoning Benchmark for Explainable Persian Hate Speech
url: http://arxiv.org/abs/2610.20370v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_15-42-15Z_FromTriagetoImpact_AMulti_HopReasoningBenchmarkfor.md
generated_at: 2026-10-14 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a fine-grained, multi-hop reasoning benchmark designed to evaluate large language models on explainable Persian hate speech analysis across six progressively complex tasks, from basic content triage to severity assessment. The authors find that LLM performance degrades as tasks demand finer-grained semantic and inferential reasoning, and that incorporating intermediate reasoning steps significantly improves severity prediction over single-shot approaches.

## Key Takeaways
- The benchmark spans six distinct analytical stages—content triage, target identification, hate tactic and moral foundation analysis, textual evidence extraction, harmful narrative inference, and severity assessment—revealing that state-of-the-art LLMs struggle increasingly as tasks require more granular semantic reasoning, with proprietary models consistently outperforming open-weight alternatives and reasoning-oriented models showing no consistent advantage over standard models.
- Incorporating intermediate reasoning steps substantially improves severity prediction compared to one-shot assessment, suggesting that decomposing hate speech analysis into sequential sub-tasks is a more effective strategy for LLM-based moderation than attempting to produce a holistic judgment in a single pass.
- The analysis identifies specific linguistic and thematic patterns tied to severity: Incitement to Violence or Harm is most strongly associated with higher severity ratings, while political-affiliation targets are particularly linked to subversion-based moral framing, offering concrete guidance for moderation policies targeting Persian-language social media content.

## Context
Persian is a low-resource language with limited annotated datasets and computational infrastructure for fine-grained hate speech analysis, making it a challenging yet important target for NLP research. This work sits at the intersection of multilingual NLP, explainable AI, and social media moderation, contributing a publicly available benchmark that tests whether current LLMs can handle the layered reasoning required to explain why a piece of text constitutes hate speech, who it targets, what moral foundations it invokes, and how severe its impact is.

## Implications
For practitioners building moderation systems for Persian-language platforms, this benchmark provides a structured evaluation framework and actionable insights—such as the finding that multi-step reasoning pipelines outperform single-pass classification—that can directly inform model selection and pipeline design. For the broader AI research community, the results highlight a persistent gap between proprietary and open-weight models on low-resource, culturally specific tasks, underscoring the need for targeted benchmark development and fine-tuning strategies to ensure accountable and equitable content moderation across diverse languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20370v1)
