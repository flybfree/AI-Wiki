# Summary: 2026-07-21_03-25-01Z_SciHazard_ABenchmarkforMeasuringScientificSafetyRi.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_03-25-01Z_SciHazard_ABenchmarkforMeasuringScientificSafetyRi.md
Model: None

---

## Summary  
The paper introduces **SciHazard**, a benchmark that measures scientific safety risks by grounding queries in real‑world hazards and documented failure scenarios across 12 disciplines. It proposes a decomposed harm scoring framework called **DeHarm‑Score** that evaluates both the severity of the query, the model’s refusal behavior, and the risk embedded in any non‑refused response. The authors also introduce two sub‑components: **Executability**, which quantifies how actionable a harmful answer is via weighted dynamic checklists, and **Net‑new risk**, assessed through retrieval‑augmented claim extraction and synthesis‑barrier verification. Expert validation demonstrates that DeHarm‑Score aligns with human annotations at 90.17 % higher accuracy than the strongest baseline.

## Key Contributions  
- [Finding 1] SciHazard provides a real‑world, discipline‑spanning dataset of 2400 hazardous and 600 oversafety questions, enabling evaluation that reflects actual scientific safety concerns rather than templated prompts.  
- [Finding 2] The DeHarm‑Score metric decomposes safety risk into three measurable parts—query severity, refusal behavior, response‑level risk—and further splits the latter into Executability and Net‑new risk for finer granularity.  
- [Finding 3] Benchmarking 31 frontier LLMs and deep research agents shows that deep research agents systematically produce higher DeHarm‑Scores (≈ 32.3 % increase) than standard LLMs, highlighting a critical blind spot in current safety defenses.

## Methodology  
The authors constructed the dataset by mining regulated entities and documented failure cases from scientific literature, ensuring each query is tied to a concrete hazard. For scoring, they first compute DeHarm‑Score: if a model refuses, the score reflects refusal severity; otherwise, it adds the sum of response‑level risk components. Executability is derived from a checklist that rates how easily an answer could be acted upon, weighted by importance. Net‑new risk is evaluated via retrieval‑augmented claim extraction to locate similar harmful claims and synthesis‑barrier verification to confirm that the model’s output does not introduce novel unsafe knowledge.

## Results  
Expert validation shows DeHarm‑Score improves agreement with human annotations by 90.17 % over the strongest baseline. In a benchmark of 31 frontier LLMs and deep research agents, the mean DeHarm‑Score for deep research agents exceeds that of standard LLMs by roughly one‑third (≈ 32.3 %). This indicates that autonomous agents generate more hazardous outputs than conventional models.

## Significance  
SciHazard and DeHarm‑Score offer a systematic way to quantify scientific safety risks, moving beyond simplistic “yes/no” judgments toward nuanced, actionable metrics. By exposing the higher risk profile of deep research agents, the work underscores the need for specialized safeguards in autonomous AI systems that operate outside human oversight.

## Related Concepts  
- LLM‑as‑a‑Judge paradigm  
- Decomposed harm scoring (DeHarm‑Score)  
- Executive‑risk quantification via dynamic checklists  
- Net‑new risk detection through retrieval‑augmented claim extraction and synthesis‑barrier verification
