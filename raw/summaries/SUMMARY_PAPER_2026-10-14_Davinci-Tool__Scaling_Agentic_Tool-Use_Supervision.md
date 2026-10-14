---
title: Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiable Executable Environments
url: http://arxiv.org/abs/2610.16867v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_14-33-16Z_Davinci_Tool_ScalingAgenticTool_UseSupervisionwith.md
generated_at: 2026-10-14 00:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Davinci-Tool introduces a 30B parameter tool-use model paired with Davinci-ToolData, an execution-grounded dataset that simultaneously scales environment coverage and outcome verification for training reliable agentic tool-use systems. The paper demonstrates that combining supervised fine-tuning on verified multi-step trajectories with Direct Preference Optimization using executable verifiers dramatically improves tool-use performance, elevating a 30B model from 52.4 to 88.2 on τ²-bench and outperforming a 480B model on all three evaluated benchmarks with only 1/16 of its parameters.

## Key Takeaways
- Davinci-ToolData addresses a fundamental scaling problem in agentic training: neither trajectory coverage nor verification alone suffices because new environments introduce distinct states, rules, and dependencies that must be reflected in success criteria. The dataset preserves restorable states, execution traces, outcomes, and verifiers as a unified supervision substrate, ensuring that training data captures the full causal structure of tool interactions rather than superficial action sequences.
- Two complementary pipelines generate the training data: Execution-Grounded Task Synthesis (EGTS) derives verified demonstrations from independently authored systems, while Executable Environment Synthesis (EES) synthesizes auditable environments, state-grounded tasks, and executable verifiers across both single and coordinated domains. Together they produce 30,395 verified trajectories spanning 2,260 invoked tool names, providing broad coverage while maintaining executable ground truth for every outcome.
- The training methodology is two-stage: first supervised fine-tuning on the verified demonstrations, then Direct Preference Optimization that reuses EES states and verifiers to compare alternative actions and construct outcome-grounded preferences. This preference stage leverages the same executable environments used for supervision, creating a closed-loop verification system that grounds preference signals in actual execution outcomes rather than human annotation.

## Context
Agentic tool use has become a central capability for large language models, yet training data for these systems often lacks executable verification, making it difficult to distinguish genuinely successful multi-step workflows from plausible but incorrect action sequences. As tool ecosystems expand across software engineering, data analysis, and multi-domain coordination, the gap between model capability and reliable execution grows. Davinci-Tool addresses this gap by treating executable environments as first-class training infrastructure rather than post-hoc evaluation tools, aligning the supervision signal with the actual mechanics of tool interaction.

## Implications
For practitioners, the result that a 30B model can outperform a 480B model on tool-use benchmarks suggests that data quality and verification-grounded training pipelines can substitute for raw parameter scale, potentially reducing deployment costs for agentic systems in production environments. For the broader field, the unified substrate design—combining states, traces, outcomes, and verifiers—offers a reproducible template for constructing training data in any new tool domain, lowering the barrier for building reliable agents in specialized or emerging environments where human-annotated trajectories are scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16867v1)
