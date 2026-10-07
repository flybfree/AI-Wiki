---
title: Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models
published: 2026-10-06T05:09:02Z
authors: Ziyuan Yang, Wenxuan Ding, Shangbin Feng, Yulia Tsvetkov
url: http://arxiv.org/abs/2610.07774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models

## Abstract
Vision-language models (VLMs) face compositional safety risks where harmful intent emerges from the interaction between visual and textual inputs. As mixture-of-experts (MoE) VLMs become increasingly common, recent work has explored various safety interventions, including prompting, supervised fine-tuning, and routing-based expert steering. However, these methods show inconsistent improvements across models and evaluation distributions, and the intervention into model behavior or internal states introduce safety-utility tradeoffs by over-refusal. Rather than manipulating internal states to steer model behavior, we instead ask whether routing states can serve as diagnostic signals for multimodal safety. We find that router logits indeed provide highly predictive signals of whether a multimodal input is safe or not. Motivated by this observation, we introduce a lightweight router-logit safety detector that reads out routing signals during prompt prefill and identifies unsafe requests before generation, without modifying model parameters or expert routing. Across Qwen3-VL and Kimi-VL, the proposed detector substantially reduces safety errors on the HoliSafe benchmark and resoundingly generalizes to out-of-distribution safety benchmarks featuring different safety patterns, including MISHard and MM-SafetyBench. The success of the proposed router-logit detector also suggests a broader perspective on model internals: rather than focusing only on manipulating internal components to steer behavior, simply reading naturally emerging signals and linking them to an external safety mechanism can provide a simple, effective, and non-intrusive complement to existing safety interventions.

## Metadata
- **Published**: 2026-10-06T05:09:02Z
- **Authors**: Ziyuan Yang, Wenxuan Ding, Shangbin Feng, Yulia Tsvetkov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07774v1)