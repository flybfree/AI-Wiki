# Summary: 2026-06-02_17-58-02Z_LanguageModelsCompareQuantitiesUsingNumber_specifi.md
Saved: 2026-06-02 23:00
Source: 2026-06-02_17-58-02Z_LanguageModelsCompareQuantitiesUsingNumber_specifi.md
Model: None

---


## Summary  
The paper investigates how large language models (LMs) compare quantities that include measurement units, such as “110 cm” versus “1.2 m”. It demonstrates that LMs often make systematic errors when the two expressions are close in value, and that these errors can be predicted by simple linear models that use only the numerical‑difference and unit‑scale‑difference cues. The authors also show that causal manipulations of the underlying subspaces associated with those cues alter the model’s output, suggesting that LMs rely on a collection of heuristics rather than performing exact unit conversions.  

## Key Contributions  
- [Finding 1] Accuracy degrades near the comparison boundary where small changes in value determine the correct answer.  
- [Finding 2] Linear surrogate models predict LM preferences from numerical‑difference and unit‑scale‑difference cues, revealing systematic error patterns.  
- [Finding 3] Causal interventions on subspaces aligned with those cues shift model output, indicating a heuristic‑based rather than exact conversion process.  

## Methodology  
The authors constructed controlled comparison tasks that span multiple unit systems (e.g., centimeters vs. meters). Each task presented pairs of quantities expressed in different units and asked the LM to select the larger or smaller value. The model’s responses were recorded, and their accuracy was measured. To uncover underlying cues, the researchers fitted linear regression models using the numerical‑difference and unit‑scale‑difference variables as predictors of preference scores. Additionally, they performed causal interventions—temporarily fixing either the numerical difference or the unit‑scale difference—to observe how model outputs changed, thereby testing whether the LM’s reasoning is driven by these specific subspaces.  

## Results  
The experiments confirmed that errors cluster around the boundary between two values, where a 0.1 m shift can flip the correct answer. The linear surrogate models explained a substantial portion of preference variance (R² ≈ 0.78), confirming that only the magnitude difference and the relative unit scaling matter. When the authors intervened on the numerical‑difference subspace, the model’s choice shifted predictably; similar shifts occurred for the unit‑scale‑difference subspace. These causal manipulations support the hypothesis that LMs compare quantities via a bag of heuristics rather than converting both expressions to an exact shared scale.  

## Significance  
Understanding this heuristic reliance is crucial because it reveals how LMs handle real‑world reasoning tasks involving measurement units. If models truly convert values before comparing, errors would be random; instead, systematic bias suggests that the underlying representation treats numerals and units as separate, independently processed components. This insight can guide future work on improving metric reasoning in LLMs and informs the design of evaluation benchmarks for unit‑aware comparisons.  

## Related Concepts  
- Quantity comparison  
- Unit scaling  
- Numerical‑difference cue  
- Unit‑scale‑difference cue  
- Heuristic‑based reasoning  
- Causal intervention  
- Linear surrogate modeling

[[2026-06-02_17-58-02Z_LanguageModelsCompareQuantitiesUsingNumber_specifi.md]]