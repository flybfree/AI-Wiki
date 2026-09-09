---
title: ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing
published: 2026-09-08T04:57:58Z
authors: Yi Ting Shen, Kentaroh Toyoda, Alex Leung
url: http://arxiv.org/abs/2609.08256v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ACEA: An Adversarial Co-Evolution Arena for Head-to-Head Red-Team and Blue-Team LLM Testing

## Abstract
Automated red-team attacks and blue-team defenses for large language models (LLMs) are advancing quickly. However, attackers and defenders are built and tested in isolation, and the resulting scores are hard to trust. To tackle this, we present ACEA (Adversarial Co-Evolution Arena), a platform that connects a pluggable red-team adapter and a pluggable blue-team adapter to a shared target LLM and scores their attack and defense rates with an LLM judge. ACEA contributes four components. First, a pluggable, model-agnostic arena. Any red or blue project connects over a minimal HTTP protocol, which we call the ACEA Standard Adapter Protocol (ASAP). It can be written in any language, and a project that exposes nothing but the protocol is a full participant. Second, an evaluation methodology built for adversarial rounds. Seeding the target with canonical secrets gives verifiable ground truth that separates real leakage from hallucination. We also send each attack to the target even when the defense blocks it, which measures the attack's raw potency independently of whether it was stopped. Together these yield a per-round decomposition of attack strength and defense effectiveness. Third, a real-time, game-style visualization with a detailed end-of-battle report that localizes each failure. The evaluation thus becomes an actionable signal for improving a red or blue project. Fourth, an optional in-context improvement loop that turns each round's outcome into advisory hints for the next. An adapter can then adapt across rounds without keeping state, provided it reads the hints. We describe the design of ACEA and the metrics through which red and blue teams are scored head to head.

## Metadata
- **Published**: 2026-09-08T04:57:58Z
- **Authors**: Yi Ting Shen, Kentaroh Toyoda, Alex Leung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08256v1)