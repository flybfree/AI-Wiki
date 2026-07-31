# Summary: 2026-07-30_16-41-55Z_BeyondSentiment_StructuredInformationExtractionfro.md
Saved: 2026-07-30 22:20
Source: 2026-07-30_16-41-55Z_BeyondSentiment_StructuredInformationExtractionfro.md
Model: None

---

## Summary  
The paper argues that financial news sentiment analysis is insufficient because it collapses multi‑dimensional information into a single polarity score. It proposes extracting six orthogonal semantic dimensions—event type, impact scope, temporal horizon, and semantic confidence—using LLaMA‑3.1 to enrich sentiment signals for stock prediction. The study demonstrates that structured features capture independent predictive value beyond sentiment.

## Key Contributions  
- Finding 1: FinBERT sentiment features show strong nonlinear predictive power (F1=0.576) but weak linear performance (F1=0.230), indicating a highly nonlinear relationship between sentiment and returns.  
- Finding 2: LLM‑extracted structured features exhibit substantial disagreement with sentiment, capturing orthogonal information as shown by a 53.5% systematic disagreement rate.  
- Finding 3: Combining both signal sources yields F1=0.600, significantly outperforming either alone (p<0.0001), and each structural dimension independently adds +0.019 F1.

## Methodology  
The authors leverage LLaMA‑3.1‑70B to parse 41,618 news–stock pairs from FNSPID into six structured dimensions: event type (e.g., earnings, merger), impact subject (company vs market), temporal horizon (short‑term vs long‑term), and semantic confidence (high/low). FinBERT is used for standard sentiment extraction. The framework extracts both sentiment scores and the six dimensions, then evaluates their predictive utility via F1 on a binary classification task.

## Results  
Experiments reveal that nonlinear models exploit sentiment’s high F1, while linear models underperform dramatically. Structured features alone are weaker but orthogonal to sentiment, evidenced by 53.5% disagreement. Ensemble of both yields the highest F1 (0.600). Ablation shows each structural dimension contributes ~14–21% importance, confirming that compressing news into a single sentiment score loses substantial information.

## Significance  
By decoupling sentiment from semantics, this work opens a new multi‑dimensional pathway for financial NLP, enabling more accurate stock forecasts and revealing hidden market signals. The balanced contributions of all six dimensions underscore the value of preserving diverse information in news analysis.

## Related Concepts  
Sentiment analysis, LLaMA‑3.1 language model, structured feature extraction, orthogonal information, F1 score, FNSPID dataset, event‑type classification, impact scope, temporal horizon, semantic confidence.
