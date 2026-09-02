---
title: Measuring consistency via ensemble margin and local prediction variability: Auditing decision systems in the presence of predictive multiplicity
url: http://arxiv.org/abs/2609.01397v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-22-01Z_Measuringconsistencyviaensemblemarginandlocalpredi.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a consistency criterion that combines the ensemble margin with local prediction variability to audit decision systems affected by the Rashomon effect. It demonstrates that finite ensembles of models from the Rashomon set converge to the expected model's score as their size and sample counts increase, thereby reducing undetected errors while incurring only a modest rise in diversions.

## Key Takeaways
- Finite ensembles of models from the Rashomon set approximate full‑set auditing with negligible risk.  
- Consistency scores converge to those of the expected model as ensemble size and sample count increase.  
- The criterion outperforms existing consistency measures in capturing predictive multiplicity.

## Context
In artificial intelligence, decision systems often rely on ensembles that may generate conflicting predictions due to multiplicities among constituent models. Traditional auditing focuses on individual models, which can miss systematic errors introduced by the Rashomon effect. This work fills a gap by providing a principled metric for ensemble reliability in complex settings.

## Implications
Practitioners can deploy lightweight auditing pipelines that balance false positives and negatives, enhancing trust in high‑stakes applications such as natural language understanding and tabular classification. The method offers scalable oversight without requiring heavy computational resources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01397v1)
