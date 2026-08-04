---
title: When Collaboration Becomes a Trigger: Collective Evidence-Threshold Backdoors in Multi-Agent Systems
published: 2026-08-02T08:38:44Z
authors: Jia-Hao Xiao, Lei Feng, Min-Ling Zhang
url: http://arxiv.org/abs/2608.01085v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Collaboration Becomes a Trigger: Collective Evidence-Threshold Backdoors in Multi-Agent Systems

## Abstract
LLM-based multi-agent systems (MAS) extend LLM capabilities through iterative communication and shared contexts. However, this collaboration introduces a vulnerability: backdoor behavior can be activated when peer evidence reaches a hidden threshold, rather than being determined by any single message. We introduce a collective evidence-threshold backdoor paradigm for MAS and Boundary-Conditioned Backdoor Injection (BCBI), which constructs counterfactual boundary pairs to separate benign behavior before the threshold from the adversarial objective after it, and learns latent progression aligned with evidence. To mitigate this threat, we propose LAtent Transition Test-time Evaluation (LATTE), a clean-only latent-transition defense that learns benign communication dynamics and quarantines anomalous agent updates before their responses propagate. Across several benchmarks, BCBI yields selective activation with little premature activation; without knowing the attack target or trigger, LATTE limits propagation with minimal disruption.

## Metadata
- **Published**: 2026-08-02T08:38:44Z
- **Authors**: Jia-Hao Xiao, Lei Feng, Min-Ling Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01085v1)