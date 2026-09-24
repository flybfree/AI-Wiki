---
title: CART: Closed-Loop Adaptive Red Teaming for Large Language Models
published: 2026-09-23T04:16:46Z
authors: Dongdong Zhang, Tengchao Lv, Yilin Jia, Yuzhong Zhao, Yupan Huang, Wenshan Wu, Xiangyang Zhou, Shaohan Huang, Nan Yang, Li Dong, Lei Cui, Furu Wei
url: http://arxiv.org/abs/2609.27336v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CART: Closed-Loop Adaptive Red Teaming for Large Language Models

## Abstract
Automated red teaming often replays a fixed set of prompts, which measures known risks but cannot learn from failures found during testing. We present CART (Closed-Loop Adaptive Red Teaming), a framework that uses each result to guide what it tests next. CART begins with broad risk coverage, follows weaknesses that emerge, keeps new probes diverse, and records the evidence and source of every finding. It separates the Challenger that creates tests, the Target being tested, which may be a text-only model or a bounded tool-using agent, and the Judge that evaluates the results, allowing these roles to be studied independently. Across three evaluation families (Frontier, JAH, and Agentic), CART discovers more failures and higher average risk than static seed replay for every Target with an available baseline. The gains extend to tool-mediated agent tests, suggesting that contextual adaptation can reveal weaknesses that direct prompt replay does not exercise. These results describe what the test policies discover, not how often failures occur in real deployments. We also find that Challenger-Judge choices affect the evidence uncovered, highlighting the need for role separation and independent review. Overall, CART turns red teaming from a one-time checklist into a continuous, adaptive, and auditable search for model and agent weaknesses.

## Metadata
- **Published**: 2026-09-23T04:16:46Z
- **Authors**: Dongdong Zhang, Tengchao Lv, Yilin Jia, Yuzhong Zhao, Yupan Huang, Wenshan Wu, Xiangyang Zhou, Shaohan Huang, Nan Yang, Li Dong, Lei Cui, Furu Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27336v1)