# Summary: 2026-07-29_19-22-09Z_BenchmarkingLLMCompetenceonLogicalInferenceoverPro.md
Saved: 2026-07-30 20:22
Source: 2026-07-29_19-22-09Z_BenchmarkingLLMCompetenceonLogicalInferenceoverPro.md
Model: None

---

## Summary  
The paper’s goal is to benchmark large language models’ ability to perform logical inference on sentences that contain gradable epistemic modals such as “probably,” “might,” or “must.” By creating a systematic set of 14,320 English prompts across fifteen inference templates, the authors aim to separate principled symbolic reasoning from surface‑level pattern matching. Their contribution is both methodological and empirical: they introduce a competence floor metric that captures the worst performance on correct Yes/No items and demonstrate that only nine out of twenty‑nine models exceed random chance, while also uncovering pervasive answer biases across multiple dimensions.  

## Key Contributions  
- **Finding 1:** Most LLMs exhibit a systematic preference for “Yes” or “No,” regardless of the underlying logical form of the probability operator.  
- **Finding 2:** The authors define a competence floor as the minimum accuracy between Yes‑correct and No‑correct items, showing that only nine models surpass random guessing on this metric.  
- **Finding 3:** Biases persist across variations in question phrasing, verb phrases/activities, gender, and name origin, indicating that surface characteristics heavily influence outputs.  

## Methodology  
The authors procedurally generated English prompts using fifteen inference templates that vary the question form, negation strategy, and surface content while embedding gradable epistemic modals (e.g., “probably,” “might,” “must”). This creates a balanced dataset of 14,320 prompts. Twenty‑nine publicly available LLMs were evaluated on their accuracy for each prompt. To test robustness, the authors also varied question phrasing, verb phrases/activities, and the gender/origin of names within the prompts, measuring any resulting bias.  

## Results  
The experimental results reveal that the majority of models achieve low overall accuracy; the competence floor metric consistently underestimates their true performance because it isolates only the worst‑scoring Yes/No items. Only nine out of twenty‑nine models exceed random chance (≈31 % above chance), confirming a pervasive lack of competence. Crucially, answer bias is independent of logical form; “Yes” responses are favored uniformly across all templates. Additional tests confirm that biases propagate through question form, verb phrases/activities, gender, and name origin, suggesting surface‑level influences dominate over genuine reasoning.  

## Significance  
These findings highlight a critical gap in current LLM evaluation: they struggle with principled symbolic inference over uncertainty, which is essential for high‑stakes domains such as medicine and law. The competence floor provides a transparent metric that can be used to compare models on this specific task, while the observed biases underscore the need for more rigorous testing of fairness across demographic variables.  

## Related Concepts  
- Probability operators (e.g., “probably,” “might,” “must”)  
- Gradable epistemic modals and logical inference  
- Answer bias in language models  
- Competence floor metric  
- Surface‑level pattern matching vs. symbolic reasoning  
- Systematic evaluation of LLMs on uncertainty tasks
