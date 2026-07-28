# Summary: 2026-07-27_10-50-37Z_GenerativeArtificialIntelligence_GenAI_toconvertim.md
Saved: 2026-07-27 22:56
Source: 2026-07-27_10-50-37Z_GenerativeArtificialIntelligence_GenAI_toconvertim.md
Model: None

---

## Summary  
The paper proposes Sketch2DES, an open‑weight LLM workflow that converts queuing network diagrams into verifiable discrete‑event simulation models. It introduces a three‑stage pipeline (multimodal translation → schema‑validated JSON via reflection loop → deterministic code generation) to improve reproducibility and reduce the need for programming expertise. The approach is evaluated on eight varied diagrams with results matching human‑coded benchmarks. This work demonstrates that structured, workflow‑based model generation can serve as a robust foundation for LLM‑assisted simulation modelling.

## Key Contributions  
- Sketch2DES provides an open‑weight LLM pipeline converting visual queuing network diagrams into verifiable simulation models.  
- The three‑stage workflow (multimodal translation → schema‑validated JSON with reflection) ensures intermediate artefacts are inspectable and automatically validated.  
- Experimental results show high reliability, statistical indistinguishability from human‑coded solutions across eight test cases.

## Methodology  
The authors built Sketch2DES as a sequential LLM pipeline. Stage 1 uses a multimodal model to translate the diagram into a natural‑language description. Stage 2 employs an LLM with reflection prompting to produce JSON that conforms to a predefined schema, iterating until validation passes. Stage 3 maps the validated JSON to executable code via a deterministic adapter. All stages are modular and can be inspected for traceability.

## Results  
The workflow achieved high reliability for all eight queuing diagrams; performance metrics (e.g., execution‑time variance) were within statistical limits of human‑coded models, confirming equivalence. No significant errors or hallucinations were observed in the generated simulation models.

## Significance  
By decoupling visual input from code generation and embedding verification loops, Sketch2DES enhances transparency, reproducibility, and accessibility of simulation modelling for non‑programmers, offering a scalable alternative to direct LLM code generation.

## Related Concepts  
Large Language Models (LLMs), multimodal AI, discrete‑event simulation, verifiable models, schema validation, reflection in prompting, open‑weight frameworks, queuing networks, discrete‑event simulation (DES).
