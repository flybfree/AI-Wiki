# Summary: 2026-08-03_03-54-22Z_FAUatImageCLEF2026TaskonMultimodalReasoningRobustC.md
Saved: 2026-08-03 23:35
Source: 2026-08-03_03-54-22Z_FAUatImageCLEF2026TaskonMultimodalReasoningRobustC.md
Model: None

---

## Summary  
The paper presents a multimodal reasoning system for the ImageCLEF 2026 Visual Multiple Choice Question Answering (Visual MCQ) and Visual Open Question Answering (Visual OpenQA) subtasks, which require reliable multilingual visual answering over dense text, diagrams, charts, tables, formulas, and units. It replaces fragile free‑form generation with direct candidate label scoring derived from vision‑language model logits to enforce strict answer formats. The approach emphasizes inference engineering—score fusion, voting, deterministic decoding, and post‑processing—as the key to robust performance. Without task‑specific training, the official submissions achieved top placements in both tasks.

## Key Contributions  
- [Finding 1] Direct candidate label scoring from vision‑language model logits provides reliable, repeatable answers for Visual MCQ.  
- [Finding 2] Score fusion and voting across multiple runs improves accuracy while preserving answer format constraints.  
- [Finding 3] Deterministic decoding with targeted post‑processing yields concise multilingual visual answers free of reasoning traces and formatting artifacts.

## Methodology  
The authors adopt a vision‑language model (e.g., CLIP or ViLT) to generate logits for each candidate label in Visual MCQ, then apply score fusion and voting to select the best answer. For Visual OpenQA they enhance images, use concise prompting that explicitly requests a short multilingual answer, enforce deterministic decoding, and perform targeted post‑processing to strip any residual reasoning traces or formatting artifacts.

## Results  
Official submissions achieved third place in Visual MCQ with 0.7108 accuracy and first place in Visual OpenQA with COMET 0.6488, BLEU 0.1391, ROUGE L 0.2762, and METEOR 0.2383.

## Significance  
This work demonstrates that inference engineering—careful scoring, ensembling, prompting, and cleanup—can elevate strong vision‑language models to competition‑level performance without retraining the model, highlighting the practical value of post‑processing in multimodal reasoning tasks.

## Related Concepts  
- Vision‑language models  
- Logit‑based candidate scoring  
- Score fusion  
- Deterministic decoding  
- Post‑processing  
- Multilingual visual answering  
- VQA competitions  
- Inference engineering
