# Summary: 2026-08-05_11-01-47Z_PersonalizedFederatedSparseAdaptationofTime_Series.md
Saved: 2026-08-05 22:29
Source: 2026-08-05_11-01-47Z_PersonalizedFederatedSparseAdaptationofTime_Series.md
Model: None

---

## Summary  
The paper addresses the challenge of adapting time‑series foundation models (TSFMs) for energy forecasting while respecting privacy and heterogeneity across buildings. It introduces a personalized federated sparse adaptation framework that combines globally pretrained TSFM representations with client‑specific, sparsely activated experts via a heterogeneous temporal MoE adapter. A sequence router selects the most relevant expert subset for each 168‑hour window, enabling fine‑grained personalization without full retraining. The approach balances cross‑building transfer with local adaptation, avoiding the pitfalls of fully shared or fully local strategies.  

## Key Contributions  
- [Finding 1] A heterogeneous temporal MoE adapter that maps a fixed 168‑hour context to a top‑k subset of domain‑specialized experts (periodicity, long‑range interactions, etc.).  
- [Finding 2] A federated routing mechanism that learns client‑aware expert assignments while preserving sparsity and enabling global model sharing.  
- [Finding 3] Empirical evidence that personalized FL consistently outperforms Global FL‑MoE and Local MoE across diverse building backbones.  

## Methodology  
The authors start with three pretrained TSFM backbones, each trained on a large public dataset. In the federated setting, client models receive only their local meter data. The proposed framework inserts a lightweight sequence router after the backbone representation; this router outputs an expert index list for each window. Clients train only the selected experts locally (client‑private) and share the resulting adapter weights via FL, while the global MoE bank remains shared. Training proceeds in rounds where clients compute gradients on their private data, update local experts, and broadcast updates to a central aggregator.  

## Results  
Experiments across 50 buildings using three TSFM backbones show that personalized FL achieves higher accuracy than Global FL‑MoE (≈1.8% absolute gain) and Local MoE (≈2.3% absolute gain). The best sparse‑adaptation strategy varies: for backbone A, global sharing with a 5‑expert pool is optimal; for backbone B, client‑private experts dominate; for backbone C, mixed routing yields the highest performance. Routing analysis reveals that clients preferentially activate experts matching their building’s dominant temporal pattern.  

## Significance  
By decoupling adaptation granularity from model sharing, this work enables scalable, privacy‑preserving personalization of foundation models in real‑world settings where data is non‑IID and sensitive. The sparse MoE design reduces communication overhead while maintaining high accuracy, offering a template for other federated AI applications.  

## Related Concepts  
- Federated learning (FL)  
- Sparse adaptation / expert networks  
- Time‑series foundation models (TSFMs)  
- Heterogeneous mixture‑of‑experts (MoE)  
- Sequence routing  
- Non‑IID data
