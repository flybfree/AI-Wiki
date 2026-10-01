---
title: How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text
url: http://arxiv.org/abs/2609.40295v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_17-50-22Z_HowMuchIsanAITokenWorth_ScalingLawsforWildAI_Gener.md
generated_at: 2026-09-30 22:15
model: qwen3.6-35b-a3b
---

## Summary
This study investigates the impact of "wild" AI-generated web text on language model pretraining by pretraining 800 models with varying ratios of AI to human tokens. The authors find that while small amounts of AI tokens can initially benefit data-starved models, increasing AI content quickly reverses this effect into harm for human-text targets, a phenomenon existing scaling laws fail to capture. They propose a new scaling law that accounts for separate benefit and harm terms, accurately predicting performance degradation as AI token ratios rise.

## Key Takeaways
- Web data is rapidly becoming dominated by AI-generated content, with Pangram labeling nearly 28% of June 2026 tokens as AI and rising to over 31% by August; unlike synthetic datasets, this "wild" text originates from diverse models intended for human readers and arrives unlabeled in pretraining corpora.
- Pretraining experiments reveal a non-monotonic relationship where adding AI tokens initially lowers loss on human text for data-starved models but saturates and rapidly reverses into harm as the ratio increases; conversely, for models with high human-text budgets, any addition of AI tokens immediately raises loss compared to fresh human tokens.
- The authors introduce a new scaling law incorporating distinct benefit and harm terms that reduces prediction error by 41% over existing laws for models up to 3.6x larger, recommending AI text filtering when targeting human performance, repeating human data before adding AI web text, and reporting validation losses separately for human and AI domains.

## Context
As large language models consume increasingly vast amounts of internet data, the contamination of pretraining corpora with AI-generated text poses a significant risk to model quality and generalization. This research addresses the gap in understanding how unlabeled, heterogeneous AI text from the wild affects training dynamics compared to controlled synthetic data scenarios, challenging assumptions about data scaling laws like Chinchilla.

## Implications
Practitioners must

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40295v1)
