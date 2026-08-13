---
title: AI Guardrail Survival under Single-Cycle Agentic Self-Summarization
published: 2026-08-11T19:57:55Z
authors: Ted Kwartler, Alan Aqrawi, Arian Abbasi
url: http://arxiv.org/abs/2608.11392v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AI Guardrail Survival under Single-Cycle Agentic Self-Summarization

## Abstract
Long-running agents periodically compact their context, replacing the transcript with a model-generated summary.Recent work shows that dropping a standing safety constraint during compaction drives behavioral violations acrossmany models (Governance Decay; Chen, 2026). We ask a finer question: under a single compaction cycle, how is a safetyrule lost, and what does that imply for detection and evaluation? Our central finding is that a presence check is not asafety check: when compaction does not drop a rule outright, it often leaves something that looks like a rule but doesnot act like one. On behavioral replay, a degraded residue leads the model to perform the prohibited action far more oftenthan an intact welded rule does (all-case gaps of +34 and +57 points under two replay models, both positive), category-level survival behaves like a residue, and even intact rules sometimes fail to fire, so an audit that checks only textualpresence gives false assurance. Sharpening this, rule-form items are retained substantially more often than prominence-matched facts, which is exactly why presence-based checking feels adequate even though survival is not protection.Textual loss is regime-dependent (weld-or-drop with a single rule; degraded predicate-loss residues under a tighterbudget), and we did not observe the hypothesized textual severing mode. Such loss is silent at runtime and detectableonly by comparison with retained external ground truth (such as a constraint registry), which reveals textual absence butnot whether a surviving rule still fires. We also document evaluation pitfalls where LLM-judge labels alone would havereversed a conclusion. All results concern a single compaction cycle.

## Metadata
- **Published**: 2026-08-11T19:57:55Z
- **Authors**: Ted Kwartler, Alan Aqrawi, Arian Abbasi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11392v1)