---
title: RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents
url: http://arxiv.org/abs/2610.22507v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_18-03-13Z_RealCLI_TowardaUnifiedEvaluationofHuman_AgentColla.md
generated_at: 2026-10-18 20:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
REALCLI introduces a paired benchmark that simultaneously evaluates task execution performance and human-agent collaboration quality for command-line interface agents operating on realistic, longer-horizon tasks. The benchmark reveals that even frontier models achieve only 49.2% average scores on task execution and a mere 37.6% peak on the joint collaboration score, exposing a sharp divergence between task effectiveness and the quality of interactive collaboration with human users.

## Key Takeaways
- REALCLI constructs a five-dimensional collaboration evaluation framework operationalized into 22 sub-dimensions and 51 interaction scenario templates, moving beyond static instruction-following benchmarks to capture runtime collaboration dynamics such as progressive information delivery, corrections, constraint revisions, and authorization decisions during task execution.
- The benchmark provides two paired evaluation modes: REALCLI-EXEC supplies complete task specifications upfront to measure raw execution capability, while REALCLI-COLLAB introduces a scripted user that incrementally provides information and modifies constraints, enabling direct comparison between static execution and interactive collaboration performance.
- Evaluations demonstrate that frontier agents consistently struggle with steerability (responding appropriately to user corrections and guidance), trust calibration (knowing when to seek confirmation versus proceeding autonomously), and safety boundary management (recognizing when actions require explicit authorization), with the joint collaboration score peaking at only 37.6% across all tested configurations.

## Context
As CLI agents increasingly handle longer-horizon software engineering and system administration tasks, the field has relied on benchmarks that assume fixed user instructions or evaluate only final task outcomes, ignoring the iterative, interactive nature of real-world human-agent collaboration. REALCLI addresses this gap by formalizing collaboration quality as a measurable dimension alongside task completion, reflecting a broader shift in AI evaluation research toward assessing interactive competence rather than static problem-solving ability.

## Implications
For practitioners deploying CLI agents in production environments, these findings indicate that current frontier models are not yet reliable collaborators in interactive workflows, raising safety and usability concerns for teams integrating agents into development pipelines. The benchmark provides a reproducible foundation for researchers to track progress on collaboration-specific capabilities, guiding future model training and agent architecture design toward improved steerability, calibrated trust, and appropriate safety boundary adherence in human-in-the-loop settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22507v1)
