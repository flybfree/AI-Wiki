# Summary: 2026-08-07_08-14-46Z_BlindtothePivotalVote_AggregateIndependenceMetrics.md
Saved: 2026-08-09 20:12
Source: 2026-08-07_08-14-46Z_BlindtothePivotalVote_AggregateIndependenceMetrics.md
Model: None

---

## Summary  
The paper investigates why aggregate independence metrics fail to detect the places where a verification signal actually improves panel accuracy in Large Language Model judge panels. It shows that adding an external test‑suite signal does not change the effective vote count at scale, yet the accuracy gain from a marginal substitution rule concentrates exclusively on one‑vote‑margin queries and can increase overall performance by 6–23 percentage points across multiple benchmarks. The authors therefore argue that population‑level dependence diagnostics and margin‑stratified utility are complementary tools for designing call‑reduction policies.

## Key Contributions  
- **Finding 1:** Adding a signal from an external test suite does not alter the effective vote count of nine judges; the aggregate remains highly dependent (≈2 independent judgments) even at scale.  
- **Finding 2:** The entire accuracy improvement produced by marginal substitution is confined to pivotal queries with a one‑vote margin, where gains range from +10.4 pp to +23.3 pp depending on the headline configuration.  
- **Finding 3:** Population‑level dependence diagnostics and marginal utility are complementary; a call‑reduction rule that targets only one‑vote‑margin queries can boost accuracy while preserving independence.

## Methodology  
The authors evaluate three headline configurations (e.g., blind, majority, and signal‑augmented) on the HumanEval+/MBPP+ code benchmarks. They examine four panel sizes—including a 9‑judge extension and multiple subsampling checks—and compare two regimes: one where a verification signal is invoked for a subset of queries and another where it is omitted entirely. Accuracy gains are measured per query, stratified by margin (one‑vote vs. larger margins), and the effective vote count is computed using elementary majority arithmetic.

## Results  
Overall accuracy rises from 82.44 % to 85.62 % when a call‑reduction rule that substitutes only one‑vote‑margin queries is applied, while invoking the signal on 16.2 % of queries yields no net benefit (signal‑only remains at 87.60 %). Across three code benchmarks and four panel sizes, the total gain varies between +6.5 pp and +16.1 pp. Crucially, the entire accuracy improvement is zero for queries outside the one‑vote margin; the signal has no effect on those “non‑pivotal” decisions.

## Significance  
This work reveals a blind spot in aggregate independence metrics: they cannot identify where verification actually helps, leading to suboptimal call budgets. By pinpointing pivotal votes and offering a targeted substitution rule, the study provides a practical framework for improving LLM judge panels without sacrificing independence, thereby advancing both fairness and efficiency in automated evaluation.

## Related Concepts  
- LLM judge panels  
- Aggregation of independent judgments  
- Effective vote count  
- Majority arithmetic  
- Pivotal (one‑vote) votes  
- Substitution rules  
- Marginal utility  
- Dependence diagnostics
