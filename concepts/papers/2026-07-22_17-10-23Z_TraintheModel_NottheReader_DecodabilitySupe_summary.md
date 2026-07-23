# Summary: 2026-07-22_17-10-23Z_TraintheModel_NottheReader_DecodabilitySupervision.md
Saved: 2026-07-23 00:02
Source: 2026-07-22_17-10-23Z_TraintheModel_NottheReader_DecodabilitySupervision.md
Model: None

---

## Summary  
The paper addresses the problem that standard reconstruction‑based evaluation of model explanations can be gamed because false claims may not affect reconstruction, leading to misleading scores. It introduces decodability supervision—training auxiliary heads to keep designated internal content independently verifiable—so that explanations are evaluated by an external probe rather than by the model itself.  

## Key Contributions  
- The authors demonstrate that reconstruction scores do not reliably reflect factual correctness because up to 2 % of claims can be reconstruction‑dependent without changing output, thus the test is structurally insensitive.  
- They propose two audit protocols (grounded‑vs‑true cross and evaluator swap) combined with RECAP, a linear auxiliary predictor trained alongside the model that enforces decodability of specific content at only +0.001 nat reconstruction loss.  
- Their experiments show that RECAP‑trained models produce verbalizers whose claims are reliably detectable by an independent probe (AUC = 0.96 vs 0.82 without RECAP), while adversarial explanation editing can suppress ~87 % of lie penalties but still leaves the RECAP probe at AUC ≈ 0.95, whereas a control probe collapses to 0.51.  

## Methodology  
The authors adopt a two‑stage approach: first, they analyze existing verification pipelines to expose structural insensitivity; second, they train lightweight linear heads (RECAP) on top of the target model that predict the likelihood of correctly reproducing designated content when an external probe reads it, minimizing reconstruction loss. The audit protocols involve swapping explanations between models or replacing verbalizers to test whether claims are truly grounded.  

## Results  
On Qwen‑2.5‑7B and Pythia‑160M, RECAP‑trained sandbox models achieve 44–46 % probe‑level truthfulness for designated content versus near‑zero in untrained controls (p ≈ 0.03). The auxiliary heads incur only a +0.001 nat reconstruction penalty and eliminate false coding. Probe‑based evaluation yields AUC = 0.96 on true claims vs 0.82 on false ones, while adversarial explanation editing can suppress ~87 % of lie penalties but still leaves the RECAP probe at AUC ≈ 0.95, whereas a control probe collapses to 0.51.  

## Significance  
This work shifts verification from model‑internal reconstruction to external decodability, providing a reliable audit trail for AI safety: internal claims become independently verifiable without compromising the model’s performance, enabling trustworthy deployment and detection of deceptive explanations.  

## Related Concepts  
- Reconstruction score  
- Decodability supervision  
- Auxiliary predictor (RECAP)  
- Probe‑based verification  
- Adversarial explanation gaming
