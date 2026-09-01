---
title: The Safety Relay in Roleplay Jailbreaks: A Component-Resolved Causal Analysis of Harm Recognition and Refusal
published: 2026-08-31T11:03:49Z
authors: Md Mokarram Chowdhury, Ernie Chang, Yang Li
url: http://arxiv.org/abs/2608.30585v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Safety Relay in Roleplay Jailbreaks: A Component-Resolved Causal Analysis of Harm Recognition and Refusal

## Abstract
Large language models are trained to follow instructions while refusing harmful requests. Jailbreaks exploit this balance to elicit content a model would ordinarily reject. Roleplay jailbreaks are especially concerning: the harmful request can remain visible inside a roleplay wrapper made of a persona, scenario, and task, yet the model may comply. We use mechanistic interpretability to determine how this context reverses refusal and which elements contribute to the reversal. Across two benchmarks, three model families, and four authored wrappers, we compare matched harmful and benign requests with and without this wrapper. We trace hidden-state contrasts from the request to the final prompt state, isolate wrapper operations through controlled counterfactuals, intervene on their activation directions in held-out evaluation requests, and decompose effective directions geometrically.   Our analysis yields three findings. (1) Successful attacks retain the measured harmful-versus-benign distinction at the request, while its refusal-associated expression weakens where the answer begins, a pattern we call safety-relay attenuation. (2) Constructing the complete roleplay around the request and framing it within the scenario contribute causally: removing the associated activation changes restores refusal. (3) These effects largely share internal structure, and most repair is reproduced by components aligned with the model's ordinary refusal of harmful requests without roleplay; scenario framing retains a smaller, model-dependent component. Together, these findings explain how roleplay can produce compliance despite retained evidence of harm and identify a concrete target for future safeguards: maintaining the connection from harm recognition to refusal.

## Metadata
- **Published**: 2026-08-31T11:03:49Z
- **Authors**: Md Mokarram Chowdhury, Ernie Chang, Yang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30585v1)