---
title: HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving
published: 2026-09-08T06:26:46Z
authors: Han Jin
url: http://arxiv.org/abs/2609.08306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HoneyRoute: Honeypot-Model Routing for Adversarial LLM Serving

## Abstract
We introduce HoneyRoute, an inference-serving layer that detects whether an incoming request is malicious and, if so, routes it to a dedicated honeypot model, shielding production while the adversary's interaction is continuously harvested for intelligence. Existing defenses embed traps inside model memory or rebuild deception at the protocol layer, leaving the serving tier unprotected and feeding nothing back into detection. HoneyRoute couples (i) a streaming router (a frozen 0.8B-embedding backbone with per-domain MLP heads), (ii) a dual-implementation honeypot (a rule/prompt-engineered code honeypot or a dedicated same-family replica), and (iii) an analysis loop that converts trapped interactions into attacker fingerprints for router retraining. On a production trace plus a seven-domain attack corpus, the router reaches F1=.911 at 38 ms median added latency, matching 96% of a two-tier guard-LLM cascade's F1 at 1/385 of its latency with 0% evasion under 13 adversarial transformations; diverting the malicious share cuts production-model token consumption under concurrent flooding with real GCG-suffix payloads by 97.8%; the trained replica agrees with the production model on 92.9% of benign holdout requests, while naive unconditional bait injection collapses to 7.6% and selective camouflaged injection recovers to 88.9%, mapping the recoverable fidelity-traceability frontier; and a loop-trained correction head cuts misrouting of legitimate security research 9x while raising detection F1 to .933.

## Metadata
- **Published**: 2026-09-08T06:26:46Z
- **Authors**: Han Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08306v1)