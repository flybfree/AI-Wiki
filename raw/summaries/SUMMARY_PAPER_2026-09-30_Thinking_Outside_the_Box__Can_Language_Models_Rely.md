---
title: Thinking Outside the Box: Can Language Models Rely on External Guidance Selectively?
url: http://arxiv.org/abs/2609.39578v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_12-10-24Z_ThinkingOutsidetheBox_CanLanguageModelsRelyonExter.md
generated_at: 2026-09-30 22:07
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces "thinking outside the box," a capability where agents selectively rely on external guidance by accepting helpful workflows while overriding misleading or unreliable ones. Using Box^2-Bench to isolate workflow reliability, the authors find that frontier models benefit from reliable cues but fail when guidance becomes fallible. Training via counterfactual supervised fine-tuning and outcome-based reinforcement learning can instill this selective reliance, improving robustness across diverse external information sources like peer correction and memory integrity.

## Key Takeaways
- Box^2-Bench reveals that while frontier models leverage reliable workflow guidance effectively, they remain highly vulnerable to misleading instructions; training open-weight models on bad workflows with good ones reserved for evaluation demonstrates that counterfactual supervised fine-tuning significantly improves robustness against unreliable constraints, whereas outcome-based reinforcement learning shifts the model's behavior toward greater utilization of helpful workflows.
- The ability to selectively rely on external information generalizes beyond structured workflows to other forms of fallible input, including peer correction mechanisms and corrupted memory states, indicating that this selective regulation is a broad meta-cognitive skill that enhances overall agent resilience against noisy or erroneous signals.
- Selective reliance on fallible external guidance constitutes a distinct dimension of agent reliability that is not captured by standard task performance metrics alone, highlighting a critical gap in current evaluation frameworks where high accuracy may mask an inability to navigate imperfect human-designed scaffolding.

## Context
As large language models evolve into autonomous agents embedded within complex, multi-step workflows, their performance increasingly depends on external scaffolding such as tool-use pipelines and human feedback loops. However, these external components are inherently prone to errors or suboptimal designs that can constrain model execution if the agent lacks the agency to question them. This research addresses a vital need in the field by shifting focus from mere task completion to the meta-cognitive regulation of trust

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39578v1)
