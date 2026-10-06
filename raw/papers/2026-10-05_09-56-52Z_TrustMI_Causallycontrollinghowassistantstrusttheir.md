---
title: TrustMI: Causally controlling how assistants trust their users
published: 2026-10-05T09:56:52Z
authors: Théo Lasnier, Romain Froger, Maxence Lasbordes, Djamé Seddah
url: http://arxiv.org/abs/2610.06064v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrustMI: Causally controlling how assistants trust their users

## Abstract
Large Language Model (LLM) assistants routinely decide whether they can trust users and third parties whose competence, intentions, and integrity they cannot verify. This uncertainty matters for safety, as trusting the wrong party can lead an agent to comply with harmful requests or act on malicious instructions encountered during tool use. To study this problem, we define trust as an assistant's willingness to accept vulnerability to the actions of another party and ask whether such behavior can be causally controlled through model activations. We build 2,000 contrastive conversations spanning ability, benevolence, and integrity, where paired responses complete the same request but differ in whether the assistant trusts the user. From these pairs, we learn steering matrices while keeping the model parameters frozen and test them across six instruction-tuned models from three families, finding that steering changes trust decisions monotonically in both directions. We then ask whether this effect extends to several safety-related agent settings involving harmful requests, prompt injections, and insider threats, while using benign-task and reasoning as controls. Our findings provide evidence that trust in the user can be causally controlled along linear directions in model activations and provide a way to study how trust shapes safety-relevant behavior in language models.

## Metadata
- **Published**: 2026-10-05T09:56:52Z
- **Authors**: Théo Lasnier, Romain Froger, Maxence Lasbordes, Djamé Seddah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06064v1)