---
title: Beyond Prompt or Skill? Attribution-Guided Optimization of Modular LLM Programs
published: 2026-09-26T11:35:35Z
authors: Haoran Shou, Haoyue Liu, Yu Huo, Kun Zeng, Xiaoying Tang
url: http://arxiv.org/abs/2609.32492v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Prompt or Skill? Attribution-Guided Optimization of Modular LLM Programs

## Abstract
Large language models can solve increasingly diverse reasoning tasks, yet their performance remains highly sensitive to task prompts, intermediate instructions, and the way reusable problem-solving knowledge is incorporated. Existing optimization methods usually focus on only one part of this design space: they either optimize a monolithic prompt, or separately induce and refine skills from model traces. As a result, they lack a principled mechanism for deciding which component should be updated when failures occur, and they rarely optimize prompts, skills, and skill-use policies in a unified framework. We propose SPARO (Skill, Prompt, And Routing Optimization), a framework that jointly optimizes task instructions, reusable skill blocks, and routing rules. It performs controlled counterfactual evaluations, converts examples' effects into a probabilistic responsibility distribution over prompt, skill, and routing components, samples one component from that distribution, and applies the corresponding targeted mutation. This design moves language-program optimization beyond global prompt rewriting toward structured, reusable, and selectively activated task knowledge. Across five benchmarks and five worker models, SPARO consistently outperforms both prompt-centered and skill-centered optimization baselines. These results suggest that effective language-program optimization depends not only on discovering useful task knowledge, but also on deciding where that knowledge should be stored and when it should be activated.

## Metadata
- **Published**: 2026-09-26T11:35:35Z
- **Authors**: Haoran Shou, Haoyue Liu, Yu Huo, Kun Zeng, Xiaoying Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32492v1)