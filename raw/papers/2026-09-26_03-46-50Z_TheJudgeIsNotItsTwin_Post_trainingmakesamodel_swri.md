---
title: The Judge Is Not Its Twin: Post-training makes a model's writing more predictable but barely moves its taste, as a judge, toward predictable writing
published: 2026-09-26T03:46:50Z
authors: Arman Nik Khah, Arvin Bahreini
url: http://arxiv.org/abs/2609.32196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Judge Is Not Its Twin: Post-training makes a model's writing more predictable but barely moves its taste, as a judge, toward predictable writing

## Abstract
Language models are now routinely graded by other language models. If post-training makes a model's own writing more predictable, it may also teach the same model, acting as a judge, to reward predictable writing, so that progress on creativity would be invisible to automated evaluation. We follow two open model families, OLMo-2 and Zephyr (7B parameters each), through their public training stages and measure every stage twice, as a writer of short stories and as a judge of pairs of stories. As writers, the models drift as feared: each family's fully trained model finds the stories of its base, supervised fine-tuned (SFT) and preference-trained (DPO) stages progressively more familiar, in all ten prompts, and a model from the other family finds the trained stories 7.0 to 9.2 percent (OLMo-2) and 24 to 25 percent (Zephyr) less surprising per token. As judges, they barely move toward predictable writing. Asked which story is better, a question every judge can use to tell a story from its own words in scrambled order, no trained judge's estimated tilt toward the more predictable story grows by as much as one point in the probability of picking it. A post hoc one-sided 95% upper bound on that growth is 2.7 points on an average pair, about the size of the untrained OLMo-2 judge's own tilt. Asked which is more creative, no trained judge's estimate favors the predictable story more than its base's does. Training instead strengthens a preference for longer stories when the question is creativity, and for one answer slot, and it breaks "more creative" as a question: trained judges asked it no longer reliably prefer a story to its scrambled words. A follow-up could not build pairs that differ in predictability but not in quality, because the routes that made this writer's stories less predictable also broke some of them, often enough to fail a quality floor set in advance.

## Metadata
- **Published**: 2026-09-26T03:46:50Z
- **Authors**: Arman Nik Khah, Arvin Bahreini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32196v1)