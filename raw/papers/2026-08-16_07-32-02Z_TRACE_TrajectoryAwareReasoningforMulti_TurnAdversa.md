---
title: TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation
published: 2026-08-16T07:32:02Z
authors: Md Messal Monem Miah, Adrita Anika, Zhiyuan Yu, Ruihong Huang
url: http://arxiv.org/abs/2608.15594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation

## Abstract
Multi-turn jailbreak attacks have emerged as a critical safety threat to LLMs, as harmful objectives are decomposed across a sequence of apparently benign turns to bypass guardrails. Existing defenses lack the reasoning capacity to identify evolving manipulation patterns, often trading helpfulness for safety by over-refusing benign requests related to sensitive topics. We introduce Trace, a multi-turn defense with trajectory-aware structured reasoning. Before generating each response, the model identifies manipulation cues from the trajectory, evaluates both the benign and adversarial interpretations of user intent, assigns a jailbreak score, and commits to an action: Allow, Caution, or Decline. We curate 4k multi-turn adversarial conversations from five attack frameworks, pair them with 2.4k benign dialogs, and 600 sensitive-but-benign conversations. We train Llama-3.1-8B-Instruct with SFT and GRPO under a multi-component reward that jointly optimizes helpfulness on benign prompts and robustness against jailbreak attempts. Across seven multi-turn attack benchmarks, Trace attains an average attack success rate (ASR) of 14.5% against 31.4% for the strongest baseline and 74.9% for the undefended target, while significantly raising the attacker effort required per successful jailbreak. Trace also balances usability and safety, achieving a 93.3% average compliance on over-refusal benchmarks.

## Metadata
- **Published**: 2026-08-16T07:32:02Z
- **Authors**: Md Messal Monem Miah, Adrita Anika, Zhiyuan Yu, Ruihong Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15594v1)