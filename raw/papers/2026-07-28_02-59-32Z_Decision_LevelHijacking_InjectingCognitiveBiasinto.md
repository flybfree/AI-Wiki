---
title: Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks
published: 2026-07-28T02:59:32Z
authors: Yu Yan, Jiahao Chen, Siqi Lu, Yongjuan Wang, Ziming Zhao, Zhaoxuan Li, Tianyu Du, Qingjun Yuan, Shouling Ji
url: http://arxiv.org/abs/2607.25227v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks

## Abstract
Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. This paper defines such threats as decision-level hijacking. Existing attacks fail to achieve targeted cognitive manipulation without triggering prohibited content or degrading model functionality. To fill this gap, this paper reveals that Bit-Flip Attacks (BFAs) can serve as an attack vector for inducing decision-level hijacking, requiring no real-time interaction or control over the training process, and only a minimal number of weight bits need to be flipped after deployment to achieve stealthy, low-cost, and persistent cognitive manipulation. Therefore, we propose CogBias, a cognitive bias injection framework for LLMs. CogBias converts subjective preferences into optimization signals via a differentiable sentiment evaluator, uses a multi-objective loss to jointly constrain multiple dimensions, and constructs BitScout to locate critical bits, achieving targeted cognitive intervention under an ultra-sparse flip budget. Experiments on Llama-3.2-3B, Mistral-7B, and Qwen2.5-14B, as well as on the commercial recommendation and controversial factual topic scenarios, demonstrate that flipping only a small number of bits stably induces significant stance shifts on target topics, while the impact on non-target tasks and overall output distribution is limited. This work demonstrates that minute perturbations to low-level weight data suffice to undermine the high-level value alignment of LLMs.

## Metadata
- **Published**: 2026-07-28T02:59:32Z
- **Authors**: Yu Yan, Jiahao Chen, Siqi Lu, Yongjuan Wang, Ziming Zhao, Zhaoxuan Li, Tianyu Du, Qingjun Yuan, Shouling Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25227v1)