# Summary: 2026-07-30_06-24-38Z_MeasuringAlignmentWithReaderHighlightsNetofPositio.md
Saved: 2026-07-30 21:40
Source: 2026-07-30_06-24-38Z_MeasuringAlignmentWithReaderHighlightsNetofPositio.md
Model: None

---

## Summary  
The paper addresses the problem of measuring how well a context‑compression model aligns with human social highlights while avoiding bias from crowd‑marking front‑loading and longer marked sentences. It introduces a novel alignment metric that matches marked to unmarked sentences at equal relative depth and length rank, calibrates estimators on synthetic nulls built solely from position and length, and demonstrates that the resulting ranking outperforms naive truncation and human judgment. The authors also show that classic heuristics are not null, indicating partial recoverability of signal.  

## Key Contributions  
- [Finding 1] A bias‑free alignment metric that matches marked sentences to unmarked ones sharing both relative depth and within‑document length rank.  
- [Finding 2] Calibration on synthetic nulls constructed only from position and length eliminates false positives seen with depth‑only stratification.  
- [Finding 3] The model’s importance ranking retains 38.4 % of crowd‑marked sentences versus 19.9 % of matched neighbours, yielding a statistically significant enrichment (+0.196, p=0.0005).  

## Methodology  
The authors collect at least twelve independent readers’ highlights on 120 web documents. For each document they compute the relative depth (position within the document) and the length rank of every highlighted sentence. They then create a null set by randomly pairing sentences that share identical depth and length rank but are not marked, ensuring the only difference is marking status. Estimators such as language‑model importance scores are calibrated on these nulls to control for position‑only effects. The calibration step is crucial because depth‑only stratification alone produces false positives in 20–36 % of nulls that contain no true effect.  

## Results  
On the benchmark corpus, the calibrated ranking keeps 38.4 % of marked sentences while its nearest unmarked neighbours are kept at 19.9 %, an enrichment of +0.196 (95 % CI [+0.148, +0.239], p=0.0005). This beats naive truncation (+0.003) and is indistinguishable from a single human reader’s score (+0.182), comparable to GPT‑5.4 (+0.002) but lower than Claude Opus 5. Classical heuristics such as Luhn’s 1958 method reach +0.088, showing that some signal is recoverable by counting words; conditioning on lexical centrality only reduces the effect by 0.010, indicating centrality is not the primary driver.  

## Significance  
By removing both front‑loading and length bias, this work provides a reliable metric for evaluating model alignment with human social highlights, enabling fair comparisons across compression strategies. The calibration on synthetic nulls ensures statistical validity without assuming clustering or lexical properties, making the results robust to variations in data sources. Moreover, the finding that classic heuristics are not null suggests that some aspects of reader selection can be recovered by simple word‑count measures.  

## Related Concepts  
- Context compression  
- Social highlighting  
- Crowd‑marked sentences  
- Relative depth  
- Within‑document length rank  
- Synthetic null calibration  
- Language‑model importance ranking  
- Null set construction
