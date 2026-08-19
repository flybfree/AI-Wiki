---
title: MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps
published: 2026-08-18T11:33:22Z
authors: Sujin Chen, Lijun Li, Tianyi Du, Jing Shao
url: http://arxiv.org/abs/2608.17659v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps

## Abstract
LLM-powered GUI agents that autonomously operate smartphones are rapidly transitioning from research prototypes to early real-world deployment. However, because these agents routinely process untrusted environmental content, they are highly vulnerable to environmental injection attacks, which include indirect prompt injections and adversarial instructions. Such attacks can manipulate the behavior of agents without user awareness through diverse channels encountered in everyday mobile use. Despite these risks, existing benchmarks often fail to capture everyday user scenarios, lacking a systematic evaluation of GUI agents under environmental injection attacks on mobile devices. To address this gap, we introduce MobileWorldSafety, a benchmark of 142 risk tasks built on real Android applications. For each task, we define a programmatically verifiable risk indicator over the final system state and evaluate outcomes with a two-stage pipeline: rule-based verification handles unambiguous cases, while an LLM judge adjudicates ambiguous ones. This distinguishes safety failures from capability failures and enables objective and reproducible assessment. Evaluations on six agents, including both general agents and specialized GUI agents, demonstrate that all agents remain highly vulnerable, with attack success rates ranging from 40.4% to 66.9%. These findings indicate that current agents often fail to maintain safety alignment when adversarial content is presented as ordinary mobile context. MobileWorldSafety provides a foundation for quantifying these vulnerabilities and advancing research on robust mobile GUI agents.

## Metadata
- **Published**: 2026-08-18T11:33:22Z
- **Authors**: Sujin Chen, Lijun Li, Tianyi Du, Jing Shao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17659v1)