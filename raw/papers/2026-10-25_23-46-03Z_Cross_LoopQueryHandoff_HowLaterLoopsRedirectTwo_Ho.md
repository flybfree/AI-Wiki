---
title: Cross-Loop Query Handoff: How Later Loops Redirect Two-Hop Retrieval in the Ouro Looped Language Models
published: 2026-10-25T23:46:03Z
authors: Ziyu Mu, Zehua Wang
url: http://arxiv.org/abs/2610.34639v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Loop Query Handoff: How Later Loops Redirect Two-Hop Retrieval in the Ouro Looped Language Models

## Abstract
How do later loops in a pretrained looped language model repair two-hop retrieval? We study Ouro-1.4B and Ouro-2.6B by transplanting attention queries between loops at the same layer, head and final prompt position. On synthetic in-context questions, injecting the layer-indexed collection of loop-3 queries throughout loop 1 rescues 90% and 97% of questions answered incorrectly at loop 1 and correctly at loop 3, versus 24% and 21% for shuffled donors. The rescue also holds under greedy generation in Ouro-2.6B; in Ouro-1.4B it is limited to four-candidate ranking. Crossed donor-recipient swaps favor retrieval through the donor's bridge entity over copying its answer, although a substantial positional component remains in Ouro-2.6B. Late keys and values rescue far fewer targets. Freezing queries at their loop-1 values also damages two-hop accuracy more than a matched question that supplies the bridge. On natural questions, rescue is smaller and replicates only in Ouro-2.6B, and crossed swaps do not establish bridge redirection. These results identify a transferable collection of late-loop queries that supports bridge-conditioned retrieval on synthetic scenes; they do not locate where the bridge is computed or establish a single-vector handoff.

## Metadata
- **Published**: 2026-10-25T23:46:03Z
- **Authors**: Ziyu Mu, Zehua Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34639v1)