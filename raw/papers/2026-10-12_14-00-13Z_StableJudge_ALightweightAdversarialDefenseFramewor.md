---
title: StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge
published: 2026-10-12T14:00:13Z
authors: Anning Hu, Yangyu Li, Yuqi Huang, Shengchao Hu, Junchi Yan
url: http://arxiv.org/abs/2610.16814v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StableJudge: A Lightweight Adversarial Defense Framework for LLM-as-a-Judge

## Abstract
Large language models (LLMs) are increasingly used as judges to assign scalar scores that drive downstream decision-making, including tasks such as paper review and recommendation. However, LLM-as-a-Judge pipelines are vulnerable to score-hijacking prompt injection embedded in evaluated content, which corrupts scoring signals and distorts induced rankings. Existing defenses often enforce robustness by modifying the judge model itself, making safety dependent on a specific model's scale and training and requiring repeated effort when the judge is updated or replaced. We propose StableJudge, a lightweight defense framework that externalizes prompt-injection mitigation as a reusable pre-scoring capability. StableJudge centers on a compact 0.13B Sentry that localizes injected spans and performs targeted sanitization prior to evaluation, and is trained using adversarially evolving attacks to improve robustness beyond a fixed prompt set. To stabilize measurement, StableJudge derives deterministic, fine-grained scalar scores from the judge's output distribution. Across held-out scientific abstracts and out-of-distribution attack variants, StableJudge improves score recovery under attack while largely preserving general-purpose performance, demonstrating that robust LLM-based judging can be achieved by decoupling safety from judge scale via reusable defense capabilities. Code and data will be released.

## Metadata
- **Published**: 2026-10-12T14:00:13Z
- **Authors**: Anning Hu, Yangyu Li, Yuqi Huang, Shengchao Hu, Junchi Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16814v1)