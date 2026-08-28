---
title: Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction
published: 2026-08-27T07:26:13Z
authors: Yu-Lin Tsai, Yu-An Lu, Ci-Yang Tsai, Muxi Lyu, Raluca Ada Popa, Chia-Mu Yu
url: http://arxiv.org/abs/2608.26733v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Daydreaming: Stealing Hidden Agent Skills through Black-Box Task Interaction

## Abstract
Agent skills bundle instructions, reference data, and executable helpers that let a general agent perform specialized tasks. Hosted providers can keep these files secret while selling access to task results, making the skill itself a valuable target. Existing disclosure defenses can block requests that ask for the skill or reproduce its text, but they cannot block customers from submitting the ordinary tasks the service is built to complete. We present Daydreaming, an execution-only attack that steals a multi-file skill through black-box task interactions. The victim is never asked to reveal the skill or grade a reconstruction. Instead, Daydreaming adaptively creates crafted tasks whose results distinguish possible hidden behaviors. It tests individual behaviors, uses attacker-controlled shadow agents to choose a design, and completes each file using stored victim results and local execution checks. We formalize three nested threat levels of access as Differential, Trace, and Output, and focus on Output, where the attacker sees only the final response and returned files. Across 7 skills and 4 victim models, Daydreaming recovers 86.8% of the original skill's capability at Output, outperforming SigLeak by almost 4x. It produces installable skills using a median of 32 victim calls per skill even with disclosure defenses enabled. These results show that hiding skill files and filtering direct disclosure do not, by themselves, prevent functional reconstruction through normal use.

## Metadata
- **Published**: 2026-08-27T07:26:13Z
- **Authors**: Yu-Lin Tsai, Yu-An Lu, Ci-Yang Tsai, Muxi Lyu, Raluca Ada Popa, Chia-Mu Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26733v1)