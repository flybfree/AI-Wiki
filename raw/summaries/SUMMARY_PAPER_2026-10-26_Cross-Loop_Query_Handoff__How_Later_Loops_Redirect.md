---
title: Cross-Loop Query Handoff: How Later Loops Redirect Two-Hop Retrieval in the Ouro Looped Language Models
url: http://arxiv.org/abs/2610.34639v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_23-46-03Z_Cross_LoopQueryHandoff_HowLaterLoopsRedirectTwo_Ho.md
generated_at: 2026-10-26 23:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how later loops in pretrained looped language models (Ouro-1.4B and Ouro-2.6B) repair two-hop retrieval failures that occur in earlier loops. By transplanting attention queries between loops at identical layer, head, and prompt positions, the authors demonstrate that a layer-indexed collection of loop-3 queries can rescue the vast majority of questions that loop 1 answers incorrectly but loop 3 answers correctly, identifying a transferable query mechanism that supports bridge-conditioned retrieval on synthetic multi-hop questions.

## Key Takeaways
- Injecting the full layer-indexed collection of loop-3 queries into loop 1 rescues 90% of questions in Ouro-1.4B and 97% in Ouro-2.6B that were incorrectly answered at loop 1 but correctly answered at loop 3, compared to only 24% and 21% rescue rates when using shuffled donor queries, demonstrating that the specific query vectors—not merely any attention pattern—carry the retrieval repair signal.
- Crossed donor-recipient swaps reveal that the mechanism favors retrieval through the donor's bridge entity rather than simply copying the donor's final answer, though a substantial positional component persists in Ouro-2.6B; meanwhile, transplanting late keys and values rescues far fewer targets, and freezing queries at their loop-1 values damages two-hop accuracy more than a matched control question that supplies the bridge entity directly.
- On natural (non-synthetic) questions, the rescue effect is substantially smaller and replicates only in the larger Ouro-2.6B model, and crossed swaps fail to establish bridge redirection, indicating that the identified mechanism is specific to controlled synthetic scenes and does not yet explain where the bridge entity is computed or establish a single-vector handoff mechanism.

## Context
Looped language models represent a growing architectural paradigm where a single transformer is iterated multiple times to deepen reasoning without adding parameters, offering a parameter-efficient alternative to scaling model size. Understanding how information flows across loop iterations—particularly how later loops correct earlier retrieval failures—is critical for both interpreting these models and designing better training objectives. This work sits at the intersection of mechanistic interpretability and retrieval-augmented reasoning, probing whether multi-hop question answering in looped models relies on a localized query-transplant mechanism or a distributed computation spread across iterations.

## Implications
For practitioners building or deploying looped language models, these findings suggest that late-loop query vectors encode reusable retrieval strategies that could potentially be distilled or transferred to earlier loops, offering a pathway to improve multi-hop reasoning without additional training. However, the failure to replicate on natural questions and the inability to pinpoint where bridge entities are computed mean that current results do not yet support a practical engineering recipe for improving two-hop retrieval in production systems, and further mechanistic work is needed before these insights can guide model design or fine-tuning strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34639v1)
