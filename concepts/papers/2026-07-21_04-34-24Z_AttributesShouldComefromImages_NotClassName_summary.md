# Summary: 2026-07-21_04-34-24Z_AttributesShouldComefromImages_NotClassNames_Distr.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_04-34-24Z_AttributesShouldComefromImages_NotClassNames_Distr.md
Model: None

---

## Summary  
The paper argues that interpretable zero‑shot classification descriptors should be derived from image content rather than class names because LLM‑generated labels are label‑conditioned, not image‑conditioned, and therefore degrade when data shifts. It proposes selecting attributes directly from the target image collection via CLIP joint embeddings to create a data‑driven attribute set for prompts. This approach yields higher accuracy (23.8 % vs 15.5 %) on ImageNet and four shifted variants while being fast, interpretable, and requiring no soft prompt. The method also serves as a textual summary of the dataset’s distribution.

## Key Contributions  
- [Finding 1] LLM‑generated descriptors are conditioned on class names rather than images, causing poor zero‑shot performance under distribution shift; removing the label collapses ImageNet accuracy from 59.5 % to 15.5 %.  
- [Finding 2] Selecting attributes from the target image collection via CLIP embeddings improves accuracy significantly across multiple shifted variants and outperforms CoOp by three points when using a single image per class.  
- [Finding 3] The attribute‑selection method is computationally cheap (under one minute), requires no learned soft prompt, and provides a readable summary of the dataset that can be used to describe distribution shift.

## Methodology  
The authors evaluate two strategies: (1) prompting CLIP with LLM‑generated class descriptors and (2) prompting CLIP with attributes selected from the target image set. They score a pool of candidate attribute phrases against CLIP’s joint embedding space, rank them per class, and keep the top‑scoring ones for each class label. The selected attributes are then used to prompt the language model for zero‑shot classification. Performance is measured on ImageNet, four shifted ImageNet variants, and compared to the CoOp baseline that uses a single image per class.

## Results  
Attribute prompts achieve 23.8 % accuracy versus 15.5 % for LLM descriptors, demonstrating a substantial gain. This improvement holds across all four shifted ImageNet datasets. The attribute‑based approach outperforms CoOp by +3 points while requiring only one image per class and completing in under a minute—compared with CoOp’s 14‑hour training time. No soft prompt is learned, preserving interpretability.

## Significance  
This work challenges the assumption that class names are reliable visual descriptors, offering a data‑driven alternative that is both accurate and transparent. By basing attributes on actual image content, the method not only boosts zero‑shot performance but also provides a clear textual summary of dataset distribution, facilitating better communication about shift phenomena.

## Related Concepts  
- Zero‑shot classification  
- CLIP embeddings  
- Distribution shift  
- Attribute selection  
- Interpretability in vision‑language models  
- CoOp (Cooperative) method
