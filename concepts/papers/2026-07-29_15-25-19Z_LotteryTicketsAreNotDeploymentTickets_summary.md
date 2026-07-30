# Summary: 2026-07-29_15-25-19Z_LotteryTicketsAreNotDeploymentTickets.md
Saved: 2026-07-29 22:28
Source: 2026-07-29_15-25-19Z_LotteryTicketsAreNotDeploymentTickets.md
Model: None

---

## Summary  
The authors investigate the practical feasibility of replacing a dense reference model with an accuracy‑matched lottery ticket (LT) or another sparse challenger in real deployment settings without altering downstream decision logic. Their contribution is to define and measure “behavioral‑compatibility distance” across several production‑relevant behaviors—calibration, out‑of‑distribution (OOD) response, class‑level reliability, learned representations, and final policy decisions—to determine whether such a drop‑in replacement truly preserves the incumbent’s behavior. By auditing a protocol‑specific panel of these metrics, they show that sparse candidates can achieve clean accuracy yet still cause measurable churn in acceptance‑review outcomes.

## Key Contributions  
- [Finding 1] Sparse lottery tickets recover dense‑reference top‑1 accuracy but remain behaviorally distinct; in several study‑band‑matched settings they produce a 7 %–10 % churn of accept‑review decisions.  
- [Finding 2] In band‑matched regimes, LTs exhibit lower corruption accuracy than the dense reference model.  
- [Finding 3] Clean‑accuracy certification does not guarantee deployment compatibility; small confidence shifts near the operating boundary can generate first‑order routing churn.

## Methodology  
The authors construct a comprehensive panel of deployment‑relevant behaviors and summarize deviations from the incumbent using a “behavioral‑compatibility distance.” They conduct extensive experiments across multiple study bands, comparing dense reference models with accuracy‑matched lottery tickets (sparsified or compressed). The evaluation focuses on how each behavior changes when the model is swapped out while keeping downstream decision logic fixed.

## Results  
Across the panel, sparse candidates achieve clean‑accuracy parity with the dense reference but exhibit systematic deviations: calibration drifts, OOD misclassifications, and class‑level reliability drops are observed. The most striking finding is a 7 %–10 % increase in accept‑review decisions that were previously rejected by the dense model, indicating churn in downstream policy actions. Additionally, corruption accuracy is reduced for LTs in band‑matched settings, suggesting they handle ambiguous inputs less robustly.

## Significance  
These results establish the limits of clean‑accuracy certification: achieving pointwise top‑1 agreement does not ensure compatibility with a fixed incumbent when decision thresholds are immutable. The churn observed—especially the 7 %–10 % shift in accept‑review outcomes—highlights the practical burden of drop‑in replacement, which is precisely what deployment pipelines aim to avoid. By exposing how small confidence fluctuations near the operating boundary can trigger routing changes, the work informs theory on fixed‑threshold policy behavior and underscores that sparsity effects must be evaluated against real‑world decision logic.

## Related Concepts  
- Sparsification, compression, lottery tickets (LTs)  
- Deployment, drop‑in replacement, behavioral compatibility  
- Calibration, out‑of‑distribution response, class‑level reliability  
- Learned representations, downstream policy decisions  
- Corruption accuracy, clean‑accuracy certification, routing churn  
- Fixed‑threshold policies, small confidence shifts, operating boundary
