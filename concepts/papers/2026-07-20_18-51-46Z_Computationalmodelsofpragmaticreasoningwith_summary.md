# Summary: 2026-07-20_18-51-46Z_Computationalmodelsofpragmaticreasoningwithflexibl.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_18-51-46Z_Computationalmodelsofpragmaticreasoningwithflexibl.md
Model: None

---

## Summary  
The paper proposes a computational framework called ScAffolded Generative models for Explanation (SAGE) that integrates the generative power of large‑language models (LMs) with the transparent, rule‑based analysis typical of cognitive models of pragmatics. SAGE treats pragmatic reasoning as a three‑stage process: proposers generate an open space of alternative expressions or interpretations; evaluators rank those alternatives according to semantic plausibility, complexity, and typicality; selectors then apply cognitively motivated rules to produce the final output. The authors test this architecture on three case studies involving M‑implicatures and Gricean conversational implicatures. Their work demonstrates that neuro‑symbolic models can capture both the flexibility of language generation and the systematic reasoning required for pragmatic inference.

## Key Contributions  
- [Finding 1] SAGE provides a unified framework that couples LM‑driven alternative generation with cognitive evaluation modules, enabling transparent yet flexible modeling of pragmatic processes.  
- [Finding 2] The model’s proposers reliably produce alternatives suitable for pragmatic reasoning, whereas its evaluators excel at intuitive judgments rather than formal theoretical metrics.  
- [Finding 3] Across experimental tasks, SAGE models achieve high accuracy and often surpass conventional baselines that rely solely on rule‑based or handcrafted generators.

## Methodology  
SAGE decomposes a pragmatic task into three modules: proposers use state‑of‑the‑art language generation to output a diverse set of candidate alternatives; evaluators apply heuristic criteria (e.g., semantic coherence, typicality) and optionally formal measures to rank these candidates; selectors execute rule‑based steps derived from cognitive task analyses. The composition of these modules is parameterized so that the LM’s generative strength is balanced with the rigor of symbolic reasoning.

## Results  
Empirical evaluations across M‑implicature and Gricean implicature tasks show that SAGE models consistently achieve higher performance than baseline systems, including rule‑only generators and standard LLM inference pipelines. Ablation studies reveal an asymmetry: LM proposers generate high‑quality alternatives, while LM evaluators provide intuitive scores rather than precise theoretical judgments, suggesting a complementary role for each component.

## Significance  
This work advances neuro‑symbolic AI by offering a concrete model that bridges the gap between flexible language generation and systematic cognitive reasoning. By demonstrating that such hybrid architectures can outperform purely symbolic or purely generative approaches, SAGE contributes to both theoretical understanding of pragmatic language use and practical applications in conversational agents.

## Related Concepts  
pragmatic reasoning, alternative expressions, implicatures (M‑implicatures, Gricean), neuro‑symbolic modeling, large‑language models, cognitive task analysis, rule‑based selection, semantic plausibility, typicality.
