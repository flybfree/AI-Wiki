---
title: Gated Decoupled Compositional Bandits: A Unified Theory of Contextual Bandits with Supervised-Calibrated Action Scaling and Pre-Execution Gating
published: 2026-08-22T14:58:25Z
authors: Oleg Miroshnichenko
url: http://arxiv.org/abs/2608.21993v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gated Decoupled Compositional Bandits: A Unified Theory of Contextual Bandits with Supervised-Calibrated Action Scaling and Pre-Execution Gating

## Abstract
We introduce Gated Decoupled Compositional Bandits (GDCB), a family of contextual bandit algorithms with three structural innovations that jointly fall outside the taxonomy of LinUCB, LinTS, HierTS, factored bandits, neural contextual bandits, and RLHF. In a GDCB system: (i) the action delivered to the environment is the composition of a nominal arm, drawn by a discrete or hierarchical bandit, with a context-dependent scaler; (ii) the scaler parameter is learned in a separate supervised loop, not jointly with arm selection; and (iii) every action passes through a pre-execution gate that may modify or veto the composed action before it reaches the environment. We formalise this class of algorithms, prove four structural theorems characterising its statistical behaviour, and show that six industrially significant systems -- short-term rental dynamic pricing, clinical drug dosing, credit origination, grid demand response, content moderation, and LLM tool-use agents -- are all instances of GDCB, differing only in the composition operator, scaler family, and gate. The central result is the Decoupling Variance Reduction theorem: a well-calibrated scaler removes context-induced variance from the arm-to-reward mapping, turning a non-stationary bandit problem into an approximately stationary one. The Gate-Induced Equivalence theorem shows that under a stationary gate, historical data collected under any prior policy is a valid warm-up initialiser without importance-sampling correction, generalising the companion P-HITL result (arXiv:2606.02595) from human approval to arbitrary gates. In regulated, high-stakes domains, constraints usually treated as deployment frictions -- approval gates, compliance rules, safety shields -- are the mechanism that makes fast deployment possible, not an obstacle to it. The companion paper validates instance 1 (STR dynamic pricing) on real production data.

## Metadata
- **Published**: 2026-08-22T14:58:25Z
- **Authors**: Oleg Miroshnichenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21993v1)