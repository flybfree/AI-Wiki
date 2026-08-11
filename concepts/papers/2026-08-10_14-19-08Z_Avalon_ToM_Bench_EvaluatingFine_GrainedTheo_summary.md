# Summary: 2026-08-10_14-19-08Z_Avalon_ToM_Bench_EvaluatingFine_GrainedTheoryofMin.md
Saved: 2026-08-10 23:51
Source: 2026-08-10_14-19-08Z_Avalon_ToM_Bench_EvaluatingFine_GrainedTheoryofMin.md
Model: None

---

## Summary  
Avalon‑ToM‑Bench introduces a fine‑grained benchmark for evaluating Theory of Mind (ToM) by operationalizing it through the asymmetric‑information mechanics of *The Resistance: Avalon*. The study decomposes ToM into epistemic versus motivational reasoning crossed with inference versus action, using perspective‑constrained queries that isolate specific mental‑state components. By benchmarking 28 large language models on these tasks, the authors reveal that performance is driven more by learned reasoning policies than by raw knowledge or deliberative inference. The work thus provides a diagnostic framework for pinpointing where ToM failures occur in AI agents.

## Key Contributions  
- **Finding 1:** Reasoning, not knowledge – Models demonstrate strong comprehension of game rules but exhibit markedly weaker ToM abilities, indicating that failures stem from social reasoning rather than missing domain facts.  
- **Finding 2:** Expression, not representation – Linear probing and activation‑steering analyses recover 77–82 % accuracy in hidden states for correct mental‑state inferences, whereas the models’ own chain‑of‑thought generation yields only 62–70 % accuracy.  
- **Finding 3:** Policy, not deliberation – Dedicated reasoning training improves performance by ~11 points on average, while test‑time chain‑of‑thought reasoning contributes only a marginal gain of +1.1 points.

## Methodology  
The authors constructed Avalon‑ToM‑Bench around the game *The Resistance: Avalon*, where players adopt hidden roles and must infer others’ intentions using asymmetric information. The benchmark decomposes ToM into four sub‑domains (epistemic vs. motivational, inference vs. action) and generates human‑crafted queries that are constrained to a single player’s perspective. Evaluation proceeds by feeding each query to 28 LLMs and measuring both the final answer and intermediate reasoning traces.

## Results  
The three findings above quantify the observed gaps: (1) Reasoning scores average ~70 % versus knowledge benchmarks at >90 %; (2) Linear probing outperforms self‑generated chains by roughly 15–20 percentage points; (3) Training‑policy improvements are ~10 times larger than test‑time chain‑of‑thought gains. These results collectively show that ToM in LLMs is a policy problem rather than a knowledge or deliberation one.

## Significance  
Avalon‑ToM‑Bench supplies the first systematic, fine‑grained diagnostic for ToM in AI systems, enabling researchers to target specific failure modes (e.g., expression vs. representation) and develop tailored interventions such as reasoning‑focused training. It bridges theory of mind research with practical LLM evaluation, offering a clear pathway from abstract mental‑state concepts to actionable model improvement.

## Related Concepts  
Theory of Mind, epistemic reasoning, motivational reasoning, inference, action, *The Resistance: Avalon* game mechanics, linear probing, activation steering, chain‑of‑thought, policy learning.
