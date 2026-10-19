---
title: LexPilot: Benchmarking the Proactive Interaction Ability of Legal LLMs with Laypeople in Chinese Civil Case Consultation
url: http://arxiv.org/abs/2610.23141v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_08-38-20Z_LexPilot_BenchmarkingtheProactiveInteractionAbilit.md
generated_at: 2026-10-18 20:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces LexPilot, a benchmark designed to evaluate how well legal LLMs can proactively interact with laypeople who provide underspecified legal consultations in Chinese civil cases. The benchmark links proactive legal interaction to claim-level verdict prediction using 432 real-world judgments across 36 common causes of action, revealing that current LLMs perform substantially worse (-23.84% on average) when consultations lack sufficient detail, highlighting a critical gap in their ability to elicit crucial context from non-expert users.

## Key Takeaways
- Current LLMs produce irresponsible responses with limited utility when faced with underspecified consultations from non-experts, failing to identify focal points of dispute or proactively elicit crucial context needed for definitive legal conclusions. This represents a fundamental usability failure for laypeople seeking legal guidance.
- LexPilot is constructed from 432 authentic Chinese civil judgments spanning 36 common causes of action, providing expert-reviewed pairs of complete and underspecified consultation histories paired with corresponding court verdicts. This design uniquely connects proactive interaction quality to downstream claim-level judgment prediction, a gap that existing data resources fail to address.
- Experiments demonstrate that downstream judgment prediction underperforms by an average of 23.84% in underspecified consultation setups compared to fully specified ones, and further analysis identifies critical bottlenecks hindering LLMs' proactive legal interaction capabilities, underscoring the urgent need for more user-centered legal AI systems.

## Context
The broader AI landscape has seen rapid deployment of LLMs in legal assistance, yet most benchmarks focus on response quality or interaction fluency rather than the practical ability to handle incomplete, real-world queries from ordinary citizens. This paper addresses a critical blind spot: existing evaluation frameworks do not measure how proactive information-gathering behavior affects downstream legal judgment accuracy. By grounding evaluation in authentic court verdicts and real consultation scenarios, LexPilot shifts the field toward measuring what actually matters for public-facing legal AI services.

## Implications
For legal technology practitioners and developers, these findings signal that simply improving model reasoning or response generation is insufficient; systems must be explicitly designed to detect underspecified inputs and proactively guide users toward providing legally relevant details. For the industry, the 23.84% performance drop in underspecified scenarios suggests that current legal AI products deployed to the public may deliver misleading or incomplete guidance, raising accountability and trust concerns. Policymakers and legal service providers should prioritize user-centered interaction design to ensure AI-assisted legal consultations genuinely serve laypeople rather than merely mimicking expert-level outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23141v1)
