# Summary: 2026-07-27_08-18-05Z_BioSentinelatEXIST2026_Soft_LabelOptimizationwithX.md
Saved: 2026-07-28 00:10
Source: 2026-07-27_08-18-05Z_BioSentinelatEXIST2026_Soft_LabelOptimizationwithX.md
Model: None

---

## Summary  
The BioSentinel team entered EXIST 2026 Task 2.2 (Source Intention in Memes) at CLEF 2026, where the goal is to classify meme intent as direct, judgemental, or non‑sexist using a Learning with Disagreement framework that requires both hard labels and soft‑label probability distributions. Their contribution is a text‑centric model built on xlm‑roberta‑base trained with a composite loss that blends KL divergence for soft‑label consistency and weighted cross‑entropy for hard‑label accuracy, achieving strong performance in the official test set.

## Key Contributions  
- Finding 1: Introducing a composite loss function that jointly optimizes soft‑label (KL) and hard‑label (CE) objectives to handle annotator disagreement.  
- Finding 2: Demonstrating that KL loss improves soft‑label metrics while CE loss boosts hard‑label accuracy, highlighting the complementary roles of each component.  
- Finding 3: Achieving an ICM‑Soft‑Norm of 0.3229 and a hard F1‑score of 0.4236, ranking 40th in soft‑soft evaluation and 49th in hard‑hard evaluation among 187 submissions.

## Methodology  
The authors employed xlm‑roberta‑base (270 M parameters) as the language model backbone for meme text. Training used a composite loss: KL divergence between predicted probability distributions from multiple annotators and weighted cross‑entropy on the ground‑truth labels. The Le‑Wi‑Di paradigm mandates both predictions, so the model outputs a full soft‑label distribution alongside the hard label. A validation set temperature analysis was performed to assess sensitivity to temperature scaling.

## Results  
On the official test set, BioSentinel achieved an ICM‑Soft‑Norm of 0.3229 and an ICM‑Norm of 0.3778. The hard F1‑score reached 0.4236, placing it 40th in soft‑soft evaluation and 49th in hard‑hard evaluation out of 187 submissions. Ablation studies confirmed that removing the KL component degrades soft‑label performance, while eliminating CE loss reduces hard‑label accuracy.

## Significance  
This work advances the handling of subjective NLP tasks by explicitly modeling annotator disagreement through a composite loss, offering a principled way to improve both soft and hard evaluation metrics. It provides a scalable template for future meme classification challenges where human annotators produce conflicting judgments.

## Related Concepts  
- xlm‑roberta‑base: a multilingual transformer model fine‑tuned for text classification.  
- Soft‑label optimization: training to predict probability distributions rather than discrete labels.  
- Learning with Disagreement (Le‑Wi‑Di): a paradigm that uses multiple annotator predictions.  
- KL divergence loss: measures divergence between two probability distributions.  
- Weighted cross‑entropy: combines CE loss with per‑example weights.
