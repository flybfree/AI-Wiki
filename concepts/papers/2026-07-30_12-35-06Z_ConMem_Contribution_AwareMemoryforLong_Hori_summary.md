# Summary: 2026-07-30_12-35-06Z_ConMem_Contribution_AwareMemoryforLong_HorizonManu.md
Saved: 2026-07-30 20:36
Source: 2026-07-30_12-35-06Z_ConMem_Contribution_AwareMemoryforLong_HorizonManu.md
Model: None

---

## Summary  
Long‑horizon steel‑equipment inspection demands reasoning over heterogeneous records that accumulate across multiple cycles. Existing retrieval‑augmented generation systems treat these logs as a static corpus and ignore each record’s diagnostic value, leading to missed early risks. ConMem addresses this by segmenting the logs into functional evidence units, estimating each unit’s contribution to downstream diagnosis with a Shapley‑style model, and then retaining only the high‑value units within a constrained memory budget. The framework is designed for LLM‑assisted inspection that supports a human‑in‑the‑loop early‑risk screening system.

## Key Contributions  
- [Finding 1] ConMem introduces a contribution‑aware memory framework that segments inspection logs into functional evidence units and evaluates each unit’s diagnostic impact using Shapley‑style estimation.  
- [Finding 2] The method retains only the most valuable evidence under a strict token budget, achieving an 88.2 % reduction in average input tokens compared with naive 8K‑context baselines.  
- [Finding 3] Ablation studies demonstrate that functional‑role‑aware segmentation and contribution‑based valuation prioritize weak degradation signals for targeted field inspection.

## Methodology  
ConMem first parses a long inspection log into discrete evidence units, each representing a specific functional aspect of the equipment. For every unit, a Shapley value is computed to quantify its marginal contribution to overall diagnosis accuracy. The system then ranks these units and selects a subset that maximizes diagnostic utility while respecting a fixed memory token limit. This selected set is fed to an LLM‑based QA model within a human‑in‑the‑loop workflow, enabling early‑risk screening before full inspection.

## Results  
On a real‑world dataset, ConMem achieves 76.0 % QA accuracy, surpassing the strongest directly comparable baseline. Compared with naive 8K‑context LLM baselines, it reduces average input tokens by 88.2 % and response time by 86.6 %. Ablation experiments confirm that functional‑role‑aware segmentation and contribution‑based valuation are essential for prioritizing weak degradation signals toward targeted field inspection.

## Significance  
By focusing memory on the most informative evidence, ConMem enables early detection of subtle failures, reduces unnecessary data loading, and shortens inspection turnaround time. This improves safety by flagging potential issues to inspectors before they become critical, while also lowering computational overhead for LLM‑based systems in manufacturing environments.

## Related Concepts  
retrieval‑augmented generation, memory constraints, functional evidence units, Shapley value estimation, LLM, manufacturing inspection logs, human‑in‑the‑loop early‑risk screening.
