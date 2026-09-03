---
title: Context Inference Attacks Without Jailbreaks
published: 2026-08-31T21:53:52Z
authors: Prince Jha, Samuele Poppi, Nils Lukas
url: http://arxiv.org/abs/2609.01663v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context Inference Attacks Without Jailbreaks

## Abstract
Agentic AI systems are increasingly deployed to process sensitive data at inference time, such as healthcare records or financial documents assembled into a hidden \emph{context} before the system answers. Prior work has studied privacy risks primarily through \emph{jailbreaking} attacks that induce models to directly disclose sensitive content, but has largely overlooked the agentic setting where the context is assembled by the agent's own tool calls. We show that the agents we evaluate remain vulnerable to hidden-context leakage despite the controls we test against them, namely an instruction not to disclose the context, logit suppression, and context dilution. For instance, a web-browsing agent answering benign user queries still carries exploitable signals about records silently loaded into its context. We introduce and formalize \emph{context-inference attacks} through a security game and evaluate three settings under decreasing attacker knowledge and increasingly indirect delivery of the context: a known context, an unknown context, and a context the agent retrieves through its own tool calls. We distinguish a grey-box setting, in which the target model is used to score observations, from black-box settings in which the attacker scores with a surrogate it controls. We further characterize how leakage varies with query budget, context size, and target-model size. A single attack carries through all three settings without modification, reaching $100\%$ ASR on small candidate sets and $63\%$ at $1024$ candidates against a known context, $78.9$ AUROC when the template and surrounding records are unknown, $92.5$ AUROC when a 14B surrogate scores a 32B target, and $81.8$ AUROC when the records arrive as an agent's retrieval returns, against chance rates of $1/|\mathcal{Z}|$ and $50$ respectively.

## Metadata
- **Published**: 2026-08-31T21:53:52Z
- **Authors**: Prince Jha, Samuele Poppi, Nils Lukas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01663v1)