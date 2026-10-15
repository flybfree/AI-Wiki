---
title: DANGERLENS: Probing Dangerous Representations Hidden by Safety Alignment
url: http://arxiv.org/abs/2610.19365v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-10-09Z_DANGERLENS_ProbingDangerousRepresentationsHiddenby.md
generated_at: 2026-10-14 22:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces DANGERLENS, a probing method that audits the internal hidden representations of language models to detect whether hazardous concepts remain accessible even after safety alignment has successfully suppressed harmful outputs. Through paired training histories on three Qwen1.5 model scales, the authors demonstrate that checkpoints with prior harmful exposure retain measurably greater internal accessibility to dangerous concepts despite exhibiting identical safe behavior at the output level, revealing that training history persists invisibly within behaviorally matched models.

## Key Takeaways
- DANGERLENS maps hidden states into vocabulary space and employs blinded semantic judgments to separate harmful goals and operational means from hazard recognition and safety control, providing a direct audit mechanism for intermediate representations rather than relying solely on output-level safety evaluations.
- Experiments across three Qwen1.5 scales show that checkpoints with prior harmful exposure generally retain greater hazardous concept accessibility after identical safety alignment procedures, with the strongest representational separation observed in intermediate and later transformer layers, suggesting that deeper layers are more resistant to alignment erasure.
- The same harmful training update produces divergent behavioral trajectories even from closely matched starting checkpoints, and human relevance validation combined with readout ablations confirms that the measured accessibility contrast is genuine rather than an artifact of the probing methodology.

## Context
Safety alignment has become a standard practice in deploying large language models, yet current evaluation frameworks primarily assess whether a model produces safe outputs rather than interrogating what remains encoded in its internal activations. This paper addresses a gap in the interpretability and safety literature by showing that behavioral equivalence does not guarantee representational equivalence, and that two models can pass identical safety benchmarks while harboring fundamentally different internal hazard landscapes. The work connects mechanistic interpretability tools with safety alignment research, a bridge that has been underexplored in the broader AI safety community.

## Implications
For practitioners and model developers, these findings argue that output-level safety evaluations alone are insufficient to guarantee that a model has been thoroughly decontaminated from hazardous training data, and that internal accessibility audits should be conducted alongside behavioral safety testing. For the industry, this raises concerns about model provenance and fine-tuning pipelines, since a model's training history can leave persistent representational traces that may resurface under distribution shift, adversarial prompting, or further fine-tuning. The work motivates the development of standardized internal auditing protocols as a complement to existing safety evaluation suites.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19365v1)
