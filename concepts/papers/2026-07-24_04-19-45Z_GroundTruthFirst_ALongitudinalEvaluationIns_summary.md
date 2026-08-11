# Summary: 2026-07-24_04-19-45Z_GroundTruthFirst_ALongitudinalEvaluationInstrument.md
Saved: 2026-07-26 21:34
Source: 2026-07-24_04-19-45Z_GroundTruthFirst_ALongitudinalEvaluationInstrument.md
Model: None

---

## Summary  
The paper introduces **Ground Truth First**, a longitudinal evaluation framework that inverts the conventional LLM‑memory benchmark pipeline. Instead of generating conversations first and extracting answer keys later, it creates a synthetic fact‑based corpus where facts are emitted with validity intervals, volatility classes, and source channels before any text is written. The authors then render chat and email from these manifest events, verify each planted fact, and mechanically generate questions whose gold answers are script‑valid by construction. This approach yields a fully reproducible dataset of 380 questions across 15 types that tests memory architectures over multiple weeks.

## Semantic links
- [[concepts/papers/2026-07-28_18-29-45Z_SharedSFTLessonsAcrossAlignment_ModelOrgani_summary.md|Summary: 2026-07-28_18-29-45Z_SharedSFTLessonsAcrossAlignment_ModelOrganisms_and.md]] — 4 title terms overlap; 7 summary/topic terms overlap; semantic match 0.03
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 1 backlink; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The inverted pipeline eliminates label‑error and contamination problems, producing ground‑truth answers that are simultaneously valid and answerable.  
- [Finding 2] Memory‑architecture rankings flip with history length: the budgeted curated‑map memory leads at three weeks but loses recall to 72 % at nine weeks, while a provenance‑typed graph rises to 90 %. The inversion is statistically significant (p = 0.031) across all six users under full cross‑family re‑judging.  
- [Finding 3] A layered architecture called Veracium achieves the best performance in both regimes—96.8 % short‑horizon and 90 % long‑horizon recall—making it the top model and released as an open‑source library.

## Methodology  
The authors built a **seeded life‑script sampler** that emits facts with per‑fact validity intervals, volatility classes, and source channels. An LLM renderer writes chat and email from these fact manifests, while a fidelity verifier confirms every planted fact. Questions are mechanically instantiated from the script, ensuring gold answers are script‑valid. Benchmarking five memory architectures (budgeted curated‑map, provenance‑typed graph, full‑rendered‑history baseline, etc.) against a no‑memory control (fixed answerer, versioned LLM judge) is performed over two horizons: three weeks and nine weeks.

## Results  
The benchmark shows that the budgeted curated‑map memory’s recall drops from 96 % to 72 % after nine weeks, indicating severe eviction of evicted content. The provenance‑typed graph improves to 90 % recall at the long horizon. The full‑rendered‑history baseline ties or exceeds the best short‑horizon system but shows no judge‑independent advantage at nine weeks, costing roughly twice the read time. Write‑stage quality correlates weakly with downstream quality: poorly written facts fail 24 % of the time versus only 2 % for well‑written ones. Injection resistance is measured by how often provenance boundaries survive representation.

## Significance  
Ground Truth First provides a reliable, longitudinal benchmark that exposes hidden biases and dynamic performance changes in LLM memory systems, enabling fair ranking across different horizons. By eliminating label contamination and offering an open‑source toolkit (Veracium), the work advances both research methodology and practitioner tools for evaluating agent memory.

## Related Concepts  
Ground Truth First pipeline, synthetic fact corpus, per‑fact validity intervals, trust distinctions, provenance‑typed graph, layered architecture, memory degradation over time, injection resistance, read cost vs. quality tradeoff.
