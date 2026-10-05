---
title: When History Fails to Become Experience: Action Calibration in Language Agents
url: http://arxiv.org/abs/2610.02769v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_03-50-34Z_WhenHistoryFailstoBecomeExperience_ActionCalibrati.md
generated_at: 2026-10-04 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why language agents often fail to effectively leverage their own interaction history when making sequential decisions within a task. The authors demonstrate that agents do not reliably connect past actions with their resulting observations, and they propose two interventions—explicit outcome labeling and a learned calibrator module—that help agents transform raw history into actionable experience, thereby improving task success.

## Key Takeaways
- The authors show that while providing interaction history generally improves task completion, much of this benefit persists even when past actions are randomly shuffled, and disrupting the correspondence between actions and observations causes only a modest decline in success. This reveals that agents are not genuinely learning from the causal structure of their prior attempts but are instead relying on surface-level patterns or residual information in the context window.
- Explicitly labeling each returned observation as the outcome of the preceding action is a simple annotation that improves task success and reduces next-action repetition without introducing any new environmental information. This finding suggests that the bottleneck is not information availability but the agent's failure to attribute outcomes to specific prior decisions.
- Building on this insight, the authors introduce a learned calibrator that explicitly reassesses past actions and selectively records experience to guide subsequent decisions. This calibrator improves task success beyond what outcome labeling alone achieves, indicating that a structured, learned mechanism for filtering and attributing experience is more effective than passive context accumulation.

## Context
This work sits at the intersection of language agent design, in-context learning, and reinforcement learning for sequential decision-making. As autonomous agents increasingly operate in multi-step environments such as web navigation, code execution, and tool use, understanding how they process and learn from their own trajectories becomes critical. Prior work has largely assumed that providing more history in the context window automatically improves performance, but this paper challenges that assumption by showing that agents treat history as undifferentiated text rather than as a structured record of cause and effect.

## Implications
For practitioners building agentic systems, this research suggests that simply increasing context length or appending raw interaction logs is insufficient and may even degrade performance. Instead, developers should invest in explicit action-outcome attribution mechanisms and learned calibration modules that help agents distinguish useful experience from noise. For the broader AI research community, these findings highlight a fundamental gap between information provision and information utilization in language agents, pointing toward the need for architectures that treat episodic memory as a structured, attributable resource rather than an unstructured context dump.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02769v1)
