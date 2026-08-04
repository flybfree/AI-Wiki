---
title: Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech
published: 2026-08-01T15:41:55Z
authors: Chenlin Liu, Minghui Fang, Zhonghao Bi, Zekai Su, Rong Wang, Jiqing Han
url: http://arxiv.org/abs/2608.00722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech

## Abstract
Language model-based text-to-speech (LM-based TTS) remains vulnerable to speech hallucinations that deviate from the target text. Existing mitigation mainly relies on architectural changes or additional training, while decoding-time control remains underexplored. We present a conditional information view that distinguishes text-derived alignment information from experience information supplied by acoustic context and learned speech regularities. We hypothesize that an important class of hallucinations begins when alignment support is insufficiently reflected in the selected token at a vulnerable transition. Using predictions from the same speech LM with and without text conditions, we propose Experience-Calibrated Contrastive Decoding (ECCD), a training-free method that strengthens alignment support while preserving useful experience information. ECCD preserves the original expert distribution, applies only positive alignment enhancement, and calibrates its strength using set-level experience compatibility. Across four models, ECCD reduces WER/CER by up to 55.6% in all SeedTTS-Eval settings and 24 of 25 multilingual CV3-Eval settings. A listening test yields a CMOS gain of $+0.644$ while retaining strong speaker similarity. Further analysis shows that alignment influence and decision-level gain vary within linguistic units and are lower at first-error boundaries than at matched correct boundaries. Overall, these extensive experiments and analyses identify conditional information control as a promising decoding-time direction for mitigating speech hallucination.

## Metadata
- **Published**: 2026-08-01T15:41:55Z
- **Authors**: Chenlin Liu, Minghui Fang, Zhonghao Bi, Zekai Su, Rong Wang, Jiqing Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00722v1)