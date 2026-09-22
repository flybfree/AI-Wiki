---
title: AutoGym: Blueprint-First Generation of Verifiable Agent Gyms
published: 2026-09-18T21:18:49Z
authors: Aarati Andrea Noronha, Kavya Ravikumar, Carly Xiaoyu Lin
url: http://arxiv.org/abs/2609.22592v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoGym: Blueprint-First Generation of Verifiable Agent Gyms

## Abstract
Training agents with reinforcement learning requires a gym, comprising a task, an executable environment in which the task can be attempted, and a verifier that reliably distinguishes success from failure. Constructing such gyms remains manual, expensive, and static. Task sets saturate as models improve and are increasingly exposed to contamination. Synthetic generation offers scale, but single-pass synthesis produces tasks whose difficulty is largely cosmetic. Models comparable in capability solve them despite convoluted phrasing, and correctness must be adjudicated post-hoc by unreliable LLM judges. We present AutoGym, a framework that generates complete gyms (tasks, executable environments, and verifiers) from a minimal domain seed or prior model trajectories. AutoGym introduces three mechanisms. (1) Blueprint-first generation specifies the valid solution space, environment requirements, and verification criteria before the environment is materialized, making solvability a construction prerequisite rather than a property verified after the fact. (2) Explicit generation parameters control task topology, interaction depth, capability axes, question obfuscation, and distractor composition, enabling fine-grained difficulty steering. (3) Active curriculum synthesis uses performance-informed calibration to adjust the distribution over these parameters as model capabilities evolve. Across productivity and temporal-reasoning settings, AutoGym generates gyms spanning the capability spectrum, including instances that challenge frontier models.

## Metadata
- **Published**: 2026-09-18T21:18:49Z
- **Authors**: Aarati Andrea Noronha, Kavya Ravikumar, Carly Xiaoyu Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.22592v1)