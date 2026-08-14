---
title: ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification
published: 2026-08-13T06:41:56Z
authors: Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, Dongyang Zhang
url: http://arxiv.org/abs/2608.12877v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReflectFact: Self-Reflective Agents for Improving Comprehension and Reasoning in Multi-Hop Fact Verification

## Abstract
Multi-hop fact verification, which verifies claims by reasoning over multiple pieces of evidence, is critical for combating misinformation on social media yet remains highly challenging. Recent methods primarily rely on multi-agent collaboration to decompose fact verification into specialized subtasks. However, these methods face two critical limitations: (1) agents may perform individual subtasks without sufficient awareness of the global verification objective, causing their reasoning to deviate from the intended direction; and (2) conflicts between parametric knowledge and the provided evidence may undermine evidence-grounded reasoning and lead to incorrect verdicts. To address these challenges, we propose ReflectFact, a novel self-reflective agent framework for multi-hop fact verification. ReflectFact introduces three key tasks. Explicit Reasoning Path Planning builds an evidence-grounded reasoning path by resolving implicit entities, decomposing the claim into sub-questions, and integrating the verified facts into a verdict. Evidence-Drift Verification makes the agent re-answer by quoting the supporting evidence when a grounded answer merely echoes its parametric prior, thereby calibrating evidence deviation to ensure grounded comprehension. Reasoning Reflection Verification re-examines each reasoning step and regenerates it once an inconsistency is detected, correcting reasoning flaws such as location bias and replacement bias through a global task perspective. Subsequently, the agent aggregates validated reasoning chains to yield reliable verdicts. Extensive experiments on HOVER and EX-FEVER demonstrate that ReflectFact effectively remedies the comprehension and reasoning defects of existing methods, achieving state-of-the-art performance and respectively outperforming the strongest baseline by 3.32\% and 2.78\% on the two datasets.

## Metadata
- **Published**: 2026-08-13T06:41:56Z
- **Authors**: Runze Zhao, Zixin Tang, Xiaoshuai Hao, Leyuan Chang, Xiaopeng Fu, Boyu Qiao, Dongyang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12877v1)