---
title: Attributes Should Come from Images, Not Class Names: Distribution-Conditioned Attribute Selection for Vision-Language Models
published: 2026-07-21T04:34:24Z
authors: Gautam Rajendrakumar Gare, Jia Shi, Zhiqiu Lin, Deepak Pathak, John Galeotti, Deva Ramanan
url: http://arxiv.org/abs/2607.18695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Attributes Should Come from Images, Not Class Names: Distribution-Conditioned Attribute Selection for Vision-Language Models

## Abstract
A popular route to interpretable zero-shot classification asks a large language model (LLM) to describe each class name and prompts CLIP with the resulting descriptors. We show that these descriptors carry little visual evidence of their own: removing the class name from the prompt collapses ImageNet accuracy from 59.5% to 15.5%. The diagnosis is that the descriptors are conditioned on the label rather than on the images, so they describe the concept in general and mislead exactly when the data shifts; an LLM insists that strawberries are red, but every strawberry in ImageNet-Sketch is a colorless line drawing. We therefore select attributes from the target image collection instead: we score a large attribute pool against the images in CLIP's joint embedding space and keep the top-scoring attributes per class. Selected this way, class-name-free attribute prompts reach 23.8% on ImageNet (against 15.5% for LLM descriptors), the gain holds on four shifted ImageNet variants, and reselecting from the LLM's own pool isolates the selection mechanism as the cause. With one image per class, the selected attributes outperform the prompt-tuning method CoOp by 3 points while fitting in under a minute instead of 14 hours, with no learned soft prompt to obscure the decision. Because the attribute set is chosen by the data, it doubles as a readable summary of a dataset, which we use to describe distribution shift in words.

## Metadata
- **Published**: 2026-07-21T04:34:24Z
- **Authors**: Gautam Rajendrakumar Gare, Jia Shi, Zhiqiu Lin, Deepak Pathak, John Galeotti, Deva Ramanan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18695v1)