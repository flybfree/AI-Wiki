---
title: Playing log(N)-Questions over Wikipedia Abstracts: How Per-Round Errors Compound Under Information Asymmetry
published: 2026-09-16T17:41:12Z
authors: Peter Potash
url: http://arxiv.org/abs/2609.19113v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# Playing log(N)-Questions over Wikipedia Abstracts: How Per-Round Errors Compound Under Information Asymmetry

## Abstract
We evaluate six frontier language models on the two-agent $\log_2 N$-Questions game (Potash et al., 2019) to measure self-communication across an information asymmetry. A questioner with access to $N$ candidate Wikipedia lead paragraphs ($N = 4$ to $1024$) must identify a secret target using exactly $\log_2 N$ binary questions answered by an agent from the same provider that sees only the target. Across 408 games, win rate decays cleanly as a geometric power of horizon length, $p^{\log_2 N}$ ($p \approx 0.93$). Per-round failure rates are flat across the horizon, indicating that errors compound because more rounds must succeed rather than because individual rounds grow harder. Adjudication across three independent judges shows that losses divide between single-agent answer errors and discrimination failures, which become undetectable and unrecoverable under the two-agent structure rather than from channel breakdown. Claude Opus 5 lags behind due to systematic false-negative answers (82% answer errors), whereas the five leading models (GLM-5.3, GPT-5.6 Sol, Grok 4.6, Gemini 3.8 Flash, and Kimi K3) are closely clustered. Maximizing information gain requires structural partitioning (e.g., splitting on document titles), and neither reasoning-token expenditure nor API cost correlates with success ($r = -0.05$), highlighting communicative reliability as a distinct bottleneck from inference compute.

## Metadata
- **Published**: 2026-09-16T17:41:12Z
- **Authors**: Peter Potash
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19113v2)