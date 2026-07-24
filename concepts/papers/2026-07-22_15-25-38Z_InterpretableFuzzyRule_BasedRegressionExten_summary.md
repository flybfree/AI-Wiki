# Summary: 2026-07-22_15-25-38Z_InterpretableFuzzyRule_BasedRegressionExtensionfor.md
Saved: 2026-07-24 02:02
Source: 2026-07-22_15-25-38Z_InterpretableFuzzyRule_BasedRegressionExtensionfor.md
Model: None

---

## Summary  
The paper proposes an interpretable regression extension for the Ex‑Fuzzy library that enables Mamdani fuzzy inference with scalar consequents learned directly from data. It introduces a target‑aware partition initialisation strategy based on Fuzzy C‑Means clustering applied to an augmented input‑output space, which emphasises regions of feature space relevant to the output variable. The approach yields compact rule bases (10–15 human‑readable rules) that are both transparent and competitive with standard black‑box models. Experimental evaluation on ten regression datasets from the KEEL repository demonstrates that Gaussian partitions outperform uniform trapezoidal partitions, achieving a mean coefficient of determination of about 0.86.

## Key Contributions  
- [Finding 1] The authors introduce a target‑aware partition initialisation method using Fuzzy C‑Means clustering on an augmented input‑output space to generate linguistic variables that highlight output‑relevant regions.  
- [Finding 2] Gaussian partitions consistently outperform uniform trapezoidal partitions, delivering a higher mean coefficient of determination (≈0.86) than baselines such as linear regression or random forests.  
- [Finding 3] The extension produces compact rule bases of roughly ten to fifteen readable rules, illustrating the trade‑off between interpretability and predictive performance.

## Methodology  
The authors extended Ex‑Fuzzy with a Mamdani fuzzy regression module that learns scalar consequents from data rather than predefined membership functions. They employ Fuzzy C‑Means clustering on an augmented space formed by concatenating input features with the target variable, producing fuzzy partitions that are initialised to maximise relevance to the output. Two partition strategies—Gaussian and trapezoidal—are compared, and their rule bases are generated via Mamdani inference. The implementation is benchmarked against linear regression, multilayer perceptrons, and random forests on ten datasets from the KEEL repository.

## Results  
On the ten KEEL regression datasets, Gaussian partitions achieved a mean coefficient of determination of approximately 0.86, significantly higher than uniform trapezoidal partitions (≈0.75) and most black‑box baselines. The fuzzy rule bases contain between ten and fifteen rules, each interpretable in plain language, illustrating the method’s ability to balance accuracy with transparency.

## Significance  
This work matters because it provides a practical, transparent alternative to opaque regression models for safety‑critical and regulated applications where interpretability is required. By delivering competitive predictive performance while generating compact, human‑readable rule sets, the extension supports decision‑making processes that must be auditable and explainable.

## Related Concepts  
Fuzzy logic, Mamdani inference, fuzzy regression, Ex‑Fuzzy library, Fuzzy C‑Means clustering, target‑aware partition initialisation, Gaussian partitions, trapezoidal partitions, KEEL repository, interpretability in machine learning.
