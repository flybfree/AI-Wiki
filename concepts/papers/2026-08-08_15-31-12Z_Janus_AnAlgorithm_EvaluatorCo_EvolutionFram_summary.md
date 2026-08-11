# Summary: 2026-08-08_15-31-12Z_Janus_AnAlgorithm_EvaluatorCo_EvolutionFrameworkfo.md
Saved: 2026-08-10 23:00
Source: 2026-08-08_15-31-12Z_Janus_AnAlgorithm_EvaluatorCo_EvolutionFrameworkfo.md
Model: None

---

## Summary  
LLM-driven program discovery is constrained by expensive, high-fidelity evaluations that are impractical for large-scale or scientific tasks. Traditional approaches rely on fixed surrogate evaluators, which suffer from distribution shift and poor calibration due to sparse, search-biased labels. Janus addresses these limitations by introducing a co-evolution framework where language models (LLMs) jointly evolve target programs and executable proxy evaluators. By integrating domain knowledge into the LLM-generated evaluator code and using real outcomes for calibration, Janus enables scalable discovery even under expensive evaluation budgets.

## Key Contributions  
- [Finding 1] Janus introduces a co-evolution framework that evolves both target programs and executable proxy evaluators in parallel, leveraging LLMs to generate task-specific evaluator programs and calibrating them using real outcomes.  
- [Finding 2] The system mitigates distribution shift by evolving evaluators alongside targets, selecting them via a promotion-aligned objective, and maintaining region-conditioned portfolios with online credit updates to preserve evaluation reliability.  
- [Finding 3] Janus uses proxy predictions only for candidate prioritization, requiring real validation before candidates enter the target population or update the incumbent, ensuring high-fidelity feedback is not compromised.

## Methodology  
Janus employs an algorithm-evaluator co-evolution framework where LLMs generate executable evaluator programs based on domain knowledge and task specifications. These evaluators are initially seeded from existing code but are refined through iterative training using real evaluation outcomes. The system maintains a portfolio of candidate programs, each associated with a region or feature space, and uses credit-based selection to promote promising candidates. Evaluators are selected via a promotion-aligned objective that rewards high accuracy in predicting real outcomes. Crucially, proxy predictions are used only for ranking and do not influence the final population; only validated candidates proceed to target evaluation.

## Results  
Across five scientific and engineering design tasks—including mechanical optimization, circuit design, and fluid dynamics modeling—Janus significantly outperformed a matched baseline that evolved only target programs. Janus achieved a larger area under the best-so-far improvement curve over the real-evaluation budget and reached 99% of the baseline’s final performance with just 59.1% fewer real evaluations. Evolved proxy evaluators also demonstrated improved accuracy in ranking candidates compared to their seed versions, indicating successful adaptation through co-evolution.

## Significance  
This work extends evaluator-guided LLM discovery from domains with cheap, scalable feedback—such as synthetic benchmarks—to high-stakes scientific fields where evaluation is costly and unreliable. By enabling trustworthy, adaptive surrogate evaluation, Janus opens the door to large-scale program discovery in engineering and science without sacrificing performance or accuracy.

## Related Concepts  
- LLM-driven discovery  
- Co-evolution of algorithms and evaluators  
- Surrogate evaluation  
- Distribution shift mitigation  
- Region-conditioned portfolios  
- Credit-based selection  
- Best-so-far improvement curve
