---
title: RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment
url: http://arxiv.org/abs/2610.09294v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_01-57-17Z_RT_Safe_BenchmarkingAgentSafetyinReal_TimeEmbodied.md
generated_at: 2026-10-07 21:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
RT-Safe introduces a simulated urban benchmark designed to evaluate the safety of embodied AI agents operating under real-time constraints, where the physical environment continues to evolve during both inference and action execution. The benchmark reveals a critical gap between task completion and actual safety: across eight vision-language models, agents achieve high task success rates yet almost never complete episodes without a safety event, with only 0.7% of episodes finishing safely in the hardest setting. The paper further demonstrates that decision latency itself becomes a source of physical risk, as real-time execution increases collisions by 12.3 times compared to static evaluation.

## Key Takeaways
- Standard task success metrics can severely mask safety failures in embodied agents. RT-Safe shows that while agents achieve task completion rates of 91.3% in static evaluation and 94.1% in real-time evaluation, the real-time setting increases collisions by a factor of 12.3, meaning an action that appears safe at observation time may become unsafe before execution due to moving pedestrians, approaching vehicles, and evolving environmental hazards.
- Decision latency is not merely a performance concern but a direct source of physical risk. The benchmark explicitly allows the world to evolve throughout inference and action execution, demonstrating that agents must account for both decision quality and decision speed. An agent that reasons correctly but too slowly can produce actions that are unsafe by the time they are executed in a dynamic physical environment.
- RT-Safe supports offline reinforcement learning training that can substantially reduce collision rates while maintaining strong task completion, suggesting that safety-aware training pipelines are feasible and necessary for deploying embodied agents in real-world urban settings where failures can cause human injury and costly hardware damage.

## Context
As AI agents transition from purely digital environments into physical spaces such as autonomous vehicles, delivery robots, and humanoid assistants, the safety evaluation frameworks developed for text-based or digital agent benchmarks become insufficient. RT-Safe addresses a fundamental gap in the field: existing agent safety evaluations largely assume a static world during inference, whereas embodied agents must operate in continuously evolving physical environments where timing, latency, and dynamic interactions with other actors determine whether an action is truly safe.

## Implications
For practitioners deploying embodied agents in urban or industrial settings, RT-Safe demonstrates that current VLM-based agents are not yet safe enough for real-world operation, and that safety evaluation must incorporate real-time dynamics rather than relying on static snapshots. For the broader AI safety community, the finding that decision latency itself constitutes a safety risk calls for new evaluation paradigms, training methods, and deployment standards that jointly optimize for task performance, safety, and temporal responsiveness in physical environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09294v1)
