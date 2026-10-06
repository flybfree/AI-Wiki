---
title: Beyond Instruction Following: Learning Grounded Skill-Following with Skill Contracts
published: 2026-10-04T12:10:49Z
authors: Jianghan Shen, Zhenjie Liu, Yue Li, Jie Huang, Siqi Luo, Yiming Cheng, Yizhi Yao, Kaijie Zhang, Cheng Tang, Minghui Zhang, Ming Hu, Yirong Chen, Ziyan Huang
url: http://arxiv.org/abs/2610.05161v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Instruction Following: Learning Grounded Skill-Following with Skill Contracts

## Abstract
Instruction following typically enforces discrete, response-level requirements, whereas an expert-authored skill prescribes procedural requirements spanning multiple phases and environment interactions. Given such a skill, we train the executor to execute all required phases instead of focusing solely on the final answer. We therefore introduce Grounded Skill-Following, which requires an agent to execute a fixed, expert-authored skill across its required phases by grounding decisions in environment observations. To achieve verifiable procedural execution, we formulate each skill as a skill contract combining visible skill instructions with an explicit contract runtime. The runtime specifies required phases, admissible actions, permitted transitions, and accepted termination. This structure provides a dense, verifiable training signal throughout execution. We leverage this by introducing Verified Progress Credit, which assigns rewards upon the initial completion of contract milestones and aggregates them into the trajectory return to guide policy optimization. During rollout, the contract runtime continuously tracks state transitions to provide Contract-State Feedback, which indicates whether the latest action is accepted and guides the agent toward valid next actions. To measure procedural compliance, we introduce the Protocol Completion Rate (PCR), defined as reaching accepted termination through all required phases, and decouple it from the final Task Outcome. Jointly trained with our framework, Qwen3.5-4B achieves Protocol Completion Rates of 99.27% on Math and 99.96% on Search, while slightly outperforming original baselines in Task Outcome (82.95% and 46.61%, respectively). Controlled studies examine how skill instructions, training signals, and contract-state feedback affect both metrics, while withholding interventions evaluate behavioral dependence on observation content.

## Metadata
- **Published**: 2026-10-04T12:10:49Z
- **Authors**: Jianghan Shen, Zhenjie Liu, Yue Li, Jie Huang, Siqi Luo, Yiming Cheng, Yizhi Yao, Kaijie Zhang, Cheng Tang, Minghui Zhang, Ming Hu, Yirong Chen, Ziyan Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05161v1)