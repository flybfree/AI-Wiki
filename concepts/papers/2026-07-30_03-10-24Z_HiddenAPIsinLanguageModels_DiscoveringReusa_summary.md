# Summary: 2026-07-30_03-10-24Z_HiddenAPIsinLanguageModels_DiscoveringReusableCaus.md
Saved: 2026-07-30 21:37
Source: 2026-07-30_03-10-24Z_HiddenAPIsinLanguageModels_DiscoveringReusableCaus.md
Model: None

---

## Summary  
The paper tackles the problem that identical language‑model answers can arise from different internal hidden states because future computations are not yet fixed, preventing the reuse of causal interfaces. To address this, it introduces **forked futures**, a framework where future operations are sampled only after a prefix state has formed, allowing empirical discovery of reusable causal interfaces without predefined latent labels. By comparing response distributions induced by those operations, the authors compute an empirical causal quotient over hidden states and evaluate four interface types (Shared, Local, Mixture, Distributed) under prequential causal description length constraints. The Shared interface emerges as the most efficient with minimal distortion.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- **Forked futures framework**: A systematic way to discover reusable causal interfaces by comparing response distributions of future operations after a prefix state is established.  
- **Empirical ranking and validation**: Four interface types are ranked using prequential description length, future‑signature fidelity, and capacity constraints; Shared shows the lowest held‑out description length across two model evaluations.  
- **Blind model‑organism test**: 14 out of 16 architectures are correctly identified as Shared, demonstrating that the method works for a wide range of models while preserving the conditional nature of the claim.

## Methodology  
The authors generate a prefix state from a language model and then sample a set of future operations (e.g., token generation, classification tasks) to produce distinct response distributions. By treating each operation bank as an “API” that can be applied to the same hidden state, they compute a causal quotient that measures how much the hidden state is shared across banks. Interfaces are defined by shared latent variables; the evaluation uses description length (a measure of redundancy) and distortion of future signatures while keeping capacity matched. The Shared interface is selected as the one with minimal held‑out description length.

## Results  
In two detailed model evaluations—Qwen2.5‑1.5B and Llama‑3‑8B—the Shared interface achieved the lowest held‑out description length, improving it by 0.216 nats and 0.294 nats respectively compared with other interfaces. A five‑backbone sweep confirmed that the gain remains positive across models. Table‑aligned transplantation analysis revealed high joint target‑correctness, locality, copy‑preservation, and composite profile for Shared versus API‑aligned null paths (0.749 vs 0.150). In a blind four‑class model‑organism test, 14/16 architectures were recovered as Shared, with only one error among the non‑Shared organisms.

## Significance  
The work provides an economical reusable causal interface that operates within existing operation banks, offering a principled metric (prequential description length) to quantify internal reuse without labeling. By conditioning its claim on specific architectures and interventions, it advances our understanding of hidden APIs in LLMs and suggests practical pathways for more efficient model design.

## Related Concepts  
- Causal interfaces  
- Forked futures  
- Prequential causal description length  
- Future‑signature fidelity  
- Shared latent variables  
- API alignment  
- Model‑organism test
