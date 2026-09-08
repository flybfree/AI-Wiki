# Summary: 2026-09-01_05-35-36Z_HowDoLanguageModelsChooseBetweenContextandMemory.md
Saved: 2026-09-01 21:50
Source: 2026-09-01_05-35-36Z_HowDoLanguageModelsChooseBetweenContextandMemory.md
Model: None

---

## Summary  
The paper investigates how language models decide whether to rely on the short‑term context supplied during inference versus knowledge encoded in their parameters, showing that activation directions can encode an “authority” signal but are not causally reusable. It demonstrates that model behavior shifts when contextual and parametric sources conflict by using counterfactual experiments across Qwen, Llama, and OLMo. The study distinguishes between authority representation, its causal use within a single task, and cross‑task reuse of those cues. This work clarifies the internal mechanisms governing source selection in large language models.  

## Key Contributions  
- Authority directions can be extracted from agreement prompts where context and parameters agree, indicating a learned signal.  
- Interchanging coordinates along these directions reproduces 30–68 % of the authority‑induced shift in source choice, showing that steering is task‑specific.  
- Cross‑task transferability recovers only ~9 % of the authority gap, whereas local learning closes ~57 %, indicating limited reuse across tasks.  

## Methodology  
The authors create unambiguous prompts where both the supplied context and model parameters support identical answers. They then perturb the activation directions that encode “authority” by swapping natural coordinates between matched prompts, forcing the model to prioritize either the context or its parametric knowledge. This intervention is measured across three models (Qwen, Llama, OLMo) on a set of authority‑induced shifts.  

## Results  
The perturbation reproduces 30–68 % of the observed shift in source choice, while matched controls produce almost no effect. Cross‑task learning yields only ~9 % recovery of authority alignment, whereas task‑specific learning recovers ~57 %, highlighting the limited cross‑task reuse.  

## Significance  
Understanding these mechanisms matters because it reveals that model behavior is not a universal rule but depends on how authority cues are encoded and used within each task. This insight can inform more reliable prompt engineering and prevent overreliance on parameter knowledge when context is available.  

## Related Concepts  
- Authority direction  
- Activation steering  
- Source selection  
- Cross‑task transferability  
- Parametric vs. contextual memory  
- Counterfactual experiments
