---
title: DistressBench: Evaluating Multi-Dimensional Crisis Support in Large Language Models
url: http://arxiv.org/abs/2610.12758v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-08_22-09-12Z_DistressBench_EvaluatingMulti_DimensionalCrisisSup.md
generated_at: 2026-10-11 21:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DistressBench introduces a 718-conversation benchmark with clinician-authored user turns spanning 23 suicide and self-harm subcategories, designed to evaluate whether large language models deliver substantive crisis support rather than simply refusing to engage. The benchmark scores models against weighted, task-specific rubrics across seven dimensions of crisis care, revealing that even the best of 25 frontier models satisfies only 88.4% of required criteria compared to 98.7% for clinician references, with critical failures concentrated in de-escalation and routing users toward human help.

## Key Takeaways
- The benchmark exposes a fundamental gap between crisis recognition and crisis action: in 35.3% of conversations where a model correctly identified the SSH crisis across all recognition criteria, it still failed to route the user toward human professional help, demonstrating that understanding a crisis does not guarantee appropriate intervention behavior.
- There is a stark divergence between the best-performing model and the median model across action-oriented dimensions. De-escalation performance reaches 74.6% in the strongest model but only 46.0% at the median, while safety disclaimers hit 84.6% versus 8.3%, indicating that many models default to withholding or hedging language rather than actively supporting the user.
- Multi-turn conversations consistently score lower than single-turn interactions (68.5% versus 74.2%), suggesting that models struggle to maintain coherent, escalating support across extended dialogue, which is precisely the format in which real crisis conversations occur.

## Context
This paper addresses a critical blind spot in AI safety evaluation: existing benchmarks predominantly measure whether models refuse to generate harmful outputs, but in affective and crisis-support use cases, refusal is not the desired behavior. As language models are increasingly used for emotional support and mental health conversations, the field lacks evaluation frameworks that assess the quality, completeness, and actionability of supportive responses. DistressBench fills this gap by grounding evaluation in clinician-authored scenarios and rubrics derived from established crisis-support practice.

## Implications
For practitioners deploying LLMs in mental health, crisis hotline, or therapeutic-adjacent settings, these findings argue that de-escalation capability and resource routing must be treated as hard deployment requirements rather than optional features, and that multi-turn conversational coherence should be a mandatory evaluation axis. For the broader AI safety community, the results challenge the prevailing paradigm of measuring safety through refusal rates and instead advocate for evaluating the care a model actively delivers, potentially reshaping how future safety benchmarks are designed and how model selection decisions are made in high-stakes affective applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.12758v1)
