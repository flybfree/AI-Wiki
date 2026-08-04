---
title: Does the Competitive Component of Adversarial Self-Play Improve Legal Reasoning? A Controlled Negative Result
published: 2026-08-03T00:31:34Z
authors: Miseog Shawn Kim
url: http://arxiv.org/abs/2608.01559v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does the Competitive Component of Adversarial Self-Play Improve Legal Reasoning? A Controlled Negative Result

## Abstract
Adversarial self-play is an appealing recipe for legal reasoning: have a student model draft an argument, have an adversary attack it, and reward the student when its argument survives the attack. We designed exactly such a training signal -- a verifiable "survival" reward in which both the student's cited authorities and the adversary's counter-authorities are checked by a citation verifier, so that survival is decided on verified grounds rather than rhetoric, and fabricated citations are automatically neutralized. We then asked a narrow but important question: does the competitive component itself -- the adversary and the survival reward -- add anything on top of an otherwise identical non-competitive training run? Across four independent tests -- a bootstrap comparison, a two-seed replication, a paired per-case adversarial-robustness comparison, and a blinded head-to-head judgment of generated arguments, plus a follow-up pilot with a deliberately strengthened self-play adversary -- the competitive component produced no reliable benefit. The blinded judgment gave a 49% win rate (binomial p approx. 1.000); the strengthened-adversary pilot gave a 50% win rate (32:32, p approx. 1.000). An early apparent +29% advantage reversed and proved to be a small-sample artifact. We report this as an honest negative result. The value of the paper is reproducibility and the sharing of concrete pitfalls: an initially promising metric that inverted on more data, and an adversarial-robustness metric that silently collapsed to plain recall once the adversary stopped citing the same authorities as the gold answer. This null is consistent with, and reconfirms in the legal domain, the conclusion of the companion coding-domain study (Kim, 2026, arXiv:2607.08255) that the value of multi-teacher curricula arises from constructing a verifiable environment rather than from competition itself.

## Metadata
- **Published**: 2026-08-03T00:31:34Z
- **Authors**: Miseog Shawn Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01559v1)