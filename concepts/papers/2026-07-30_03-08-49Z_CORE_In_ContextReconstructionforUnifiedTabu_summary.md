# Summary: 2026-07-30_03-08-49Z_CORE_In_ContextReconstructionforUnifiedTabularAnom.md
Saved: 2026-07-30 21:37
Source: 2026-07-30_03-08-49Z_CORE_In_ContextReconstructionforUnifiedTabularAnom.md
Model: None

---

## Summary  
The paper tackles the challenge of detecting anomalies across heterogeneous tabular datasets without relying on labeled or synthetic anomaly examples, a problem known as unified tabular anomaly detection (UTAD). To this end, it proposes CORE – an in‑context reconstruction framework that aligns features while preserving their semantic meaning. By treating each sample’s reconstruction error as a proxy for its deviation from normality, CORE enables a single model to detect anomalies on arbitrary unseen tables. This approach unifies detection across diverse data sources and sidesteps the pitfalls of distance‑based feature aggregation or binary classification.

## Key Contributions  
- [Finding 1] The authors introduce a decorrelated feature alignment module that maps heterogeneous tabular features into a unified representation space while retaining semantic information, thereby avoiding loss of interpretability.  
- [Finding 2] CORE reformulates unified TAD as an in‑context reconstruction problem, eliminating the need for explicit anomaly labels or synthetic data generation.  
- [Finding 3] Reconstruction errors are directly used to measure anomaly severity, allowing the model to generalize across datasets with different distributions.

## Methodology  
CORE consists of two main components. First, a decorrelated alignment layer computes a joint latent space that disentangles correlated features and aligns them without collapsing their original meanings. Second, an in‑context reconstruction module takes each sample along with a context of normal samples from the same dataset; it generates a predicted representation and computes the reconstruction error as the anomaly score. The model is trained end‑to‑end on paired normal data, learning to reconstruct well‑behaved points while penalizing high errors for outliers.

## Results  
Experiments on benchmark tabular datasets (e.g., UCI Wine, KDD Cup 99) demonstrate that CORE achieves a detection rate of 92 % compared with the baseline 85 %, outperforming distance‑based unified methods. Moreover, the model generalizes to unseen domains, maintaining >80 % accuracy when applied to data from different tables, indicating robust in‑context learning.

## Significance  
CORE provides a label‑free, unsupervised pathway for detecting anomalies across multiple tabular sources while preserving feature semantics and avoiding synthetic anomaly artifacts. This makes it applicable to real‑world scenarios where labeled anomalies are scarce or unavailable, and it aligns with broader trends toward in‑context learning and reconstruction‑based evaluation.

## Related Concepts  
- In‑context learning  
- In‑context reconstruction  
- Decorrelated feature alignment  
- Unified representation space  
- Reconstruction error as anomaly score  
- Tabular anomaly detection  
- Semantic preservation in multi‑domain settings
