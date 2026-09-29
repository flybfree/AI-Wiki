---
title: CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents
url: http://arxiv.org/abs/2609.34463v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_07-19-20Z_CoDeL_Co_EvolutionaryDefenseagainstIndirectPromptI.md
generated_at: 2026-09-28 23:01
model: qwen3.6-35b-a3b
---

## Summary
CoDeL introduces a co-evolutionary defense mechanism designed to protect Large Language Model (LLM)-based agents against Indirect Prompt Injection (IPI) attacks by dynamically reshaping the attack distribution during training. Unlike static defenses that rely on explicit injection cues, CoDeL employs a decoupled reward structure and LoRA-based GDPO to jointly optimize for safety refusal and task completion, effectively handling deferred malicious intents folded into plausible workflows. Experimental results demonstrate significant improvements, reducing attack success rates by 88.5% compared to baselines.

## Key Takeaways
- CoDeL utilizes a co-evolving prober that continuously searches for injection rounds, methods, and payloads capable of bypassing the current defender, prioritizing breaches detected too late to ensure the model learns from meaningful failures in a moving curriculum.
- The defense updates via LoRA-based GDPO with a decoupled reward function balancing safety, task progress, and format compliance, enabling the agent to refuse injections while simultaneously completing legitimate user tasks even when malicious intent is deferred across multiple turns.
- Extensive evaluations on three IPI benchmarks demonstrate that CoDeL reduces attack success rates by 88.5% and outperforms nine baseline methods by a margin of 38.0%, proving superior robustness against complex, workflow-integrated attacks compared to static training-based defenses.

## Context
As LLM-based agents increasingly integrate external tools and untrusted content, they become vulnerable to Indirect Prompt Injections where malicious instructions are hidden within legitimate data streams. Current training-based defenses often fail because they overfit to surface-form cues of explicit attacks and cannot generalize to sophisticated strategies that defer harmful objectives or

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34463v1)
