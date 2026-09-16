---
title: Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks
published: 2026-09-14T15:20:30Z
authors: Xiaoyan Li, Yunli Wang
url: http://arxiv.org/abs/2609.16098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks

## Abstract
Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strategies within a unified framework across these four attack types. We introduce two universal tool-based defenses: Attacker Tool Filtering, which uses anomaly detection (e.g., Isolation Forest) to identify and remove suspicious tools, and Normal Tool Recalling, a white-box method that restores the agent's original toolset prior to planning. Additionally, we incorporate prompt-based defenses: Chain-of-Thought prompting and self-reflection techniques to enhance reasoning and task paraphrasing to mitigate attacks. Experimental results across both four open-source LLMs (Gemma2-9B, Qwen2-7B, LLaMA3-8B, and LLaMA3.1-8B) and three proprietary LLMs (GPT-3.5, GPT-4, and GPT-5) show that our methods significantly reduce the Attack Success Rates (ASR), achieving 0% ASR in many settings, while preserving or even improving the original task success rate. These findings highlight the promise of simple, modular, multi-layered defenses for strengthening the security and robustness of tool-integrated LLM agents. The code is available at https://github.com/Xiaoyan-Lisa/Defenses-for-Tool-Integrated-LLM-Agents-Against-Adversarial-Attacks.

## Metadata
- **Published**: 2026-09-14T15:20:30Z
- **Authors**: Xiaoyan Li, Yunli Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16098v1)