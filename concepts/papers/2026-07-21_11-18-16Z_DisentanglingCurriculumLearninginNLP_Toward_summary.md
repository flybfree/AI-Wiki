# Summary: 2026-07-21_11-18-16Z_DisentanglingCurriculumLearninginNLP_TowardsaUnify.md
Saved: 2026-07-24 00:44
Source: 2026-07-21_11-18-16Z_DisentanglingCurriculumLearninginNLP_TowardsaUnify.md
Model: None

---

## Summary  
The paper seeks to create a taxonomy that separates difficulty evaluation from training scheduling in curriculum learning for NLP, providing formal definitions and enabling systematic comparison across studies. It distinguishes two dimensions of difficulty—attribution source (what makes an instance hard) and task dependence (how hard the task is intrinsically)—and introduces a formal model of CL schedulers based on expected training contribution, retention regimes, and monotonicity constraints.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 4 title terms overlap; 121 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Founding a fine‑grained taxonomy that separates difficulty evaluation from training scheduling in NLP curriculum learning.  
- Introducing a formal definition of CL schedulers expressed through expected training contribution, retention regimes, and monotonicity properties.  
- Demonstrating systematic incomparability among prior NLP CL works because they conflate distinct notions of difficulty and scheduling.

## Methodology  
The authors performed a comprehensive literature analysis, categorising each study according to its chosen difficulty function (attribution‑source vs task‑dependence) and its scheduler implementation (defined by expected contribution). They introduced retention regimes that track model performance after the curriculum stops, and formalised monotonicity constraints that require the training contribution to be non‑decreasing. This taxonomy allows researchers to map their experiments onto a common framework.

## Results  
The taxonomy reveals that many earlier NLP CL papers use identical labels for different difficulty functions or schedulers, leading to incomparable results. When studies align with the taxonomy—using consistent attribution sources and monotonic schedulers—the retention‑based approach consistently yields higher performance than non‑monotonic alternatives. The study also shows that aligning definitions improves reproducibility across experiments.

## Significance  
By disentangling these concepts, the taxonomy provides a unifying framework for curriculum learning research in NLP, guiding future work and evaluation practices toward clearer, comparable studies.

## Related Concepts  
Curriculum Learning, difficulty function, training scheduler, expected contribution, retention regime, monotonicity, attribution source, task dependence.
