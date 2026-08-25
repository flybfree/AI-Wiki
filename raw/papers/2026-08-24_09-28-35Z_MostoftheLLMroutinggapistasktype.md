---
title: Most of the LLM routing gap is task type
published: 2026-08-24T09:28:35Z
authors: Janghoon Lee
url: http://arxiv.org/abs/2608.23023v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Most of the LLM routing gap is task type

## Abstract
An LLM router picks which model should answer each query. The appeal is that models fail on different questions. Whatever single model is best overall still gets some wrong, and another model in the pool gets many of those right. Getting that choice right every time is the ceiling, and a router is an attempt to approach it.   However, recent work reports that routers do not get close. Across 21 routing methods on five benchmarks, sharply different designs land within a fraction of a point of each other, and all of them stay far below that ceiling. Learned routers often fail to beat simply always calling the strongest model.   We ask what those missed questions have in common. We set fourteen models to answer all 294 questions, with 7 task types across 3 languages: Korean, English and Hindi. We ran the whole matrix twice, changing nothing, but 5.37% of the 4,116 model-question pairs came out scored differently anyway. Run-to-run movement like that is normal, and we argue that a small win does not show that routing did anything, ours or anyone else's.   Counting an answer correct only when the model got it right in both runs, 29 questions on this matrix can be improved with routing. Every correct-answer count here is on that rule. Task type accounts for most of them: assigning each task type one model in advance, chosen once and never updated, improves 21 of the 29. Splitting each task type by language improves 2 more and leaves 6 of 294 unoptimized. That handful is what a learned router would have been built for, and it is smaller than the run-to-run movement above, which is a share of pairs rather than of questions. The static table we adopted answers 262 of 294 questions at $3.33 per run, against the best single model's 245 at $7.69.   All of this is fitted and scored on the same 294 questions with no holdout.

## Metadata
- **Published**: 2026-08-24T09:28:35Z
- **Authors**: Janghoon Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23023v1)