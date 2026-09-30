---
title: Looped Actor: Depth-Recurrent Reasoning Models for Reinforcement Learning
published: 2026-09-29T12:57:04Z
authors: T. Konstantin Rusch, Tim Seyde, Jared Boyer, Zach J. Patterson, Daniela Rus
url: http://arxiv.org/abs/2609.37432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looped Actor: Depth-Recurrent Reasoning Models for Reinforcement Learning

## Abstract
Looped reasoning models repeatedly apply a shared set of parameters, enabling more computation without increasing the model size. These models also support input-dependent computation by dynamically deciding when to stop looping. Motivated by the recent success of looped transformers in language modeling and reasoning, we investigate whether dynamic looping can similarly benefit sequential decision-making. We provide a complexity-theoretic motivation for this approach by showing that there exist Markov decision processes in which a state-adaptive policy achieves the optimal return with asymptotically less expected computation than any optimal fixed-runtime policy. To learn compute-adaptive policies in practice, we introduce Looped Actor, a transformer-based policy that repeatedly refines a latent representation toward a fixed point using a shared computational block. This allows the model to allocate computation adaptively by varying the number of loops based on the current state. We evaluate Looped Actor on 22 tasks across six environments, ranging from combinatorial puzzles to robotic manipulation and spanning online and offline reinforcement learning (RL) with discrete and continuous actions. Looped Actor matches or exceeds the performance of an untied baseline with 16$\times$ more parameters, with the largest gains in environments where action selection requires substantial multistep planning. For the Boxoban environment, we find that the computation allocation is structured: the number of loops increases with the number of remaining pushes and future optimal pushes become increasingly predictable from the latent state over successive loops. Together, these results highlight actor looping as a simple and efficient way to equip RL agents with adaptive computation and improve their planning capabilities. Code is available at https://github.com/camail-official/LoopedActor

## Metadata
- **Published**: 2026-09-29T12:57:04Z
- **Authors**: T. Konstantin Rusch, Tim Seyde, Jared Boyer, Zach J. Patterson, Daniela Rus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37432v1)