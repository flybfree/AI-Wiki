---
title: Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research
url: http://arxiv.org/abs/2608.24306v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_09-34-18Z_WhoistheAgenttoBlame_LocalizingFaithfulnessandCita.md
generated_at: 2026-08-25 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the source of errors in deep‑research (DR) systems by isolating which agent introduces each mistake, and it classifies those mistakes into four categories: hallucination, uncited input reliance, uncited output, or insufficient citations. Experiments on three leading open‑source DR systems show that most errors originate from the orchestrator, with 84.7 % of AI‑Q report errors arising there, mostly as citation problems; simple interventions raise citation recall by five points without hurting quality.

## Key Takeaways
- The dominant error type varies across agents, but the orchestrator is responsible for most final‑report mistakes, especially citation omissions.  
- 84.7 % of AI‑Q errors originate at the orchestrator, with roughly 31 % being hallucinations and the rest citation mistakes.  
- Two simple interventions improve citation recall by five percent while leaving output quality unchanged.

## Context
Deep research systems aim to generate long, cited reports that mimic human expertise, yet their reliability is undermined by systematic citation failures. Understanding where these errors originate helps researchers design more robust multi‑agent architectures and improves trust in AI‑generated knowledge products.

## Implications
For practitioners, pinpointing error sources enables targeted fixes rather than broad overhauls, leading to faster improvements in factual accuracy. The findings suggest that small architectural tweaks can significantly boost citation reliability, making DR outputs more useful for downstream tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24306v1)
