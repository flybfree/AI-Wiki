# Summary: 2026-08-06_13-15-54Z_HERALD_CounterfactualAuditsandMinimalRepairsforPro.md
Saved: 2026-08-06 20:44
Source: 2026-08-06_13-15-54Z_HERALD_CounterfactualAuditsandMinimalRepairsforPro.md
Model: None

---

## Summary  
The paper addresses a critical flaw in proof‑of‑retrieval reward systems: high scores can be achieved even when the cited evidence was not actually retrieved, because penalties for oracle support are missing or too weak. HERALD proposes an offline audit that applies exact same‑question interventions, strictly separates candidate‑visible information from oracle data, and enumerates detector contracts before any policy optimization is performed. The authors identify a minimal repair $L$, which involves citing a passage absent from the retrieved evidence, as the most effective intervention; empirically it yields zero answer‑set‑ratio (ASR) violations with a tight 0.50% one‑sided upper bound. This work demonstrates that separating robust scoring signals from learning data can produce sparse yet powerful improvements.

## Key Contributions  
- [Finding 1] HERALD separates candidate‑visible information from oracle information and applies exact same‑question interventions to audit reward misalignment.  
- [Finding 2] The minimal repair $L$, which cites an absent corpus passage, improves citation precision and recall while eliminating unsupported citations with zero empirical ASR.  
- [Finding 3] The repair is effective across four Qwen3‑8B pools (HotpotQA, 2WikiMultiHopQA, MuSiQue), reduces attackability of the citation‑laundering attack, and satisfies EM non‑inferiority on HotpotQA and 2Wiki.

## Methodology  
The authors conduct an offline audit by generating counterfactual queries that test whether a high reward can hide unretrieved evidence. They enforce strict separation between what is visible to the candidate and what is known to the oracle, then enumerate detector contracts—conditions under which each piece of information should be penalized or rewarded. These contracts are used as constraints before any policy optimization proceeds. Experiments are run on four Qwen3‑8B pools from HotpotQA, 2WikiMultiHopQA, and MuSiQue, with a full $2^3$ ablation to identify the most impactful intervention.

## Results  
R0 rejects search deletion and fake IDs but fails against citation‑laundering. The $L$ repair shows zero empirical ASR and a 0.50% one‑sided cluster upper bound. A complete $2^3$ ablation confirms that strengthening $L$ is the optimal intervention. Across benchmarks, EM non‑inferiority gates are met on HotpotQA (p≈0) and 2Wiki (p≈0), whereas MuSiQue shows a larger gap. Citation precision rises by 2.02 points, support recall by 1.46 points, unsupported citations drop by 1.69 points, and the laundering attackability falls on 2Wiki and MuSiQue. Natural $L$ is unchanged, and the detector appears in only 18 of 58,368 training trajectories.

## Significance  
HERALD provides a principled framework for separating robust scoring from learning signals, enabling sparse yet effective improvements to proof‑of‑retrieval reward systems. By isolating minimal repairs that target specific attack vectors, the method enhances safety without compromising model performance, and it supports reliable policy transfer across diverse search environments.

## Related Concepts  
proof-of-retrieval rewards, counterfactual audits, minimal repairs, detector contracts, oracle support‑ID penalty, same‑question interventions, answer‑set‑ratio (ASR), EM non‑inferiority gate, BM25 attacker, citation‑laundering attack.
