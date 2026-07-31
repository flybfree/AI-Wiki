# Summary: 2026-07-30_17-05-20Z_ScaFE_Data_EfficientScarClassificationwithLLM_Gene.md
Saved: 2026-07-30 22:22
Source: 2026-07-30_17-05-20Z_ScaFE_Data_EfficientScarClassificationwithLLM_Gene.md
Model: None

---

## Summary  
This paper addresses the challenge of classifying pathological scars from clinical photographs when expert‑labeled data is scarce and acquisition varies across hospitals. Instead of relying on end‑to‑end image models or sending images to a vision‑language model, they propose ScaFE, which converts LLM knowledge into deterministic feature programs that run locally. These programs generate visual attributes, are executed in a restricted environment, and only produce aggregated validation statistics and SHAP summaries for auditability. A lightweight Random Forest then classifies on the structured representation.

## Key Contributions  
- Finding 1: ScaFE achieves 81.0% site‑macro balanced accuracy on a leave‑one‑site‑out evaluation, surpassing BiomedCLIP by 10 percentage points.  
- Finding 2: With only 10% of development data, ScaFE retains 72.0% balanced accuracy and maintains an 11.8‑point lead, demonstrating strong data efficiency.  
- Finding 3: Iterative refinement raises the executable‑program rate from 66.7% to 95.0%, with verified evidence for 91.7% of final features.

## Methodology  
The authors first query a web‑enabled LLM for clinical evidence, synthesize feature programs that quantify scar attributes such as size, shape, and texture, then execute these programs locally using a sandboxed environment. The output is a structured representation containing only summary statistics and SHAP values; raw images and patient data remain local. A Random Forest classifier processes this representation to produce final predictions.

## Results  
On 600 photographs from three hospitals evaluated with leave‑one‑site‑out, ScaFE reaches 81.0% site‑macro balanced accuracy, the highest among baselines. The model’s performance remains robust when trained on only ten percent of the development set, achieving 72.0% balanced accuracy and an 11.8‑point advantage over the best baseline. Iterative refinement further improves feature reliability, increasing executable‑program usage to 95.0% while confirming evidence for 91.7% of features.

## Significance  
This work shows that large language models can augment medical image analysis without violating data governance policies, offering a reproducible and auditable alternative to direct VLM inference. By converting knowledge into local feature programs, ScaFE enables clinicians and researchers to trust the output with explainability and compliance, while still achieving state‑of‑the‑art classification performance.

## Related Concepts  
- Large language model (LLM)  
- Vision‑language model (VLM)  
- Feature engineering  
- SHAP summary values  
- Random Forest classifier  
- Leave‑one‑site‑out evaluation  
- Data‑efficient learning
