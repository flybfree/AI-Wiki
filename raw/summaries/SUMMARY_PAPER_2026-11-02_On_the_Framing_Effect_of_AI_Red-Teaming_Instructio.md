---
title: On the Framing Effect of AI Red-Teaming Instructions: Evidence from Prior Exercises and Controlled Simulations
url: http://arxiv.org/abs/2611.00412v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-30_22-02-40Z_OntheFramingEffectofAIRed_TeamingInstructions_Evid.md
generated_at: 2026-11-02 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the instructions given to red-teamers conducting adversarial evaluations of generative AI systems significantly influence the outcomes of those evaluations, drawing an analogy to the framing effect in psychology. Through a systematic review of 228 prior red-teaming exercises and a controlled simulation involving 22,500 attacks across five open-weights models, the authors find that specific properties of instructions—such as risk granularity level, instruction length, presence of examples, and explicit harm definitions—significantly predict attack success rates, demonstrating that human-authored instructions remain a powerful determinant of red-teaming findings.

## Key Takeaways
- The authors reviewed 228 historical instances of red-teaming instructions to catalog the range of formulations used across industry and academic organizations, then derived 45 instruction frames spanning three risk domains and three levels of risk granularity, generating 100 variants per frame and deploying them against five open-weights target models for a total of 22,500 attacks. This systematic approach isolates the effect of instruction wording while holding the risk domain, attacker, and target model fixed.
- Using a generalized linear mixed model, the study finds that both the lowest and highest levels of risk granularity outperform intermediate specificity, and that both short and long instructions outperform medium-length ones. Additionally, the presence of examples in instructions is associated with higher attack success rates, while supplying explicit harm definitions yields lower success rates. These findings suggest that instruction design choices are not neutral scaffolding but active drivers of evaluation outcomes.
- The paper demonstrates that even as alignment evaluations become increasingly automated, humans continue to shape red-teaming outcomes substantially through the instructions they provide to scaffold the activity, meaning that the framing of a task can bias what harms are discovered or missed.

## Context
AI red-teaming has become a central evaluation method for surfacing potential harms in generative AI systems, yet it remains an open-ended task laden with design choices that can shape findings. Prior work has acknowledged this ambiguity, but this paper is among the first to systematically quantify how instruction framing specifically drives differential outcomes, bridging insights from cognitive psychology's framing effect literature with AI safety evaluation methodology. As organizations increasingly rely on automated or semi-automated red-teaming pipelines, understanding the hidden influence of instruction design becomes critical for ensuring evaluation validity and comparability across studies.

## Implications
For practitioners and organizations conducting red-teaming exercises, these findings imply that instruction design should be treated as a controlled experimental variable rather than a neutral procedural step, and that standardizing or carefully documenting instruction templates is essential for reproducible and comparable safety evaluations. For the broader AI safety field, the results caution against assuming that automated red-teaming pipelines eliminate human bias, since the initial framing instructions still exert substantial influence on which harms are surfaced. Industry and academic organizations should consider publishing their instruction templates alongside red-teaming results to enable meta-analysis and reduce the risk of framing-induced blind spots in AI safety assessments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00412v1)
