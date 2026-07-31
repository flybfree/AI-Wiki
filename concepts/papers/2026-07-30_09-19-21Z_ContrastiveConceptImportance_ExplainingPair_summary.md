# Summary: 2026-07-30_09-19-21Z_ContrastiveConceptImportance_ExplainingPairwiseCla.md
Saved: 2026-07-30 21:42
Source: 2026-07-30_09-19-21Z_ContrastiveConceptImportance_ExplainingPairwiseCla.md
Model: None

---

## Summary  
The paper introduces contrastive concept importance (CCI) to explain why a model chooses one class over another by attributing logit margins to automatically extracted visual concepts, moving beyond single‑class feature attribution. It provides signed scores that decompose into target‑logit and foil‑logit effects, enabling analysis of class‑pair distinctions such as misclassifications and low‑margin predictions. The method leverages CRAFT‑style concept bases and visual concept representations to quantify how strongly each concept supports the target versus its contrast.

## Key Contributions  
- Contrastive concept importance (CCI) attributes logit margins between a target class and a foil class to automatically extracted visual concepts, providing signed scores that decompose into target‑logit and foil‑logit effects.  
- CCI reveals class‑pair specific model behavior that ordinary concept importance cannot capture, especially in misclassifications or low‑margin predictions.  
- Highly contrastive concepts can be evaluated against semantic superclass hierarchy to distinguish fine‑grained distinctions from broad category evidence.

## Methodology  
The authors built a visual concept basis using CRAFT (Contrastive Receptive Feature Transform) on ImageNet images, producing interpretable binary concepts for each pixel. For every class pair, they compute the logit margin of the model’s output and assign each concept a score proportional to its contribution to that margin, yielding target‑logit and foil‑logit components. The scores are signed, indicating support direction, and can be decomposed analytically.

## Results  
Experiments on ImageNet class pairs show that CCI uncovers concepts whose importance is driven by the contrast between specific classes rather than global category evidence. Insertion/deletion curves illustrate how adding or removing a concept shifts the margin, confirming its role in class‑pair decisions. Decomposition analysis reveals one‑sided and shared effects, and semantic superclass evaluation confirms that fine‑grained concepts affect narrow distinctions.

## Significance  
This work bridges feature attribution with contrastive reasoning, offering interpretable explanations for model uncertainties and low‑margin predictions. By linking concept importance to logit margins, CCI enables more nuanced diagnostics of misclassifications and improves trust in black‑box systems.

## Related Concepts  
- Contrastive Concept Importance (CCI)  
- Logit margin attribution  
- Visual concept basis (CRAFT)  
- Feature attribution decomposition  
- Semantic superclass hierarchy
