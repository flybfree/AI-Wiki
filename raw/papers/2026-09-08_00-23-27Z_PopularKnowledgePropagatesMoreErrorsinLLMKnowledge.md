---
title: Popular Knowledge Propagates More Errors in LLM Knowledge Updating
published: 2026-09-08T00:23:27Z
authors: Yuji Zhang, Weibing Wang, Cheng Qian, Duo Zhou, Dilek Hakkani-Tür, Kathleen McKeown, Chengxiang Zhai, Heng Ji
url: http://arxiv.org/abs/2609.08067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Popular Knowledge Propagates More Errors in LLM Knowledge Updating

## Abstract
Updating a language model's knowledge through fine-tuning is essential for keeping its outputs current, yet can also induce factual forgetting and new hallucinations. Prior work shows that long-tail knowledge is harder to acquire and newly memorized long-tail facts are difficult to retain during later fine-tuning. We study a complementary question: among facts that a model has encoded correctly, which are most vulnerable to collateral corruption during other updates? To investigate this question under a realistic factual distribution, we construct a large-scale graph FACTPROP of verified Wikipedia facts by linking triples that share head or tail entities, thereby preserving connections among factual knowledge. We fine-tune models on factual statements and measure correct-to-incorrect facts after each update. Our results reveal a pattern distinct from prior findings on long-tail vulnerability during acquisition and retention: among facts that models already answer correctly, those associated with highly connected entities are more likely to be corrupted by neighboring updates, and updates to such facts propagate errors more broadly. Structural popularity therefore predicts both vulnerability and downstream damage. Inspired by this finding, we propose Popularity-based Anchoring (PopAnchor), a lightweight rehearsal strategy that preserves a small set of popular facts and reduces forgetting.

## Metadata
- **Published**: 2026-09-08T00:23:27Z
- **Authors**: Yuji Zhang, Weibing Wang, Cheng Qian, Duo Zhou, Dilek Hakkani-Tür, Kathleen McKeown, Chengxiang Zhai, Heng Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08067v1)