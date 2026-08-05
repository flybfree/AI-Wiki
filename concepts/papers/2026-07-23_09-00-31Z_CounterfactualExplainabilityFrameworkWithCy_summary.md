# Summary: 2026-07-23_09-00-31Z_CounterfactualExplainabilityFrameworkWithCycleGANA.md
Saved: 2026-07-24 02:34
Source: 2026-07-23_09-00-31Z_CounterfactualExplainabilityFrameworkWithCycleGANA.md
Model: None

---

## Summary  
The paper introduces **CounterFundus**, a CycleGAN‑driven counterfactual explainability framework that generates plausible healthy counterpart images for retinal disease classification and aligns their difference maps with the classifier’s attention using a new metric. By integrating an EfficientNet‑B5 detector with visual translation, CounterFundus produces localized explanations that correspond to clinically meaningful regions of fundus pathology. The framework also introduces the **Counterfactual‑Classifier Alignment Score (CCAS)**, which combines Spearman correlation, binary IoU and pointing accuracy into a single assessment protocol. Ablation experiments show that filtering counterfactuals by high CCAS improves downstream classification performance.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- Introduces CycleGAN‑based generation of disease‑to‑normal fundus images as interpretable counterfactual explanations.  
- Develops the Counterfactual‑Classifier Alignment Score (CCAS) to quantify spatial agreement between difference maps and classifier saliency across three dimensions.  
- Demonstrates that CCAS‑filtered counterfactual augmentations enhance downstream classification accuracy in retinal disease detection.

## Methodology  
The authors first employ an EfficientNet‑B5 model to detect retinal diseases on fundus images. The CycleGAN generator then creates a healthy counterpart image, and the pixelwise difference map is computed between the original pathological image and its translation. This difference map is aligned with EigenCAM attention maps using Euclidean distance minimization. To evaluate alignment, CCAS is calculated as the weighted sum of Spearman correlation (correlation of sorted pixel values), binary IoU (overlap of non‑zero regions), and pointing accuracy (matching attention hotspots). Finally, an ablation study filters counterfactuals by a minimum CCAS threshold and tests whether this subset improves classification performance.

## Results  
Experiments on the standard retinal disease dataset show that generated explanations are spatially consistent with classifier evidence across all three CCAS components. When only high‑CCAS counterfactuals are used, the model’s accuracy increases by 2–4 % compared to using all counterfactuals, confirming the value of the alignment filter. Visual inspection confirms that disease regions are correctly localized in the difference maps.

## Significance  
CounterFundus bridges the gap between deep‑learning classification and clinical interpretability by providing visually plausible, region‑specific explanations for each prediction. The CCAS metric offers a rigorous way to assess how well counterfactuals align with model attention, ensuring that explanations are both accurate and useful. By enabling automated screening with transparent visual maps, the framework reduces reliance on specialist assessments and supports trustworthy deployment of AI in ophthalmology.

## Related Concepts  
CycleGAN, EfficientNet‑B5, EigenCAM alignment, counterfactual explanations, saliency maps, post‑hoc interpretability, XAI (Explainable AI), retinal disease classification, difference maps, CCAS metric (Spearman correlation, binary IoU, pointing accuracy).
