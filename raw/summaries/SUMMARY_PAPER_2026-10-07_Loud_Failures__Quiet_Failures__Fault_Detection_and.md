---
title: Loud Failures, Quiet Failures: Fault Detection and Recovery in Tool-Using Language Model Agents
url: http://arxiv.org/abs/2610.10062v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_13-29-59Z_LoudFailures_QuietFailures_FaultDetectionandRecove.md
generated_at: 2026-10-07 22:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how tool-using language model agents detect and recover from failures in their execution environments, distinguishing between "loud" failures (explicit error messages) and "quiet" failures (plausible but incorrect outputs). By injecting four typed faults into a function-calling benchmark across 1,920 trials with six models, the study finds that agents overwhelmingly trust tool outputs that fail silently, responding primarily to the error channel rather than the semantic content of results. Reasoning models, contrary to expectation, notice silent failures less than their instruct counterparts while showing no improvement in task recovery.

## Key Takeaways
- Agents treat a failure as a problem in 91.3% of trials when the tool returns an explicit error, but only 58.8% when it returns a plausible wrong value, compared to a 26.8% false-positive rate when nothing is wrong. This gap reveals a fundamental over-trust in well-formed but incorrect tool outputs, meaning failures that stay inside the expected format pass through undetected.
- Reasoning models are not better at fault handling than instruct models: they notice silent failures 9.3 percentage points less (p < .001) and change plan 10.4 points more (p < .001), yet recovery rates remain statistically unchanged (p = .512). This suggests that reasoning capabilities do not translate into improved fault detection, and increased plan changes may reflect instability rather than effective recovery.
- Only a missing tool clearly lowers recovery (39.9%), while timeouts, schema drift, and data corruption remain within the 63.3% run-to-run variation baseline. After a fault, agents repeat the same tool three or more times in up to 22.2% of trials, and a prompt line instructing the agent to verify each result failed to improve detection, indicating that the problem is structural rather than addressable through simple prompting.

## Context
This work sits at the intersection of LLM agent reliability research and robust systems engineering. Prior studies have established that language models over-trust tool outputs, but this paper extends that finding across the full pipeline of failure handling—detection, planning adjustment, recovery, and repetition—within multi-turn agent trajectories. By introducing a fault-injection layer over an established benchmark, it provides a controlled experimental framework for measuring agent resilience against realistic deployment failures such as endpoint disappearance, parameter drift, and silent data corruption, which are common in production tool-calling environments but rarely tested in academic benchmarks.

## Implications
For practitioners deploying tool-using agents in production, the findings suggest that current agent architectures are structurally blind to failures that preserve expected output formats, making silent corruption the dominant operational risk rather than outright tool crashes. The inability of reasoning models to outperform instruct models in detection, and the failure of verification prompts to improve outcomes, indicate that robust fault handling requires architectural changes—such as independent validation layers, schema-aware monitoring, or deterministic recovery protocols—rather than reliance on the model's own reasoning. This has direct consequences for safety-critical applications where a plausible-but-wrong tool result could propagate through a multi-step plan without any agent-initiated correction.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10062v1)
