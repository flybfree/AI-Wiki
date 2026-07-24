# Summary: 2026-07-21_04-35-47Z_DecoupledPipelinewithProposalRerankingandScoreFusi.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_04-35-47Z_DecoupledPipelinewithProposalRerankingandScoreFusi.md
Model: None

---

## Summary  
The FathomNetCLEF 2026 competition challenges teams to detect and classify marine species from underwater images under a positive‑unlabeled setting, where training labels are sparse and test data is out‑of‑distribution. DS@GT ARC proposes a decoupled pipeline that separates proposal generation, classification, and ranking while keeping model training confined to the provided competition data. By fusing detector confidence with a LoRA‑fine‑tuned DINOv3 classifier through geometric weighting, the system achieves 12th place on the private leaderboard and improves proxy‑evaluation scores.

## Key Contributions  
- Decoupled pipeline that isolates proposal generation from downstream classification and ranking.  
- Integration of a frozen Megalodon YOLOv8x detector as a class‑agnostic proposal generator combined with a LoRA‑adapted DINOv3 ViT‑H classifier using weighted geometric fusion for confidence scoring.  
- A locally trained TTN‑style validity head that serves as an additional reranking signal, boosting public and proxy performance without retraining the main model.

## Methodology  
The authors restrict training to the competition dataset only, employing a frozen YOLOv8x detector that generates proposals agnostically to species labels. Global and tiled inference with tile‑edge filtering expands each proposal crop for classification by the LoRA‑fine‑tuned DINOv3 classifier. Prediction ranking is performed via geometric fusion of the detector’s confidence and the classifier’s score, while validation relies exclusively on proxy datasets rather than train‑derived metrics to avoid overfitting.

## Results  
The private leaderboard model ranks 12th among 102 teams, outperforming many submissions despite limited labeled data. Adding the locally trained TTN validity head raises public‑leaderboard and proxy scores by roughly 5 % while preserving recall. Ablation studies indicate that maintaining high proposal recall, avoiding overly aggressive filtering, and enhancing downstream ranking are more effective than fine‑tuning the detector or using noisy pseudo‑labels.

## Significance  
This work demonstrates a practical approach to positive‑unlabeled marine species detection where annotation scarcity and source shift dominate performance. By decoupling stages and focusing on reliable proxy metrics, DS@GT ARC offers a scalable framework for similar competition settings beyond marine biology.

## Related Concepts  
positive‑unlabeled learning, proposal‑based object detection, LoRA fine‑tuning, geometric fusion ranking, tile‑edge filtering, TTN validity head, proxy datasets.
