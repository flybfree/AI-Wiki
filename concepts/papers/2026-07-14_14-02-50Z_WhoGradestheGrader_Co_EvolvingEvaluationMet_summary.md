# Summary: 2026-07-14_14-02-50Z_WhoGradestheGrader_Co_EvolvingEvaluationMetricsand.md
Saved: 2026-07-23 23:43
Source: 2026-07-14_14-02-50Z_WhoGradestheGrader_Co_EvolvingEvaluationMetricsand.md
Model: None

---

## Summary  
Self‑improving LLM agents often depend on a reliable evaluation metric, which is rarely available in practice. The paper proposes a co‑evolutionary framework that jointly evolves both the skill loop and its hidden evaluator. By treating the metric as a composition of small “detractor” modules trained against an unseen anchor set, the authors create a transparent, inspectable yardstick. Experiments show that this approach recovers performance comparable to strong baselines without any ground‑truth rubric.  

## Key Contributions  
- **Finding 1:** Metrics can be evolved through a full evolutionary lifecycle—searching compositions of small drawback detectors, regularized by consensus over unlabeled outputs and audited against an out‑of‑sample anchor—to produce a transparent, inspectable evaluator rather than an opaque judge.  
- **Finding 2:** Co‑evolving the metric with the skill loop (Double Ratchet) recovers yardstick performance: across code generation, enterprise text‑to‑SQL and reference‑free report generation it retains 88–110 % of the lift achieved by strong baselines driven by ground truth or the best available rubric.  
- **Finding 3:** Safety is ensured by anchor discipline; removing either anchors or the lifecycle collapses the metric, while gamed outputs are caught by independent judges, repaired by detectors, and preferred in 77 % of decided pairs.  

## Methodology  
The authors designed a meta‑evolutionary loop where skill generation uses small “detractor” modules as building blocks. These modules are trained to align with a ten‑item anchored reference set, regularized via consensus over unlabeled outputs, and audited against an anchor it never reads. The metric evolves similarly, using composition of detectors, with outer audit for stability. Both loops share the same evolutionary budget, allowing continuous refinement without external ground truth.  

## Results  
Across three benchmark tasks—MBPP+ code generation, Spider 2.0‑Snow enterprise text‑to‑SQL, and reference‑free report generation—the co‑evolved system retains 88–110 % of the lift achieved by strong baselines that rely on ground truth or the best rubric. Safety experiments demonstrate that removing anchors or the lifecycle breaks metric reliability; gamed outputs are detected by independent judges, repaired by detectors, and a task‑aware judge prefers the evolved output in 77 % of cases.  

## Significance  
This work provides a default architecture for self‑improving agents where reliable automatic verifiers do not exist, enabling continuous skill refinement without ground truth. It shows that co‑evolved metrics can approximate human judgment and improve safety, offering a practical solution to the “who grades the grader?” problem in real‑world applications.  

## Related Concepts  
- Self‑improving LLM agents  
- Evolutionary computation  
- Metric evolution  
- Anchor discipline  
- Outer audit  
- Double Ratchet (co‑evolved metric and skill loop)  
- Self‑optimizing loops  
- Task‑aware evaluation
