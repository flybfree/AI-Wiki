---
title: SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration
published: 2026-09-11T04:04:11Z
authors: Md Jueal Mia, Yanzhao Wu, Selcuk Uluagac, M. Hadi Amini
url: http://arxiv.org/abs/2609.12413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoK: Rethinking Jailbreaking in the Era of Agentic AI: Attacks, Defenses, and Practical Consideration

## Abstract
Large language models (LLMs) are rapidly evolving from conversational assistants into agentic AI systems that reason, plan, invoke tools, maintain persistent memory, communicate with other agents, and execute multi-step tasks. At the same time, modern models exhibit substantially stronger native safety alignment than earlier generations on which many jailbreak attacks and defenses were originally studied. This shift raises a fundamental question: \textit{which established jailbreak-security findings remain valid in the era of modern LLMs and agentic AI?} We address this question through a Systematization of Knowledge (SoK) that reframes jailbreak security around the full agentic execution pipeline. We develop unified taxonomies of attacks and defenses spanning user interaction, planning and reasoning, memory, tool use, and inter-agent communication, and introduce a security--utility--efficiency evaluation framework that separates native harmful-prompt safety, adversarial jailbreak robustness, and agent-level security outcomes. We further conduct a controlled empirical study of representative attacks and defenses within a common agentic framework. Our results reveal three important gaps. First, strong native alignment does not imply robustness to adversarial jailbreaks. Second, defense effectiveness is highly model-, attack-, and component-dependent and can come at substantial cost in over-refusal, utility, and latency. Third, low final-response attack success can mask severe intermediate compromise: planning, memory, and tool interactions may remain unsafe even when the final response is successfully filtered. These findings motivate a shift from response-centric jailbreak defense toward cross-layer, execution-aware security that protects agent state, component transitions, and external actions while preserving practical utility and efficiency.

## Metadata
- **Published**: 2026-09-11T04:04:11Z
- **Authors**: Md Jueal Mia, Yanzhao Wu, Selcuk Uluagac, M. Hadi Amini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12413v1)