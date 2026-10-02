---
title: AuraForge: Scaling Security Supervision for Training Coding Agents
published: 2026-10-01T00:07:01Z
authors: Danqing Wang, Songwen Zhao, Harsh Sharma, Jierui Wang, Andre Vicente Duarte, Ivan Bercovich, Lei Li
url: http://arxiv.org/abs/2610.00850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AuraForge: Scaling Security Supervision for Training Coding Agents

## Abstract
Coding agents are now proficient enough to generate complex software applications from a single prompt. As their capabilities have grown, human oversight has increasingly shifted from line-by-line code review toward hands-off evaluation of outcomes. However, recent studies have shown that such a transition exposes a critical risk: functional correctness alone does not guarantee a secure implementation. Despite growing attention to code security, training safer coding agents remains challenging because reliable security supervision is difficult to obtain at scale from real-world repositories. We introduce AuraForge to synthesize and validate executable security tests for training secure coding agents. Our approach combines attack-oriented test synthesis, language-extensible task construction, and safeguards against reward hacking. Using AuraForge, we construct AuraGym, a multi-language and multi-CWE executable training gym: 679 executable feature-implementation tasks from 344 real-world repositories across Python, JavaScript, and TypeScript, covering 177 CWE categories. On the subset with human-written security tests, AuraForge produces about 3 times as many test cases on average and reduces the false-positive rate by 83.23%, allowing alternative secure implementations to receive correct supervision. Training Qwen3.5-4B with synthesized security tests gains larger improvements than human-written security tests (average 19.7 FuncPass and 6.2 SecPass vs. 14.9 FuncPass and 4.4 SecPass) on three languages. These results demonstrate that AuraForge provides more diverse and reliable security supervision to train secure coding agents.

## Metadata
- **Published**: 2026-10-01T00:07:01Z
- **Authors**: Danqing Wang, Songwen Zhao, Harsh Sharma, Jierui Wang, Andre Vicente Duarte, Ivan Bercovich, Lei Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00850v1)