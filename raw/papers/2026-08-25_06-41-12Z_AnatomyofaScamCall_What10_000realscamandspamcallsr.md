---
title: Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate
published: 2026-08-25T06:41:12Z
authors: Ethan Traister, Ankit Raj, Jiaqi Gan, Xingyu Shen, Tyler Wu, Yuchen Zhou, Tommy Duong, Kidus Zewde, Siying Chen, Simiao Ren
url: http://arxiv.org/abs/2608.24127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anatomy of a Scam Call: What 10,000 real scam and spam calls reveal about how phone scammers operate

## Abstract
Telephone fraud is pervasive and costly, but its inner workings are rarely observed at scale. We analyze a complete corpus of 10,211 inbound scam and spam calls -- 913 hours of audio and 330,956 transcribed turns from 5,780 distinct numbers -- collected over 54 days by an AI voice-agent honeypot that answered callers and kept them talking, and introduced in a companion data descriptor. We separate outright scams, which solicit sensitive information, from the larger stream of predatory but legal lead generation ("spam") that feeds them. Scam operations keep office hours (6.6x more calls per weekday than weekend day); thousands of disposable numbers run a small catalog of recycled scripts (thirty opening clusters, half the traffic in the top five); and callers solicit identity anchors -- a home address and a date of birth -- far more often than payment credentials, pressing through persistence and manufactured authority rather than overt threats. Our central experiment asks: does it matter who picks up? Every seeded lead carried one of ten fictitious identities drawn uniformly at random, so the identity a fraud operation reaches is fixed before the caller exists. Across 1,823 randomized calls, scammers spent about 15% more conversational turns per decade of the target's apparent age (rate ratio 1.15, 95% CI 1.08-1.23; randomization p = 0.005) -- yet what they asked for did not change (26.3% of calls reached a request for sensitive information; odds ratio 0.99 per decade, 95% CI 0.90-1.08). A second experiment casts early detection as a benchmark: from a scammer's opening lines alone, on a caller-disjoint split, escalation is predictable at 0.72 ROC-AUC from the first line and 0.87 by the eighth, and a plain bag-of-words classifier matches a fine-tuned on-device language model. Telephone fraud emerges as a templated industry that varies how hard it works a target, but not what it wants.

## Metadata
- **Published**: 2026-08-25T06:41:12Z
- **Authors**: Ethan Traister, Ankit Raj, Jiaqi Gan, Xingyu Shen, Tyler Wu, Yuchen Zhou, Tommy Duong, Kidus Zewde, Siying Chen, Simiao Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24127v1)