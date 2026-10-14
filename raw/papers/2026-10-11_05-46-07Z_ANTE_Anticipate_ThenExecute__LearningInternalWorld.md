---
title: ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs
published: 2026-10-11T05:46:07Z
authors: Yi Ge, Kangrui Ruan, Jifan Chen, Manish Prajapat, Christian Bock, Xiaoyang Wang, Rein Houthooft, Aritra Sengupta, Varun Kumar
url: http://arxiv.org/abs/2610.15368v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs

## Abstract
Rapid advances in large language models have made software engineering agents capable of tackling complex coding tasks. Within a containerized environment, a coding agent receives tool responses or execution results, and determines its later actions by those earlier results. However, most existing coding agents never look ahead: their policies do not anticipate the consequences of actions, and the terminal reward barely attributes a failure to certain earlier steps, so an ill-judged edit can corrupt the repository state irreversibly before any signal arrives. Recent code world models aim to address these challenges, but they are either trained and then frozen before reinforcement learning (RL), or reduced to an auxiliary next-token loss on the environment's outputs. We present ANTE (Anticipate, Then Execute), an agentic RL framework that verifies the policy's pre-action predictions by real execution and turns them into per-step credit for its actions and trust-or-abstain decisions. With an internal belief stated before each action, Belief-Anchored Policy Optimization (BAPO) turns the settled predictions into per-step advantages by anchoring credit on the policy's own forecasts. To turn the trained forecasts into better actions at inference, thereby facilitating effective test-time scaling, ANTE-TTO (test-time optimization) selects among candidate actions without an external scorer. ANTE raises Qwen3-32B from 25.0% to 57.2% pass@1 on SWE-bench Verified, 6.2% above a matched GRPO baseline trained without the belief state; its world model's accuracy climbs from 44% to 69% during RL, and the learned foresight capability transfers across harnesses and out-of-distribution domains. In summary, we aim to build a code world model that knows what has happened, what holds now, and what the next action will achieve.

## Metadata
- **Published**: 2026-10-11T05:46:07Z
- **Authors**: Yi Ge, Kangrui Ruan, Jifan Chen, Manish Prajapat, Christian Bock, Xiaoyang Wang, Rein Houthooft, Aritra Sengupta, Varun Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15368v1)