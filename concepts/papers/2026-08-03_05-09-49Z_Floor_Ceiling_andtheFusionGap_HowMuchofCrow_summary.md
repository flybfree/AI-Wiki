# Summary: 2026-08-03_05-09-49Z_Floor_Ceiling_andtheFusionGap_HowMuchofCrowdReadin.md
Saved: 2026-08-03 23:36
Source: 2026-08-03_05-09-49Z_Floor_Ceiling_andtheFusionGap_HowMuchofCrowdReadin.md
Model: None

---

## Summary  
The paper investigates how much of the “crowd‑reading” signal that humans implicitly generate when they highlight sentences in web documents can be captured by machine models, establishing a quantitative gap between naïve and optimal performance. By defining a floor (naïve truncation) and a ceiling (split‑half oracle), the authors quantify this gap as +0.2028 AP and uncover three interrelated findings that explain why frontier language models succeed only partially. Their work bridges human‑level intuition with AI capability, showing that the crowd’s advantage lies in document‑level structure rather than individual token cues.

## Key Contributions  
- [Finding 1] The semantic gap between trivial position/length features and the full crowd signal is only ~5 % of the total AP improvement.  
- [Finding 2] Frontier language models capture 35–53 % of the gap zero‑shot, while a state‑of‑the‑art prompt compressor (LLMLingua‑2) falls below the floor, indicating random performance.  
- [Finding 3] An unweighted fusion of five frontier rankings plus a position prior reaches 60 % AP, beating any single model by +0.0159 and surviving multiple perturbations; replication on 217 documents confirms this gain.

## Methodology  
The authors construct two extreme baselines for the task: the floor (naïve truncation) and the ceiling (split‑half oracle where each half of a crowd predicts the other). The gap between these bounds is measured as +0.2028 AP, providing a realistic ceiling for human performance. They then evaluate how well various AI approaches—including zero‑shot language models, prompt compressors, and model‑fusion strategies—approach this ceiling.

## Results  
The semantic feature contribution accounts for 5 % of the gap; frontier LLMs achieve 35–53 % of it without fine‑tuning. The best single model reaches ~40 % of the gap, while a prompt‑compressed model drops below chance. Fusion of five rankings with a position prior yields 60 % AP, surpassing any individual model by +0.0159 (Holm p=0.019). Ablations confirm robustness: removing the best member, paraphrasing prompts, or altering label gating does not reduce performance. A pre‑registered replication on 217 documents yields a gain of +0.0179 (Holm p=0.042). Distilling this fusion into an open‑weight 8B student restores 90 % of the edge, matching the strongest single model (+0.0070) and showing that local‑context models retain only 63 %.

## Significance  
This study clarifies why crowd reading attention is hard for AI: most benefit comes from document‑level structure rather than token‑wise cues, and the cheapest improvement is to combine diverse model outputs. It also demonstrates that prompt compression can be detrimental, offering a cautionary baseline for future work.

## Related Concepts  
- Floor / ceiling bounds  
- Fusion gap (difference between trivial and optimal performance)  
- Crowd reading attention  
- Zero‑shot language models  
- Prompt compression (LLMLingua‑2)  
- Model fusion strategies  
- Semantic vs. positional feature contributions
