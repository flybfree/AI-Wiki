---
title: Agent Safety From Within: Detecting Harmful Trajectories from LLM Internal States
published: 2026-09-27T00:09:10Z
authors: Difan Jiao, Ashton Anderson
url: http://arxiv.org/abs/2609.33039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Safety From Within: Detecting Harmful Trajectories from LLM Internal States

## Abstract
Language model agents can now perform sophisticated sequences of actions via tools and harnesses, which has increased the scope of the damage they can cause. Guard models, however, are mainly built for content moderation and thus are not well-suited to detecting this agentic risk. To address this, we proceed by first conducting a representational analysis, then use the resulting insights to build a solution. In our analysis, we focus on two types of trajectory-level agentic harms: harmful content, which is expressed directly, and unsafe tool use, which depends on whether an action is consistent with the interaction that produced it. We investigate how open-source guard models represent these two types of harm and find that they are linearly readable inside the model, even though guard models predict no better than chance on pairs that differ only in the called tool's schema. The two harm types also follow nearly orthogonal internal directions, and neither reliably serves as a proxy for the other. These results motivate reading trajectory safety directly from internal states. We introduce TACIT, a readout of a frozen backbone's internal states that decodes no tokens. Trained on six trajectory-safety benchmarks, a linear probe raises mean macro-F1 from 62.3 for the strongest open guard to 80.7, and refined readouts reach 86.2. With each benchmark held out of training entirely, the refined readouts still lead the strongest guard (65.7 vs. 61.1). With the same backbone, training data and test split, the frozen readout is on par with full safety fine-tuning, and it improves the fine-tuned model further when applied on top. The probe trains about one millionth as many parameters as full fine-tuning in about a sixth of the time, and TACIT has the lowest latency of the guards we evaluate.

## Metadata
- **Published**: 2026-09-27T00:09:10Z
- **Authors**: Difan Jiao, Ashton Anderson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33039v1)