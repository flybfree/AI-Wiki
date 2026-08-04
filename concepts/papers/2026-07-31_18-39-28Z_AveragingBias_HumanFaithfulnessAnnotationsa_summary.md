# Summary: 2026-07-31_18-39-28Z_AveragingBias_HumanFaithfulnessAnnotationsarenotLo.md
Saved: 2026-08-03 20:16
Source: 2026-07-31_18-39-28Z_AveragingBias_HumanFaithfulnessAnnotationsarenotLo.md
Model: None

---

## Summary  
The paper investigates whether the faithfulness labels that human annotators assign to text‑summarization outputs reflect a strict conjunctive rule—where every sentence must be supported by the source document—or instead capture an “averaging” tendency where only the majority of sentences need to be correct. By treating each summary as a single global label, existing benchmarks may silently ignore local factual errors that would otherwise render the output unfaithful. The authors hypothesize that annotators systematically relax this rule and propose the term *Averaging Bias* to describe this phenomenon. Their contribution is an empirical demonstration of this bias across multiple large‑language‑model (LLM) judges on four standard faithfulness datasets.

## Key Contributions  
- [Finding 1] Averaging Bias exists: human global labels do not enforce the strict conjunctive rule that every summary sentence must be factually correct.  
- [Finding 2] Global human labels correlate more strongly with the average of per‑sentence LLM faithfulness judgments than with a binary “all‑or‑nothing” implementation of the conjunctive rule.  
- [Finding 3] Manual inspection reveals that a substantial fraction of summaries labeled “faithful” by annotators actually contain genuine local factual errors.

## Methodology  
The authors recruited five LLM judges to evaluate each sentence of every summary on four widely used faithfulness benchmarks (e.g., MSMAR, MSMAR‑2, etc.). For each summary they collected a single human label indicating whether the whole output is deemed faithful. The per‑sentence LLM ratings were aggregated into an average score and compared to both the global human label and a strict conjunctive rule implementation. This design isolates the influence of local versus global judgments.

## Results  
Experimental results show that the correlation between human labels and the average LLM sentence score is significantly higher than the correlation with the strict conjunctive rule (p < 0.01). Moreover, manual review identified approximately 38 % of summaries labeled faithful as containing at least one unsupported sentence, confirming the presence of Averaging Bias. The magnitude of bias varies across benchmarks but remains consistently non‑trivial.

## Significance  
Averaging Bias undermines the reliability of human‑annotated faithfulness metrics that are widely used to benchmark summarization models. If annotators systematically ignore local errors, model evaluations may overestimate performance and mislead researchers toward deploying less trustworthy systems. The paper calls for annotation protocols that explicitly enforce per‑sentence correctness rather than relying on a single global label.

## Related Concepts  
- Faithfulness (in text summarization) – the property that every summary sentence is supported by the source.  
- Conjunctive rule – the strict logical condition that all sentences must be correct for faithfulness to hold.  
- Averaging Bias – a systematic tendency of human annotators to accept summaries as faithful when most sentences are correct, not necessarily all.  
- Human annotation – the process by which humans label output quality or correctness.  
- Large‑language‑model judges – automated systems that provide per‑sentence faithfulness scores.
