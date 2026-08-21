---
title: Continuous Adversarial MeanFlow Transfer
published: 2026-08-20T01:20:31Z
authors: Yara Bahram, Zahra Dehghani, Mélodie Desbos, Eric Granger, Pablo Piantanida, Mohammadhadi Shateri
url: http://arxiv.org/abs/2608.19540v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continuous Adversarial MeanFlow Transfer

## Abstract
Training fast generators on new domains with limited data remains challenging for two reasons. First, adapting a pretrained diffusion or flow model to a new domain leaves its costly multi-step sampling unaddressed, and existing acceleration methods are tied to the source parameterization--$ε$, $x$, $v$, or $u$--leaving heterogeneous pretrained models with no common acceleration target. Second, while adversarial refinement is proven effective for few-step quality, it is formulated only for instantaneous-velocity flows, not for the finite-interval average velocities that MeanFlow (MF) models predict. We address both problems. We propose MeanFlow-Transfer, which maps heterogeneous source outputs into a shared velocity representation, uses it to initialize an MF generator from the source weights, and optimizes an MF objective on the target domain. This unifies adaptation and acceleration in a single training loop across a broad range of pretrained models. We then introduce Continuous Adversarial MeanFlow, a post-training stage that extends continuous adversarial flow models from instantaneous velocities to MF's finite-interval average velocities. CAMF contrasts changes in a learned potential between real and predicted interval endpoints, recovering fine detail that MF regression averages away, and reduces to the instantaneous criterion in the vanishing-interval limit. Adapting four ImageNet-based source models--DiT ($ε$), SiT ($v$), JiT ($x$), iMF ($u$)--to five target domains, MF-T with CAMF matches or exceeds the fine-tuned teacher in FID and FDD at up to $125\times$ fewer Neural Function Evaluations (NFEs), while CAMF improves MF-T's few-step FID by $29\%$ on average.

## Metadata
- **Published**: 2026-08-20T01:20:31Z
- **Authors**: Yara Bahram, Zahra Dehghani, Mélodie Desbos, Eric Granger, Pablo Piantanida, Mohammadhadi Shateri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19540v1)