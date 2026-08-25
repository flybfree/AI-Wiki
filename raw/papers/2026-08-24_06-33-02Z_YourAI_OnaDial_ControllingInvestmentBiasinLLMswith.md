---
title: Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron
published: 2026-08-24T06:33:02Z
authors: Sahong Park, Suhwan Park, Hoyoung Lee, Gakyung Kwon, Wonbin Ahn, Jaewon Choi, Alejandro Lopez-Lira, Yoon Kim, Chanyeol Choi, Hyeongwoo Kong, Yongjae Lee
url: http://arxiv.org/abs/2608.22852v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron

## Abstract
Large language models (LLMs) are increasingly used in investment decision-making, yet prior work shows that they exhibit systematic, model-specific investment preferences. We study whether a model's overall investment stance can be calibrated to a specified direction and strength. We introduce an investment-bias dial, an inference-time intervention on a single neuron that continuously adjusts a model-level decision prior---its overall tendency toward buying or selling---without targeting specific firms or investment attributes. Using matched positive and negative evidence, we evaluate five open-weight LLMs and find that the dial produces monotonic changes in investment stance without modifying prompts or model parameters. At the response level, the dial shifts both investment decisions and the evidential emphasis of generated rationales under identical inputs. In an agentic retrieval setting, the dial also changes what information the model searches for, which evidence it selects, and which evidence is reflected in its final analysis. In a long-context evaluation, the dial maintains stable stance control as context length increases, whereas a matched system-prompt instruction progressively attenuates. We further show that changes in the dial propagate to security rankings and downstream portfolio composition in an exploratory backtest. Overall, our results show that an LLM's aggregate investment stance can be calibrated toward a specified target at inference time.

## Metadata
- **Published**: 2026-08-24T06:33:02Z
- **Authors**: Sahong Park, Suhwan Park, Hoyoung Lee, Gakyung Kwon, Wonbin Ahn, Jaewon Choi, Alejandro Lopez-Lira, Yoon Kim, Chanyeol Choi, Hyeongwoo Kong, Yongjae Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22852v1)