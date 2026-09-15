---
title: Safety as a Constraint: Fine-Tuning a LLM Recommender to Explain Itself
published: 2026-09-12T02:28:08Z
authors: Jiashu He, Emma Yanyang Kong, JJ Tan, David Fagnan
url: http://arxiv.org/abs/2609.13657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety as a Constraint: Fine-Tuning a LLM Recommender to Explain Itself

## Abstract
Traditional recommender systems are typically trained to predict what item users will interact with next, but not why. However, offering personalized evidence for why a user might like the predicted item is an important way to enhance the service and to raise the likelihood that the user will be genuinely interested in the recommendation. This service can be delivered by integrating a frontier-model call into the member-facing pipeline, but it will add extra cost and latency. In this paper, we train a recommender LLM to generate personalized explanations for its reccomendation, based on the user's watching history at a large video streaming service. We impose two requirements on the generated explanation: it must be faithful to the elements of the shows it links, and it must be strictly non-harmful to the user. To this end, we first train two LLM-judge reward models covering three specific criteria, and propose constrained GRPO to incorporate these different criteria. On a held-out real-world testing set, our fine-tuned model improves the all-three-criteria PASS rate rises from 0.649 to 0.956 under our own judges and from 0.677 to 0.931 under an independent judge, where as the frontier generator performs similar to the untuned recommender baseline. We conduct further experiments to show that the model's language and recommendation abilities remain unchanged. Based on these results, we conclude that an LLM-based recommender can be fine-tuned on other complex tasks without compromising its original recommendation performance, thus provide insights for further agentic user interface powered by a single model.

## Metadata
- **Published**: 2026-09-12T02:28:08Z
- **Authors**: Jiashu He, Emma Yanyang Kong, JJ Tan, David Fagnan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13657v1)