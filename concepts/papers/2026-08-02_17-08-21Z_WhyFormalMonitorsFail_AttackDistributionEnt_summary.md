# Summary: 2026-08-02_17-08-21Z_WhyFormalMonitorsFail_AttackDistributionEntropyasa.md
Saved: 2026-08-04 00:17
Source: 2026-08-02_17-08-21Z_WhyFormalMonitorsFail_AttackDistributionEntropyasa.md
Model: None

---

## Summary  
The paper investigates why formal safety monitors based on Linear Temporal Logic (LTL) and finite automata achieve variable recall across LLM architectures, ranging from 68 % to near‑zero. It establishes a theoretical bound linking monitor recall to the entropy of attack distribution. The authors show that high‑entropy attacks cannot be covered by any fixed invariant set without large size, while low‑entropy attacks can be captured efficiently. This work provides both a proof and an empirical validation across eight frontier models.  

## Key Contributions  
- [Finding 1] Recall of any fixed‑invariant FSA monitor is bounded above by the concentration of the attack distribution: the fraction of attacks covered by the k most frequent trigger‑completion patterns.  
- [Finding 2] When attacks concentrate (low Shannon entropy), a small invariant set achieves high recall; when they disperse across many structurally distinct patterns (high entropy), no tractable fixed invariant can achieve meaningful recall regardless of how invariants were derived.  
- [Finding 3] Entropy accounts for 76 % of variance in coverage (Pearson r = –0.87, p = 0.005, 95 % CI [-0.98, –0.78]), and a small pre‑deployment entropy test predicts monitor coverage from a sample attack trace with high accuracy.  

## Methodology  
The authors derived the bound analytically using information theory, then collected attack traces from eight LLM backends (GPT‑class, DeepSeek, Gemini). For each backend they computed Shannon entropy per trigger‑completion pattern, compared recall to entropy, performed leave‑one‑out analysis, and conducted statistical testing. A lightweight test that measures the distribution of observed patterns is introduced as a predictor of coverage.  

## Results  
Across architectures, GPT‑class and DeepSeek attacks had H ≈ 0.24 bits with one pattern covering 96 % of attacks, yielding recall of 68–75 %. Gemini variants exhibited high entropy (H ≈ 2.81 bits) with seven clusters each ≤7 % coverage, resulting in near‑zero recall (6–13 %). The Pearson correlation between entropy and recall was r = –0.87 (p = 0.005). Leave‑one‑out analysis gave r in [-0.91, –0.82]. A small sample entropy test predicts coverage with high accuracy.  

## Significance  
This theory clarifies the observed variability of safety monitor performance, enabling architecture‑aware monitor selection and preventing overfitting to narrow attack patterns. It also offers a simple diagnostic tool for designing runtime monitors that are both effective and efficient across diverse LLM systems.  

## Related Concepts  
Linear Temporal Logic (LTL), finite automata (FSA), Shannon entropy, Markov chain, coverage bound, LLM agents, runtime safety monitors, information theory, statistical correlation.
