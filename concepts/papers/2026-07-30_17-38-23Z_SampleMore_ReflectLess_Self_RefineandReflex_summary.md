# Summary: 2026-07-30_17-38-23Z_SampleMore_ReflectLess_Self_RefineandReflexionLose.md
Saved: 2026-07-30 22:22
Source: 2026-07-30_17-38-23Z_SampleMore_ReflectLess_Self_RefineandReflexionLose.md
Model: None

---

## Summary  
This paper investigates why language‑model methods that add self‑refinement, critique, or debate to a single chain of thought generate more tokens and yet often perform worse than simply sampling the same question repeatedly. The authors conduct a controlled experiment comparing seven open models (1.5 B–7 B parameters) against repeated sampling under equal token budgets, measuring both accuracy and token usage. They find that self‑inspection techniques do not improve performance and can even degrade it, while simple sampling remains competitive or superior.  

## Key Contributions  
- [Finding 1] No method is reliably better than repeated sampling at equal token cost across model sizes.  
- [Finding 2] Self‑refine and reflexion methods are consistently worse; they generate more text but lower accuracy.  
- [Finding 3] Best‑of‑N sampling outperforms self‑inspection by ~8–11 points at the 1.5 B model, with negligible differences at 7 B.  

## Methodology  
The authors selected seven open models of 1.5 B, 3 B, and 7 B parameters, applied two mathematics benchmarks (150 questions each), and measured every generated token—including those spent on critiques, reflections, debate turns, and verification steps. Each method was paired with repeated sampling at its own measured cost; comparisons were made per question using bootstrap confidence intervals and multiplicity correction to control for the 36 pairwise tests.  

## Results  
All 36 paired comparisons showed no statistically significant advantage of any self‑inspection method over repeated sampling. Ten methods were reliably worse, all involving self‑inspection, with average accuracy deficits of 3.6–10.1 points at 7 B. Best‑of‑N (eight samples) outperformed self‑refine and reflexion by 8.0 and 11.3 points at the smallest model but only 2.0 and 1.3 points at the largest, indistinguishable from zero after correction.  

## Significance  
The study debunks the assumption that more elaborate reasoning automatically yields higher accuracy when token budgets are equal, highlighting a trade‑off between generation length and performance. It also clarifies why self‑inspection often fails: models may over‑refine without actually correcting errors, especially as scale increases. These findings guide researchers toward simpler sampling strategies for comparable efficiency.  

## Related Concepts  
- Token cost accounting  
- Self‑refine / reflexion loops  
- Best‑of‑N sampling  
- Bootstrap confidence intervals
