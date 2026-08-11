# Summary: 2026-08-10_14-19-08Z_Avalon_ToM_Bench_EvaluatingFine_GrainedTheoryofMin.md
Saved: 2026-08-11 00:13
Source: 2026-08-10_14-19-08Z_Avalon_ToM_Bench_EvaluatingFine_GrainedTheoryofMin.md
Model: None

---

## Summary  
The paper introduces Avalon‑ToM‑Bench, a fine‑grained benchmark that evaluates Theory of Mind (ToM) by exploiting the asymmetric information structure of The Resistance: Avalon. Rather than measuring overall game performance, it isolates ToM reasoning into epistemic versus motivational dimensions and inference versus action using perspective‑constrained queries. By probing 28 large language models, the authors uncover three distinct failure modes that reveal where current ToM evaluations fall short.

## Key Contributions  
- [Finding 1] Reasoning, not knowledge: Models demonstrate strong comprehension of game rules but exhibit markedly weaker ToM abilities, indicating failures are in social reasoning rather than missing factual knowledge.  
- [Finding 2] Expression, not representation: Linear probing and activation‑steering analyses show that correct mental‑state inferences appear in hidden states yet are rarely expressed during generation; probes achieve 77–82 % accuracy versus only 62–70 % from the models’ own chain‑of‑thought.  
- [Finding 3] Policy, not deliberation: Dedicated reasoning training yields substantial improvements (≈11 points) whereas test‑time chain‑of‑thought offers marginal gains (+1.1 points), suggesting robust ToM depends on a learned policy rather than increased inference time.

## Methodology  
The authors operationalize ToM through the asymmetric information mechanics of The Resistance: Avalon, where each player holds private knowledge and must infer others’ motives or beliefs. They design a 2×2 taxonomy that pairs epistemic (belief) reasoning with motivational (desire) reasoning, and inference with action. Human‑crafted queries from multiple perspectives are generated to probe these dimensions, and the performance of 28 LLMs is measured on both rule‑following and ToM tasks.

## Results  
The benchmark reveals a gap between model knowledge of game mechanics and their capacity for social reasoning. While linear probes recover high accuracy when probing hidden representations, the models’ own generation yields low expression rates. Training the models to adopt a dedicated reasoning policy improves average scores by 11 points compared with only a 1‑point boost from adding chain‑of‑thought prompting.

## Significance  
Avalon‑ToM‑Bench provides a granular diagnostic tool that separates ToM failures from knowledge gaps, guiding more targeted model improvement strategies. By highlighting the importance of expression and policy learning over mere deliberation, it informs future research on how to better embed social cognition in language models.

## Related Concepts  
Theory of Mind, epistemic reasoning, motivational reasoning, inference, action, asymmetric information games, linear probing, activation steering, chain‑of‑thought prompting, reasoning policy.
