---
title: CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution
url: http://arxiv.org/abs/2610.10426v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_17-06-59Z_CoTrace_DataRecipesforTrainingTerminalAgentswithHa.md
generated_at: 2026-10-07 22:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoTrace introduces a harness-aware data recipe for training terminal agents that explicitly accounts for the runtime harness under which training trajectories were generated, rather than pooling them indiscriminately. The authors establish an alternating co-evolution framework that decouples harness search from policy training, showing that a compact, harness-matched corpus yields substantially better model gains at lower compute than larger corpora aggregated across sibling harnesses. On the Tmax promotion split, CoTrace lifts Qwen3.5-9B from 78 to 88 solved tasks under supervised fine-tuning and to 90 under an online reinforcement learning variant, while also demonstrating that out-of-distribution transfer on Terminal-Bench 2.1 and SWE-bench Lite hinges critically on harness compatibility between training and evaluation runtimes.

## Key Takeaways
- Existing harness-model co-evolution methods treat trajectories from harness search as an undifferentiated replay buffer, ignoring that a trajectory's training value is contingent on the specific harness that produced it. CoTrace addresses this by governing trajectory routing, provenance matching, and curriculum refresh, ensuring that supervised fine-tuning uses only verified rollouts matched to the adopted runtime and that reinforcement learning relies on fresh online interactions aligned with the current harness.
- A compact harness-matched corpus produces steady model gains at substantially lower compute than much larger corpora pooled across sibling harnesses, demonstrating that data quality and harness alignment matter more than raw data volume. Recurring execution failures are leveraged to guide harness synthesis, creating a feedback loop where the harness evolves in response to observed model weaknesses.
- Out-of-distribution transfer on benchmarks like Terminal-Bench 2.1 and SWE-bench Lite depends fundamentally on harness compatibility. Maintaining consistency between training and evaluation runtimes prevents procedural execution breakdowns that occur when agents are deployed under foreign scaffolds, highlighting that the harness is not merely a convenience layer but a core component of agent capability.

## Context
Terminal agents—models that interact with command-line environments, execute code, and manage multi-step workflows—are increasingly central to AI-assisted software engineering and autonomous task completion. However, the runtime harness that formats prompts, binds tools, and handles error recovery has historically been treated as a fixed or secondary concern relative to model training. This paper reframes the harness as a first-class training variable, bridging the gap between model development and deployment infrastructure in a way that parallels how data curation transformed large language model training.

## Implications
For practitioners building terminal agents, CoTrace suggests that investing in harness-aware data curation and provenance tracking can yield larger performance gains than simply scaling up training data or model size, making it a practical lever for teams with limited compute budgets. For the broader field, the finding that out-of-distribution transfer collapses under foreign harnesses implies that benchmark evaluations must carefully match training and evaluation scaffolds, and that agent deployment pipelines should treat harness selection as a co-design problem rather than an afterthought. Industry applications in autonomous coding, DevOps automation, and agentic workflows stand to benefit from tighter integration between the training loop and the runtime environment in which agents ultimately operate.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10426v1)
