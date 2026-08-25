---
title: Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming
published: 2026-08-23T22:52:13Z
authors: Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, Tegawendé F. Bissyandé
url: http://arxiv.org/abs/2608.22638v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Not Copy/Paste: Soft Barriers for Copying in AI-Assisted Programming

## Abstract
Copying a function from a chat window into an editor takes less than a second. For many uses of AI coding tools, that speed is the point; in settings such as programming education, code review, and security-sensitive development, it can also be the problem. This paper frames copy-paste as an \emph{AI code handoff problem}: the moment model-generated text crosses from a conversational context into executable or committed software is a design boundary that current tools leave largely unmanaged. We argue that AI coding assistants should not only be evaluated by the code they generate, but also by how they mediate the transfer of that code into software artifacts. We propose \emph{soft barriers} as one class of handoff-aware mechanisms. Soft barriers preserve access to AI assistance while making unexamined transfer less frictionless. As an initial technical probe, we instantiate this idea using Unicode output perturbations that preserve visual readability but disrupt naive copy-paste execution. We introduce Copy-Paste Resistance (CPR), the fraction of functionally correct clean solutions that become syntactically invalid after perturbation. Across HumanEval and MBPP with four LLMs and four perturbation families, we find that output-level barriers can achieve high copy-paste resistance, but their effectiveness is highly model- and task-dependent. An exploratory pilot with 18 participants provides early evidence that soft barriers can shift users from direct transfer toward editing and reconstruction. We do not present Unicode perturbations as a deployment-ready solution; rather, we use them as a minimal probe for a broader research agenda on practical, transparent, and policy-aware AI code handoff.

## Metadata
- **Published**: 2026-08-23T22:52:13Z
- **Authors**: Iyiola E. Olatunji, Alberick Euraste Djire, Jacques Klein, Tegawendé F. Bissyandé
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22638v1)