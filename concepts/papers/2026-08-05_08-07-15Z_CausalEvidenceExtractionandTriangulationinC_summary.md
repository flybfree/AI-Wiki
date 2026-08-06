# Summary: 2026-08-05_08-07-15Z_CausalEvidenceExtractionandTriangulationinCrisisRe.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_08-07-15Z_CausalEvidenceExtractionandTriangulationinCrisisRe.md
Model: None

---

## Summary  
Humanitarian crisis reports contain vast amounts of unstructured text that obscure the causal links between interventions and outcomes, hindering rapid decision‑making. This paper proposes a ReliefWeb‑based study that leverages large language models (LLMs) to extract structured evidence with direction and strength attributes, while also providing snippet grounding for auditability. The pipeline uses query‑conditioned extraction to limit output to a specific intervention class and introduces context‑preserving triangulation that aggregates strength‑weighted evidence across disaster‑source cells using Laplace smoothing and equal cell weighting to compute a Level‑of‑Evidence score. Experimental evaluation on an expert‑annotated set of 100 reports demonstrates high performance, especially for closed‑source models and fine‑tuned Llama‑3.1‑8B.

## Key Contributions  
- [Finding 1] A two‑stage LLM pipeline that extracts intervention‑outcome records with direction and strength attributes from humanitarian crisis reports.  
- [Finding 2] Query‑conditioned extraction combined with snippet grounding to reduce over‑extraction and enable auditability of each relation.  
- [Finding 3] Context‑preserving triangulation framework that computes a Level‑of‑Evidence score by aggregating strength‑weighted evidence across disaster‑source cells.

## Methodology  
The authors first compiled a ReliefWeb dataset spanning 2000–2024, then annotated 100 reports with expert labels for interventions and outcomes. They built a query‑conditioned LLM model that takes an intervention class as input and outputs structured records limited to that class; each output is linked to the exact text snippet via grounding. For triangulation, they grouped evidence into disaster × source cells, applied Laplace smoothing to handle sparse cell counts, and weighted all cells equally to produce a cross‑context convergence score.

## Results  
The best closed‑source LLM achieved a weighted F1 of 90.73% on the annotated set, while Llama‑3.1‑8B fine‑tuned with supervised data reached 94.15%. The triangulation method yielded a Level‑of‑Evidence score of 0.865 for cash assistance and food outcomes, indicating strong positive convergence across contexts.

## Significance  
By automating causal evidence extraction and providing a quantitative convergence metric, the approach accelerates humanitarian decision‑making under uncertainty, reduces manual annotation burden, and offers transparent audit trails that can be integrated into existing relief coordination systems.

## Related Concepts  
- Large Language Models (LLMs)  
- Causal inference in text  
- ReliefWeb data mining  
- Level‑of‑Evidence scoring  
- Triangulation of evidence across contexts
