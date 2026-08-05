# Summary: 2026-07-27_22-09-46Z_MOSAIC_FL_amicro_servicebasedprivacy_preservingfra.md
Saved: 2026-07-28 22:25
Source: 2026-07-27_22-09-46Z_MOSAIC_FL_amicro_servicebasedprivacy_preservingfra.md
Model: None

---

## Summary  
The paper proposes MOSAIC‑FL, a micro‑service based privacy‑preserving framework for federated learning that addresses security concerns in sensitive domains such as genomics. It integrates gRPC communication, a Finite State Machine, and CKKS homomorphic encryption to enable secure model aggregation while minimizing network overhead. The framework ensures IND‑CPA‑D security through noise flooding and mitigates key‑recovery attacks by renewing collective keys at every round. Experiments show robust performance across image classification (EMNIST) and complex genomic tasks like breast cancer subtyping on TCGA.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 15 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 12 summary/topic terms overlap

## Key Contributions  
- MOSAIC‑FL introduces a micro‑service architecture with gRPC and Finite State Machine for reliable synchronization, fault detection, and threat mitigation.  
- It employs CKKS homomorphic encryption with threshold decryption to achieve blind model aggregation while keeping communication low.  
- The system provides IND‑CPA‑D security via noise flooding and counters key‑recovery attacks by rotating collective keys per round.

## Methodology  
The authors approached the problem by modeling federated learning as a distributed system requiring secure, low‑latency interaction among clients. They selected gRPC for efficient RPCs, implemented a Finite State Machine to coordinate component states, and integrated CKKS cryptography with threshold decryption logic. Security was enhanced through noise flooding and key rotation strategies, while fault tolerance is ensured by the t‑out‑of‑N decryption protocol.

## Results  
Experiments on EMNIST image recognition demonstrate near‑state‑of‑the‑art accuracy with reduced communication latency. On TCGA breast cancer subtyping, MOSAIC‑FL achieves comparable performance to centralized baselines while preserving privacy guarantees across various threshold values and model scales, confirming robustness under different system configurations.

## Significance  
This work bridges the gap between theoretical security in federated learning and practical deployment in high‑stakes domains such as genomics. By providing a modular micro‑service framework that balances cryptographic strength with network efficiency, MOSAIC‑FL enables real‑world privacy‑preserving AI without sacrificing model quality or scalability.

## Related Concepts  
- Federated Learning (FL)  
- Homomorphic Encryption (CKKS)  
- Threshold Decryption  
- Indistinguishability under Chosen Plaintext Attack (IND‑CPA‑D)  
- Secure Aggregation  
- Noise Flooding  
- Finite State Machine for synchronization
