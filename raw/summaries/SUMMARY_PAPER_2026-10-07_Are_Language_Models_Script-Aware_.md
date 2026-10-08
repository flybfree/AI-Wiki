---
title: Are Language Models Script-Aware?
url: http://arxiv.org/abs/2610.08037v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_09-31-04Z_AreLanguageModelsScript_Aware.md
generated_at: 2026-10-07 23:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether Small and Large Language Models possess genuine script knowledge by evaluating their behavior on multi-scriptic languages, where the same language can be written in different graphic symbol systems. Through two complementary experiments testing script adaptation to input and adherence to explicit script instructions, the authors find that models demonstrate substantial script knowledge, achieving over 98% fidelity for Latin scripts and high compliance with script directives, though Large Language Models consistently outperform Small Language Models, particularly on non-standard script combinations.

## Key Takeaways
- Script knowledge is a distinct and understudied dimension of language model capability: before any linguistic understanding can occur, users must first recognize the graphic symbols in a model's response, making script selection a prerequisite layer that existing research on off-target generation has largely overlooked in favor of language-level analysis.
- Both SLMs and LLMs demonstrate near-perfect Latin script fidelity exceeding 98% and follow explicit script instructions with high frequency, suggesting that script awareness is a relatively robust capability across model scales, but performance gaps emerge for non-standard script combinations where LLMs maintain a clear advantage over their smaller counterparts.
- The two-experiment design—testing whether models adapt output script to match input script and whether they follow explicit instructions to generate text in a specified script—reveals that script handling involves both implicit pattern matching and instruction-following, and that these two competencies can diverge in quality depending on model size and the novelty of the script pairing.

## Context
This work addresses a gap in the multilingual NLP literature, where off-target generation has been studied primarily through the lens of language selection rather than the more granular question of script choice. Multi-scriptic languages such as Serbian, Hindi, or Azerbaijani present a unique testing ground because the same linguistic content can legitimately appear in multiple writing systems, forcing models to make a script decision independent of language identification. This positions the paper at the intersection of multilingual model evaluation, instruction following, and user-facing output quality.

## Implications
For practitioners deploying language models in multilingual and multi-script regions, these findings suggest that script-level control is achievable but not uniform across model sizes, meaning smaller models may require more explicit prompting or post-processing to guarantee correct script output. For the broader AI research community, the results highlight the need to incorporate script-level metrics into standard multilingual evaluation benchmarks, since a model that selects the correct language but the wrong script can still produce output that is effectively unreadable or unusable for end users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08037v1)
