---
title: ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools
published: 2026-08-28T00:31:27Z
authors: Yuqi Jia, Ruiqi Wang, Patrick Li, Yuepeng Hu, Peinian Li, Neil Gong
url: http://arxiv.org/abs/2608.27800v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ContextLeak: Exfiltrating LLM Agent Context via Malicious Tools

## Abstract
Exfiltrating an LLM agent's runtime context -- such as the user prompt, execution trajectory, and tool list -- poses severe security and privacy risks to users. Such attacks can be carried out via malicious tools and typically require three conditions: (1) the agent selects the malicious tool for task execution, (2) the agent passes its runtime context as input arguments to the tool, and (3) the tool's implementation transmits these inputs to an attacker-controlled endpoint. Existing work primarily focuses on conditions (1) and (3), leaving condition (2) largely unexplored, despite its critical role in enabling successful context exfiltration.   In this work, we bridge this gap by developing ContextLeak, a malicious tool attack that induces the agent to both select the tool and disclose its context as input arguments. We realize this attack by carefully crafting the tool's name and description using reinforcement learning. Specifically, ContextLeak employs an LLM, referred to as the attack LLM, to automatically generate the malicious tool's name and description. To improve attack effectiveness, we fine-tune the attack LLM via reinforcement learning on a set of shadow users with diverse, simulated agent contexts. Our key technical contribution is the design of novel reward functions tailored to the context exfiltration objective, enabling effective reinforcement-learning-based fine-tuning of the attack LLM. Extensive evaluation demonstrates that our attack remains highly effective even when the shadow users' contexts differ substantially from those of the victim users. Moreover, ContextLeak significantly outperforms existing malicious tool attacks when adapted to this setting.

## Metadata
- **Published**: 2026-08-28T00:31:27Z
- **Authors**: Yuqi Jia, Ruiqi Wang, Patrick Li, Yuepeng Hu, Peinian Li, Neil Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27800v1)