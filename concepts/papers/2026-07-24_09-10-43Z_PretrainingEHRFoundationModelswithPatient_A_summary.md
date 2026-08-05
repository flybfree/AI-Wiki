# Summary: 2026-07-24_09-10-43Z_PretrainingEHRFoundationModelswithPatient_AwareSam.md
Saved: 2026-07-26 20:42
Source: 2026-07-24_09-10-43Z_PretrainingEHRFoundationModelswithPatient_AwareSam.md
Model: None

---

## Summary  
This paper addresses a critical limitation in the pretraining of autoregressive foundation models for electronic health records (EHRs), where standard sequence construction methods often introduce bias by unevenly weighting patient contributions and mixing data across patients. The authors propose Patient Sampling, a novel approach that enables fine-grained control over how training signals are distributed during model pretraining. By decoupling the selection of training windows from the global stream structure, Patient Sampling allows for more equitable and clinically meaningful representation of individual patient trajectories. This work identifies sequence construction as an underexplored yet crucial design choice in EHR foundation models.

## Semantic links
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-07-27]] — 4 title terms overlap; 13 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 16 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 12 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The standard concatenation-based approach (referred to as Global Stream) can introduce bias by over-representing patients with longer records and underrepresenting those with shorter or sparse data, leading to skewed optimization.  
- [Finding 2] Patient Sampling enables dynamic weighting of patient trajectories during pretraining, allowing for balanced sampling across different patient lengths and clinical contexts.  
- [Finding 3] Stochastic Patient Sampling with controllable weighting significantly improves performance on real-world EHR datasets compared to the Global Stream baseline.

## Methodology  
The authors address the imbalance in training signal distribution by introducing a patient-aware sampling mechanism that treats each patient’s record as an independent entity rather than part of a single continuous stream. Instead of concatenating all records into one long token sequence and sampling windows globally, Patient Sampling constructs sequences per patient or small groups, then samples them with adjustable probabilities based on factors like record length, clinical relevance, or temporal spread. This method allows researchers to control the frequency and balance of patient inclusion in training batches. The approach is implemented as a preprocessing step that generates training sequences with explicit patient-level metadata, enabling adaptive sampling strategies during model pretraining.

## Results  
The authors evaluate Patient Sampling across two major EHR datasets: MIMIC-IV v2.2 and v3.1, using standard clinical prediction tasks such as sepsis detection and readmission risk modeling. They compare Patient Sampling against the Global Stream method under identical experimental conditions. Results show that Patient Sampling consistently improves macro AUROC and AUPRC scores by 0.05 to 0.12 points over the baseline, with improvements most pronounced in v3.1 where data diversity is higher. These gains are attributed to more representative training signals that reduce patient-level bias and improve generalization.

## Significance  
This work highlights a fundamental flaw in current EHR foundation model pretraining: the assumption of uniform representation across patients. By introducing Patient Sampling, the authors demonstrate that sequence construction is not just a technical detail but a clinical design decision with measurable impact on model performance. Their findings suggest that future research must consider patient-level dynamics when building generative models for healthcare data.

## Related Concepts  
- Autoregressive foundation models  
- Electronic health records (EHRs)  
- Patient trajectories  
- Sequence construction in NLP  
- Global stream vs. patient-aware sampling  
- Macro AUROC and AUPRC metrics  
- MIMIC-IV dataset  
- Pretraining bias mitigation
