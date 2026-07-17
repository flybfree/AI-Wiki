# Summary: 2026-07-16_17-02-25Z_MM_IssueLoc_AControlledBenchmarkforEvaluatingVisua.md
Saved: 2026-07-16 21:01
Source: 2026-07-16_17-02-25Z_MM_IssueLoc_AControlledBenchmarkforEvaluatingVisua.md
Model: None

---

## Summary  
The paper introduces **MM‑IssueLoc**, a controlled benchmark designed to evaluate the impact of visual evidence in repository‑level issue localization across multimodal software repositories. It provides a dataset of 652 issue‑PR instances spanning 23 languages, annotated with seven image categories and four relevance levels, allowing researchers to isolate whether images help, hinder, or are ignored by downstream models. The authors evaluate both LLM‑based and retrieval‑based systems in two modes—text‑only and multimodal—and use VCE (Visual Evidence Conversion) diagnostics to turn images into structured textual evidence for analysis. This work moves beyond end‑to‑end repair benchmarks that entangle localization with patch synthesis, offering a clear experimental variable for future research.

## Key Contributions  
- **MM‑IssueLoc is a controlled benchmark** containing 652 issue‑PR instances across 23 languages, annotated with seven image categories and four relevance levels.  
- **It provides file‑level and function‑level gold labels** together with VCE diagnostics that convert images into structured textual evidence for systematic evaluation.  
- **The study demonstrates that visual evidence can be an explicit variable**, revealing a performance gap between text‑only localization (high on SWE) and multimodal localization.

## Methodology  
The authors constructed the dataset by pairing each repository issue with its associated PR files, which may include screenshots, error dialogs, rendered UI states, or logs. Each instance is annotated for relevance level and image type, and gold labels are supplied at both file and function granularities. Evaluation follows a split protocol: (1) text‑only retrieval that uses only the textual description of the issue, and (2) multimodal retrieval that can optionally incorporate the associated images; VCE transforms each image into a structured textual evidence vector for analysis.

## Results  
The strongest LLM‑based system achieves **38.96 % file Acc@5** and **22.45 % function Acc@10**, while the best retrieval‑based system reaches **33.86 % function Acc@10**. Cross‑benchmark comparisons show that high scores on text‑dominant SWE benchmarks do not transfer cleanly to MM‑IssueLoc; multimodal tasks are significantly more challenging, underscoring the limited benefit of visual evidence in current models.

## Significance  
MM‑IssueLoc makes it possible to test whether incorporating visual evidence actually improves repository‑level issue localization, rather than attributing gains to downstream patch‑generation effects. By treating images as an explicit evaluation variable, the benchmark enables future research to systematically explore the utility of visual cues in identifying issues within software repositories.

## Related Concepts  
- Multimodal retrieval  
- Repository‑level issue localization  
- Visual evidence (images, screenshots, logs)  
- VCE (Visual Evidence Conversion) diagnostics  
- File vs. function accuracy metrics  
- LLM‑based and retrieval‑based systems
