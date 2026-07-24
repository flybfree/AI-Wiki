# Summary: 2026-07-21_17-42-50Z_Two_LevelMeta_RubricsforEvaluatingOpen_EndedGenera.md
Saved: 2026-07-24 01:21
Source: 2026-07-21_17-42-50Z_Two_LevelMeta_RubricsforEvaluatingOpen_EndedGenera.md
Model: None

---

## Summary  
The paper tackles the “missing half” of factuality in long‑form generation by proposing a two‑level meta‑rubric framework that captures both the organization and importance of required content. To operationalize this idea, it creates **Gamut**, a multimodal benchmark with 1 813 questions spanning ten diverse domains, each paired with an expert‑verified rubric. The framework converts the structured meta‑rubric into a flat binary checklist that can be scored reliably by language models, thereby measuring factual completeness rather than just precision.

## Key Contributions  
- **Finding 1:** A two‑level meta‑rubric representation separates high‑level content organization/importance from low‑level binary checks, enabling a systematic conversion to machine‑gradable rubrics.  
- **Finding 2:** The authors construct a large, domain‑diverse dataset (1 813 multimodal questions) with evidence‑backed rubrics validated by human annotators, demonstrating the benchmark’s breadth and reliability.  
- **Finding 3:** Evaluation on fourteen frontier and open‑weight models shows that factual completeness remains a genuine challenge—best score 58.7% (Gemini 3.1 Pro)—and is highly discriminative while robust to judge selection.

## Methodology  
The authors first define a structured meta‑rubric that encodes the logical hierarchy of facts required for each question, assigning importance weights. This meta‑rubric is then mechanically decomposed into a flat list of binary statements (e.g., “the model mentions X”, “X is true”). These statements become the checklist that an LLM judge evaluates. The dataset was built by pairing real wearable imagery with expert annotations, ensuring factual grounding. The framework is modality‑agnostic; a text‑only version is also released for comparative testing.

## Results  
Across 14 models (including Gemini 3.1 Pro, GPT‑4, Claude 2), the average factual‑completeness score was around 58–60%, with the highest at 58.7%. Scores varied widely per model and question type, indicating that completeness is not a trivial task. The benchmark’s performance remained stable across different judge implementations, confirming its robustness to evaluation pipeline choices.

## Significance  
Gamut provides the first comprehensive benchmark for measuring factual completeness in open‑ended generation, directly addressing the gap left by precision‑only metrics. By offering a reproducible two‑level rubric and large‑scale dataset, it enables researchers to compare models on a dimension that is currently under‑evaluated but critical for real‑world applications.

## Related Concepts  
- Factuality (truthfulness of claims) vs. factual completeness (coverage of required facts).  
- Precision‑recall trade‑off in generation evaluation.  
- Decompose‑search‑verify pipeline (common for precision).  
- Meta‑rubric: high‑level structure that guides low‑level binary checks.  
- Multimodal grounding and open‑ended question answering.
