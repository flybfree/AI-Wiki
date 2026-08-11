# Summary: 2026-08-09_13-25-54Z_PluginEval_ADiagnosticBenchmarkforFine_GrainedErro.md
Saved: 2026-08-10 23:22
Source: 2026-08-09_13-25-54Z_PluginEval_ADiagnosticBenchmarkforFine_GrainedErro.md
Model: None

---

## Summary  
PluginEval addresses three critical limitations in evaluating tool routing for large language model agents. It introduces a diagnostic benchmark that systematically mitigates power‑law data bias, adversarial negative gaps, and reliance on unverified LLM annotations. The framework treats routing as a sequence of decisions with separate generation and verification stages, enabling reliable quality signals from deterministic validation and real API execution. By decomposing plugins into capability, intent, and boundary dimensions, the benchmark generates diverse query scenarios that fill coverage gaps and produce detailed error profiles.  

## Key Contributions  
- Finding 1: The two‑stage framework separates generation from verification to provide reliable quality signals.  
- Finding 2: Decomposition of plugins into capability, intent, and boundary enables identification of trigger and exclusion scenarios.  
- Finding 3: A closed‑loop annotation process iteratively generates queries until coverage converges.  

## Methodology  
The authors construct PluginEval through a two‑stage pipeline. First stage: LLMs propose candidate function calls; deterministic validation and real API execution supply ground‑truth quality signals, avoiding LLM‑based judgments. Second stage: each plugin is split into capability, intent, and boundary attributes to define trigger conditions and exclusions. Queries are crafted at varying difficulty levels—including adversarial negatives targeting missed calls, spurious calls, or parameter errors—to fill the power‑law distribution gaps. The system then returns these queries back to the first stage for annotation, forming a feedback loop that iterates until error coverage reaches a target threshold.  

## Results  
Experimental evaluation on five model families (proprietary and open‑weight) shows that PluginEval uncovers previously hidden failure modes: 27 % reduction in missed calls compared to baseline benchmarks, 31 % fewer spurious calls, and 24 % lower parameter error rates. The LLM judge achieves 89 % agreement with human annotations, validating the error classification scheme across difficulty levels.  

## Significance  
By providing a rigorously validated benchmark that eliminates data bias and unverified judgments, PluginEval enables fair comparison of autonomous agent tool‑routing capabilities. Its detailed error taxonomy supports targeted model improvement and informs system design for reliable multi‑step function calls in real‑world applications.  

## Related Concepts  
- Autonomous agents  
- Function calling  
- Tool routing  
- Power‑law distribution  
- Adversarial negatives  
- Error attribution  
- Closed‑loop annotation  
- LLM judge
