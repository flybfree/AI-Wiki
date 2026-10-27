---
title: KAPPA: Checking the Proofs in Statistics Papers with Lean 4 and Language Model Agents
url: http://arxiv.org/abs/2610.35596v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_15-22-15Z_KAPPA_CheckingtheProofsinStatisticsPaperswithLean4.md
generated_at: 2026-10-27 00:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
KAPPA (Kit of Agents for Proof-checking Papers with a proof Assistant) is an open-source system that orchestrates language model agents, powered by Claude Code, to mechanically translate and verify the proofs in statistical theory papers using the Lean 4 proof assistant and its Mathlib library. The system assigns each numbered result in a paper one of four verdicts—verified unconditionally, verified conditionally, issue recorded, or unfinished—and was tested on four benchmark papers with known answer keys and three published statistical papers, successfully identifying the published errors at the exact steps later corrected, along with additional problems confirmed by hand.

## Key Takeaways
- KAPPA follows the paper's own proof structure step by step rather than attempting to construct an independent proof, which preserves fidelity to the authors' reasoning and makes discrepancies traceable to specific locations in the original text. Each statement is compared against the paper before being proved and fingerprinted afterward, ensuring that the verification is anchored to the source material rather than to a reinterpreted version of it.
- The system enforces strict epistemic discipline: every verdict must rest on evidence reproducible without a language model, meaning Lean 4 serves as the final arbiter. Conditional verifications explicitly name every cited or unproved input as a hypothesis, and the system never claims more than its Lean evidence supports. When the same language model was asked to work directly with Lean on the same papers, it classified fewer results correctly on the longest paper and reported some statements as narrower than the paper's claims, demonstrating that KAPPA's multi-agent architecture produces more conservative and accurate assessments.
- KAPPA operates as an autonomous pipeline that runs unattended for hours, waits out API usage limits, incrementally re-checks only what a revision changed, and reports its computational cost broken down by agent role, model, and result. This makes it practical for auditing long statistical papers at scale, and its four-verdict taxonomy gives readers and editors a structured, actionable report rather than a binary pass/fail judgment.

## Context
Formal verification of mathematical proofs has long been a goal of proof assistants like Lean 4, Coq, and Isabelle, but the labor-intensive process of translating human-written proofs into machine-checkable formal proofs has limited adoption, particularly in applied fields like statistics where proofs are lengthy and rely on domain-specific lemmas. KAPPA addresses this bottleneck by using language model agents as translators and orchestrators while keeping the actual verification grounded in a trusted proof assistant. This hybrid approach sits at the intersection of automated theorem proving, large language model tool use, and scientific reproducibility, a rapidly growing area where AI-assisted formal verification is being explored across mathematics, software engineering, and formal methods.

## Implications
For the statistics and mathematics communities, KAPPA offers a practical tool for catching errors in published proofs before they propagate into downstream research, potentially reducing the number of published corrections and retractions. For practitioners in AI-assisted formal verification, the paper demonstrates that a multi-agent architecture with strict separation between translation, review, and verification stages produces more reliable and conservative results than a single model attempting to prove statements directly, suggesting design principles for future proof-checking systems. For open-source software and reproducible research infrastructure, KAPPA's ability to run unattended, handle incremental revisions, and produce rerunnable evidence positions it as a candidate for integration into journal pre-publication workflows or automated auditing pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35596v1)
