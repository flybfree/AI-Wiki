---
title: Scoring Both Directions: LLMs realize the MRS they cannot reliably parse
published: 2026-09-24T16:27:54Z
authors: Soham Dan
url: http://arxiv.org/abs/2609.30071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Scoring Both Directions: LLMs realize the MRS they cannot reliably parse

## Abstract
The English Resource Grammar (ERG) is a hand-written computational grammar of English. Given a sentence, its processor, ACE, produces a formal meaning representation called Minimal Recursion Semantics (MRS): a graph of the sentence's predicates and their arguments. The grammar is bidirectional and can also turn an MRS back into an English sentence. \citet{hajdik2019} used the ERG's treebank to build a benchmark for that generation task, MRS to text, and trained sequence-to-sequence models to solve it. The parsing task, text to MRS, can be tested on the same sentences. We reconstruct their 10K-sentence test split, and score two large language models, Claude Sonnet~4.5 and Claude Opus~5, in both directions against their trained systems and against ACE, with no task-specific training. Given an MRS and three examples, Opus writes the sentence at 76.3 BLEU, ten points above their system trained on 72k pairs (66.1 BLEU), and comparable to their system trained on a million extra pairs (77.2 BLEU). Sonnet scores 65.7 BLEU, and letting it choose among ACE's own candidate sentences lifts it to 69.6, while a pooled judge that keeps Opus's own sentence among the candidates adds 0.6 points (77.0 BLEU). In the parsing direction, however, the models fall far behind ACE: asked for the MRS of the same sentences, they reach 57.2 (Sonnet) and 65.5 (Opus) F$_1$ on the graph's predicates and arguments against 91.0 for ACE, and exact-match the gold on about 1\% of sentences. We characterize the failure modes for the parsing tasks, and conclude that a generation score alone does not show that models understand formal semantic representations.

## Metadata
- **Published**: 2026-09-24T16:27:54Z
- **Authors**: Soham Dan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30071v1)