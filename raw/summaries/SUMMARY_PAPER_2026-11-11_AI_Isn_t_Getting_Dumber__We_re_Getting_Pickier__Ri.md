---
title: AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models
url: http://arxiv.org/abs/2611.14333v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-10_16-56-16Z_AIIsn_tGettingDumber_We_reGettingPickier_RisingSta.md
generated_at: 2026-11-11 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether perceived declines in AI assistant quality reflect actual model degradation or shifting human evaluation standards. By analyzing 1.26 million blind votes on Chatbot Arena between May 2023 and August 2024, the authors demonstrate that for fixed, unchanged model pairs, the proportion of "both are bad" votes rose by approximately 1.71 percentage points per month, while relative rankings between models remained stable. The findings suggest that absolute human verdicts on AI outputs drifted upward in stringency even as comparative judgments held steady.

## Key Takeaways
- The "both are bad" vote share increased by 1.71 percentage points per month on a mean of 17.1% for identical model pairs, rising from 15.5% to 23.3% across fourteen frequently observed pairs between 2023 and 2024. This trend persisted within individual voters, across arrival cohorts, in every major language, and across interface changes, ruling out confounding variables such as prompt shifts or model version changes.
- Relative model rankings did not trend downward: in 2024, the stronger model's share of decisive votes remained flat. This critical distinction shows that the perceived decline is not a degradation of model quality but a tightening of what humans consider acceptable output, meaning absolute verdicts drifted while comparative assessments stayed constant.
- The drift is shared across models rather than attributable to any single model's behavior. Month effects estimated from other models' pairs removed the trend from each model's own pairs, indicating a platform-wide shift in human standards. A model that stands still would be expected to score 78% against the 2023 average, yet the "both are bad" share ended near its starting level, confirming the standards-following-the-category hypothesis.

## Context
This research addresses a persistent and consequential question in the AI community: whether public complaints about ChatGPT and similar assistants becoming "worse" reflect genuine model regressions or evolving user expectations. As LLM leaderboards like Chatbot Arena increasingly influence model development, funding decisions, and public trust, understanding whether human evaluation criteria are drifting is essential for interpreting benchmark results accurately. The paper fills a methodological gap by isolating human judgment drift from model performance changes using fixed model pairs over a sustained period.

## Implications
For practitioners and researchers relying on human preference data to train or evaluate models, this drift means that feedback signals collected over time are not directly comparable across periods, potentially introducing systematic bias into reinforcement learning from human feedback pipelines. Industry leaders and benchmark maintainers must account for rising evaluation standards when interpreting leaderboard scores or communicating model progress to the public, since a static model will appear to decline purely due to shifting human expectations rather than any technical regression.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14333v1)
