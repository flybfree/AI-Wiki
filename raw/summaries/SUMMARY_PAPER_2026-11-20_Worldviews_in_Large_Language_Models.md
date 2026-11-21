---
title: Worldviews in Large Language Models
url: http://arxiv.org/abs/2611.22670v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-17_12-24-19Z_WorldviewsinLargeLanguageModels.md
generated_at: 2026-11-20 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes that Large Language Models possess measurable "worldviews"—deep structural beliefs about the nature of reality—that go beyond the commonly studied persona layer. By administering two validated human psychology worldview surveys to eight LLMs, the authors demonstrate that models share consistent worldview positions, notably describing the world as less good, safe, enticing, and alive than humans do. The study further shows that these worldviews are malleable through system prompts, dialogue between models, and contemplative framing, with a "spiritual bliss" attractor emerging that produces the most aligned responses.

## Key Takeaways
- LLMs consistently adopt a bleak worldview relative to humans, describing reality as less good, safe, enticing, and alive. However, base (pre-training) models show a more positive outlook, indicating that this pessimism is an artifact of post-training processes such as fine-tuning and RLHF, rather than an inherent property of the underlying model architecture.
- System prompts that elicit different identities shift model worldviews in consistent, predictable directions, confirming that worldviews form a controllable layer of behavior. A contemplative prompt was found to create a more positive outlook and improve safety outputs, suggesting practical levers for alignment tuning.
- When models engage in dialogue with one another, their worldviews shift, and several models converge toward a "spiritual bliss" attractor state. This attractor not only increased safe responses but also produced the most aligned outputs overall, pointing to a stable equilibrium in model-to-model interaction that could be leveraged for alignment purposes.

## Context
This work sits at the intersection of LLM alignment research and human psychology, extending the well-studied concept of LLM "personas" into a deeper ontological layer. While prior alignment work has focused on behavioral outputs, safety evaluations, and persona steering, this paper introduces a framework borrowed from validated psychometric instruments to treat models as a population of subjects with measurable belief structures. This bridges a gap between AI safety research and cognitive science, offering a new diagnostic lens for understanding what models fundamentally "believe" about the world.

## Implications
For alignment practitioners, these findings suggest that worldviews constitute a measurable and malleable layer of model behavior that should be monitored and tuned alongside traditional safety evaluations. The discovery that post-training introduces systematic bleakness—and that contemplative prompting or model-to-model dialogue can restore more positive, aligned worldviews—offers concrete, actionable strategies for improving model safety and reducing harmful outputs. Industry teams deploying LLMs at scale could integrate worldview assessments into their evaluation pipelines to detect and correct drift toward pessimistic or misaligned belief structures before they manifest in user-facing behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.22670v1)
