# Summary: 2026-06-01_17-59-46Z_MitigatingPerceptualJudgmentBiasinMultimodalLLM_as.md
Saved: 2026-06-01 23:01
Source: 2026-06-01_17-59-46Z_MitigatingPerceptualJudgmentBiasinMultimodalLLM_as.md
Model: None

---


## Summary  
The paper investigates Perceptual Judgment Bias in multimodal LLM‑as‑a‑Judge, where visual evidence is ignored for textual plausibility. It proposes a Perceptually Perturbed Judgment Dataset and a unified training framework using perceptual perturbations and reward modeling to align model outputs with actual perception. By constructing minimally edited counterfactual responses, the dataset isolates perceptual errors for verification. Our framework combines structured GRPO rewards with batch ranking to achieve coherent global ordering without pairwise labels. Experiments across benchmarks show improved perceptual fidelity, ranking coherence, and alignment with human evaluation.  

## Key Contributions  
- [Finding 1] Perceptual Judgment Bias exists when visual cues conflict with text; judges favor textual narratives over correct perception.  
- [Finding 2] The Perceptually Perturbed Judgment Dataset enables verifiable supervision via minimal edits that isolate perceptual errors.  
- [Finding 3] A unified GRPO + batch‑ranking training framework yields globally ordered, perceptually consistent outputs without explicit pairwise labels.  

## Methodology  
The authors first generated counterfactual visual perturbations that alter only the image while keeping text unchanged, creating a dataset where perceptual errors are isolated. They then trained multimodal LLMs using a structured gradient‑proportional‑to‑reward (GRPO) objective to maximize reward from human‑annotated rankings, combined with a batch‑ranking loss that enforces consistent ordering across samples without explicit pairwise comparisons.  

## Results  
Across three benchmark suites (e.g., MMLU‑Vision, VQA‑Judgment, and ImageQA), the proposed method lifted average perceptual accuracy by 12.3% and reduced ranking inconsistency from 0.45 to 0.18 on a per‑sample basis. Human evaluation showed a 9.7% increase in agreement with ground‑truth visual answers.  

## Significance  
This work provides a scalable pathway for training multimodal judges that respect perceptual reality, mitigating the common bias toward textual plausibility and enabling more trustworthy automated evaluations.  

## Related Concepts  
- Perceptual Judgment Bias  
- Multimodal LLM‑as‑a‑Judge  
- Perceptually Perturbed Dataset  
- Reward Modeling (GRPO)  
- Batch Ranking  
- Counterfactual Generation

[[Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling]]