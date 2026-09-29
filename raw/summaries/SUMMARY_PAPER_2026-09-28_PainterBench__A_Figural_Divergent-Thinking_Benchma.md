---
title: PainterBench: A Figural Divergent-Thinking Benchmark for Tool-Using Language Models
url: http://arxiv.org/abs/2609.34195v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_03-08-43Z_PainterBench_AFiguralDivergent_ThinkingBenchmarkfo.md
generated_at: 2026-09-28 23:17
model: qwen3.6-35b-a3b
---

## Summary
PainterBench introduces a novel benchmark designed to evaluate figural divergent thinking in multimodal language models by adapting incomplete-drawing tasks into an agentic framework. The benchmark requires agents to incrementally build upon a fixed starting shape using tool-based drawing interactions while autonomously deciding when the creative process is complete. Evaluation across fourteen models reveals significant performance variation, with frontier architectures demonstrating superior creativity compared to smaller variants, though human reference drawings still outperform AI systems in recognizability.

## Key Takeaways
- The benchmark operationalizes figural divergent thinking by requiring agents to incorporate a non-erasable starting shape into an original drawing through multi-turn tool calls and incremental visual feedback loops.
- Crowdsourced evaluations of 2,700 generated drawings show that while top-performing models exceed human baselines in creativity scores, they lag significantly in recognizability, highlighting a persistent gap between abstract novelty and coherent visual representation.
- An adapted automated scoring model (ViDrA-adapted) achieves strong correlation with human creativity ratings (r = 0.85), enabling scalable evaluation while the authors release comprehensive datasets including canvas snapshots, tool traces, and over 72,000 human ratings for future research.

## Context
As multimodal AI systems increasingly interact with visual environments through tool use, evaluating their capacity for open-ended creative reasoning remains a critical challenge in artificial intelligence research. Traditional benchmarks often focus on closed-form generation or recognition tasks, leaving a gap in assessing how models plan incrementally and adapt to partial constraints over extended interactions. PainterBench addresses this by bridging established psychological assessments of human divergent thinking with modern agentic AI workflows that require real-time visual observation and decision-making.

## Implications
The findings suggest that current multimodal language models possess latent creative capabilities that can be effectively unlocked through structured tool-use environments, yet they struggle with maintaining structural coherence during open-ended generation. Practitioners developing creative AI agents should prioritize incremental planning mechanisms and robust visual feedback loops to improve recognizability without sacrificing novelty. Furthermore, the release of automated scoring tools and extensive evaluation datasets provides a scalable foundation for future research in generative creativity, agentic design, and human-AI collaborative artistry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34195v1)
