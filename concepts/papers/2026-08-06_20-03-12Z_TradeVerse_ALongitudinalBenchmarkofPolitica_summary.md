# Summary: 2026-08-06_20-03-12Z_TradeVerse_ALongitudinalBenchmarkofPoliticalNegoti.md
Saved: 2026-08-09 22:24
Source: 2026-08-06_20-03-12Z_TradeVerse_ALongitudinalBenchmarkofPoliticalNegoti.md
Model: None

---

## Summary  
TradeVerse is a longitudinal benchmark that reconstructs minutes from the World Trade Organisation (WTO) ministerial meetings to evaluate large language models on tasks that require tracking multi‑round political negotiations, predicting harmonized system codes, identifying responding countries, and generating final statements. By using 1 170 meeting transcripts across five groups and eighty‑nine product groups, the authors create the first benchmark that forces LLMs to maintain context over years of diplomatic exchange.

## Key Contributions  
- TradeVerse is the first longitudinal benchmark dedicated to political negotiation in international trade.  
- It reconstructs 1 170 WTO meeting minutes and defines three downstream tasks: HS‑code prediction, respondent‑country identification, and role‑playing final statements.  
- Experiments demonstrate that current state‑of‑the‑art LLMs struggle with these tasks due to the need for long‑term context.

## Methodology  
The authors extracted anonymized transcripts of WTO ministerial meetings covering five negotiation groups and 89 product groups. They built three tasks: (1) given a meeting transcript, predict the HS chapter codes of the products discussed; (2) infer which country is responding to a statement based on its content; and (3) generate the response for the very last round as if playing the role of that country. All labels are recovered directly from the official minutes without manual annotation.

## Results  
State‑of‑the‑art LLMs achieve low accuracy on HS code prediction (≈ 40 % F1), moderate success in respondent identification (≈ 55 % accuracy), and poor performance in generating coherent final statements (BLEU ≈ 30). These results highlight the difficulty of maintaining long‑term context across many negotiation rounds.

## Significance  
TradeVerse reveals that existing benchmarks ignore longitudinal dynamics, limiting LLM evaluation. It provides a realistic test for models handling political negotiation data and informs future research on institutional AI and multilingual trade policy analysis.

## Related Concepts  
Longitudinal data, HS codes, WTO negotiations, LLMs, contextual understanding, role‑playing generation, benchmarking in political discourse.
