---
title: EduWild: How Teacher-Configured Chatbots Fail in Real-World Use and How to Fix Them
url: http://arxiv.org/abs/2610.23530v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_14-28-06Z_EduWild_HowTeacher_ConfiguredChatbotsFailinReal_Wo.md
generated_at: 2026-10-18 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces EduWild, a dataset of 1,726 conversations with 217 teacher-configured educational chatbots, designed to systematically catalog how these bots fail in real-world educational settings. The authors develop a 29-code taxonomy of failure modes—spanning factual, workflow, diagnostic, and pedagogical errors—and validate it using a human-calibrated LLM judge. They then design a prompt-based harness targeting the six most frequent failure modes, demonstrating a 65.2% relative reduction in target failures across a study with 200 college students and ten bots.

## Key Takeaways
- The most prevalent failure mode is lapses in following teacher intent: 53.8% of end-user conversations involve bots skipping required workflow steps, 33.4% omit expectation setup, and 37.1% overload learners with excessive information or questions. This reveals that the dominant problem is not hallucination or factual error but rather a systematic misalignment between the teacher's configured instructions and the bot's actual conversational behavior.
- The authors constructed a rigorous 29-code taxonomy covering factual, workflow, diagnostic, and pedagogical failure categories, applied through a human-calibrated LLM judge. This methodological contribution provides a reproducible framework for auditing educational chatbot behavior at scale, moving beyond anecdotal complaints toward quantifiable failure analysis.
- A prompt-based harness targeting the six most frequent failure codes reduced the mean number of target failure codes per conversation from 1.406 to 0.489 across 200 college students and ten bots, achieving a 65.2% relative reduction when bots are weighted equally. This demonstrates that targeted, failure-informed prompt engineering can meaningfully improve deployed educational chatbots without requiring model retraining.

## Context
As large language models become embedded in educational workflows, teachers increasingly configure chatbots through natural-language instructions rather than programming, creating a gap between intended pedagogical behavior and actual bot output. Prior research on LLM failures has focused largely on benchmark evaluations or single-model studies, leaving a critical blind spot around how teacher-authored configurations interact with model behavior in authentic, multi-student deployments. EduWild addresses this gap by grounding failure analysis in real deployed systems with real end users, bridging the divide between AI safety research and practical educational technology deployment.

## Implications
For educational technology practitioners and platform developers, this work provides a concrete, actionable taxonomy and a validated mitigation strategy that can be integrated into chatbot configuration pipelines to reduce the most common failure modes before deployment. For the broader AI research community, it demonstrates that systematic failure auditing of real-world deployments—rather than reliance on synthetic benchmarks—can directly inform practical improvements, suggesting a template for how AI systems in high-stakes domains like education should be evaluated and iteratively refined.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23530v1)
