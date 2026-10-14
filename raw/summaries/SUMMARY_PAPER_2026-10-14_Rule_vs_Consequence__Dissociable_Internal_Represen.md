---
title: Rule vs.Consequence: Dissociable Internal Representations of Moral Reasoning in LLMs
url: http://arxiv.org/abs/2610.16371v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_08-22-28Z_Rulevs_Consequence_DissociableInternalRepresentati.md
generated_at: 2026-10-14 00:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models encode distinct internal representations for rule-based versus consequence-based moral reasoning, or whether their differential responses are merely surface-level lexical sensitivity. Using a 2×2 factorial dataset crossing reasoning style with judgment polarity, the authors identify two orthogonal directions in the residual stream—Dir-A tracking reasoning style and Dir-B tracking judgment polarity—that are near-blind to each other (cross-correlation |r| < 0.04). The findings replicate across three instruction-tuned models from different developers and are causally effective across an extended band of network layers, though generalization to novel phrasings beyond training templates remains partial.

## Key Takeaways
- The study demonstrates a double dissociation in LLM internal representations: Dir-A encodes reasoning style (rule-based vs. consequence-based framing) while Dir-B encodes judgment polarity (permissive vs. prohibitive), with cross-correlation below 0.04, indicating these are genuinely independent geometric structures rather than confounded lexical artifacts.
- Dir-A is causally effective and selective: in conflict pairs where the two framings predict opposite labels, Dir-A can correct errors in rule-based judgments without altering consequence-based judgments, ruling out a simple "accept everything" mechanism and suggesting targeted intervention in reasoning-style processing.
- Generalization is limited: while the direction transfers across benchmark sources, its advantage over lexical baselines on novel phrasings is modest, leading the authors to frame the finding as "moral reasoning style sensitivity"—a geometrically dissociable structure—rather than evidence of internalized normative reasoning.

## Context
As LLMs are increasingly deployed in morally and legally sensitive applications such as legal advisory systems, content moderation, and policy analysis, understanding whether models possess structured internal representations of moral reasoning styles versus superficial pattern-matching is critical for safety and reliability. This paper contributes to the growing mechanistic interpretability literature by applying linear probing and activation steering to moral reasoning specifically, bridging cognitive science frameworks of moral psychology (deontological vs. consequentialist reasoning) with neural network geometry. The cleanroom test set with conflict pairs represents a methodologically rigorous approach to distinguishing genuine internal structure from lexical confounds.

## Implications
For practitioners deploying LLMs in legal, ethical, or policy-sensitive domains, this work suggests that models do encode separable representations of reasoning style that can be causally intervened upon, opening potential pathways for targeted steering to correct specific reasoning-style errors without broadly altering model behavior. However, the modest generalization to novel phrasings cautions against over-interpreting these directions as robust internalized moral reasoning, implying that current safety interventions based on such steering may be fragile under distribution shift. The replication across three models from different developers strengthens confidence that this is a general architectural property rather than a model-specific artifact, informing future alignment and interpretability research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16371v1)
