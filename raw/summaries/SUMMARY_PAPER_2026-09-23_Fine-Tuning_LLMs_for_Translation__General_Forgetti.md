---
title: Fine-Tuning LLMs for Translation: General Forgetting Mitigation Does Not Preserve MT-Specific Instruction Following
url: http://arxiv.org/abs/2609.28395v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_17-02-59Z_Fine_TuningLLMsforTranslation_GeneralForgettingMit.md
generated_at: 2026-09-23 22:08
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates whether common techniques used to mitigate catastrophic forgetting during large language model (LLM) fine-tuning also preserve machine translation (MT) specific instruction following, such as controlling for formality and length. The study reveals that while certain methods may preserve general knowledge better than standard fine-tuning, they often fail to maintain the nuanced control required for high-quality, instruction-driven translations in specialized domains like Arabic or Spanish.

## Key Takeaways
- Evaluation of Mitigation Strategies: The authors compare three distinct types of mitigation strategies—those anchored to auxiliary data, those based on model outputs, and those targeting base model parameters—to determine how they affect the trade-off between general knowledge retention and task-specific performance.
- Performance of Elastic Weight Consolidation (EWC): The study found that EWC is highly effective at preserving a model's general capabilities compared to standard fine-tuning; however, it does not necessarily preserve MT-specific instruction following as effectively as other methods might in specific contexts.
- Limitations of Data Mixing: While data mixing with control-task examples was identified as the only method capable of preserving specific controls like grammatical gender and formality, these improvements did not generalize to unseen prompts for those same tasks, highlighting a significant hurdle in model generalization.

## Context
As LLMs become more prevalent in translation workflows, researchers have struggled with "catastrophic forgetting," where models lose general reasoning abilities after being fine-tuned on specific datasets. This paper is significant because it highlights that the metrics used to evaluate these mitigation strategies (general benchmarks) may not be sufficient for ensuring high-quality, controllable machine translation outputs.

## Implications
For practitioners and researchers, this study suggests that standard weight-based preservation techniques are insufficient for maintaining complex control over translation output. Developers must prioritize specific data mixing strategies while recognizing the difficulty of generalizing those controls to new prompts, indicating a need for more sophisticated training regimes in specialized domains like machine translation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.28395v1)
