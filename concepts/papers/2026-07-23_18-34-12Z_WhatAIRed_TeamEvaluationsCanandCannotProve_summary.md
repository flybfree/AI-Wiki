# Summary: 2026-07-23_18-34-12Z_WhatAIRed_TeamEvaluationsCanandCannotProve.md
Saved: 2026-07-26 21:28
Source: 2026-07-23_18-34-12Z_WhatAIRed_TeamEvaluationsCanandCannotProve.md
Model: None

---

## Summary  
The paper investigates the limits of AI red‑team evaluations, establishing a calculable “evidential ceiling” that determines how much belief can change under a fixed testing budget. It derives this boundary in closed form for the benchmark null result and shows where it separates regimes of certifiable safety from those that cannot be certified. The work emphasizes that discrimination between hypotheses—not merely attack success—drives evidential worth.

## Key Contributions  
- Derives the evidential ceiling as the largest factor by which belief can move under a fixed testing budget, expressed in closed form for the benchmark null result.  
- Shows that above a calculable harm rate, modest benchmarks certify a category to an evidentiary standard; below that rate no feasible benchmark provides the specified evidence of safety.  
- Demonstrates that discrimination between hypotheses (not just attack success) determines the evidential worth of red‑team evaluations.

## Methodology  
The authors define the evidential ceiling using hypothesis conditional elicitation rates, then derive a closed‑form expression for the null result. They apply this bound to eight evaluation suites, comparing them against the boundary and analyzing regimes where a clean sheet outweighs a single failure versus regimes where no passive benchmark of feasible size yields evidence under an independent trial structure.

## Results  
The calculated bound aligns with observed experimental regimes: current safety benchmarks are adequate for high‑frequency harm categories but are orders of magnitude short for rare, catastrophic ones. Consequently, a clean sheet is the stronger observation above the threshold, while below it no passive benchmark provides the required evidence of safety under the fixed scoring rule.

## Significance  
Providing a precise, computable boundary clarifies when red‑team evaluations can be trusted to certify safety and when they cannot, guiding researchers to state explicitly which propositions their benchmarks prove. This formalizes the discipline’s need for transparent claims rather than vague judgments.

## Related Concepts  
- Evidential ceiling  
- Harm rate  
- Hypothesis discrimination  
- Red‑team evaluation  
- Closed‑form boundary  
- Safety benchmarking  
- Adaptive/automated testing

## Related Concepts

- [[concepts/ai-safety/ai-safety-hub.md|AI Safety Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/search-retrieval/search-retrieval-hub.md|Search Retrieval Hub]]
