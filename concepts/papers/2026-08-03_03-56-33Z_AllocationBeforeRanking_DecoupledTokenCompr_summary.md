# Summary: 2026-08-03_03-56-33Z_AllocationBeforeRanking_DecoupledTokenCompressionf.md
Saved: 2026-08-03 23:36
Source: 2026-08-03_03-56-33Z_AllocationBeforeRanking_DecoupledTokenCompressionf.md
Model: None

---

## Summary  
The paper critiques the conventional token‑compression approach in OmniLLMs, which treats compression as a single saliency‑ranking problem that inherently favors audio tokens over video ones. It introduces **Macer**, a training‑free compressor that separates allocation from ranking to give each modality its own capacity budget. By assigning explicit audio and video budgets and performing allocation‑normalized ranking within shallow layers of the model, Macer reduces token cost while preserving accuracy across multimodal tasks. The method achieves high performance at low retention rates without requiring any fine‑tuning.

## Key Contributions  
- [Finding 1] The single top‑K rule is mis‑specified because it inherits an audio‑favoring allocation bias that disadvantages video tokens.  
- [Finding 2] Explicit audio and video budgets decouple capacity assignment from ranking, enabling fair competition within each modality’s shallow layers.  
- [Finding 3] Allocation‑before‑ranking improves compression efficiency without sacrificing accuracy across diverse benchmarks.

## Methodology  
The authors first compute separate budgets for audio and video tokens based on their typical contribution to model performance. These budgets are then used to allocate capacity at shallow layers of the model, where each modality’s token set is ranked independently using a normalized ranking function that respects the allocated budget. This decoupling allows the compression process to be applied without retraining the model.

## Results  
At 25 % token retention, Macer retains 98.7 % of full‑token performance on Qwen2.5‑Omni‑7B and 97.3 % on Qwen2.5‑Omni‑3B. It reaches OmniZip‑level performance at only 45 % retention while using fewer FLOPs than the original method. On OmniVinci‑9B, allocation‑before‑ranking outperforms shared top‑K ranking by up to 12.9 points.

## Significance  
This work demonstrates that separating allocation from ranking can mitigate modality bias in token compression, leading to more efficient and equitable models. The results show tangible gains in both performance preservation and computational savings, encouraging broader adoption of allocation‑aware compression techniques.

## Related Concepts  
- Token compression  
- Saliency ranking  
- Modality budgeting  
- Allocation‑before‑ranking  
- OmniLLMs  
- FLOPs efficiency
