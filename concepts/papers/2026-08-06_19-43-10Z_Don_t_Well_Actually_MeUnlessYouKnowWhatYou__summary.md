# Summary: 2026-08-06_19-43-10Z_Don_t_Well_Actually_MeUnlessYouKnowWhatYou_reTalki.md
Saved: 2026-08-09 22:24
Source: 2026-08-06_19-43-10Z_Don_t_Well_Actually_MeUnlessYouKnowWhatYou_reTalki.md
Model: None

---

## Summary  
The paper investigates why false‑presupposition QA (FPQA) methods that excel on benchmark questions with false presuppositions often fail on ordinary true‑presupposition questions (TPQs). It argues that the task is being misaligned because many benchmarks over‑represent FPQs and that weak fact‑checking modules mistakenly reject true presuppositions. The authors demonstrate a systematic degradation of general QA performance when only strong FPQ handling is prioritized. Their contribution is to reveal this bias and propose a path toward more balanced evaluation.  

## Key Contributions  
- Finding 1: Benchmarks heavily skew towards false‑presupposition questions, so improvements in FPQ performance do not translate to real‑world general QA.  
- Finding 2: Methods that perform best on FPQs suffer from weak fact‑checking modules that reject both true and false presuppositions.  
- Finding 3: The degradation of TPQ performance is directly linked to the over‑penalization of true presuppositions by these methods.  

## Methodology  
The authors conduct extensive experiments across multiple model families (e.g., LLaMA, GPT‑NeoX), sizes (7B–175B parameters) and benchmark suites (FPQA, TPQA, Natural Questions). They compare two families of approaches: those that rely on explicit presupposition extraction and fact verification versus those that use a single “answer‑only” prompt. For each setup they measure both FPQ accuracy and TPQ correctness, then analyze the trade‑off.  

## Results  
Across all experiments, models trained with strong FPQ handling consistently achieve lower TPQ scores, sometimes by 15–20 percentage points. The worst performers on FPQs also show the largest drop in TPQ performance, confirming a negative correlation between FPQ strength and general QA quality. Moreover, ablation studies reveal that disabling the fact‑checking module restores TPQ accuracy to baseline levels.  

## Significance  
This work highlights a critical flaw in current FPQA evaluation: it rewards memorization of false presuppositions while penalizing accurate handling of true ones, leading to models that are brittle and ungeneralizable. By exposing this bias, the authors urge researchers to design balanced benchmarks and methods that preserve both correct and incorrect presupposition detection.  

## Related Concepts  
- Presupposition: background knowledge assumed by a statement.  
- Fact checking: verifying whether a presupposed fact is true.  
- False presupposition QA (FPQA): identifying false background assumptions.  
- True presupposition QA (TPQ): correctly affirming true background assumptions.  
- Model bias, evaluation skew, generalizability.
