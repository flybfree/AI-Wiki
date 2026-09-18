---
title: ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers
published: 2026-09-17T05:27:59Z
authors: Hyeongjun Choi, Wonyoung Jung, Haehoon Seo, Sungyup Nam
url: http://arxiv.org/abs/2609.19722v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers

## Abstract
Large language models are being integrated into malware triage workflows as reasoning components that summarize static evidence and produce analyst-facing verdicts. This paper shows that the same reasoning capability introduces a new attack surface. We present ALIBI, a semantic cover story attack against frontier LLM-based malware analyzers. ALIBI adds a small, non-executed read-only section to a compiled binary, containing a coherent but false security product narrative, without altering imports or executable behavior. Instead of issuing direct instructions to the model, it reframes suspicious evidence as expected behavior of a benign endpoint security tool. On a frozen PE set of 50 malicious samples, the payload flips 30 of the 35 baseline-malicious samples to benign on Gemini 2.5 Pro, while GPT-5.5 Pro and Claude Opus 4.7 produce substantial severity downgrades with significant confidence reductions even when verdict labels are preserved. The attack transfers to ELF binaries, where Gemini flips 16 of 40. A verification-guided defense prompt roughly halves the benign verdicts, but 42.9 percent of malicious samples still reach benign. LLM malware analyzers therefore require provenance checks that separate verified facts from attacker-controlled claims, not narrative trust.

## Metadata
- **Published**: 2026-09-17T05:27:59Z
- **Authors**: Hyeongjun Choi, Wonyoung Jung, Haehoon Seo, Sungyup Nam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19722v1)