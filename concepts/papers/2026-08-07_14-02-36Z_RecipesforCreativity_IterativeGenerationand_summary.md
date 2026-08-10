# Summary: 2026-08-07_14-02-36Z_RecipesforCreativity_IterativeGenerationandEvaluat.md
Saved: 2026-08-09 22:58
Source: 2026-08-07_14-02-36Z_RecipesforCreativity_IterativeGenerationandEvaluat.md
Model: None

---

## Summary  
This paper investigates whether iterative generation and evaluation can enhance the creativity of large language models (LLMs) by adapting the FunSearch algorithm to a real‑world recipe‑generation task—the 2024 Pillsbury Bake‑Off. The authors compare model outputs against human benchmarks using a TTCT‑based LLM evaluator, varying iteration count, generator temperature, and the size of an in‑loop selection scorer. Their findings reveal that while iterative generation can approach human‑level creativity, the design of the evaluation component is far more decisive than sheer number of iterations or temperature settings.

## Key Contributions  
- [Finding 1] Iterative generation‑selection can produce recipes with creativity scores comparable to human benchmarks.  
- [Finding 2] Additional iterations alone do not improve creativity beyond a certain point.  
- [Finding 3] The in‑loop evaluator matters most: a smaller selection scorer yields significantly higher scores across TTCT dimensions, while temperature has limited effects except for originality.  

## Methodology  
The authors repurposed FunSearch—a reinforcement‑learning framework—to generate recipes iteratively. They employed a TTCT (Two‑Task‑Cycle‑Test) based LLM evaluator to score each candidate recipe on creativity metrics such as novelty, coherence, and aesthetic appeal. Experimental runs varied three hyperparameters: the number of iterations performed, the generator temperature controlling randomness, and the model size used for the in‑loop selector that chose which recipes to keep. This systematic variation allowed them to isolate the impact of each factor.

## Results  
Across two experiments, iterative generation combined with selection produced scores that matched human benchmark averages on most TTCT dimensions. However, increasing iteration count beyond a modest threshold did not yield further gains in creativity. Notably, models using smaller selection scorers consistently outperformed larger ones, indicating that the evaluator’s capacity to discriminate quality is more critical than its scale. Temperature only marginally affected originality scores; higher temperatures sometimes increased novelty but also reduced coherence.

## Significance  
These results underscore that evaluator design is a first‑order design variable in subjective creative search for LLMs. By highlighting how the selection scorer shapes outcomes, the study provides guidance for future research on iterative creativity and informs practitioners about which evaluation components to prioritize when building or tuning generative systems.

## Related Concepts  
FunSearch, recipe generation, TTCT (Two‑Task‑Cycle‑Test), Large Language Models (LLMs), creativity scoring, iterative search, generator temperature, in‑loop selection scorer, subjective evaluation.
