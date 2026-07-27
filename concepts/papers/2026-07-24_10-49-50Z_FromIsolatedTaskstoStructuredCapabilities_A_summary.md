# Summary: 2026-07-24_10-49-50Z_FromIsolatedTaskstoStructuredCapabilities_AMultila.md
Saved: 2026-07-26 21:48
Source: 2026-07-24_10-49-50Z_FromIsolatedTaskstoStructuredCapabilities_AMultila.md
Model: None

---

## Summary  
The paper proposes a multi‑layer taxonomy that organizes LLM evaluation around 14 capability domains and their constituent subskills rather than isolated tasks, aiming to improve cross‑study comparison and reveal coverage gaps. By grounding the framework in human cognitive science and mapping it onto model behavior, the authors create a structured view of what LLMs can do, enabling systematic diagnosis, training, and transfer research. The taxonomy is validated through a large‑scale literature scan that links 15,934 LLM papers to the capability layers, revealing which domains dominate current research attention.

## Key Contributions  
- [Finding 1] A comprehensive multilayer taxonomy of 14 capability domains (Primitive, Constructed, Integrative) and 91 subskills is introduced.  
- [Finding 2] The authors mapped 31,505 papers from ACL, AAAI, ICML, NeurIPS (2023‑2025) to this taxonomy using multi‑model annotation, consensus, and arbitration.  
- [Finding 3] Language‑Semantic Competence and Reasoning together account for the highest volume of research attention (n = 1,864; 11.7% lift), while Theory of Mind and Social Reasoning show the greatest relative increase when co‑occurring.

## Methodology  
The authors leveraged human cognitive science to define capability domains based on developmental precedence and functional support, then adapted these constructs to observable LLM behavior. They screened a corpus of 31,505 conference papers for LLM relevance, performed multi‑model annotation to identify which capabilities were reported, and resolved disagreements via consensus and arbitration to produce a consensus mapping across all studies.

## Results  
The taxonomy revealed that Language‑Semantic Competence (22.3%) and Reasoning (21.3%) dominate the field, each with median subskill prevalence of 97.9% in ten domains. Six capability domains appear in fewer than 2% of papers, indicating under‑explored areas. The highest lift for co‑occurring pairs is Theory of Mind & Social Reasoning (n = 62; lift = 30.84), suggesting a strong synergistic interest.

## Significance  
By shifting analysis from task‑centric to capability‑centric, the taxonomy provides a unifying metric for evaluating LLM progress, facilitates systematic coverage audits, and supplies testable hypotheses for diagnosing model weaknesses, designing training regimes, and enabling transfer across domains. This structured approach can reduce redundancy, highlight gaps, and guide future research priorities.

## Related Concepts  
- Capability theory (human cognitive science)  
- Primitive, Constructed, Integrative layers  
- Subskill prevalence and median coverage  
- Literature mapping and consensus arbitration  
- LLM evaluation benchmarks
