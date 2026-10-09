---
title: Tracing the Thoughts of a Coding Agent Playing ARC-AGI-3: Lessons for Continual Learning
url: http://arxiv.org/abs/2610.11450v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_08-04-18Z_TracingtheThoughtsofaCodingAgentPlayingARC_AGI_3_L.md
generated_at: 2026-10-08 21:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a white-box measurement protocol for tracing how a coding agent learns across a sequence of abstract reasoning tasks in ARC-AGI-3, a set of interactive reasoning games with no explicit instructions. By analyzing only the files the agent writes—Python scripts, shell scripts, and text notes—without any access to the underlying model's internal states, the authors reveal that the agent's continual learning process is characterized by selective forgetting, knowledge rewriting rather than reuse, and the accumulation of uncorrected contradictions in its notes.

## Key Takeaways
- Scripts written for one task are almost never called again in a later task: only 33 out of 630 references cross a task boundary. The agent abandons 74% of the scripts it wrote before encountering a new level, because most scripts embed the specific state of the current level. Instead of reusing code, the agent rewrites its knowledge into entirely new scripts, preserving general rules while discarding level-specific details. This reveals that the agent's "learning" is fundamentally a process of rewriting rather than building upon prior work.
- The text notes that only the model reads are never revised. The agent appends new claims without removing or correcting earlier ones, causing contradictions to accumulate over time. These contradictions are resolved not by editing the notes but by consulting the complete action-and-observation log maintained by the harness. This means the agent's memory is append-only and its reasoning about past beliefs is mediated entirely through external logs rather than through self-correction of its own written knowledge.
- The most costly error identified is a hard-coded value carried forward into a task where it no longer holds. Because the agent forgets selectively rather than catastrophically—preserving general rules while dropping specific details—it can inadvertently retain a concrete value from a prior level and apply it in a new context where the rules have changed, leading to failures that are difficult to detect from the agent's own written artifacts alone.

## Context
This work sits at the intersection of AI agent evaluation, continual learning, and interpretability. ARC-AGI-3 represents a frontier benchmark for abstract reasoning that deliberately provides no instructions, forcing agents to infer rules from interaction alone. Most prior analyses of agent learning rely on probing model internals or measuring final task performance. This paper instead treats the agent's written artifacts as the primary object of study, offering a methodological shift toward studying learning as an observable, file-based process. It contributes to growing interest in understanding how frozen foundation models can be made to exhibit learning-like behavior through external scaffolding and persistent artifacts.

## Implications
For practitioners building coding agents or autonomous systems, this analysis highlights a critical design tension: append-only memory and script-based knowledge storage create a brittle form of continual learning where stale hard-coded values silently poison future reasoning. The finding that agents overwhelmingly rewrite rather than reuse code suggests that current agent architectures do not achieve genuine compositional learning but instead perform a costly cycle of knowledge re-derivation. For the broader field, the measurement protocol offers a reproducible, model-agnostic tool for auditing agent behavior without requiring access to model weights or activations, which could inform safer deployment of autonomous coding agents in production environments where silent carry-over of outdated assumptions poses real risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11450v1)
