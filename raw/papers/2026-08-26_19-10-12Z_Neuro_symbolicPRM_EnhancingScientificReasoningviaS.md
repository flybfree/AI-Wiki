---
title: Neuro-symbolic PRM: Enhancing Scientific Reasoning via Structured Traces and Symbolic Verification
published: 2026-08-26T19:10:12Z
authors: Yuxin Zi, Cong Xu, Suparna Bhattacharya, Martin Foltin, Amit Sheth
url: http://arxiv.org/abs/2608.26329v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neuro-symbolic PRM: Enhancing Scientific Reasoning via Structured Traces and Symbolic Verification

## Abstract
While tool-augmented Large Language Models have significantly improved multi-step reasoning in quantitative STEM tasks, a critical residual failure mode remains: intermediate reasoning steps that are syntactically well-formed, mathematically executable, and unit-consistent, yet contextually ungrounded. Current approaches either rely on formal verifiers that cannot assess semantic intent, or burden Process Reward Models (PRMs) with the dual task of checking both arithmetic and logic. In this paper, we propose a neuro-symbolic framework that cleanly decouples reasoning into two formal dimensions: Symbolic Validity ($V$) and Semantic Groundedness ($G$). We guarantee $V$ by construction using a deterministic symbolic verifier acting as a hard filter. To assess $G$, we train a PRM conditionally on the verifier-accepted manifold. To train this PRM efficiently, we introduce Counterfactual Symbolic Perturbation (CSP), a novel data synthesis strategy that algorithmically generates constraint-preserving hard negatives (steps that perfectly pass the verifier but are logically flawed). At inference, we deploy a verifier-first constrained search that guarantees execution consistency for verifier-covered operations while relying on the PRM solely to rank semantic grounding. By targeting the exact residual error class of strong tool-using LLMs, our method significantly improves reasoning reliability without the sprawling heuristics of prior frameworks.

## Metadata
- **Published**: 2026-08-26T19:10:12Z
- **Authors**: Yuxin Zi, Cong Xu, Suparna Bhattacharya, Martin Foltin, Amit Sheth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26329v1)