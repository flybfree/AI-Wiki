# Summary: 2026-08-10_17-59-30Z_MultimodalModelDiffingforFeatureDiscoveryandContro.md
Saved: 2026-08-11 00:19
Source: 2026-08-10_17-59-30Z_MultimodalModelDiffingforFeatureDiscoveryandContro.md
Model: None

---

## Summary  
Multimodal Large Language Models (MLLMs) achieve strong visual‑spatial understanding, but the specific features that drive these capabilities are opaque and hard to control. The authors introduce **MMDiff**, a framework that leverages multimodal sparse autoencoders (SAEs) to expose, isolate, and steer feature directions that change during multimodal training. By diffing base‑model SAE representations from their multimodal‑adapted counterparts, MMDiff discovers causal features whose removal degrades target tasks such as spatial reasoning and OCR, while steering them improves performance. The work thus bridges interpretability with practical control mechanisms for safer, more capable model generation.

## Key Contributions  
- [Finding 1] **Feature isolation**: Diffing a base‑model SAE against its multimodal‑adapted counterpart reveals sparse feature directions that are altered only by multimodal training.  
- [Finding 2] **Task‑specific detection**: Per‑token contrastive firing analysis isolates those features that causally affect particular downstream tasks (spatial understanding, OCR).  
- [Finding 3] **Feature‑level control**: Removing or steering the identified directions degrades target behaviors by ~12% on spatial tasks and 17% on OCR, while reducing multimodal safety attack success rates by 24%, with no adverse impact on VQA.

## Methodology  
The authors train multimodal SAEs for three MLLM families—LLaVA‑MORE, PaliGemma 2, and InternVL3.5—using contrastive learning to encode visual inputs alongside token embeddings. They then compute the difference between the base‑model latent space and the multimodal‑adapted latent space (the “diff”). This diff is projected onto a low‑dimensional feature basis, yielding interpretable direction vectors. Per‑token analysis measures how strongly each direction fires across tokens, enabling causal attribution to specific visual features. Finally, they evaluate control by either zeroing out or scaling these directions while measuring task performance.

## Results  
Across the three models, MMDiff uncovers a handful of sparse feature directions that are uniquely activated during multimodal training. Their removal reduces spatial‑task accuracy by an average 12% and OCR precision by 17%, while also lowering multimodal safety attack success rates by 24%. Steering these features improves the same metrics by +3.6% (spatial) and +1.8% (OCR) compared to a baseline single‑layer steering approach, with VQA scores unchanged.

## Significance  
MMDiff demonstrates that multimodal SAEs can serve as both diagnostic tools for feature discovery and actuators for behavioral control, offering a pathway toward more transparent and safer MLLMs. By providing causal, task‑specific features, the framework enables researchers to audit model behavior without sacrificing performance, paving the way for responsible AI deployment.

## Related Concepts  
- Multimodal Large Language Models (MLLMs)  
- Sparse Autoencoders (SAEs) and their latent representations  
- Feature diffusion / feature difference analysis  
- Causal attribution via contrastive firing  
- Model steering and control mechanisms
