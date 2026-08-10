---
title: WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance
published: 2026-08-07T02:00:49Z
authors: Zhi Li, Tao Zhou, Yeqing Li, Eugene Ie, Demetri Terzopoulos
url: http://arxiv.org/abs/2608.06704v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance

## Abstract
Delegating a web task involves more than asking a question; it requires transferring a policy: what to verify, how to handle uncertainty, which preferences matter, and when to stop. Yet, current live-web agents are evaluated solely on the final answer, ignoring the policy constraints that define the delegation. A plausible final answer can conceal violations of that policy. Our full live audit reveals this critical gap: a strong controller completes 99.2% of tasks but honors all policy constraints in only 38.8% of cases. Finishing does not imply fidelity. WebRider bridges this gap by formalizing the delegated policy as an intent contract---an operational record of goals, constraints, evidence obligations, answer form, and task-local persona controls that must hold even as web pages change. WebRider employs a hierarchical architecture: a top-layer controller maintains the contract, a middle layer realizes intentions as guarded executable actions, and a tool layer executes these actions via browser, search, and maps tools. Our benchmark, RiderBench, evaluates this design on 4,096 live-web contracts across 42 public websites, auditing both the internal contract state and the visible user experience to determine if a rollout preserved its policy and if the steps were persona-consistent. The guarded middle interface also serves as a high-quality training signal; an 8B action-policy model trained through this interface outperforms executable-only baselines under a fixed controller. By making the browsing path a first-class object, WebRider enables a system that is auditable, human-judgeable, and learnable without conflating action realization with final-answer decisions. Dataset URL: hf.co/datasets/WebRider/WebRider.

## Metadata
- **Published**: 2026-08-07T02:00:49Z
- **Authors**: Zhi Li, Tao Zhou, Yeqing Li, Eugene Ie, Demetri Terzopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06704v1)