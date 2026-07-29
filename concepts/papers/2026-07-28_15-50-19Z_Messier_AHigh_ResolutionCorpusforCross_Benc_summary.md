# Summary: 2026-07-28_15-50-19Z_Messier_AHigh_ResolutionCorpusforCross_BenchmarkAg.md
Saved: 2026-07-28 22:55
Source: 2026-07-28_15-50-19Z_Messier_AHigh_ResolutionCorpusforCross_BenchmarkAg.md
Model: None

---

## Summary  
The paper introduces Messier, a high‑resolution corpus that unifies scores from many benchmarks to enable fair cross‑benchmark evaluation of AI agents. By standardizing each record with model, scaffold, environment, task, verifier and aggregation rule, the authors create a scalable dataset for analyzing progress across domains and occupations. The study also reveals uneven advancement in different benchmark types and shows that strict all‑pass scoring can mask real improvements. Consequently, Messier provides a reusable infrastructure for capability scaling, audit of benchmarks, and fine‑grained failure analysis.  

## Key Contributions  
- [Finding 1] The creation of a unified corpus containing 957,253 records across 30 benchmarks, 714 agents, 11,891 tasks, and 74,205 verifiers.  
- [Finding 2] Identification that frontier progress is uneven: function calling saturated, programming improving fastest, enterprise workflows most challenging.  
- [Finding 3] Demonstration that strict all‑pass aggregation in multi‑verifier tasks can obscure progress and alter rankings.  

## Methodology  
The authors compiled existing benchmark scores and added five‑agent runs across six underrepresented domains (including a legal benchmark). Each record is tagged with standardized metadata: model, scaffold, environment, task, verifier, aggregation rule, SOC/NAICS classifications. They then aggregated results using various rules to produce comparable capability scales that align with Epoch’s Evaluation Capability Index.  

## Results  
The corpus reveals three main trends: function‑calling tasks plateaued at ~85% of top‑model performance; programming benchmarks show ~12% relative improvement per iteration; enterprise workflows lag ~30% behind. Counterfactual rescoring shows that all‑pass aggregation inflates scores by up to 7% in multi‑verifier settings, while selective aggregation aligns more closely with human judgments.  

## Significance  
Messier addresses the fragmentation of AI evaluation, offering a common ground for comparing agents across diverse tasks and industries. Its standardized data enables systematic tracking of capability growth, helps identify overfitting or scoring bias, and supports targeted interventions in under‑performing domains such as enterprise workflows.  

## Related Concepts  
- Benchmark aggregation  
- Capability scaling index  
- Verifier consistency  
- Counterfactual rescoring  
- SOC/NAICS classification
