# Summary: 2026-07-31_20-42-53Z_Sixteenmodels_fewerthantwovoices_measuringensemble.md
Saved: 2026-08-03 21:24
Source: 2026-07-31_20-42-53Z_Sixteenmodels_fewerthantwovoices_measuringensemble.md
Model: None

---

## Summary  
This paper investigates how the semantic diversity of language‑model outputs varies when multiple models are combined into an ensemble, using a psychotherapeutic case as the test stimulus. It introduces a novel measure of per‑model dissent—defined as the complement of each model’s mean similarity to its peers—in order to identify which voice contributes most to overall dispersion. The authors demonstrate that ensembles generate more distinct formulations (average 1.69) than any single model alone (1.43), and they show that model identity does influence this variance, though conventional categorisations capture only part of the effect.  

## Key Contributions  
- [Finding 1] Ensembles produce a higher Vendi Score (≈ 1.69) than a single‑model baseline (≈ 1.43), indicating greater semantic diversity across model families.  
- [Finding 2] The per‑model dissent metric, derived from the similarity matrix of an ensemble, pinpoints the most divergent voice and quantifies how much each model diverges from its peers.  
- [Finding 3] Model identity accounts for a non‑zero share of the variance in dissent, but this effect is not fully explained by standard taxonomy (e.g., scale differences or family grouping).  

## Methodology  
The study assembled sixteen language models drawn from ten families and evaluated them on fifteen stratified psychotherapeutic vignettes, yielding 7,082 distinct formulations. For each ensemble the Vendi Score—computed as the exponential of the von Neumann entropy of a pairwise similarity matrix—was calculated to gauge diversity. Per‑model dissent was obtained by subtracting each model’s mean similarity from one, providing a direct measure of its contribution to overall dispersion. The authors preregistered a hypothesis that model identity would explain part of the variance in dissent and tested it using stratified vignettes, ensuring reproducibility.  

## Results  
The ensemble average distinct formulations rose to 1.69 versus 1.43 for a single model, confirming higher diversity. Dissent values ranged from low (≈ 0.05) to high (≈ 0.28), with the highest dissent belonging to models that were most dissimilar to their peers. Model identity contributed to this variance; scale differences sometimes aligned across pairs, while family grouping produced only five two‑member lines of similar dissent. Crucially, the most divergent voice shifted when the panel composition changed, suggesting the outlier reflects ensemble dynamics rather than a single model’s inherent style. Dissent did not track the intended interpretive openness of the vignettes; instead it clustered by clinical content, indicating that dispersion is an emergent property of the ensemble.  

## Significance  
Understanding where diversity originates in model ensembles is crucial for applications such as therapeutic dialogue generation, where multiple perspectives can be beneficial yet must not obscure a single correct answer. This work provides a principled way to quantify dissent and highlights methodological pitfalls when assuming that a single “correct” response exists. By separating ensemble‑level dispersion from individual model behavior, the study advances both theory and practice in AI‑driven human‑centered applications.  

## Related Concepts  
- Vendi Score (exponential von Neumann entropy of similarity matrix)  
- Ensemble dispersion and uncertainty  
- Per‑model dissent as complement of mean similarity  
- Model identity effects on variance decomposition  
- Interpretive openness vs. clinical content stratification  
- Spectral index and spectral decomposition in diversity analysis
