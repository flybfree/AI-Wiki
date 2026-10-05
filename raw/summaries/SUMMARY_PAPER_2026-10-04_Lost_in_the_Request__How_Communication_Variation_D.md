---
title: Lost in the Request: How Communication Variation Disrupts Retrieval and Action in Email Agents
url: http://arxiv.org/abs/2610.02627v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_00-35-05Z_LostintheRequest_HowCommunicationVariationDisrupts.md
generated_at: 2026-10-04 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether email assistants maintain consistent performance when users express the same request using different communication styles, dialects, or levels of directness. The authors construct validated variants across five communication-style axes and four rule-based dialect conditions, then evaluate them against a retrieval-augmented generation pipeline and two tool-using agentic benchmarks. They find that indirect and formal phrasing significantly degrade performance, and crucially, these failures stem from distinct mechanisms—retrieval failures versus action-omission failures—revealing that a single successful response does not establish true robustness.

## Key Takeaways
- Indirect requests degrade performance across all three evaluated benchmarks, while formal requests specifically harm the two agentic benchmarks. This demonstrates that communication style variation is a systematic and measurable vulnerability in current email assistant systems, not merely an edge case.
- The failure mechanisms differ by system type. Verbose requests primarily impair a lexical retriever by making the target email harder to locate in a search corpus. In contrast, indirect and dialect variants remain harmful even when the relevant email is successfully retrieved, indicating that the breakdown occurs at the reasoning or planning stage rather than the retrieval stage.
- In agentic settings, indirect and formal requests cause agents to omit required actions rather than to take more unsupported or hallucinated actions. This distinction is critical: the agents are not generating incorrect outputs but are failing to complete the requested work, meaning a superficially successful response can mask incomplete task execution.

## Context
Most existing benchmarks for email assistants and agentic AI systems test each task with a single canonical request, leaving robustness to natural language variation largely unmeasured. As large language model–based assistants are increasingly deployed in enterprise communication workflows, users will inevitably phrase requests in diverse ways—formally, indirectly, or in varied English dialects. This paper addresses a gap in evaluation methodology by systematically varying how requests are expressed while holding the underlying information, evidence, and expected outcome fixed, thereby isolating communication variation as an independent source of failure.

## Implications
For practitioners building and evaluating email agents or agentic AI tools, this work signals that current benchmarking practices are insufficient: a system that succeeds on one phrasing may silently fail on another, and the failure mode (retrieval miss versus action omission) dictates entirely different remediation strategies. Industry teams should adopt evaluation suites that vary request expression along multiple axes and separately measure whether agents complete all required actions, not merely whether they produce a plausible-sounding response. This reframing of robustness testing is essential before agentic email assistants can be trusted in production environments where user communication styles are unpredictable.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02627v1)
