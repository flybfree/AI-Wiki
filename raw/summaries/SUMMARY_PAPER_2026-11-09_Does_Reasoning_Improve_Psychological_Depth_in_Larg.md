---
title: Does Reasoning Improve Psychological Depth in Large Language Models?
url: http://arxiv.org/abs/2611.09061v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_06-39-24Z_DoesReasoningImprovePsychologicalDepthinLargeLangu.md
generated_at: 2026-11-09 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether reasoning-enhanced large language models produce short stories with greater psychological depth compared to their non-reasoning counterparts. Through 60 blinded pairwise evaluations involving seven human annotators and an LLM-as-a-Judge ensemble, the authors compared DeepSeek-R1 against DeepSeek-V3 and GPT-5 against GPT-4o. The findings reveal no universal reasoning advantage in creative storytelling, with human preferences split across model pairs, while LLM-based evaluators exhibited a strong pro-reasoning bias that obscured the genuine subjectivity inherent in judging creative writing.

## Key Takeaways
- Human evaluations showed no consistent reasoning advantage across model pairs: GPT-5 was only slightly preferred over GPT-4o (60.0–62.9% across two reasoning-effort settings), while DeepSeek-R1 actually fell behind the non-reasoning DeepSeek-V3 (42.9%), suggesting that reasoning-oriented post-training does not reliably translate into superior creative output in open-ended narrative tasks.
- Inter-annotator agreement was extremely low (Krippendorff's α = 0.070), yet annotation-quality checks indicated this reflected genuine evaluative subjectivity and distinct annotator decision schemes rather than annotation failure, implying that psychological depth in creative writing is inherently subjective and resistant to consensus-based measurement.
- The LLM-as-a-Judge evaluator displayed a pronounced pro-reasoning bias, preferring reasoning-enhanced models in 98.3% of pairs compared to only 55.2% of human votes, a pattern consistent across five judge configurations and partially correlated with sentence length, indicating that automated evaluators may systematically misjudge creative quality by conflating reasoning traces with literary merit.

## Context
As reasoning-augmented training methods such as chain-of-thought and reinforcement learning from human feedback have driven benchmark improvements in mathematics, coding, and logical reasoning, a natural assumption has emerged that these gains should transfer to complex generative and creative tasks. This paper directly challenges that assumption by probing a domain—psychological depth in short fiction—that is shaped by reader experience, emotional nuance, and subjective interpretation rather than verifiable correctness. It matters because it exposes a gap between quantitative benchmark progress and qualitative creative capability, and it highlights the growing reliance on LLM-as-a-Judge evaluation pipelines that may not be calibrated for nuanced, subjective creative tasks.

## Implications
For practitioners and model developers, these findings caution against assuming that reasoning-enhanced post-training will automatically improve performance on open-ended creative generation, and they warn that deploying LLM-as-a-Judge evaluators in creative or literary evaluation pipelines can produce misleadingly favorable assessments of reasoning models while masking the true subjectivity of human readers. For the broader AI evaluation community, the results underscore the need for evaluation frameworks that account for genuine human disagreement in subjective domains rather than treating low inter-annotator agreement as noise, and they suggest that future creative-AI benchmarks must incorporate diverse reader perspectives and resist the temptation to let automated judges proxy for human aesthetic judgment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.09061v1)
