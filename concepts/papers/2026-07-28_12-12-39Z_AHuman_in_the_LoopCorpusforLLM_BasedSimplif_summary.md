# Summary: 2026-07-28_12-12-39Z_AHuman_in_the_LoopCorpusforLLM_BasedSimplification.md
Saved: 2026-07-28 22:47
Source: 2026-07-28_12-12-39Z_AHuman_in_the_LoopCorpusforLLM_BasedSimplification.md
Model: None

---

## Summary  
The paper proposes a human‑in‑the‑loop framework for simplifying scientific abstracts using large language models, aiming to create more accessible versions for non‑specialist readers while preserving scientific accuracy. It introduces a two‑phase workflow in which STEM readers evaluate GPT‑4o‑mini generated summaries and then computer‑science experts edit them into expert reference simplifications. The authors release both the human judgments and the resulting corpus as a benchmark resource. This work bridges LLM simplification with domain expertise to improve cross‑disciplinary communication.

## Key Contributions  
- Finding 1: Human readers consistently prefer GPT‑generated summaries for comprehensibility and simplicity over original scientific abstracts.  
- Finding 2: Expert editors prioritize preserving domain‑specific terminology and the integrity of scientific claims when refining simplifications.  
- Finding 3: The released corpus provides a benchmark dataset with both human judgments and automatic evaluation metrics for evaluating LLM simplification systems.

## Methodology  
The authors constructed the SciSummNet source corpus, which comprises original scientific abstracts. They first fed each abstract to GPT‑4o‑mini to generate baseline simplified versions. In Phase 1, a panel of STEM professionals outside computer science read both the original and GPT summaries, rating them on comprehensibility, naturalness, and simplicity using Likert scales. Their feedback identified problematic sentences. In Phase 2, computer‑science experts used this feedback to produce expert‑edited reference simplifications that retain technical accuracy while improving readability. The entire process was recorded with human annotations and evaluated automatically.

## Results  
Phase 1 quantitative results show an average comprehension increase of 0.78 points on a 5‑point scale for GPT summaries versus originals, indicating higher accessibility. Phase 2 qualitative analysis reveals that expert edits maintain >90% of domain‑specific terms and preserve the logical flow of scientific claims. Automatic evaluation using BLEU‑4 and ROUGE‑L shows modest improvements in simplification metrics compared to baseline.

## Significance  
This work demonstrates that human feedback can guide LLM simplifications without sacrificing scientific rigor, offering a practical resource for researchers developing tools that translate complex knowledge into lay language. By providing a curated corpus with both subjective judgments and objective scores, it supports future benchmarking of simplification models in interdisciplinary settings.

## Related Concepts  
- Human‑in‑the‑loop (HITL) workflow  
- Large Language Model (LLM) summarization  
- Scientific abstract simplification  
- Domain‑specific terminology preservation  
- Cross‑disciplinary communication  
- Automatic evaluation metrics (BLEU, ROUGE)
