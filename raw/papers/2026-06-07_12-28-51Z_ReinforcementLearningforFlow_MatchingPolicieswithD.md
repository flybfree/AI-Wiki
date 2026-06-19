---

title: Reinforcement Learning for Flow-Matching Policies with Density Transport
published: "2026-06-07T12:28:51Z"
authors: Boshu Lei, Kostas Daniilidis, Antonio Loquercio
url: http://arxiv.org/abs/2606.08602v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Reinforcement Learning for Flow-Matching Policies with Density Transport



**Source**: [Original Paper](http://arxiv.org/abs/2606.08602v1)
## Abstract
We present an online reinforcement learning (RL) algorithm for fine-tuning flow-matching policies in continuous-control problems. Our key insight is to view RL-based policy improvement as a transport of action densities towards regions of high reward, which naturally aligns with the transport formulation of flow matching models. Prior methods either approximate the current or optimal policy distribution or resort to distillation, which introduces biased gradients or sacrifices multimodal modeling capacity. In contrast, our approach for RL with Density Transport, which we name \emph{RLDT}, constructs a transport field from a maximum-entropy RL objective using Stein Variational Gradient Descent (SVGD). Then, it finetunes a pretrained flow matching policy to align with this field. Training with this alignment objective is nontrivial because flow-matching policies generate actions via a multi-step process, making direct gradient-based optimization challenging. To overcome this challenge and stabilize training, we approximate policy actions from intermediate denoising steps via expected-target estimation. This allows the transport-field update to propagate into the network parameters without unstable backpropagation through time. Experimental results demonstrate that RLDT outperforms competitive baselines in reward quality and convergence speed. This performance holds across diverse continuous-control tasks, encompassing both dense and sparse rewards, as well as state- and vision-based long-horizon robot manipulation. The project webpage is \href{https://rpfey.github.io/rldt/}{https://rpfey.github.io/rldt/}.

## Metadata
- **Published**: 2026-06-07T12:28:51Z
- **Authors**: Boshu Lei, Kostas Daniilidis, Antonio Loquercio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.08602v1)