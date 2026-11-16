---
title: Knowledge After Collapse: Context and Wording Shape Factual Accessibility in Language Models
url: http://arxiv.org/abs/2611.17763v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_05-19-42Z_KnowledgeAfterCollapse_ContextandWordingShapeFactu.md
generated_at: 2026-11-15 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Knowledge Answer Divergence (KAD), an event-conditioned evaluation protocol designed to assess how language models behave after they accept a false correction during a factual conversation. Rather than measuring only initial susceptibility to misinformation, KAD freezes the dialogue at the moment a model explicitly adopts a designated false target and then branches independent probes from that exact conversational history. The authors evaluate eight local checkpoint conditions and six hosted endpoints, demonstrating that post-adoption behavior—persistence, recovery, or abstention—varies dramatically depending on how the conversation continues, the placement of cues, and the wording of follow-up prompts.

## Key Takeaways
- KAD separates initial false-answer adoption from subsequent persistence, recovery, and abstention by freezing the conversation at the first explicit adoption of a false target and branching independent probes from that exact history. This enables matched comparisons of post-adoption behavior and history-management interventions that a single susceptibility score cannot capture, providing a more granular diagnostic of factual reliability in language models.
- In corrected Llama 3.2 Instruct 3B controls, a neutral-history branch yielded 42 out of 46 correct responses, compared with only 16 out of 46 under full history, revealing that retaining the full conversational context after a false adoption severely degrades factual accuracy. A matched cue-placement control in Qwen 3.5 4B shifted false adoption by 27.3 percentage points, showing that subtle structural changes in prompt design can dramatically alter model behavior.
- Twelve independently authored pressure templates demonstrated substantial sensitivity to wording, indicating that the phrasing of follow-up questions is not a neutral variable but a powerful lever that can either reinforce or undo a model's commitment to a false answer. This finding underscores that factual accessibility in language models is not a fixed property but a dynamic outcome shaped by conversational context and linguistic framing.

## Context
Current evaluations of language model factuality typically rely on single-turn benchmarks or aggregate susceptibility scores that treat a model's knowledge as static. This paper addresses a critical gap: in real-world deployment, models operate in multi-turn conversations where a single false adoption can cascade through subsequent exchanges, and existing metrics fail to capture whether a model will recover, persist in error, or abstain. By introducing an event-conditioned protocol that isolates the moment of false adoption and systematically probes downstream behavior, KAD aligns evaluation methodology with the interactive, conversational settings in which language models are actually deployed, bridging the divide between static benchmarking and dynamic reliability assessment.

## Implications
For practitioners building conversational AI systems, these findings suggest that mitigating misinformation requires more than improving initial factual accuracy; it demands careful management of conversational history, strategic cue placement, and awareness of how follow-up wording can entrench or undo errors. For the research community, KAD offers a reproducible framework for comparing history-management interventions across model families and scales, enabling systematic studies of recovery conditions that single-susceptibility metrics cannot support. Industry teams deploying chatbots, tutoring systems, or decision-support tools should treat post-adoption persistence as a first-class reliability concern rather than an afterthought, since a model that confidently repeats a falsehood across a multi-turn exchange poses a qualitatively different risk than one that never encountered the error in the first place.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17763v1)
