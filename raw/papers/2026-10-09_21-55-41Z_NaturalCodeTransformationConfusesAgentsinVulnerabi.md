---
title: Natural Code Transformation Confuses Agents in Vulnerability Analysis
published: 2026-10-09T21:55:41Z
authors: Jie Zhu, Ronik Bhaskar, Heather Zheng, Ben Y. Zhao, Kexin Pei
url: http://arxiv.org/abs/2610.14350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Natural Code Transformation Confuses Agents in Vulnerability Analysis

## Abstract
Having demonstrated a strong potential for automating vulnerability discovery, AI agents can also be used to attack software systems at scale. Today's software systems need mechanisms to level the playing field by slowing down potential attacks, giving them time to patch vulnerabilities and strengthen software. Along this line, our study of agent trajectories in vulnerability analysis shows a surprising finding: agents produce dramatically different results across real-world code commits that carry the same functionality and the same vulnerability. This phenomenon appears consistently in multiple code domains and vulnerability categories.   It motivates us to study natural and functionality-preserving code transformations derived from real-world software development, and their potential as a defense against attacker agents. We build a corpus of natural transformations by mining recurring development patterns from real-world code commits, and apply them to evaluate impact on agentic vulnerability analysis. Our results show that even a single form of transformation can effectively "confuse" frontier agents, e.g., Codex with GPT-6 Sol, reducing successes in vulnerability discovery. We also study different agent failures, whether transformations can be composed to provide stronger protection, and adaptive attackers who seek to reverse them. Overall, our study of natural code transformation significantly expands the research space of using code transformations to defend against malicious agents.

## Metadata
- **Published**: 2026-10-09T21:55:41Z
- **Authors**: Jie Zhu, Ronik Bhaskar, Heather Zheng, Ben Y. Zhao, Kexin Pei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14350v1)