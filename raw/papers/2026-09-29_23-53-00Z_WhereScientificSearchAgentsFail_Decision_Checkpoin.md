---
title: Where Scientific Search Agents Fail: Decision-Checkpoint Auditing of Exposure and Inspection Attempts
published: 2026-09-29T23:53:00Z
authors: Hongmin Li, Wanli Zhao
url: http://arxiv.org/abs/2609.38670v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Scientific Search Agents Fail: Decision-Checkpoint Auditing of Exposure and Inspection Attempts

## Abstract
Final-answer accuracy does not reveal whether a scientific-search agent failed to encounter a target paper, attempt to inspect it, or return an accepted answer after inspection. We introduce decision checkpoints that record observations and tool actions without benchmark labels during inference, then join target identities and evaluator labels to assign outcome categories from recorded events. Across five conditions on 540 answerable AutoResearchBench Deep questions in a fixed, target-enriched environment, keyword search achieves 24.6\% accuracy, compared with 17.8\% for raw search. The keyword condition has fewer incorrect answers with neither target exposure nor inspection, but more incorrect answers after the target is exposed and left uninspected. Compared with keyword search, read-first has 27.4\% more recorded evidence-search calls. Target inspection attempts occur on 199 questions under read-first and 191 under keyword search; both conditions achieve 24.6\% accuracy. The checkpoint protocol makes these question-level differences explicit, distinguishing target exposure and inspection from aggregate accuracy and total tool use.

## Metadata
- **Published**: 2026-09-29T23:53:00Z
- **Authors**: Hongmin Li, Wanli Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38670v1)