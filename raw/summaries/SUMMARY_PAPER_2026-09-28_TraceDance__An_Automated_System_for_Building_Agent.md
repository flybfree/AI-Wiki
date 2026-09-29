---
title: TraceDance: An Automated System for Building Agent Behavior Benchmarks from Real-World Agent Deployment Traces
url: http://arxiv.org/abs/2609.33295v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_06-58-39Z_TraceDance_AnAutomatedSystemforBuildingAgentBehavi.md
generated_at: 2026-09-28 23:02
model: qwen3.6-35b-a3b
---

## Summary
TraceDance is an automated system designed to construct targeted benchmarks from real-world agent deployment traces, enabling developers to evaluate specific undesirable behaviors encountered during execution. By leveraging Anchor-and-Confirm and decision-point continuation, the system generates benchmarks that assess LLM responses at recorded decision points without requiring reference answers or environment replay. Experiments demonstrate high fidelity in benchmark construction and reveal significant performance gaps in current frontier models when handling these behavior-specific challenges.

## Key Takeaways
- TraceDance employs Anchor-and-Confirm, which combines programmable retrieval with candidate-level confirmation via a Flash LLM, alongside an Anchor Synthesis Loop to generate and refine specifications for custom undesirable behaviors derived from deployment traces.
- The system evaluates agents using decision-point continuation, testing the next turn at recorded decision points against behavior-specific rubrics; this approach eliminates dependencies on reference answers or environment replay while maintaining rigorous evaluation standards.
- Analysis of 252,557 sessions yielded 107 benchmarks containing 4,125 instances, fulfilling 95.3% of build-target requests with human annotators confirming the requested behavior in 84% of sampled cases and automated grading agreement matching human inter-annotator reliability.
- Nine frontier LLMs achieved a mean pass rate of only 26.7%, underscoring persistent weaknesses in agent behavior at critical decision points and highlighting TraceDance's potential as a component for recursive self-improvement loops by transforming deployment problems into targeted benchmarks.

## Context
As AI agents become increasingly deployed in complex environments, static benchmark suites often fail to capture the nuanced and context-specific undesirable behaviors that arise during real-world usage. There is a critical need for evaluation frameworks that can dynamically adapt to observed failure modes, ensuring that agent reliability and safety are assessed against actual deployment patterns rather than predefined test cases.

## Implications
TraceDance allows practitioners to operationalize deployment feedback by converting specific behavioral issues into rigorous benchmarks, facilitating continuous monitoring and improvement of agent systems. This capability supports the development of more robust autonomous agents by enabling targeted remediation strategies and potentially accelerating progress toward recursive self-improvement cycles where evaluation directly informs model refinement based on real-world performance data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33295v1)
