# Summary: 2026-07-29_14-05-26Z_WhatDoesItTaketoDetectanAIAgent_MinimalFeatureSets.md
Saved: 2026-07-29 20:34
Source: 2026-07-29_14-05-26Z_WhatDoesItTaketoDetectanAIAgent_MinimalFeatureSets.md
Model: None

---

## Summary  
The paper addresses the limitation of binary bot detectors that cannot distinguish AI‑driven browser automation sessions from human traffic, a class that is neither fully human nor fully bot. By introducing a three‑class framework—human, bot, and AI agent—the authors demonstrate that adding an explicit “agent” label resolves misclassifications caused by the original binary assumption. Their experiments show that minimal feature sets can achieve perfect per‑class recall for agents while maintaining high precision across all evasion levels.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A three‑class detection framework eliminates the binary‑vs‑agent confusion, yielding per‑class agent F1 = 1.000 in every run of 30 experiments (3 model families × 10 seeds).  
- [Finding 2] Adding an explicit “agent” class resolves all misclassifications; conversely, a binary classifier misroutes agents at rates of 39.1% (MLP) and 34.5% (SAINT transformer).  
- [Finding 3] Two behavioral features—mouse_event_rate and teleport_click_ratio—provide 100 % observed agent recall with precision ≈ 0.994, while a five‑feature set lifts macro‑F1 to ≥ 0.99 across all evasion levels.

## Methodology  
The authors constructed a controlled benchmark that includes passive observation, GAN‑generated trajectories, and replay of real human cursor data from 2 299 sessions (n = 2299). They evaluated three model families—MLP binary classifier, SAINT transformer, and a baseline—across ten random seeds. To assess evasion resistance, they built a five‑level ladder that spans each technique’s output. An exhaustive search over all feature subsets of size 1–5 (9 401 Gradient Boosting Machines) was performed to identify the smallest informative sets.

## Results  
Across 22 990 per‑seed predictions, zero AI agents were missed when the three‑class model was used. The two‑feature subset (mouse_event_rate, teleport_click_ratio) achieved 100 % recall and a precision of 0.994; adding three more features raised macro‑F1 to 0.991 while preserving all classes. A single feature is degenerate—it forces the classifier to predict “agent” for every session.

## Significance  
Binary detectors cannot capture AI agents because their label space lacks an agent class, leading to systematic misrouting. The paper proves that a minimal set of behavioral artifacts is sufficient for reliable detection, challenging the assumption that richer models are always better and highlighting the importance of explicit class definitions in multi‑class problems.

## Related Concepts  
- Three‑class classification (human, bot, AI agent)  
- Browser automation artifacts (missing raw pointer‑move/wheel‑delta streams)  
- GAN‑generated synthetic trajectories  
- Replay of human cursor data for evasion testing  
- Feature engineering (mouse_event_rate, teleport_click_ratio)  
- Gradient Boosting Machine ensemble search for minimal feature sets
