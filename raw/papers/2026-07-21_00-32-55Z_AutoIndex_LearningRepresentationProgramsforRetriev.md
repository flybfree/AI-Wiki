---
title: AutoIndex: Learning Representation Programs for Retrieval
published: 2026-07-21T00:32:55Z
authors: Sam O'Nuallain, Nithya Rajkumar, Ramya Narayanasamy, Hanna Jiang, Shreyas Chaudhari, Andrew Drozdov
url: http://arxiv.org/abs/2607.18603v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoIndex: Learning Representation Programs for Retrieval

## Abstract
We present AutoIndex, a framework for learning representation programs: executable transformations that map raw documents into the representations exposed to a retrieval system. Rather than tuning retrievers, rerankers, or a small set of preprocessing hyperparameters, AutoIndex searches over programs that slice, enrich, normalize, reweight, or reorganize documents before indexing. At each iteration, AutoIndex performs validation-guided program search, in which agents diagnose failures of the current program and synthesize candidate updates, retaining only updates that improve retrieval quality under the resulting index. We evaluate AutoIndex on CRUMB, a benchmark of heterogeneous retrieval tasks, with BM25 held fixed across all experiments. The learned programs improve recall over a static full-document BM25 baseline on all 8 tasks, with average gains of +8.4% in Recall@100 and +8.3% in nDCG@10, and largest gains of +30.5% in Recall@100 and +43.6% in nDCG@10. These results suggest that document representation should not be treated as a fixed preprocessing choice made before retrieval begins, but as an explicit optimization target. Code to reproduce our results is available at https://github.com/auto-index/autoindex.

## Metadata
- **Published**: 2026-07-21T00:32:55Z
- **Authors**: Sam O'Nuallain, Nithya Rajkumar, Ramya Narayanasamy, Hanna Jiang, Shreyas Chaudhari, Andrew Drozdov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18603v1)