---
title: BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views
url: http://arxiv.org/abs/2610.17457v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_22-17-51Z_BrowseSafe___BenchmarkingPromptInjectionDetectionA.md
generated_at: 2026-10-14 00:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
BrowseSafe++ is a significantly expanded benchmark for detecting prompt injection attacks targeting browser-based AI agents, growing from 14,719 to 38,675 pairs of attacked and clean webpages sourced from production websites. The paper introduces BrowseSafe-Guard, two lightweight 0.8B-parameter detectors for text and screenshot-based injection detection that outperform frontier-model-based detectors in F1 score while maintaining low false-positive rates and inference costs, and BrowseSafe-Adapt, a feedback-driven revision mechanism that boosts attack success rates from a few percent up to 95.41%.

## Key Takeaways
- BrowseSafe++ provides paired attacked and clean versions of the same webpage in multiple formats (HTML, Markdown, accessibility tree, and screenshot), each accompanied by a user task and expected answer, covering twelve website types and 24 attack types across 18 distinct page locations. This multi-format, multi-location design ensures that prompt injection detection is tested across the full spectrum of how browser agents actually consume web content.
- The BrowseSafe-Guard detectors, at only 0.8 billion parameters, achieve higher F1 scores than detectors built on frontier models while keeping false-positive rates on benign pages low and inference cost minimal. This demonstrates that purpose-trained small models can surpass general-purpose large models for the specific task of identifying injected instructions in web contexts.
- BrowseSafe-Adapt uses browser-agent feedback to iteratively revise benchmark injections, transforming attacks that initially succeed on only a small fraction of tasks into attacks with up to 95.41% success. This reveals that static benchmark injections underestimate real-world attack effectiveness and that adaptive, feedback-driven evaluation is critical for realistic security assessment.

## Context
Prompt injection attacks represent one of the most pressing security challenges for autonomous browser agents that read untrusted webpages and execute user-directed tasks. As browser agents move from research prototypes into production deployments handling news articles, shared documents, forums, and other web content, the attack surface expands dramatically across languages, page structures, and rendering formats. Prior benchmarks like BrowseSafe covered a limited set of pages and attack types, leaving a gap in understanding how injections behave across the diverse contexts agents actually encounter. BrowseSafe++ addresses this gap by grounding its injections in real production websites and providing the paired clean-control structure needed for rigorous detection evaluation.

## Implications
For practitioners deploying browser agents in enterprise or consumer settings, BrowseSafe++ offers a realistic, large-scale testbed to evaluate and harden injection defenses before agents handle sensitive user tasks, reducing the risk of agents being silently redirected by malicious webpage content. The finding that small, task-specific detectors can outperform frontier-model-based approaches suggests that production systems can achieve strong injection defense without prohibitive inference costs, making security guardrails feasible at scale. The BrowseSafe-Adapt mechanism further signals that static security testing is insufficient; ongoing feedback loops between agent behavior and attack generation will be necessary to keep defenses aligned with evolving real-world threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17457v1)
