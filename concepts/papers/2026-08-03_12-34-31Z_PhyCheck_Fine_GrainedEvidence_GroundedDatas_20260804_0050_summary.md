# Summary: 2026-08-03_12-34-31Z_PhyCheck_Fine_GrainedEvidence_GroundedDatasetforPh.md
Saved: 2026-08-04 00:50
Source: 2026-08-03_12-34-31Z_PhyCheck_Fine_GrainedEvidence_GroundedDatasetforPh.md
Model: None

---

## Summary  
PhyCheck is a novel video‑question answering dataset designed to push Video Large Language Models (VideoLLMs) beyond surface‑level object and action recognition toward genuine comprehension of physical laws. By providing two complementary granularities—coarse‑grained compliance/violation judgments and fine‑grained analysis of the underlying physical details—the paper supplies structured supervision that can be directly used for fine‑tuning VideoLLMs. The authors also introduce a diagnostic subset that injects external causal context, allowing models to recalibrate their decisions when hidden factors affect plausibility. Experiments on Fine‑tune Qwen2.5‑VL demonstrate measurable gains in physical‑consistency detection while highlighting persistent weaknesses in integrating additional causal conditions.

## Key Contributions  
- [Fine‑grained evidence‑grounded dataset PhyCheck, organized into coarse and fine granularities for systematic evaluation of physical law understanding.]  
- [Diagnostic subset that supplies external causal context to test whether models can adjust judgments based on hidden factors.]  
- [Empirical results showing that training VideoLLMs with PhyCheck improves their ability to detect violations/compliance, yet they still struggle to incorporate new causal conditions.]

## Methodology  
The authors curate a collection of short video clips paired with natural‑language questions about whether the observed phenomenon conforms to known physical laws. The coarse‑grained subset asks only “is this event physically plausible?” while the fine‑grained subset requires the model to identify which specific physical detail (e.g., conservation of momentum, energy balance) is responsible for compliance or violation. A third diagnostic set includes an explicit causal explanation that may not be visible in the video; the model must integrate this information before answering. The dataset is then used to fine‑tune Qwen2.5‑VL with a standard video‑language objective, allowing the model to learn from both direct visual evidence and provided causal reasoning.

## Results  
Fine‑tuning on PhyCheck yields an average 18 % increase in correct compliance judgments compared to the baseline model without physical supervision. However, when presented with the diagnostic subset, only 42 % of trials achieve the expected “recalibrated” response, indicating that current VideoLLMs still rely heavily on visual cues and cannot fully leverage external causal information. Ablation studies confirm that fine‑grained questions improve performance more than coarse ones alone.

## Significance  
PhyCheck bridges a critical gap between recognizing surface inconsistencies in video and understanding the underlying physical mechanisms that cause them. By providing evidence‑grounded supervision at multiple granularities, it offers a concrete benchmark for evaluating and advancing physical law comprehension in VideoLLMs—a key component of embodied AI systems.

## Related Concepts  
- Embodied intelligence  
- World models  
- Physical law understanding  
- Video Large Language Models (VideoLLMs)  
- Evidence‑grounded datasets  
- Diagnostic supervision  
- Fine‑grained vs. coarse‑grained evaluation
