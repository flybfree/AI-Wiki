# Summary: 2026-07-31_15-44-43Z_LeakIt_AProbabilisticApproachtoTraining_DataExtrac.md
Saved: 2026-08-03 21:24
Source: 2026-07-31_15-44-43Z_LeakIt_AProbabilisticApproachtoTraining_DataExtrac.md
Model: None

---

## Summary  
The paper proposes a probabilistic framework for detecting training‑data leakage in black‑box language models by treating the model’s output distribution \(p(.|x)\) as an estimate of the data used during training and casting leakage signals into functionals of that distribution. It extends the conventional blind‑baseline critique to the sampling regime, showing that surface‑level classifiers already achieve high AUC but fail to capture per‑document disclosure. The authors introduce “LeakIt,” a tool that isolates exact identifier reproductions from individual documents rather than relying on aggregate ROC‑AUC scores. Their work demonstrates that leakage risk grows with model capacity and is unevenly distributed across code versus prose, making aggregate metrics misleading.

## Key Contributions  
- **Finding 1:** Blind bag‑of‑words classifiers on WikiMIA reach an AUC of 0.97 (TPR = 0.90 at 5% FPR), indicating that surface text alone can already expose training data, so sampling does not add detectable information.  
- **Finding 2:** Per‑document extraction is invisible to aggregate ROC‑AUC; on Pythia‑6.9B, 83 of 500 documents containing identifiers are reproduced verbatim, with a mismatched‑prefix control confirming that each leak originates from a single document.  
- **Finding 3:** The risk of identifier leakage rises sharply with model size (4.0% → 12.1% in prose; 5.6% → 16.6% in code), and temperature/nucleus sampling or corpus deduplication have negligible impact.

## Methodology  
The authors model the training‑data set as a distribution \(p(.|x)\) sampled from the model’s output for each document. They cast leakage signals as functionals of this estimated distribution, thereby extending blind‑baseline analysis to the sampling regime used in black‑box settings. Experiments are conducted on WikiMIA and an IID Pile split (MIMIR). For per‑document disclosure they use a mismatched‑prefix control: when a document’s exact identifier is reproduced under the original prefix but not under a random prefix, the leak is attributed to that specific document.

## Results  
On Pythia‑6.9B, 83 of 500 documents bearing identifiers are exactly reproduced; only 16.6% of those contain email addresses. The per‑document disclosure rate jumps from 4.0% in smaller models to 12.1% in larger ones and is roughly three times higher for code than prose. A 16‑token prefix suffices to extract a leak, temperature and nucleus sampling make little difference, and corpus deduplication does not reduce leakage. The incremental AUC gained from self‑concentration or gold‑continuation recovery is within the 95% confidence interval of zero.

## Significance  
Aggregate ROC‑AUC masks the real harm because it aggregates many small per‑document leaks into a single score. Privacy audits that rely solely on aggregate metrics cannot identify which documents are at risk, especially in high‑capacity models where leakage becomes more prevalent. The paper argues for reporting per‑document extraction decomposed by domain (code vs prose) and introduces LeakIt as an open tool to perform such audits.

## Related Concepts  
- Membership inference attacks  
- Black‑box language models  
- Sampling‑based training data leakage  
- ROC‑AUC evaluation  
- Per‑document disclosure detection  
- Identifier leakage in code versus prose  
- Temperature and nucleus sampling effects
