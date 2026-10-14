---
title: When Skills Remain But Access Fails: Factorized Skill Memory for Continual Skill Internalization
url: http://arxiv.org/abs/2610.15492v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_09-46-32Z_WhenSkillsRemainButAccessFails_FactorizedSkillMemo.md
generated_at: 2026-10-13 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how language-model agents forget previously internalized procedural skills during continual learning, discovering a two-stage hierarchical forgetting structure termed skill-addressing forgetting and skill-execution forgetting. To address this, the authors propose Factorized Skill Memory (FSM), a method that separates skill memory into a plastic Address Memory for routing requests to executors and a stable Execution Memory of frozen LoRA adapters, achieving 65.95% mean exact match on a five-stage benchmark while remaining competitive with replay-based approaches.

## Key Takeaways
- The authors identify a clear hierarchical forgetting structure in continual skill internalization: initially, a model loses the ability to invoke an old skill from a raw user request (skill-addressing forgetting), but supplying the correct canonical skill name substantially restores the learned behavior; with further optimization, even this conditional execution degrades (skill-execution forgetting). This two-stage decomposition reveals that addressing and execution capabilities erode at different rates, which prior work had not characterized.
- Factorized Skill Memory operationalizes this insight by training a new LoRA executor using only current-stage data, freezing it after acquisition, and appending it to Execution Memory, while Address Memory incrementally learns to map current requests to the appropriate frozen executor without replaying historical requests or execution trajectories. At inference, Address Memory selects one executor from the raw request, and only that frozen executor performs a single language-model generation, eliminating the need for skill-description retrieval at inference time.
- On a five-stage benchmark constructed from 100 TaskBench skills across two task orders, FSM achieves 93.38% addressing accuracy and 65.95% mean exact match, improving over the strongest replay-free parameter-isolation baseline by 14.3 percentage points while staying within 1.9 points of Replay, which retains all historical training examples, demonstrating that structured memory factorization can nearly match replay without storing past data.

## Context
Continual learning for language-model agents is a central challenge in building autonomous systems that accumulate procedural knowledge over time without catastrophic forgetting. Prior work has focused on preventing weight interference through parameter isolation or replay buffers, but has largely treated skill retention as a monolithic problem. This paper reframes retention as a two-component process—addressing and execution—and shows that existing methods fail because they conflate these components, making it impossible to diagnose or mitigate forgetting selectively.

## Implications
For practitioners deploying agent systems that must internalize and retain hundreds of procedural skills across evolving tasks, FSM offers a replay-free architecture that approaches replay-based performance while avoiding the storage and privacy costs of retaining historical training data. The hierarchical forgetting taxonomy also provides a diagnostic tool for practitioners to determine whether a deployed agent has lost routing capability or execution capability, enabling targeted remediation rather than full retraining. This work points toward modular, composable agent architectures where skill acquisition and skill retrieval are independently optimized subsystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15492v1)
