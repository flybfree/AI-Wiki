---
title: Only What You've Signed up For: Secure Workflows with Constrained Diffusion Agents
published: 2026-10-10T20:58:01Z
authors: Michael Cardei, Anjun Hu, Chenrui Ma, Francesco Pinto, Chawin Sitawarin, Chulin Xie, Ferdinando Fioretto
url: http://arxiv.org/abs/2610.15177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Only What You've Signed up For: Secure Workflows with Constrained Diffusion Agents

## Abstract
As agentic AI systems take on increasingly complex and consequential tasks, securing them against prompt injection becomes critical. Existing defenses often rely on detecting or reasoning about injected malicious instructions and can therefore remain vulnerable to adaptive attacks that optimize the injection itself. Diffusion language models (dLLMs), an emerging framework for language generation, offer a new opportunity for security enforcement: by iteratively refining their sequence wide predictions, they enable broader-scope constraint enforcement throughout generation. This paper introduces Policy-Constrained Diffusion Agents (CoDA), a framework that enforces task dependent security policies directly within the denoising process of diffusion language models. At each denoising step, CoDA projects token distributions onto a policy-compliant set, maintaining constraint satisfaction throughout generation. We evaluate CoDA across state-of-the-art diffusion language model families under both static and adaptive prompt-injection attacks. Results demonstrate substantial reductions in attack success rate with competitive task utility and practical inference overhead.

## Metadata
- **Published**: 2026-10-10T20:58:01Z
- **Authors**: Michael Cardei, Anjun Hu, Chenrui Ma, Francesco Pinto, Chawin Sitawarin, Chulin Xie, Ferdinando Fioretto
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15177v1)