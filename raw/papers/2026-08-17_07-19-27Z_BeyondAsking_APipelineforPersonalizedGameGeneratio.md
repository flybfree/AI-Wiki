---
title: Beyond Asking: A Pipeline for Personalized Game Generation that Reads Players from Behavior
published: 2026-08-17T07:19:27Z
authors: Yifan Lu, Xiaopeng Yuan, Haohan Wang
url: http://arxiv.org/abs/2608.16196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Asking: A Pipeline for Personalized Game Generation that Reads Players from Behavior

## Abstract
Personalized game generation requires inferring a player's abilities and behavioral style from how they play. Large language models have made this inference more attainable than ever: an LLM can read a raw gameplay transcript and produce a fluent, plausible profile of the player. Plausible, however, is not verified, and verification is precisely what the field lacks: latent traits are unobservable; questionnaires provide noisy proxies and become circular when self-reports are used to validate behavior-based inference; and behavior itself is ambiguous without context -- a player who never collects an item may not want it, or may never have had the chance. We address both problems. First, we construct a synthetic player population whose traits are ground truth by construction: each trait is an explicit bot parameter, accepted only after controlled manipulation produces consistent, trait-specific behavioral change. Unlike prior parameter-recovery work that inverts a known decision model, our benchmark evaluates policy-agnostic inference from behavioral transcripts alone. Second, we introduce an opportunity-aware decision-moment representation that disentangles preference from the chance to express it; ablating it selectively degrades opportunity-dependent traits. On this benchmark, few-shot LLM inference outperforms embedding- and rule-based baselines on most traits, though feature-based supervised regressors remain stronger overall. Finally, we close the loop: inferred profiles drive difficulty adaptation, evaluated against ground-truth references and mismatched-profile controls, and an exploratory human study examines whether these findings transfer to real players.

## Metadata
- **Published**: 2026-08-17T07:19:27Z
- **Authors**: Yifan Lu, Xiaopeng Yuan, Haohan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16196v1)