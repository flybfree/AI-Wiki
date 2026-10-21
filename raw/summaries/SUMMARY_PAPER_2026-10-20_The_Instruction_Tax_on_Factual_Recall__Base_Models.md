---
title: The Instruction Tax on Factual Recall: Base Models Can Beat Their Instruction-Tuned Counterparts
url: http://arxiv.org/abs/2610.28407v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_15-48-56Z_TheInstructionTaxonFactualRecall_BaseModelsCanBeat.md
generated_at: 2026-10-20 22:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a solution to the AKBC LM-KBC 2026 Shared Task, demonstrating that base language models can outperform their instruction-tuned counterparts on factual recall tasks. The authors achieved a score of 0.6836 on the leaderboard—more than double the baseline of 0.2964—by using a base model with text-completion prompting rather than the instruction-tuned chat interface, which only reached 0.5681. The paper identifies and names the "instruction tax," a measurable degradation in factual recall caused by instruction tuning altering model weights.

## Key Takeaways
- Instruction tuning introduces a measurable performance penalty on factual recall tasks: the instruction-tuned version of the model scored 0.5681 via its chat interface, while the base model scored 0.6836 using text-completion prompting. The authors attribute this gap to changes in the model's weights introduced during instruction tuning, not merely to differences in prompting methodology, and term this effect the "instruction tax."
- The prompting methodology is as critical as model architecture for knowledge-intensive tasks. The authors' solution involves prompting the base model with training-data examples, generating 64 to 256 candidate outputs, and retaining only those that appear repeatedly across generations. This repetition-based filtering strategy effectively distills reliable factual knowledge from the model's parametric memory without retrieval or fine-tuning.
- Task-specific post-processing strategies significantly improve performance on structured knowledge tasks. Two specialized methods were applied per relation type: one improves recall for relations with large answer sets, and another verifies a person's vitality before predicting their place of death, showing that domain-aware filtering can substantially boost accuracy on knowledge base completion benchmarks.

## Context
This work sits at the intersection of knowledge base completion research and the growing debate over whether instruction tuning genuinely improves language model capabilities or introduces trade-offs. As the field increasingly standardizes on instruction-tuned chat models for deployment, this paper provides empirical evidence that such tuning can degrade a model's ability to retrieve stored factual knowledge. The AKBC LM-KBC Shared Task serves as a controlled benchmark where model size is capped at 32 billion parameters and no external retrieval or fine-tuning is permitted, isolating the effect of the model's internal knowledge and prompting strategy.

## Implications
For practitioners deploying language models in knowledge-intensive applications such as question answering, fact-checking, or structured data generation, this research suggests that base models paired with carefully designed completion-style prompts may outperform instruction-tuned chat models, particularly when factual accuracy is paramount. Industry teams should reconsider the default assumption that instruction-tuned models are universally superior and instead evaluate whether their specific task benefits from the raw parametric knowledge preserved in base model weights. The findings also highlight that post-processing heuristics tailored to specific relation types can be as impactful as model selection, offering a practical lever for improving performance without additional training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28407v1)
