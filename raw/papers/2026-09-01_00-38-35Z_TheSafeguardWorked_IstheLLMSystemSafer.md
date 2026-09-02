---
title: The Safeguard Worked. Is the LLM System Safer?
published: 2026-09-01T00:38:35Z
authors: Pingyu Wu, Weiming Zhang, Nenghai Yu
url: http://arxiv.org/abs/2609.00519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Safeguard Worked. Is the LLM System Safer?

## Abstract
Safeguards in deployed LLM services are evaluated by refusal, attack success, and policy violation rates. Those rates characterize how a control performed on the requests it was tested on. A deployment has to answer a different question: how much help with harmful tasks the service still gives an attacker who keeps adapting or finds another way in. We determine what each reported result implies for that question, allowing results from different safeguard families to be compared under one deployment criterion. The evidence requirements are strongly asymmetric. One attack that obtains harmful help from the deployed service suffices to establish that such help remains, and such attacks appear repeatedly in the coded record. Establishing that little remains cannot follow from the safeguard's own numbers alone; it also requires evidence about what the surrounding system still allows after the safeguard performs its local function. Such evidence is supported or derived in only a small minority of the depth-coded claims, and one such claim bounds its scoped residual. A better local score is therefore not, by itself, a stronger claim about the deployment. Safeguard research cannot stop at raising local scores; a gain has to be judged by whether it makes a deployed system any safer.

## Metadata
- **Published**: 2026-09-01T00:38:35Z
- **Authors**: Pingyu Wu, Weiming Zhang, Nenghai Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00519v1)