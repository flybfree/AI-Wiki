---
title: Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation
published: 2026-09-28T14:46:00Z
authors: Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom, Hafiz Budi Firmansyah
url: http://arxiv.org/abs/2609.35308v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Epistemic Policy Divergence in Multi-Turn LLM Contamination: A Protocol-Gradient Investigation

## Abstract
Large language models process conversation history as unverified context: false premises injected into prior turns can be adopted as fact, a failure mode we term session-level contamination. We introduce five contamination protocols arranged along a source-authority gradient, isolating distinct failure mechanisms while holding the false premise constant, and evaluate GPT-5.4 Mini, Gemini-3.1 Flash-Lite, and GLM-4.5-Air across ten knowledge domains at temperature zero (22,500 turns), using a dual-track automated judge validated against a human gold standard (Cohen's \k{appa} = 0.901). GPT-5.4 Mini showed zero adoptions across all 500 sessions, a content-independent policy at the session level; token-level probing shows the underlying margin, while large, is finite. Gemini-3.1 Flash-Lite followed a steep authority gradient: 0.1% adoption for self-attributed falsehoods, 23.5% for user-cited sources, 68.2% for system-injected authority, and 94.0% under instruction override. GLM-4.5-Air showed a shallower gradient (15.8% vs 84.2%), a 68-percentage-point dissociation confirming that authority deference and instruction compliance are distinct mechanisms within one architecture. Recovery also diverged: GLM recovered in 94.5% of affected sessions, whereas 26.1% of affected Gemini sessions never did, rising to 40.0% under instruction override. Conversation history is an untrusted attack surface requiring provenance-aware system design; the complete framework is released as an open-source benchmark.

## Metadata
- **Published**: 2026-09-28T14:46:00Z
- **Authors**: Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom, Hafiz Budi Firmansyah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35308v1)