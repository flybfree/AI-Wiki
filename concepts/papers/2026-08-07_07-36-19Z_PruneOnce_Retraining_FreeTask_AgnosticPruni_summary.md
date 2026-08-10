# Summary: 2026-08-07_07-36-19Z_PruneOnce_Retraining_FreeTask_AgnosticPruningforVi.md
Saved: 2026-08-09 22:46
Source: 2026-08-07_07-36-19Z_PruneOnce_Retraining_FreeTask_AgnosticPruningforVi.md
Model: None

---

## Summary  
Vision‑language models (VLMs) have become powerful multimodal agents but their large size and memory footprint limit deployment in resource‑constrained settings. Existing pruning approaches are either task‑specific or rely on LLM‑centric importance scores, which cannot be reused across tasks without retraining. This paper proposes PORTA, a retraining‑free, task‑agnostic pruning framework that learns a modality‑agnostic importance measure from generic calibration data and allocates sparsity adaptively to preserve representation utility. The method enables high‑level compression of VLMs such as CLIP, BLIP, and Qwen2‑VL without any downstream fine‑tuning.

## Key Contributions  
- **Task‑agnostic importance formulation:** PORTA derives a feature‑level importance score based on activation variation across modalities using only calibration data, eliminating the need for task‑specific samples.  
- **Adaptive sparsity allocation:** The framework computes layer‑wise pruning ratios from output feature variability, avoiding uniform sparsity and mitigating performance loss at high compression levels.  
- **Retraining‑free VLM pruning:** PORTA achieves competitive downstream performance under substantial sparsity without any retraining or task‑specific tuning.

## Methodology  
PORTA first collects a small set of generic images and captions to compute activation statistics for each layer in the VLM’s encoder. The importance of each output feature is estimated as the variance of its activations across modalities, which reflects how much that feature contributes to discriminative representation. These scores are then normalized per layer, and an adaptive sparsity allocation step selects a pruning ratio inversely proportional to the average feature variability, ensuring critical features remain intact while less variable ones can be removed. The resulting sparse weights are directly applied to the model’s forward pass.

## Results  
Experiments on CLIP, BLIP, and Qwen2‑VL show that PORTA retains >90 % of original classification accuracy when compressed to 30–70 % sparsity, with only modest degradation in zero‑shot VQA tasks. Ablation studies confirm that the activation‑variance importance measure is more robust than uniform or LLM‑based measures, and the adaptive allocation reduces performance loss compared to fixed pruning ratios. The codebase supports easy integration into existing VLM pipelines.

## Significance  
By decoupling pruning from downstream tasks, PORTA offers a scalable path to deployable multimodal models that fit on edge devices while preserving strong generalization. This work advances the field of model compression for VLMs and provides a template for task‑agnostic optimization in large language‑vision systems.

## Related Concepts  
- Vision‑Language Models (VLMs)  
- Model pruning / sparsification  
- Task‑agnostic learning  
- Activation variance importance  
- Adaptive sparsity allocation  
- Retraining‑free fine‑tuning
