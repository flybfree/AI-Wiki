---
title: Buy the Rumor, Sell the News: When Is News Priced In?
url: http://arxiv.org/abs/2608.14014v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_07-02-41Z_BuytheRumor_SelltheNews_WhenIsNewsPricedIn.md
generated_at: 2026-08-16 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether financial news is priced in before it is published and how rumors versus confirmed stories affect market reactions. Using a large language model classifier on 4.57 million articles covering 3,000 US stocks from 2023‑2026, the authors find that price moves concentrate at or just after publication, that markets underreact to fundamental news and overreact to story‑driven news, and that publicity raises volatility before release while it falls afterward.

## Key Takeaways
- The cumulative move in the news direction by the close of publication day is 2.8 times its value 20 days later, indicating most price impact occurs at or before publishing.
- For rumor‑flagged events the entire move is captured on the rumor day while subsequent confirmation contributes nothing, showing a clear separation between speculation and verification.
- Fundamentals such as earnings drift in the news direction for weeks, whereas soft story news like launches give back their move, revealing differential market absorption rates.

## Context
The study leverages AI‑driven classification to quantify how quickly markets digest public information, providing empirical evidence that contradicts traditional “news is already priced in” assumptions. This work advances understanding of information processing speed and the role of uncertainty in financial markets, which are central concerns for both quantitative finance and machine learning applications.

## Implications
For practitioners, the drift patterns suggest news‑conditioned forecasting models should weight early market reactions more heavily than later price movements. In AI research, the identified volatility dynamics offer new targets for training models to predict market impact before official releases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14014v1)
