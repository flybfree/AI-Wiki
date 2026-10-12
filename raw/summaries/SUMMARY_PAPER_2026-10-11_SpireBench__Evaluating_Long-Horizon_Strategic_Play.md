---
title: SpireBench: Evaluating Long-Horizon Strategic Play of Agentic Models with Slay the Spire
url: http://arxiv.org/abs/2610.12596v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-08_18-18-19Z_SpireBench_EvaluatingLong_HorizonStrategicPlayofAg.md
generated_at: 2026-10-11 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SpireBench introduces a benchmark that evaluates large language models on their ability to play the complete commercial deck-building game Slay the Spire at its highest difficulty, testing strategic reasoning over long horizons rather than short episodic tasks. The study finds that frontier models can match average human players but remain far behind experts, with performance degrading as run length increases, revealing systematic failures in risk assessment and long-term planning across all tested models.

## Key Takeaways
- The performance gap between models and expert players widens as the game run lengthens: the strongest models win the first act as often as experts but fall behind in subsequent acts, demonstrating that long-horizon strategic planning is a distinct and underdeveloped capability that cannot be inferred from short-task performance.
- All tested models systematically misjudge risk over a full run, preferring to preserve health rather than spending it strategically to grow stronger, indicating a shared failure mode in long-horizon resource management that persists regardless of model capability level.
- A comprehensive renaming experiment reveals that part of model performance depends on prior knowledge of the game rather than genuine strategic reasoning, and models do not improve from memories they write across runs because those memories are often incorrect and overly cautious, suggesting that current memory mechanisms in agentic systems are ineffective for learning from experience.

## Context
Most existing agentic benchmarks are short and episodic, making it difficult to isolate whether a model's performance on long tasks stems from stored knowledge, genuine reasoning, or luck. SpireBench addresses this gap by providing the first harness that gives a model the complete original commercial game, enabling researchers to dissect where and why agents fail across extended decision sequences. This matters because real-world agentic applications increasingly require sustained strategic planning over many steps, yet the field lacks unsaturated benchmarks that stress-test this capability.

## Implications
For practitioners building agentic systems, SpireBench provides diagnostic tools to locate specific failure modes such as risk misjudgment and ineffective memory utilization, enabling targeted improvements rather than generic capability scaling. For the research community, the finding that prior game knowledge inflates apparent reasoning ability warns against overestimating strategic competence from benchmark scores alone, and the widening gap with run length suggests that current architectures and prompting strategies are insufficient for long-horizon planning. Industry applications involving multi-step decision-making, such as autonomous planning or strategic negotiation, may face analogous degradation that this benchmark helps anticipate and measure.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.12596v1)
