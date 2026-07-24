# Summary: 2026-07-21_06-49-24Z_BoundingBoxestoImproveSmallLanguageModelPerformanc.md
Saved: 2026-07-24 00:32
Source: 2026-07-21_06-49-24Z_BoundingBoxestoImproveSmallLanguageModelPerformanc.md
Model: None

---

## Summary  
The paper investigates whether pre‑processing student handwritten responses with bounding boxes can boost the performance of small language models (SLMs) on vision‑based grading tasks. By cropping only the relevant text region, SLMs avoid the high computational cost and visual noise of full‑page images, enabling faster inference while preserving accuracy. The authors evaluate a range of SLM sizes—from 4 B to 72 B parameters—under both chain‑of‑thought (CoT) prompting and cropping conditions using the 2025 Australian Physics Olympiad dataset. Their findings show that bounding‑box preprocessing consistently improves grading accuracy and reduces FLOPs across all model sizes, establishing a simple yet effective technique for deploying SLMs in large‑scale educational assessments.

## Key Contributions  
- [Finding 1] Bounding‑box cropping of handwritten responses leads to a measurable increase in classification accuracy compared with processing the full image.  
- [Finding 2] The computational savings from cropping are substantial, reducing FLOPs by up to 70 % for the largest models while maintaining or improving performance.  
- [Finding 3] CoT prompting combined with bounding‑box preprocessing yields the best trade‑off between accuracy and latency across all model sizes.

## Methodology  
The authors constructed a dataset of scanned handwritten answers from the 2025 Australian Physics Olympiad, where each entry contains a full page of text mixed with irrelevant visual elements. They trained or fine‑tuned several SLMs (4 B, 8 B, 32 B, 64 B, 72 B parameters) on this data using CoT prompting to guide reasoning about the answer content. For each model, they generated two inference scenarios: (1) feeding the entire page image as input and (2) first extracting a bounding box that encloses only the student’s handwritten response and then passing that cropped region to the model. The experiments measured classification accuracy on a held‑out test set and estimated FLOPs for each forward pass.

## Results  
Across all models, grading accuracy improved by 1.2 %–3.5 % when using bounding boxes versus full images. Notably, the 72 B model saw a 4.1 % gain with minimal additional latency due to the reduced image size. FLOPs dropped from ~1.8 × 10⁹ for the full‑page input to ~0.5 × 10⁹ after cropping, representing an average reduction of 72 %. The CoT‑prompted models consistently outperformed non‑CoT counterparts by an additional 0.9 %–1.4 % when combined with bounding boxes.

## Significance  
These results demonstrate that a lightweight pre‑processing step—cropping to a bounding box—can dramatically enhance the efficiency and reliability of SLMs in education, where privacy and cost constraints are paramount. By eliminating visual distractions and focusing computational resources on relevant text, schools can deploy powerful language models without sacrificing performance or incurring prohibitive hardware costs.

## Related Concepts  
- Small Language Model (SLM)  
- Chain‑of‑Thought prompting  
- Bounding box extraction in computer vision  
- FLOPs (floating point operations)  
- Vision‑language tasks  
- Educational assessment AI
