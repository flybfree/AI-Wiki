---
title: Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents
published: 2026-09-18T19:16:51Z
authors: Justin Szczepaniak, Elad Feldman, Naum Viner, Ben Nassi
url: http://arxiv.org/abs/2609.22510v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Defusing Explosive Prompts: Understanding and Preventing Trigger-Based Prompt Injections in LLM Agents

## Abstract
As LLM applications integrate with external tools, they are increasingly exposed to indirect prompt injection (IPI), where adversarial instructions are embedded in retrieved content. Conventional IPIs fire on contact: the moment an agent ingests the content, it carries out the instruction. We introduce the explosive prompt, a conditional payload that stays dormant until an attacker-chosen trigger is met, in effect a training-free, inference-time backdoor planted in a single piece of retrieved content.   This temporal separation reaches where ordinary IPI cannot. On frontier models that refuse the bare imperative almost entirely, rephrasing the same goal as a dormant conditional drives real, state-changing tool execution against a live agent backend (a paired mean of 16.5% vs. 2.4% for the imperative, reaching 34.2% on a proprietary model). In trials on nine production agents (OpenAI Codex, Google Gemini CLI, Anthropic Claude Code CLI, Cursor CLI, GitHub Copilot, Devin AI CLI, Amazon Kiro CLI, Qwen Code, Google Assistant; n=30 each), explosive prompts succeed in 43-83% of cases versus at most 3% for an imperative baseline, and they slip past deployed defenses: off-the-shelf injection classifiers are miscalibrated on them, and a preference-optimized model that closes imperative injection entirely still executes 11.8% of explosive prompts, every one at the trigger turn.   The durable defensive lever is ingestion-time detection of the conditional structure, once detectors are trained on explosive-prompt data, which no prior benchmark supplied and our generator does. Retraining cuts live tool-execution attack success from an undefended 34.3% to 7.5-8.1% for the encoder baselines. Our detector, DeFuse, reaches 3.0% at a calibrated 5% false-positive budget with the best detection quality of any method tested (AUC 0.9994) and 25x lower latency, though it needs length-aware thresholds.

## Metadata
- **Published**: 2026-09-18T19:16:51Z
- **Authors**: Justin Szczepaniak, Elad Feldman, Naum Viner, Ben Nassi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22510v1)