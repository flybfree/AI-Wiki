# Summary: 2026-07-24_19-48-32Z_CHiPS_CharacterHistogramsandPositionalSignalsforLi.md
Saved: 2026-07-27 22:32
Source: 2026-07-24_19-48-32Z_CHiPS_CharacterHistogramsandPositionalSignalsforLi.md
Model: None

---

## Summary  
The paper introduces CHiPS, a lightweight character‑level authorship attribution system for Romanian texts that combines two complementary fingerprints: a character‑histogram classifier and a positional‑signal classifier based on Fourier descriptors of impulse trains. The method avoids tokenization, n‑gram features beyond length 1, and any pretrained language models, focusing instead on transparent statistical patterns in raw characters and punctuation at fixed positions. Experiments are conducted under strict closed‑set leakage control using the ROST split, where true authorship is limited to a subset of candidates. The approach demonstrates high accuracy (0.9310) while respecting these constraints.  

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] CHiPS achieves near‑perfect classification performance on Romanian source‑text groups without using n‑gram features or external language models, showing that simple character marginal statistics can be sufficient when leakage is tightly controlled.  
- [Finding 2] The FFT12‑LR component extracts spectral signatures from binary impulse trains representing characters and punctuation at specific positions, providing a complementary positional fingerprint that improves robustness to small variations in writing style.  
- [Finding 3] A decision‑level fusion variant CHiPS‑F with leakage‑safe design and an optional top‑5 listwise reranker yields high macro‑F1 scores (0.9341) while preserving interpretability and computational lightness.  

## Methodology  
The authors approached authorship attribution by treating each text as a sequence of characters and punctuation marks, generating two fingerprints: CH‑SVM uses one‑character marginal histograms across the entire corpus to classify based on frequency distributions; FFT12‑LR builds impulse trains where selected characters or punctuation classes are encoded as binary sequences at fixed positions, then computes Fourier/Welch spectral descriptors for classification. The fused model combines both signatures via a decision‑level classifier (CHiPS‑F), and an alternative reranker uses out‑of‑fold predictions to produce a ranked list of top candidates without retraining.  

## Results  
On the locked grouped ROST split with 400 files from 392 groups, CHiPS‑F achieved 0.9310 accuracy and 0.9341 macro‑F1; the matched unrestricted TF‑IDF SVM reached perfect scores (1.0000), confirming that CHiPS’s performance is high but not necessarily optimal under full freedom. On a secondary ROST‑overlapping corpus of 1,248 files from 1,240 groups and 19 authors, CHiPS‑R delivered 0.8919 accuracy and 0.8708 macro‑F1, demonstrating scalability to larger, more diverse datasets.  

## Significance  
This work matters because it provides a transparent, low‑resource method for attributing Romanian authorship that respects strict leakage constraints—critical for privacy‑sensitive applications such as plagiarism detection or literary analysis. By avoiding complex tokenization and large language models, CHiPS offers an interpretable alternative to black‑box transformer approaches while still delivering state‑of‑the‑art results within a controlled experimental regime.  

## Related Concepts  
- Authorship attribution  
- Character histograms  
- Positional signals (impulse trains)  
- Fourier/Welch spectral descriptors  
- Closed‑set evaluation  
- Decision‑level fusion  
- Listwise reranking
