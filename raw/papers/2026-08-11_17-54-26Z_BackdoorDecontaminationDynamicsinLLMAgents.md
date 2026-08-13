---
title: Backdoor Decontamination Dynamics in LLM Agents
published: 2026-08-11T17:54:26Z
authors: Gabriel Huang, Abhay Puri, Léo Boisvert, Alexandre Drouin, Perouz Taslakian, Spandana Gella, Christopher Pal
url: http://arxiv.org/abs/2608.11295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Backdoor Decontamination Dynamics in LLM Agents

## Abstract
Open-weight LLM agents are vulnerable to backdoors installed during fine-tuning, which may be undetectable if the trigger conditions are never met during testing. Assuming defenders do not know the existing trigger, they cannot unlearn it directly. One decontamination strategy is to install a known backdoor (defensive poisoning) then to unlearn it, hoping that the original unknown backdoor is removed as a side effect. However, this procedure has uncertain outcomes: the original backdoor may persist or be erased or rerouted, among other possibilities. We introduce a framework for studying these dynamics in tool-calling agents, decoupling trigger, response, teacher, and fine-tuning method across systematic experiments on AgentDyn. Across 115 experiments, defensive poisoning alone erases around 56% of original backdoors; subsequent decontamination then drives almost all survivors to erasure, confirming that trigger recognition and malicious execution are behaviorally dissociable. Interestingly, our experiments find that malicious backdoors never persist when using different triggers of the same general type as the defensive backdoor when followed by decontamination via unlearning. Co-installing up to four backdoors increases resistance (around 36% erased), yet decontaminating a single known co-resident backdoor collaterally clears 52/60 co-residents (87%). Upon visualizing postdecontamination model internals using J-lens, we confirm that although the decontamination restores benign LLM responses, traces of original trigger awareness persist at intermediate layers.

## Metadata
- **Published**: 2026-08-11T17:54:26Z
- **Authors**: Gabriel Huang, Abhay Puri, Léo Boisvert, Alexandre Drouin, Perouz Taslakian, Spandana Gella, Christopher Pal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11295v1)