---
title: Rational Use of Time for Social Coordination in Humans and AI
url: http://arxiv.org/abs/2611.14766v1
type: paper-summary
date: 2026-11-12
source_paper: 2026-11-10_21-44-35Z_RationalUseofTimeforSocialCoordinationinHumansandA.md
generated_at: 2026-11-12 21:33
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how humans and AI systems use implicit temporal cues—such as the duration of a pause—to achieve fine-grained social coordination in dynamic, multi-turn interactions. Using the cooperative card game "The Mind," where players must coordinate without any explicit communication and can only rely on the passage of time, the authors evaluate 150 human participants alongside two classes of AI models (computer-use agents and text-prompted LLMs). The central finding is that both human and frontier AI behavior can be modeled by a Bayesian strategy that infers a partner's beliefs from timing signals, but unlike humans, the tested AI models fail to efficiently adapt their behavior to their partners across the course of the game.

## Key Takeaways
- Human social coordination in time-sensitive settings is best explained by implicit Bayesian reasoning: participants continuously update probabilistic beliefs about their partner's mental state based on the duration of pauses and the timing of actions, performing what the authors describe as "implicit probabilistic reasoning about continuous-time signals in dynamic social settings." This suggests that humans treat temporal cues as rich informational signals rather than mere noise.
- Frontier AI models, including both computer-use agents (CUAs) and standard text-prompted LLMs, exhibit a similar capacity for Bayesian inference from timing signals, indicating that probabilistic reasoning about temporal cues can emerge in artificial systems without any form of continuous real-time experience analogous to human perception. This challenges the assumption that embodied, continuous-time experience is a prerequisite for temporal social reasoning.
- A critical divergence exists in adaptive coordination: while humans progressively refine their strategies by learning from and adapting to their specific partner over repeated interactions, none of the tested AI models demonstrate equivalent efficiency in adapting their behavior to their partners throughout the game. This gap highlights a fundamental limitation in current AI systems' ability to perform dynamic, partner-specific coordination in social settings.

## Context
This work sits at the intersection of cognitive science, multi-agent coordination, and AI evaluation, addressing a gap in how temporal signals are understood as a communication channel in both human and artificial social interactions. Prior research had established that humans use implicit temporal cues to infer mental states, but the mechanisms by which these cues support dynamic, fine-grained coordination across repeated interactions remained poorly understood. By introducing a controlled cooperative game paradigm and comparing human cognition against two distinct operationalizations of time in AI systems, the paper provides a rigorous framework for studying time as a social signal and for benchmarking AI systems on a coordination task that is fundamentally different from standard language-based evaluation.

## Implications
For AI practitioners and researchers building multi-agent systems, this study reveals that current frontier models, despite demonstrating sophisticated reasoning capabilities, lack the adaptive coordination skills that humans naturally develop through repeated social interaction. This has direct consequences for deploying AI agents in collaborative human-AI or AI-AI settings, where agents must interpret implicit signals and adjust their strategies in real time. The findings also suggest a promising research direction: since Bayesian temporal reasoning appears to emerge in AI without continuous real-time experience, future work could focus on closing the adaptation gap by designing training or inference mechanisms that enable AI agents to learn from and respond to specific partners across dynamic interactions, moving beyond static prompt-based coordination toward genuinely adaptive social intelligence.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14766v1)
