# Summary: 2026-07-28_06-52-19Z_DivergenceDecoding_Training_FreeCapabilityFusion.md
Saved: 2026-07-30 23:05
Source: 2026-07-28_06-52-19Z_DivergenceDecoding_Training_FreeCapabilityFusion.md
Model: None

---

## Summary  
Large language models excel at broad reasoning but often lack specialized knowledge, while domain‑specific models suffer from reduced logic and robustness. To bridge this gap the authors propose Divergence Decoding, a training‑free framework that fuses these capabilities at inference time. The method monitors distributional disagreement using Jensen–Shannon divergence and routes control to the generalist when needed. This adaptive fusion preserves specialist expertise while injecting reasoning power from the generalist model.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Finding 1: Training‑free capability fusion is achieved by continuously measuring Jensen‑Shannon divergence between the two models at each token.  
- Finding 2: The framework implements an adaptive routing mechanism that instantly switches to the generalist when significant divergence signals a reasoning risk, thereby injecting generic reasoning without compromising domain knowledge.  
- Finding 3: Divergence Decoding outperforms both specialized and pure‑generalist baselines on multiple scientific benchmarks.

## Methodology  
The authors reconstruct the “draft‑and‑verify” skeleton of speculative decoding into an inference‑time routing system. For every token they compute Jensen‑Shannon divergence between the specialist’s probability distribution and the generalist’s, treating high divergence as a cue that the specialist may be uncertain or prone to errors. When divergence exceeds a threshold, control is transferred to the generalist, which then produces the output while the specialist continues to provide domain expertise in subsequent tokens.

## Results  
Experiments on GPQA, ChemBench, and ChemCoTBench show Divergence Decoding achieving state‑of‑the‑art performance across all tasks. It consistently exceeds both the specialist‑only and generalist‑only models and surpasses most single‑model baselines, demonstrating that the fusion approach yields superior scientific reasoning.

## Significance  
This work introduces a general, training‑free paradigm for fusing diverse LLM capabilities through adaptive inference‑time collaboration. By dynamically leveraging the strengths of both domain specialists and broad‑scope generalists, Divergence Decoding opens new possibilities for robust, high‑quality scientific AI systems without requiring costly fine‑tuning.

## Related Concepts  
- Jensen–Shannon divergence  
- Speculative decoding  
- Capability fusion  
- Adaptive routing  
- Domain vs. generalist models
