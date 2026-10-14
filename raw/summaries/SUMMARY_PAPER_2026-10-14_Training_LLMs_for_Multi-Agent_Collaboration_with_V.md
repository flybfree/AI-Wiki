---
title: Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards
url: http://arxiv.org/abs/2610.17893v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_07-46-48Z_TrainingLLMsforMulti_AgentCollaborationwithVerifia.md
generated_at: 2026-10-14 00:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces CoSIR (Collaboration via Surprisal-based Information Rewards), a post-training method that teaches LLM agents to share evidence, request missing information, and incorporate teammates' contributions in multi-agent systems. By using a Bayesian evaluator that scores information based on its reduction in team surprisal, the method provides verifiable, message-level rewards that overcome the sparse feedback problem inherent in outcome-based training. The authors demonstrate that models post-trained with CoSIR achieve the highest aggregate performance across seven unseen natural-language collaboration tasks while maintaining competitive general-task performance.

## Key Takeaways
- CoSIR addresses a fundamental training bottleneck in multi-agent LLM systems: final task outcomes provide limited feedback on the value of individual messages, making it difficult to reward agents for sharing relevant evidence, requesting missing information, or incorporating teammates' contributions. The proposed Bayesian evaluator scores shared information by its reduction in team surprisal, defined as the sum of negative log probabilities assigned to the correct option given each agent's available evidence, providing a verifiable and granular reward signal at the message level.
- The reward structure is decomposed into separate components: requests are scored by the potential reduction in surprisal if the requested information were truthfully provided, and agents receive distinct rewards for actually using received information in their private choices and calculations. This decomposition ensures that agents are incentivized not only to communicate but also to act on what they receive, closing the loop between information sharing and decision-making.
- The method was validated by post-training Qwen3-4B, Qwen3-8B, and Gemma-3-4B-it through self-play in a simple, verifiable environment, then evaluating transfer to seven unseen natural-language collaboration tasks. Behavioral analyses confirmed increased disclosure of private evidence and fewer judged failures to use teammates' input, demonstrating that collaboration behaviors learned in a controlled setting generalize to complex, unseen tasks.

## Context
Multi-agent systems powered by LLMs are increasingly deployed in research, software engineering, and decision-support applications, yet training agents to collaborate effectively remains an open challenge because reinforcement learning signals derived from final outcomes are too coarse to guide individual communicative behaviors. CoSIR contributes to the growing body of work on post-training and self-play methods for LLMs by introducing a principled information-theoretic reward that is both computable and verifiable, bridging the gap between theoretical information theory and practical agent training pipelines.

## Implications
For practitioners building multi-agent LLM systems, CoSIR offers a training recipe that can be applied to open-weight models without requiring proprietary reward models or human annotation, lowering the barrier to developing collaborative agent teams. The finding that collaboration behaviors generalize from a simple verifiable environment to complex unseen tasks suggests that carefully designed reward structures can serve as transferable training curricula, potentially accelerating the development of reliable multi-agent systems in industry applications such as automated research assistants, collaborative coding tools, and distributed decision-making platforms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17893v1)
