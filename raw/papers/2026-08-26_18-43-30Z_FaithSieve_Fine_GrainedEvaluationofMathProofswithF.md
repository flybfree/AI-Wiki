---
title: FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence
published: 2026-08-26T18:43:30Z
authors: Ziyu Wang, Qiming Dai, Yishan Wu, Zaiwen Wen
url: http://arxiv.org/abs/2608.26310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FaithSieve: Fine-Grained Evaluation of Math Proofs with Faithful Formal Evidence

## Abstract
Large language models can now generate complex, multi-step mathematical proofs, but reliably determining their correctness and localizing early logical errors remains a critical challenge. Existing evaluation approaches largely depend on model-based natural-language judgments, which often overlook local reasoning gaps. While formal theorem provers like Lean offer a path to rigorous verification, using them to evaluate informal text requires solving locality and semantic mismatches: a prover might bypass a local flaw by proving an overly broad target, or validate an auto-formalized statement that drifts from the original mathematical intent. To address this, we introduce FaithSieve, a Lean-assisted framework for fine-grained evaluation of natural-language mathematical proofs. FaithSieve decomposes coarse proof steps into local reasoning units, extracts typed proof obligations, and verifies them through a formal evaluation agent. Formal validation is gated by semantic alignment scoring, so Lean evidence is incorporated only when the formal statement faithfully preserves the context, objects, and logical form of the original claim. We construct two expert-verified datasets, ProofLoc-Olympiad and ProofLoc-University, to benchmark first-error localization. On the 350-problem Olympiad dataset, FaithSieve using a GPT-5.4 backbone achieves 81.43% exact first-error accuracy, outperforming the direct-judging baseline of 72.29%. Furthermore, on the 200-problem ProofLoc-University benchmark spanning six advanced domains, FaithSieve reaches 84.5% exact accuracy, compared to 75.0% for the direct judge. Our work demonstrates that decomposing proofs into fine-grained units and grounding them with faithful formal evidence significantly improves reliable evaluation of natural-language reasoning.

## Metadata
- **Published**: 2026-08-26T18:43:30Z
- **Authors**: Ziyu Wang, Qiming Dai, Yishan Wu, Zaiwen Wen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26310v1)