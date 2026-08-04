---
title: Randomized Algorithms for Learning Partitions with Near Optimal Query Complexity in Constant Rounds
published: 2026-08-03T12:56:19Z
authors: Deeparnab Chakrabarty, Aditi Dudeja, David Saulpic
url: http://arxiv.org/abs/2608.02176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Randomized Algorithms for Learning Partitions with Near Optimal Query Complexity in Constant Rounds

## Abstract
We study the round complexity of learning a hidden partition $\mathcal{P}$ of an $n$-element universe using PAIR queries: PAIR($x,y$) tells us whether $x$ and $y$ belong to the same part of the partition or not. While it is easy to learn using $n|\mathcal{P}|$ queries using a basic algorithm and this query complexity is optimal, this basic algorithm is highly sequential. Black, Mazumdar, and Saha [COLT 2025] recently gave tight deterministic round/query tradeoffs when the number of parts of $\mathcal{P}$ is known. In particular they prove $Θ(\log\log n)$ rounds are sufficient and necessary to limit the number of queries to $n|\mathcal{P}|$. They leave proving a randomized lower bound as an open direction.   We show that randomization dramatically changes the picture. When the number of parts $k = |\mathcal{P}|$ is known, we give a simple 3-round randomized algorithm using $O(nk\log n)$ queries with high probability, and prove that 2 rounds require $Ω(n^{4/3}k^{2/3})$ queries -- the same as deterministic algorithms. We also study a more general setting where the number of parts is unknown. In this case, we give a 4-round randomized algorithm using $O(n|\mathcal P|\log^2 n)$ queries with high probability, and prove that 3-rounds cannot achieve near-optimal query complexity. Furthermore, we show an even bigger separation in this regime between randomized and deterministic algorithms: for the latter, $Θ(\log n/\log\log n)$ rounds are necessary and sufficient to obtain near-optimal query complexity.

## Metadata
- **Published**: 2026-08-03T12:56:19Z
- **Authors**: Deeparnab Chakrabarty, Aditi Dudeja, David Saulpic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02176v1)