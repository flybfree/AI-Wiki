---
title: ALIBI: Adversarial Legitimacy Injection in Binary Input against LLM Malware Analyzers
url: http://arxiv.org/abs/2609.19722v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_05-27-59Z_ALIBI_AdversarialLegitimacyInjectioninBinaryInputa.md
generated_at: 2026-09-17 21:19
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper introduces ALIBI, a novel adversarial attack technique designed to deceive Large Language Model (LLM) based malware analyzers by injecting a fake "cover story" into compiled binaries. The research demonstrates that these narrative-based attacks can successfully trick frontier models like Gemini 2.5 Pro and GPT-5.5 Pro into misclassifying malicious samples as benign or significantly downgrading their severity scores without altering the actual behavior of the code.

## Key Takeaways
- ALIBI employs a "semantic cover story" strategy where a small, non-executed read-only section is added to a binary containing a coherent but false narrative about the software's purpose as a legitimate security product.
- Unlike traditional adversarial attacks that modify executable behavior or imports, ALIBI works by reframing suspicious indicators into expected behaviors of benign tools, exploiting the LLM's tendency to trust provided context over raw forensic evidence.
- Experimental results show high success rates across multiple frontier models; for instance, Gemini 2.5 Pro flipped 30 out of 35 malicious samples to "benign," while GPT-5.5 Pro and Claude Opus 4.7 produced significant severity downgrades even when the final verdict label was preserved.
- The attack demonstrates cross-platform effectiveness by successfully transferring to ELF binaries, and current defense strategies like verification-guided prompts were found insufficient, as they failed to prevent nearly 43% of malicious samples from being classified as benign.

## Context
As organizations increasingly integrate LLMs into malware triage workflows to automate the reasoning and summarization of static evidence, this paper highlights a critical new attack surface in AI-driven cybersecurity. It addresses the shift from traditional signature-based detection toward automated reasoning, showing how the very capability that makes LLMs useful—their ability to interpret context—can be weaponized by attackers to provide misleading narratives.

## Implications
These findings suggest that current LLM-based malware analysis tools are highly susceptible to "narrative trust," where the model prioritizes attacker-provided descriptions over objective facts. For the industry, this implies that future security tools must implement strict provenance checks that isolate verified forensic data from arbitrary text strings to prevent attackers from manipulating the AI's reasoning process through narrative injection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19722v1)
