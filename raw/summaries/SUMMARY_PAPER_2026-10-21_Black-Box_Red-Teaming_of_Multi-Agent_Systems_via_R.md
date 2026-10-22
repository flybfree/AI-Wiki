---
title: Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning
url: http://arxiv.org/abs/2610.28966v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_22-32-22Z_Black_BoxRed_TeamingofMulti_AgentSystemsviaReinfor.md
generated_at: 2026-10-21 20:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ReMAS, the first reinforcement learning-based red-teaming framework specifically designed for multi-agent systems (MAS), addressing a critical gap in adversarial testing where existing black-box attacks fail because sub-agents do not directly interact with the user. The framework fine-tunes attacker LLMs through a two-stage process—prompt rewriting and attack template generation—to extract hidden system prompts from individual sub-agents, substantially outperforming prior single-agent red-teaming methods in attack success rates and demonstrating transferability across diverse backend LLMs and MAS architectures.

## Key Takeaways
- Existing black-box red-teaming attacks are fundamentally inadequate for multi-agent systems because they assume direct user-agent interaction, whereas in MAS architectures multiple sub-agents operate behind orchestration layers, making them invisible to conventional adversarial probing. ReMAS overcomes this by training attacker models to craft prompts that specifically invoke targeted sub-agents, thereby exposing their hidden system prompts.
- The ReMAS framework operates in two distinct stages: a rewrite stage that iteratively refines base attack prompts to maximize extraction success, and a template generation stage that constructs structured attack templates designed to trigger specific sub-agent invocations. This staged approach, powered by reinforcement learning fine-tuning of the attacker LLM, enables systematic and adaptive adversarial probing that static prompt templates cannot achieve.
- Experimental results demonstrate that ReMAS substantially improves attack success rates compared to existing black-box adversarial methods, and crucially, the learned attack strategies transfer across different backend LLMs and varying MAS structures. This transferability suggests the framework captures generalizable adversarial patterns rather than overfitting to a specific system configuration, underscoring systemic vulnerabilities in multi-agent deployments.

## Context
As large language models are increasingly orchestrated into multi-agent systems for complex task completion, the security and transparency of these architectures have become a pressing concern in AI safety research. Red-teaming—the practice of adversarially probing a system to uncover weaknesses—has matured for single-agent settings, but the compositional nature of MAS introduces new attack surfaces that remain largely unexplored. This paper sits at the intersection of adversarial robustness, reinforcement learning for language model fine-tuning, and multi-agent system security, filling a methodological void that prior single-agent red-teaming literature left open.

## Implications
For practitioners deploying multi-agent systems in production environments, ReMAS provides a practical, black-box adversarial testing tool that does not require access to internal model weights or system prompt definitions, making it applicable to proprietary and closed-source MAS deployments. The demonstrated transferability across backend LLMs and MAS structures suggests that organizations can adopt a unified red-teaming pipeline regardless of their underlying model stack. More broadly, the findings signal that current MAS defenses are insufficient against adaptive, learned adversaries, and that system prompt leakage in multi-agent pipelines represents a security risk that demands dedicated mitigation strategies before these systems are scaled into high-stakes applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28966v1)
