---
title: Similar Models, Broken Odds: Where Luce's Axiom Fails in Chatbot Arena
url: http://arxiv.org/abs/2610.19095v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_19-33-25Z_SimilarModels_BrokenOdds_WhereLuce_sAxiomFailsinCh.md
generated_at: 2026-10-14 21:17
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a systematic violation of Luce's choice axiom in Chatbot Arena's Bradley-Terry ranking model, demonstrating that voters distinguish near-identical model variants far more decisively than the single-score Bradley-Terry framework predicts. Analyzing 1.8 million Arena votes, the authors show that votes between versions of the same model are 1.37 times more decisive than the model expects, with similar inflation across model sizes, generations, and labs. A lightweight four-to-six-parameter correction improves held-out prediction, primarily by better modeling ties, though the overall leaderboard ordering remains largely unchanged.

## Key Takeaways
- On 1.8 million Chatbot Arena votes, pairwise comparisons between versions of a single model are 1.37 times more decisive than Bradley-Terry predictions, between sizes of one model generation 1.26 times, and between models from one lab 1.12 times, with a one-year-later release reproducing consistent multipliers. The effect survives alternative tie treatments, restricted prompt subsets, topic filtering, and timing controls, indicating a robust structural failure of the single-score assumption.
- A compact correction with only four to six parameters outperforms both Bradley-Terry and heavily parameterized alternatives on held-out vote prediction, with gains concentrated almost entirely in modeling ties. When frozen and applied to new model releases under a pre-registered test, the correction improves tie handling but does not establish better head-to-head odds, and the leaderboard ordering barely shifts.
- In a controlled experiment using language-model judges and three-answer menus, a near-copy model draws votes predominantly from its twin when choices are pooled across prompts, producing a log-odds shift of +0.10 (95% confidence interval 0.05 to 0.16). Within a single prompt the shift is smaller but statistically clear for two of four judge models, confirming that similarity in wording and formatting tracks the violation of Luce's axiom.

## Context
Chatbot Arena has become one of the most widely referenced benchmarks for evaluating large language models, relying on the Bradley-Terry model to convert human preference votes into a single Elo-style score per model. This framework implicitly assumes Luce's choice axiom, which states that the relative probability of choosing between any two options depends only on their scores and is independent of the presence of other alternatives. Choice theory has long predicted that this axiom breaks down when alternatives are near-copies, yet no prior work had quantified the magnitude of this violation at the scale of millions of real-world preference votes across a major public leaderboard.

## Implications
For practitioners and model developers, these findings suggest that Chatbot Arena rankings systematically understate the true decisiveness of comparisons between closely related model variants, which can obscure meaningful quality differences between fine-tuned versions, quantized variants, or successive releases from the same lab. The fact that a four-to-six-parameter correction outperforms much larger models on held-out prediction signals that the dominant failure mode is tie modeling rather than complex preference structure, pointing toward a practical and parsimonious path for improving leaderboard methodology. Industry stakeholders who rely on Arena rankings for procurement, safety evaluation, or competitive benchmarking should treat near-copy comparisons with caution, as the current single-score framework may mask genuine performance distinctions that voters actually perceive.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19095v1)
