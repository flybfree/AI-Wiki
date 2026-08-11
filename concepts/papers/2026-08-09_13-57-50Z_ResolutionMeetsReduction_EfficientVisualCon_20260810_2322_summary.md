# Summary: 2026-08-09_13-57-50Z_ResolutionMeetsReduction_EfficientVisualContextfor.md
Saved: 2026-08-10 23:22
Source: 2026-08-09_13-57-50Z_ResolutionMeetsReduction_EfficientVisualContextfor.md
Model: None

---

## Summary  
The paper tackles the computational bottleneck of feeding full 3D CT volumes to vision‑language models for radiology report generation by exploring how to balance input resolution, visual token count, and projection compression. It proposes a systematic study of four vision encoders (CNNs and ViTs), five token‑reducing projectors up to 64×, and five instruction‑tuned LLMs on the CT‑RATE and Merlin datasets. The goal is to achieve state‑of‑the‑art clinical macro F1 while keeping the visual context efficient.  

## Key Contributions  
- Anatomy‑guided ROI cropping provides the most consistent improvement, raising macro F1 by +3.7 points on average for the 3D ViT Primus encoder and +1.1 for the slice‑based 2D ViT Curia encoder in 19 of 20 settings.  
- Pairing the PerceiverResampler projector with higher‑resolution Curia features yields the strongest configuration, achieving SOTA clinical macro F1 scores of 49.5 on CT‑RATE and 49.0 on Merlin.  
- Vision‑to‑language projectors can compress visual sequences up to 64× while preserving clinically relevant detail, enabling a fixed token budget across varying input resolutions.  

## Methodology  
The authors systematically evaluate four heterogeneous vision encoders (CNN‑based and ViT‑based) along with five token‑reducing projectors at up to 64× compression plus a non‑reducing MLP projector baseline, and five instruction‑tuned LLMs ranging from 1.7B to 4B parameters. They run experiments on two large CT report datasets—CT‑RATE and Merlin—matching the LLM token budget across all configurations to isolate the impact of visual context design.  

## Results  
The best overall configuration attains state‑of‑the‑art clinical macro F1 scores: 49.5 for CT‑RATE and 49.0 for Merlin, surpassing prior baselines by several points. ROI cropping consistently boosts performance across both encoders, while the PerceiverResampler with high‑resolution features delivers the highest accuracy gains. The study demonstrates that a fixed visual token budget can accommodate higher input resolutions without sacrificing report quality.  

## Significance  
By decoupling resolution and compression decisions, this work enables efficient 3D radiology report generation that is both scalable to larger scans and robust in clinical settings. It reduces the computational load of vision‑language pipelines while maintaining high diagnostic accuracy, paving the way for real‑world deployment where compute resources are limited.  

## Related Concepts  
Vision tokens, visual context, projection compressors (PerceiverResampler), attention token budgets, macro F1 metric, ROI cropping, 3D ViT Primus encoder, slice‑based 2D ViT Curia encoder, CT‑RATE dataset, Merlin dataset.
