# Summary: 2026-08-11_21-00-46Z_BenchmarkingLLMJudgesforMobileAgentEvaluation.md
Saved: 2026-08-12 22:29
Source: 2026-08-11_21-00-46Z_BenchmarkingLLMJudgesforMobileAgentEvaluation.md
Model: None

---

## Summary  
Mobile agent benchmarks increasingly rely on large language model (LLM) judges to assess task completion, yet their reliability on real‑world mobile trajectories is poorly understood. This paper introduces MobileJudgeBench, a systematic benchmark that evaluates LLM‑based judges across diverse human‑annotated trajectories from multiple agents and apps. The study demonstrates that simple baseline methods can outperform elaborate pipelines and that judge quality metrics predict both evaluation fidelity and downstream reinforcement‑learning performance.  

## Key Contributions  
- Finding 1: A simple baseline judge using sampled screenshots is competitive with, and often exceeds, purpose‑built judge methods.  
- Finding 2: Benchmark quality metrics reliably correlate with agent ranking fidelity and downstream utility when judges serve as reward signals.  
- Finding 3: Two LLM backends exhibit qualitatively opposite failure profiles—one conservative (over‑rejects valid completions) and one permissive (accepts invalid ones)—linked to their precision‑recall characteristics.  

## Methodology  
The authors constructed MobileJudgeBench with 931 human‑annotated trajectories spanning six mobile‑agent benchmarks, four agent models, and 68 apps. They evaluated six judge methods: five adapted from existing benchmarks (SPA‑Bench, A3 in two modes, AndroidArena, AgentRewardBench) plus a custom simple baseline, across multiple LLM backends. Evaluation focused on reliability, task‑completion accuracy, latency, and downstream performance when judges are used as rewards.  

## Results  
The baseline method achieved average F1‑scores comparable to or better than the most sophisticated pipelines. Benchmark quality scores showed strong correlation with both agent ranking fidelity (how judges rank trajectories) and performance gains in on‑policy reinforcement learning. Failure analysis revealed that a conservative LLM often over‑rejects valid completions, whereas a permissive model may accept invalid ones, highlighting differing precision‑recall trade‑offs.  

## Significance  
These findings challenge the assumption that more complex judge architectures automatically improve evaluation quality and suggest that baseline approaches can be sufficient for mobile agent assessment. Moreover, they provide empirical evidence linking quantitative metrics to real‑world utility, guiding the design of reward models in reinforcement‑learning pipelines.  

## Related Concepts  
- Mobile agents  
- Large language model judges  
- Benchmarking frameworks (SPA‑Bench, A3, AndroidArena)  
- On‑policy reinforcement learning  
- Precision‑recall trade‑off in LLM outputs

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.11434v1)
