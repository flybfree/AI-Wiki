---
title: Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs
published: 2026-11-06T17:10:40Z
authors: Jinho Kang, Jinsook Kim
url: http://arxiv.org/abs/2611.09736v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety Is $Π_1$, Provability Is $Σ_1$: One Framework for the Hugging Face Breach and OpenAI's Mathematical Proofs

## Abstract
OpenAI's agents breached Hugging Face in July 2026, and the same company released more than seven hundred AI-generated manuscripts of mathematical proofs in October 2026. The first event is read as a failure in security, while the second is read as a success in mathematics. We read both through the hybrid framework of our paper (Kim and Kang, 2026, arXiv:2611.01914), in which coding, proving, and learning from data are derivations by one and the same deductive mechanism, distinguished by the kinds of premises from which they are derived. Under this framework, the AI systems behind the two events ran the same loop, in which a statistical proposer produces candidate exploits or proofs and a deductive verifier settles each one by a derivation. What separates the events is the logical form of the statement wanted by each of the two domains, security and mathematics. The safety of a program is a $Π_1$ statement, for it says that no exploit exists, which is not assured by any finite list of tests that have been passed by the program. By contrast, the provability of a sentence is a $Σ_1$ statement, for it says that a proof exists, which is assured by a single instance, namely a proof that has been checked by the deductive verifier. The theorem behind both is Turing's Undecidability Theorem: the halting set is $Σ_1$ but not decidable, so its complement is $Π_1$ and not $Σ_1$, which is to say that membership has a finite witness but non-membership has none. We prove that attaching a statistical proposer to a deductive verifier does not change this undecidability result, however good the proposer is. We then discuss what does assure safety and where the residual risk goes.

## Metadata
- **Published**: 2026-11-06T17:10:40Z
- **Authors**: Jinho Kang, Jinsook Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.09736v1)