---
title: The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems
published: 2026-09-03T06:31:56Z
authors: Guangjun Liu
url: http://arxiv.org/abs/2609.03425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Civilization Framework: Sovereign-Anchored Communication Between Personal Multi-Agent Systems

## Abstract
Humans are the transport layer between AI systems, losing context at every hop. We present the Civilization Framework, whose addressable party is the civilization, not the agent (one human sovereign, a persistent ledger, and interchangeable agents), and the Embassy Protocol, a carrier-agnostic overlay: messages arrive asynchronously at a resident ledger endpoint, any online agent of the receiver handles them, and commitment state on both ledgers, not delivery, is ground truth. Authority derives from memory: an agent's power to act for its civilization is capped by the memory it can access and externalized through signed credentials, separate from civilization-level reputation. We identify the temporal-weight effect, a hazard in AI-to-AI communication where what arrives first acquires unearned authority, and test it in one frontier model in a preregistered 1,908-trial experiment. With verification removed, an incorrect upstream claim arriving first captures 54.2% of answers (4.2% under full verification), while the same claim arriving after the receiver has sealed its own answer captures 31.6% (the two prompt shells are not length-matched, so part of that gap may reflect shell form; see Section 7), and both registered question-set specifications agree on these two verdicts (the exclusion specification is preregistered as under-powered). Two secondary results, the mitigation from instruction-level provenance labeling and sealed-answer accuracy equivalence, are specification-dependent, holding only under the all-questions specification. Because a registered check of tool use failed its call-budget condition, the registration classifies the round as inconclusive and every result above, primary and secondary, is reported as exploratory; a replication with harness-enforced budgets is planned. The framework's intra-civilization layer has a working implementation.

## Metadata
- **Published**: 2026-09-03T06:31:56Z
- **Authors**: Guangjun Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03425v1)