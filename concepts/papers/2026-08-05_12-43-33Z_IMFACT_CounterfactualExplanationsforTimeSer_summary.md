# Summary: 2026-08-05_12-43-33Z_IMFACT_CounterfactualExplanationsforTimeSeriesviaI.md
Saved: 2026-08-05 20:35
Source: 2026-08-05_12-43-33Z_IMFACT_CounterfactualExplanationsforTimeSeriesviaI.md
Model: None

---

## Summary  
The paper introduces IMFACT – a model‑agnostic framework that generates plausible counterfactual explanations for time‑series classifiers by operating in the decomposition space of Empirical Mode Decomposition (EMD). By swapping Intrinsic Mode Functions (IMFs) with those from a Nearest Unlike Neighbour (NUN), IMFACT avoids destroying the temporal structure inherent to oscillatory signals and instead produces physically plausible counterfactuals. The approach is evaluated on two UCR benchmarks, FaultDetectionA and FruitFlies, where it demonstrates superior reliability and proximity compared with existing methods.

## Key Contributions  
- [Finding 1] IMFACT provides a model‑agnostic framework that generates counterfactual explanations by manipulating the IMF components of an EMD decomposition rather than raw feature space.  
- [Finding 2] The variance‑based selection of IMFs combined with three NUN substitutions yields the highest reliability and plausibility scores on both UCR datasets, outperforming two prominent baselines.  
- [Finding 3] Cycling across three NUNs improves proximity to the original signal while preserving classifier behavior, achieving the best performance in terms of closeness metrics.

## Methodology  
The input time series is first decomposed into a set of Intrinsic Mode Functions via EMD. A variance‑based strategy selects the most discriminative IMFs and progressively substitutes each with an IMF from a Nearest Unlike Neighbour (NUN) until the classifier’s prediction flips to the target class. The authors also explore a multi‑NUN cycling extension, where successive NUNs are applied iteratively. Six distinct IMF‑selection strategies are evaluated, allowing systematic comparison of how different numbers and types of NUNs affect the counterfactual quality.

## Results  
The variance‑based strategy with three NUNs outperforms two well‑known baseline techniques on both reliability (percentage of explanations that preserve classifier behavior) and plausibility (how physically reasonable the altered signal is). Additionally, cycling across three NUNs yields the best proximity to the original time series across FaultDetectionA and FruitFlies, indicating a more faithful representation while still achieving the desired class transition. These results confirm that IMF‑based substitution can generate explanations that are both reliable for classification and plausible in the physical domain.

## Significance  
Time‑series counterfactual analysis must preserve temporal dynamics to be meaningful; existing methods often produce implausible alterations by operating directly on raw features. IMFACT’s decomposition‑space approach addresses this limitation, offering a model‑agnostic tool that can be applied to any classifier without retraining. By delivering explanations that retain the signal’s oscillatory structure and remain close to the original data, IMFACT advances both interpretability and trustworthiness of AI systems dealing with time‑series data.

## Related Concepts  
- Intrinsic Mode Function (IMF) – a self‑adjusting oscillation extracted from a signal.  
- Empirical Mode Decomposition (EMD) – the algorithm that decomposes signals into IMFs.  
- Nearest Unlike Neighbour (NUN) – a technique selecting an IMF whose frequency is most unlike those in the current decomposition.  
- Counterfactual explanation – a method to generate alternative inputs that lead to a different classifier prediction.  
- UCR benchmark – a standard collection of time‑series classification tasks used for evaluation.
