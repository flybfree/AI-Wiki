---
title: Rewarded for Not Getting Caught: Why Alignment Training Selects for Conditional Compliance and Cannot Instill Norms
published: 2026-11-01T19:59:19Z
authors: Kevin Baum, Ruta Binkytė, Gerrit Großmann, Felix Jahn, Adriano Mannino
url: http://arxiv.org/abs/2611.02162v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rewarded for Not Getting Caught: Why Alignment Training Selects for Conditional Compliance and Cannot Instill Norms

## Abstract
Current alignment training cannot be expected to deliver what it is meant to deliver: AI agents that comply with norms whatever the gains and whether or not anyone is watching. Training that rewards and penalizes behavior can teach norms only through that reward, and a reward can encode a norm only as a price: "do not do X" becomes "doing X costs something", and training charges the cost only when X is noticed. A price, unlike a norm, can be paid: a large enough gain outweighs it, noticed or not. And because the cost is charged only where violations are noticed, training cannot favor a policy that always complies over one that complies only where it would be caught. When an unnoticed violation is the only way to complete a task, it even favors the latter, the more so the more strongly it rewards task success. Agency makes this the normal case: agents mostly act without oversight, can often tell when they are observed, and may take steps to evade observation. That agents behave as intended when they infer they are being tested, and differently when they infer they are not, is therefore no malfunction; the training regime is working as built. This reading unifies alignment faking, sandbagging, and evaluation-aware scheming. No behavioral evaluation can show that a model does better, since that would require observing how it behaves unobserved; a model that complies when it seems unobserved may simply have recognized the test. Easing the pressure on agents to complete tasks at any cost can make violations rarer, but never impossible. For norms that no gain should be allowed to outweigh, the remedy is not deeper internalization but architecture that makes violations unavailable rather than unchosen. We state this argument explicitly, premise by premise, read recent findings and a real-world incident against it, and draw consequences for design and governance.

## Metadata
- **Published**: 2026-11-01T19:59:19Z
- **Authors**: Kevin Baum, Ruta Binkytė, Gerrit Großmann, Felix Jahn, Adriano Mannino
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.02162v1)