---
title: KAYROS: An Anytime and Exact Open-Source Solver for Duration-Minimization Time-Dependent Vehicle Routing. A Technical Report and a Case Study in Human-AI Engineering
url: http://arxiv.org/abs/2607.23116v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_09-16-40Z_KAYROS_AnAnytimeandExactOpen_SourceSolverforDurati.md
generated_at: 2026-07-27 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
KAYROS is an open-source solver for duration-minimization time-dependent vehicle routing problems, providing anytime exact solutions that are publicly verifiable over piecewise-linear travel‑time functions. The paper reports 468 optimality certificates on the MAMUT benchmark and five improvements to published reference values. It also introduces Poryos2026, a benchmark family generated from real OpenStreetMap networks.

## Key Takeaways
- KAYROS is the first open solver that is both anytime and exact for TDVRPTW/TDVRP with piecewise-linear travel times, delivering streaming improving solutions from seconds.  
- It provides publicly verifiable optimality certificates; 468 of these match four independent solves, and five strictly improve published reference values.  
- The Poryos2026 benchmark includes 1,080 paired instances with checker‑validated best‑known solutions.

## Context
This work advances AI‑driven routing by integrating exact combinatorial optimization with streaming algorithmic improvements, showing how human‑AI collaboration can verify complex real‑world constraints. It pushes the frontier of open‑source solvers beyond discretization to continuous time functions, offering a reliable benchmark for future research.

## Implications
Practitioners can rely on provably optimal routes without costly re‑optimizations, reducing operational costs and improving reliability in logistics. The benchmark offers a transparent standard for evaluating AI routing tools with verifiable performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23116v1)
