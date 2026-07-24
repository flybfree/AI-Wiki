# Summary: 2026-07-21_04-35-47Z_DecoupledPipelinewithProposalRerankingandScoreFusi.md
Saved: 2026-07-24 00:47
Source: 2026-07-21_04-35-47Z_DecoupledPipelinewithProposalRerankingandScoreFusi.md
Model: None

---

## Summary  
The paper introduces DS@GT ARC, a decoupled pipeline tailored for the positive‑unlabeled marine species detection challenge of FathomNetCLEF 2026, where training labels are sparse and test images lie outside the distribution of the provided data. By keeping model training confined to the competition dataset, the authors fuse a frozen Megalodon YOLOv8x detector with a LoRA‑fine‑tuned DINOv3 ViT‑H classifier, applying proposal reranking through tile‑edge filtering and weighted geometric fusion to produce final predictions. The system achieved 12th place on the private leaderboard, outperforming several prior approaches that relied heavily on noisy pseudo‑labels or aggressive detector fine‑tuning.

## Key Contributions  
- [Introduces a decoupled pipeline that separates proposal generation from classification and ranking.]  
- [Uses a frozen Megalodon YOLOv8x detector with tile‑edge filtering to boost recall while limiting false positives.]  
- [Combines global and tiled inference, applying LoRA‑fine‑tuned DINOv3 ViT‑H classifier for classification and weighted geometric fusion for final ranking.]

## Methodology  
The authors adopt a modular workflow: first, they generate class‑agnostic proposals from the frozen detector using a two‑stage inference that includes global and tiled passes followed by edge filtering to preserve high‑quality crops. Expanded proposal regions are then classified with a vision transformer whose parameters are updated only through low‑rank adaptation (LoRA), preserving the original model’s knowledge. The classifier output is merged with the detector confidence via geometric fusion, producing a ranked set of predictions. Validation relies exclusively on proxy datasets and leaderboard feedback rather than train‑derived metrics, because those signals proved unreliable for model selection.

## Results  
The baseline DS@GT ARC system placed 12th out of 102 competing teams in the private leaderboard. A variant that added a locally trained TTN‑inspired validity head improved public and proxy evaluation scores but marginally reduced private‑leaderboard performance, indicating a trade‑off between robustness and recall. Across experiments, the authors observed that maximizing proposal recall, avoiding overly aggressive filtering, and enhancing downstream ranking yielded larger gains than fine‑tuning the detector or training on noisy pseudo‑labels.

## Significance  
This work demonstrates that in settings with scarce, out‑of‑distribution labels, a pipeline that isolates reliable components—such as a well‑filtered proposal generator and a lightweight classification head—can achieve superior results compared to end‑to‑end training. It also underscores the value of using proxy validation data and leaderboard feedback for model selection when true validation is unavailable.

## Related Concepts  
positive‑unlabeled dataset, proposal‑based detection, LoRA fine‑tuning, DINOv3 ViT, geometric fusion ranking, tile‑edge filtering, positive‑negative classifier, score fusion, private vs public leaderboards.
