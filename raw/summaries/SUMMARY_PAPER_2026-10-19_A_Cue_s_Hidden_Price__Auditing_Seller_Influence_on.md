---
title: A Cue's Hidden Price: Auditing Seller Influence on AI Shoppers
url: http://arxiv.org/abs/2610.25843v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_05-57-24Z_ACue_sHiddenPrice_AuditingSellerInfluenceonAIShopp.md
generated_at: 2026-10-19 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "price-equivalent (PE) auditing," a novel method for measuring how much seller-controlled content (such as badges, endorsements, and framing) influences large language models acting as shopping agents. Rather than measuring influence by how often a cue wins a choice—which saturates once a cue is dominant—the authors price each cue in monetary terms by raising the cued product's price until it is selected only 50% of the time. Running 113,472 trials across seven models and two product categories, they find that cues appearing equally strong under choice-rate audits actually differ substantially in their true influence, revealing a significant blind spot in existing evaluation methods.

## Key Takeaways
- Choice-rate audits have a fundamental ceiling problem: once a cue is strong enough to be selected nearly every time, the metric cannot distinguish between a moderately strong cue and an extremely strong one. Price-equivalent auditing removes this ceiling by converting cue influence into a monetary premium—the price increase needed to neutralize the cue's effect—making vastly different cues directly comparable on a common scale.
- The study spans 113,472 trials across seven models from different families and two product categories, using a counterbalanced, position-controlled forced-choice design. This scale and rigor reveal that cues which look equally persuasive at equal price can differ by a wide margin in their true economic influence on model recommendations, meaning current auditing practices substantially under-resolve seller influence.
- The authors conduct the first price-equivalent audit of Jev, a decision-native model that outputs choice probabilities directly rather than generating text. Jev's profile is strikingly different from all text-based models tested: it resists most cues but remains susceptible to the strongest social-proof claims, suggesting that architectural design fundamentally shapes vulnerability to seller manipulation.

## Context
As large language models increasingly serve as autonomous shopping agents on behalf of users, the field of generative engine optimization (GEO) has emerged to study how seller-controlled content steers AI recommendations. Existing evaluation methods rely on choice-rate metrics that saturate at high cue strength, leaving a critical gap in understanding the true magnitude of seller influence. This paper addresses that gap by formalizing a parity threshold grounded in economic reasoning, providing a rigorous, reproducible benchmark that moves beyond single-score evaluations toward per-model cue-price profiles.

## Implications
For AI developers and auditors, this work provides a common, reproducible benchmark—complete with released stimuli, logs, and code—that enables systematic comparison of how different models respond to seller cues, supporting more informed model selection and deployment decisions. For the industry, the findings suggest that current GEO auditing practices may significantly underestimate the economic impact of seller manipulation on AI shopping agents, potentially allowing subtle but costly biases to go undetected. The divergent behavior of decision-native models like Jev also highlights that model architecture is a critical variable in susceptibility to persuasion, urging practitioners to evaluate not just what a model recommends but how its internal decision process processes external cues.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25843v1)
