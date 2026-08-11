# Summary: 2026-08-08_07-04-28Z_ThinkingHard_NotSmart_ReasoningModelsFailtoRationT.md
Saved: 2026-08-10 22:51
Source: 2026-08-08_07-04-28Z_ThinkingHard_NotSmart_ReasoningModelsFailtoRationT.md
Model: None

---

## Summary  
The paper investigates how reasoning language models allocate a shared token budget across multiple test questions when compute is limited globally rather than per question. It shows that current models treat each question independently, leading to suboptimal distribution of inference resources. The authors introduce an exam‑style evaluation framework where a single token budget must be split among questions with varying difficulty and point values to maximize total score. Their analysis reveals systematic failures in strategic allocation across diverse reasoning tasks.  

## Key Contributions  
- [Finding 1] Models allocate tokens greedily according to presentation order, front‑loading effort on early questions regardless of difficulty or value.  
- [Finding 2] Explicit planning prompts do not improve value‑aware or difficulty‑aware prioritization; compute remains unevenly distributed.  
- [Finding 3] The same allocation bias persists across mathematical and code reasoning tasks, indicating a broader limitation in budgeting capabilities.  

## Methodology  
The authors construct an exam‑style benchmark that presents a single token budget to be divided among N questions. Each question has associated difficulty (estimated by token length) and point value. The model must generate responses sequentially while respecting the total token limit. Experiments compare baseline models, models with explicit planning prompts, and human‑rated optimal allocations. The framework isolates compute allocation as the sole variable, enabling systematic evaluation.  

## Results  
Across ten open‑source reasoning models (including GPT‑4‑Turbo, Claude 2, and LLaMA‑3), average token usage per question follows a steep front‑loading curve: early questions consume up to 70 % of the budget while later ones receive minimal tokens. Even with planning prompts, the variance in allocation remains high (standard deviation ≈ 15 %). Human‑optimal allocations distribute tokens more evenly (mean ratio 0.92 vs model 0.68). The gap widens as question count increases, confirming a systematic failure to balance load.  

## Significance  
These findings expose a critical gap between per‑question evaluation and real‑world compute constraints where multiple tasks compete for limited inference resources. By demonstrating that models lack global budgeting ability, the work motivates research into planning mechanisms and resource‑aware architectures. It also highlights that current model performance metrics may mislead by ignoring inter‑task trade‑offs.  

## Related Concepts  
- Token budget allocation  
- Test‑time compute management  
- Greedy vs optimal decision making  
- Planning prompts in language models  
- Difficulty and value weighting
