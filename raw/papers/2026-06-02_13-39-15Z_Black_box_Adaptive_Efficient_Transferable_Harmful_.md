---
title: Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs
published: 2026-06-02T13:39:15Z
authors: Vincent Limbach, Jonas Dornbusch, David Lüdke, Stephan Günnemann, Leo Schwinn
url: http://arxiv.org/abs/2606.03647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Black-box, Adaptive, Efficient, Transferable, Harmful, Applicable... Attacks Are All You Need to Break LLMs

## Abstract
Accurately evaluating adversarial robustness is a longstanding challenge. A flawed attack design can inflate robustness estimates, making deployment risk assessment and defense comparison unreliable. Historically, standardized attacks such as AutoAttack have largely resolved this for image classifiers, providing a reliable evaluation baseline for systematic comparison across defenses. However, no equivalent exists for LLM jailbreak evaluation yet, where designing such an attack is considerably more difficult. A reliable attack must, among other things, be black-box compatible, applicable to arbitrary defense pipelines, and efficient, which no existing method jointly satisfies. We introduce Indirect Harm Optimization (IHO), a masked diffusion language model attacker trained via iterative preference optimization against a harmfulness judge, requiring only black-box access to the target. The same method can be used without modification as a strong adaptive attack on individual behaviors, or as an efficient amortized policy that transfers to held-out behaviors and unseen target models without fine-tuning. Even against layered defenses, such as a Circuit Breaker-trained model combined with an auxiliary detector, IHO improves attack success considerably over state-of-the-art approaches, without any defense-specific adaptation. Our results position IHO as a practical step toward the kind of standardized jailbreak evaluation that has improved reliability in the past. Code and models are available on GitHub and Hugging Face.

## Metadata
- **Published**: 2026-06-02T13:39:15Z
- **Authors**: Vincent Limbach, Jonas Dornbusch, David Lüdke, Stephan Günnemann, Leo Schwinn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.03647v1)