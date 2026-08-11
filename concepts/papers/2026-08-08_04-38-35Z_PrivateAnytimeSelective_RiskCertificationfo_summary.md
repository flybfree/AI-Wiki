# Summary: 2026-08-08_04-38-35Z_PrivateAnytimeSelective_RiskCertificationforFedera.md
Saved: 2026-08-10 22:49
Source: 2026-08-08_04-38-35Z_PrivateAnytimeSelective_RiskCertificationforFedera.md
Model: None

---

## Summary  
The paper introduces Fed‑SRC, a private, federated, anytime selective‑risk certificate for retrieval‑augmented generation (RAG). It enables clients to release only score and loss histograms while guaranteeing that accepted outputs stay within a declared error target across any round. The contribution lies in the combined privacy‑risk certification rather than separate contrast or acceptance statistics.  

## Key Contributions  
- [Finding 1] Fed‑SRC provides a private, federated anytime certificate that bounds both risk contrast and accepted mass using martingale inequalities.  
- [Finding 2] A range‑one total‑variation term translates the calibration mixture into a declared deployment mixture, allowing flexible threshold selection without per‑client calibration.  
- [Finding 3] Empirically, Fed‑SRC never violates its privacy‑risk bounds across all cells and thresholds, whereas naive privatized certificates fail in many trials.  

## Methodology  
The authors model each client’s score and loss as a Gaussian‑perturbed martingale over rounds. They construct record‑indexed and noise‑variance‑indexed martingales that jointly track the target risk contrast and the mass of accepted outputs. By applying optional stopping and a total‑variation term, they derive certificates that are valid for any threshold and round, enabling adaptive recruitment and dropout policies.  

## Results  
Theoretical analysis shows that Fed‑SRC’s privacy guarantee holds under all evaluated privacy levels. In experiments on RAGTruth and HaluEval, the primary target r*=0.10 never certifies an output, while the secondary target r*=0.20 also fails on RAGTruth but succeeds on HaluEval where held‑out risk stays below 0.20. Naively privatized certificates violate their bounds in 146–198 of 200 trials. The private betting‑capital heuristic, which stops at ε≤4, still allows certification, though it uses about 30 times more stream events than unique calibration items.  

## Significance  
By decoupling privacy and risk guarantees into a single anytime certificate, Fed‑SRC enables scalable federated deployment of RAG systems without sacrificing either guarantee. It supports trustworthy model rollout by allowing clients to withdraw only lightweight histograms, reducing communication overhead while preserving statistical integrity.  

## Related Concepts  
- Selective‑risk certificates  
- Federated learning  
- Differential privacy  
- Martingale concentration bounds  
- Total variation term  
- RAG (Retrieval‑Augmented Generation)
