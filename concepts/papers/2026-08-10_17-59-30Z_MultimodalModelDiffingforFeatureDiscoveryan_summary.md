# Summary: 2026-08-10_17-59-30Z_MultimodalModelDiffingforFeatureDiscoveryandContro.md
Saved: 2026-08-11 00:03
Source: 2026-08-10_17-59-30Z_MultimodalModelDiffingforFeatureDiscoveryandContro.md
Model: None

---

## Summary  
Multimodal Large Language Models (MLLMs) combine strong visual understanding with language capabilities, but the internal features that drive these behaviors are hard to identify, audit, or control. This work introduces MMDiff, a multimodal model‑diffing framework that leverages sparse autoencoders as interpretable feature interfaces for discovering, detecting, and steering such features. By diffing a base‑language SAE against its multimodal‑adapted counterpart, the authors isolate features altered by multimodal training, perform per‑token contrastive firing analysis to pinpoint causal factors, and apply feature removal or steering in generation. Experiments on three MLLM families show that these sparse, task‑specific features can degrade performance predictably while improving safety.

## Key Contributions  
- [Finding 1] The MMDiff framework isolates multimodal training‑induced features through SAE diffing between a base language model and its multimodal‑adapted version.  
- [Finding 2] Per‑token contrastive firing analysis reveals causal feature directions that are specific to particular tasks such as visual‑spatial understanding or OCR.  
- [Finding 3] Feature‑level control—either removing or steering the discovered directions—improves target task accuracy without harming unrelated capabilities like VQA.

## Methodology  
The authors train multimodal sparse autoencoders (SAEs) on three MLLM families: LLaVA‑MORE, PaliGemma 2, and InternVL3.5. For each model they compute the difference between the SAE’s representation of a base language‑only prompt and its multimodal‑augmented prompt, yielding a set of feature directions that encode what changed due to visual input. To identify which features are causally responsible for specific behaviors, they conduct per‑token contrastive analysis: tokens that share similar visual context produce correlated activations, indicating shared feature usage. Finally, they apply these feature directions in generation by either zeroing them out (removal) or adjusting their weights (steering), measuring the impact on downstream tasks.

## Results  
On average, removing a discovered feature reduces spatial‑understanding accuracy by 12% and OCR performance by 17%, while steering it improves these metrics by +3.6% and +1.8% respectively compared with a single‑layer baseline. The same approach cuts the success rate of multimodal safety attacks by 24% without affecting VQA scores, demonstrating that the features are task‑specific and not globally detrimental.

## Significance  
MMDiff provides the first systematic method for auditing multimodal behavior in large language models, turning hidden feature directions into actionable controls. This bridges interpretability with utility: researchers can both understand why an MLLM behaves a certain way and deliberately steer it toward safer or more capable outputs, paving the way for responsible deployment of vision‑language systems.

## Related Concepts  
- Multimodal Large Language Models (MLLMs)  
- Sparse Autoencoders (SAEs)  
- Feature diffusion / model diffing  
- Contrastive firing analysis  
- Causal feature steering  
- VQA evaluation
