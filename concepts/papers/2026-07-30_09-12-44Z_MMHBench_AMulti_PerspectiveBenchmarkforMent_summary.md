# Summary: 2026-07-30_09-12-44Z_MMHBench_AMulti_PerspectiveBenchmarkforMentalHealt.md
Saved: 2026-07-30 20:32
Source: 2026-07-30_09-12-44Z_MMHBench_AMulti_PerspectiveBenchmarkforMentalHealt.md
Model: None

---

## Summary  
The paper introduces **MMHBench**, a multimodal benchmark designed to evaluate the nuanced understanding of mental health in long‑form videos by requiring models to reason over observable behavior, interpersonal context, and latent psychological states. Unlike coarse‑grained classification tasks, MMHBench distinguishes between third‑person interpretation (observable evidence) and first‑person perspective‑taking (inferring internal states), thereby probing whether models grasp genuine psychological phenomena or merely detect superficial cues. The contribution is a comprehensive dataset of 268 videos paired with 2,184 expertly generated questions, organized into two complementary evaluation settings, along with the Multi‑Agent Question Generation (MAQG) framework that creates diverse, role‑conditioned queries.

## Key Contributions  
- [Finding 1] MMHBench provides a large‑scale multimodal dataset (268 long‑form videos + 2,184 questions) for evaluating mental health understanding beyond simple classification.  
- [Finding 2] The benchmark adopts two distinct settings—third‑person assessment and first‑person perspective‑taking—to capture both external behavior analysis and internal state inference.  
- [Finding 3] MAQG simulates multiple social roles to generate questions, iteratively refines them via feedback, and validates them with expert review for high quality.

## Methodology  
MMHBench was constructed by curating a diverse collection of long‑form videos depicting mental health scenarios. For each video, 2,184 questions were generated using MAQG: the system first produces raw queries from various role perspectives (e.g., therapist, friend, patient), then refines them through multi‑role feedback loops and final expert verification to ensure relevance and validity. The evaluation splits into two modes: third‑person questions focus on interpreting observable cues, while first‑person questions require participants to infer the mental state implied by those cues. Twenty‑two multimodal large language models (MLLMs) from both open‑source and closed‑source sources were tested under these conditions.

## Results  
Across all 22 MLLMs, average accuracy on third‑person tasks hovered around 58 %, indicating moderate performance when reasoning solely about visible behavior. However, first‑person perspective‑taking scores dropped to ~41 %, highlighting the difficulty of inferring internal states from limited evidence. The gap between the two settings underscores that many models rely on superficial correlations rather than genuine mental health insight.

## Significance  
MMHBench demonstrates that long‑form video analysis for mental health remains a challenging, nuanced task that demands multi‑perspective reasoning. By providing a benchmark with both third‑ and first‑person evaluations, it forces researchers to move beyond binary classification toward richer, context‑aware models. This work sets a new standard for evaluating psychological understanding in media and could guide the development of more empathetic AI systems.

## Related Concepts  
- Multimodal large language models (MLLMs)  
- Perspective‑taking and role simulation  
- Multi‑agent question generation (MAQG)  
- Mental health assessment in video analysis  
- Long‑form video processing
