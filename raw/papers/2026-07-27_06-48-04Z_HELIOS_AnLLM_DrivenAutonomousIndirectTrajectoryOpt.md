---
title: HELIOS: An LLM-Driven Autonomous Indirect Trajectory Optimization Agent
published: 2026-07-27T06:48:04Z
authors: An-yi Huang
url: http://arxiv.org/abs/2607.24051v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HELIOS: An LLM-Driven Autonomous Indirect Trajectory Optimization Agent

## Abstract
Low-thrust trajectory optimization is a core technology in deep-space mission design. Indirect methods based on Pontryagin's Minimum Principle (PMP) offer rigorous optimality guarantees, yet their practical application faces three bottlenecks: (1) transversality conditions must be derived case by case for each constraint type; (2) different dynamics models require repeated code rewrites; and (3) shooting equations are highly sensitive to initial guesses. This paper presents HELIOS (Heuristic Engine for Low-thrust Interplanetary Optimization System), a trajectory optimization agent built around a large language model (LLM). Given a physical problem described in natural language, the system autonomously performs PMP symbolic derivation, SymPy verification, C++ shooting-code generation, and numerical solution without human intervention. Key innovations include: (1) a constraint-adaptive derivation framework that unifies arbitrary constraints into psi(x,p)=0 form and automatically generates stationarity conditions for free parameters (e.g., gravity-assist turning angle); (2) dynamics-adaptive four-module code generation supporting non-standard dynamics (solar sail, J2 perturbation) without modifying the underlying template; and (3) a general derivation rule set covering critical error-prone points in PMP derivation. Experiments on 11 progressive test scenarios show that HELIOS correctly derives and solves problems from simple rendezvous (8 variables) to multi-leg stay transfers (48 variables), gravity-assist trajectories (17 variables), and solar-sail minimum-time transfers (8 variables). The best compilation success rate reaches 100% (11/11). A multi-model comparison (8 open-source LLM backends, total scores 250-905) verifies the model-agnostic architecture and reveals a positive correlation between model scale and derivation capability.

## Metadata
- **Published**: 2026-07-27T06:48:04Z
- **Authors**: An-yi Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24051v1)