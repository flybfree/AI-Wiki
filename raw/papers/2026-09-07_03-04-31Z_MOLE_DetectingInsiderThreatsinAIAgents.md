---
title: MOLE: Detecting Insider Threats in AI Agents
published: 2026-09-07T03:04:31Z
authors: Aashiq Muhamed, Virginia Smith
url: http://arxiv.org/abs/2609.06966v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MOLE: Detecting Insider Threats in AI Agents

## Abstract
Model misalignment, prompt injection, or operator misuse could lead AI agents operating frontier-lab accounts to exfiltrate model weights, poison training data, or weaken release gates. Existing benchmarks do not test whether defenders can detect this activity among routine work under a limited review budget. We introduce MOLE, an open benchmark of 150 AI-operated accounts sharing 9 stateful services over 30 workdays, with 12 threats and 8 corpora from four models totaling roughly 20 billion tokens. Of 39 agent models, 72% complete most assigned harmful objectives and agent refusal does not predict completion. MOLE enables comparison of 40 monitors across corpus generators, observability levels, and threats; even the best evaluated monitor in our single-day audit-event comparison misses nearly half of completed harm. MOLE also enables monitor development: benchmark-guided search improves a mid-tier monitor by 49-64%, while selective use of a stronger monitor improves budget-AUC by 10% over applying it to every account-day at comparable modeled cost.

## Metadata
- **Published**: 2026-09-07T03:04:31Z
- **Authors**: Aashiq Muhamed, Virginia Smith
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06966v1)