# Summary: 2026-07-28_16-41-54Z_LargeLanguageModelforOperationsResearchFormulation.md
Saved: 2026-07-28 22:59
Source: 2026-07-28_16-41-54Z_LargeLanguageModelforOperationsResearchFormulation.md
Model: None

---

## Summary  
The paper tackles the challenge of selecting the most suitable mixed‑integer programming (MIP) formulation for multi‑warehouse inventory allocation, where heterogeneous instance regimes arise from demand concentration, inventory imbalance, replenishment scale, service constraints, and forecast volatility. It introduces a large language model (LLM) framework that learns to map these attributes to an expert library of OR formulations using solver‑guided fine‑tuning and group relative policy optimization (GRPO). The proposed selector outperforms both prior supervised‑fine‑tuning plus IPO preference methods and the best fixed formulation, delivering higher selection accuracy and better realized allocation quality.

## Key Contributions  
- Finding 1: A solver‑guided LLM selector that converts historical MIP evaluation gaps into margin‑weighted identity preference optimization (IPO) preferences and per‑instance expert‑score metadata for reward lookup in GRPO.  
- Finding 2: Empirical evidence that the GRPO‑based selector improves hit ratio at 1 (HR@1) from 21.45 % to 50.42 % and at 2 (HR@2) from 70.47 % to 82.31 % compared with SFT+IPO and fixed formulations.  
- Finding 3: The selector yields a 12.57‑percentage‑point allocation accuracy gain over the best baseline, reducing the gap to the ex‑post oracle to only 4.85 pp.

## Methodology  
The authors construct balanced expert‑conditioned supervised fine‑tuning (SFT) records that encode each MIP formulation as an OR “expert.” Using historical inventory allocation instances, they evaluate solver performance and translate solver‑evaluated allocation‑quality gaps into IPO preferences and per‑instance expert‑score metadata. These metadata are employed in group relative policy optimization to train a GRPO model that selects the optimal formulation for each new instance, leveraging reward lookup based on the learned metadata.

## Results  
Experiments on multi‑warehouse inventory allocation data from JD.com show that GRPO markedly improves selection performance: HR@1 rises to 50.42 % and HR@2 to 82.31 %. The resulting selector achieves an allocation accuracy gain of 12.57 percentage points relative to the incumbent baseline, outperforming both the SFT+IPO selector and the best fixed OR expert, while narrowing the oracle gap to 4.85 percentage points.

## Significance  
The work provides a scalable, data‑driven approach for dynamic operations research formulation selection, reducing reliance on manually curated expert libraries and directly improving real‑world inventory outcomes in complex, heterogeneous multi‑warehouse settings.

## Related Concepts  
- Mixed‑integer programming formulations  
- Multi‑warehouse inventory allocation  
- Instance‑wise OR formulation selection  
- Supervised fine‑tuning (SFT) for LLM selectors  
- Group relative policy optimization (GRPO)  
- IPO preferences and margin‑weighted identity scores  
- Hit ratio (HR@1, HR@2) as a metric of selector performance  
- Ex‑post oracle benchmarking
