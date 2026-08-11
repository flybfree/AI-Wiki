# Summary: 2026-08-08_18-32-34Z_FairontheSurface_BenchmarkingHidden_OutputFairness.md
Saved: 2026-08-10 23:06
Source: 2026-08-08_18-32-34Z_FairontheSurface_BenchmarkingHidden_OutputFairness.md
Model: None

---

## Summary  
The paper introduces FairGap, a benchmark that evaluates fairness in LLM‑based recommender systems at both observable and hidden levels of output. It argues that existing audits only examine the visible recommendation shift (OBS) while ignoring substantial internal representation changes (IBS). The authors demonstrate that ROA—measuring alignment between these two metrics—often stays below 0.22, revealing a widespread decoupling where users see stable outputs despite hidden shifts. Moreover, activation steering can dramatically reduce IBS but at the cost of worsening OBS, exposing a fundamental tension between internal and output‑level fairness.

## Key Contributions  
- **Finding 1:** FairGap is the first benchmark that jointly assesses observable output shift (OBS) and hidden representation shift (IBS) using controlled counterfactual identity probes across gender, age, and race.  
- **Finding 2:** The study reveals pervasive hidden‑output decoupling: Representation‑Output Alignment (ROA) rarely exceeds 0.22, indicating that many users experience stable recommendations while the model’s internal representations shift substantially.  
- **Finding 3:** Activation steering that reduces IBS by up to eightfold simultaneously worsens OBS, highlighting a trade‑off between internal and output fairness that current frameworks cannot diagnose.

## Methodology  
The authors construct FairGap by applying gender, age, and race counterfactual identity probes to six open‑weight LLM families across three recommendation domains. For each probe pair they compute OBS (difference in recommended items) and IBS (distance between hidden embeddings). ROA is defined as the correlation between these two shifts, and quadrant diagnostics categorize user‑level mismatches where outputs are stable but internal representations shift.

## Results  
Across the evaluated models, ROA averages 0.18 with a maximum of 0.22, confirming that most systems show low alignment between hidden and observable fairness. A non‑negligible subset of users exhibits stable OBS while IBS changes by up to 4×, which FairGap can detect but output‑only audits cannot. When the authors apply activation steering to reduce IBS, it drops by an average of 8×, yet OBS deteriorates by roughly 15%, illustrating the identified tension.

## Significance  
This work challenges the prevailing assumption that stable recommendations imply fair internal processing and underscores the need for holistic fairness audits. By exposing hidden‑output gaps, FairGap informs designers to consider both representation and output levels, potentially preventing subtle biases from propagating through recommendation pipelines.

## Related Concepts  
- LLM recommenders  
- Fairness audits (observable vs. hidden)  
- Counterfactual identity probes  
- Representation‑Output Alignment (ROA)  
- Activation steering  
- Hidden‑output decoupling
