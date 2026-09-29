---
title: Identical Runs, Different Results: Benchmarking AI Coding Agents on Open-Weight Models
published: 2026-09-27T18:05:02Z
authors: Eduardo Ariño de la Rubia, Szilard Pafka
url: http://arxiv.org/abs/2609.33812v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Identical Runs, Different Results: Benchmarking AI Coding Agents on Open-Weight Models

## Abstract
Repeated runs of the same coding agent are known to give different benchmark scores. We ask what that variation means for a team running an agent on its own task, by intensive replication on one machine-learning task: an agent improves the training code of an XGBoost classifier for airline delays, and a holdout it never sees scores the result. Across 584 runs, we compare six agents on six open-weight model endpoints, run six agent-model pairings 52 times each under fixed settings, and repeat three of them on a larger model from the same family. Identical runs of one pairing varied more than the pairings differed from one another, so comparisons of a few runs ranked them unreliably; resolving the agent differences we observed would take tens to more than a hundred runs of each. Runs on the larger model scored clearly higher, but by less than one run-to-run standard deviation, and the gap was more than twice as large with one agent as with the others. Fewer than one run in twenty broke the task's data rules, but those runs held the highest scores. Rejecting those runs first and keeping the best compliant result among a few attempts reliably improved the delivered model, even though a few runs could not rank the agents. On flights from a later year, the delivered models kept only a third of their gain over the starting code. At list prices, cost differed more than twentyfold between two agents on the same model, mostly through the prompt cache. Agents and models should be evaluated as pairings, over repeated attempts, with compliance reported beside quality. Data, code and every delivered program: https://github.com/earino/identical-runs-different-results

## Metadata
- **Published**: 2026-09-27T18:05:02Z
- **Authors**: Eduardo Ariño de la Rubia, Szilard Pafka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33812v1)