---
title: RETRACE: Resilience-Guided Trait-Conditioned Craving Estimation from Wearable Physiology in Opioid Use Disorder
published: 2026-08-15T00:05:16Z
authors: Yi Xiao, Harshit Sharma, Dessa Bergen-Cico, Asif Salekin
url: http://arxiv.org/abs/2608.14947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RETRACE: Resilience-Guided Trait-Conditioned Craving Estimation from Wearable Physiology in Opioid Use Disorder

## Abstract
Detecting opioid craving from wearable physiological signals is critical yet difficult, with the potential to support proactive interventions for individuals with opioid use disorder (OUD). This challenge is especially pronounced under subject-independent evaluation because craving is subjective, heterogeneous, and often physiologically entangled with stress. Our empirical analysis shows that stress elicits strong and reproducible autonomic responses, while craving-related signals are weaker, sparse, and largely embedded within stress-related physiology. We further show that psychological resilience, which shapes stress regulation and craving vulnerability, is not reliably observable from short-term wearable windows, but can be captured through reusable subject-level proxies, including post-stress heart-rate recovery and autobiographical memory recall.Motivated by these findings, we introduce RETRACE, a resilience-guided trait-conditioned framework for subject-independent craving estimation from wearable physiology. RETRACE reframes craving detection as trait-conditioned physiological interpretation: rather than assuming the same physiological pattern has the same meaning across individuals, it uses resilience-related subject context to guide inference. Technically, RETRACE introduces a novel dual-encoder design that separates generalizable stress physiology from subject-specific craving interpretation. It combines a frozen stress-pretrained encoder with a resilience-conditioned craving encoder, using feature-level gating and representation-level fusion to enable lightweight personalization without target-user craving labels or per-user retraining. We evaluate RETRACE on a novel multimodal OUD dataset containing wearable physiology, stress and craving annotations, and autobiographical narratives. Under LOSO setup, RETRACE achieves up to 7% absolute improvement over the strongest baseline

## Metadata
- **Published**: 2026-08-15T00:05:16Z
- **Authors**: Yi Xiao, Harshit Sharma, Dessa Bergen-Cico, Asif Salekin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14947v1)