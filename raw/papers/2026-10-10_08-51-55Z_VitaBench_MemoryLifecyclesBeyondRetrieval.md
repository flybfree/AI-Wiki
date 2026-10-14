---
title: VitaBench: Memory Lifecycles Beyond Retrieval
published: 2026-10-10T08:51:55Z
authors: Muquan Yu, Dihan Hu
url: http://arxiv.org/abs/2610.14731v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VitaBench: Memory Lifecycles Beyond Retrieval

## Abstract
Long-term memory benchmarks for language agents primarily evaluate whether information from earlier interactions can be retrieved and used when relevant. Persistent memory systems face an additional problem before future use is known: deciding whether a memory should remain exact, be compressed, consolidated, or deleted. Existing benchmarks capture long-range retrieval, temporal reasoning, evidence reuse, and incremental interaction, but do not directly evaluate these earlier representation decisions. We formalize memory lifecycle evaluation and introduce VitaBench, a benchmark that makes lifecycle decisions measurable through repeated memory reviews and full-horizon counterfactual evaluation. VitaBench contains a controlled Diagnostic tier that isolates future-use patterns and a Naturalistic tier that composes them into generated customer-service-style interaction streams. We characterize lifecycle decision structure with three diagnostics: lifecycle headroom, measuring the advantage of adaptive choices over the best fixed strategy; horizon reversal, measuring when short-horizon decisions change under delayed consequences; and optimal-action diversity, measuring whether different memory states favor different lifecycle operations. Across both tiers, VitaBench exhibits substantial lifecycle structure: lifecycle headroom is 1.364 in Diagnostic and 1.405 in Naturalistic, and 60.2% and 56.5% of states, respectively, change their preferred action between short and full horizons. A learned delayed lifecycle policy further improves over the best fixed strategy on VitaBench-Naturalistic, reaching 101.5 versus 83.4 joint utility. These results show that retrieving past information and deciding how it should persist are distinct evaluation problems, and that lifecycle management requires evaluation of the delayed consequences of representation decisions.

## Metadata
- **Published**: 2026-10-10T08:51:55Z
- **Authors**: Muquan Yu, Dihan Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14731v1)