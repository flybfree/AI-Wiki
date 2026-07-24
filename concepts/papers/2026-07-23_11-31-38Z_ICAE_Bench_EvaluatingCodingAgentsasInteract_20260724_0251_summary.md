# Summary: 2026-07-23_11-31-38Z_ICAE_Bench_EvaluatingCodingAgentsasInteractiveProj.md
Saved: 2026-07-24 02:51
Source: 2026-07-23_11-31-38Z_ICAE_Bench_EvaluatingCodingAgentsasInteractiveProj.md
Model: None

---

## Summary  
The paper introduces ICAE‑Bench, a benchmark designed to evaluate coding agents in interactive project‑building scenarios where requirements are fuzzy and dynamic. It moves beyond static tasks by simulating user‑agent driven interactions that clarify ambiguous specifications while preserving repository integrity. The framework integrates three core designs: (1) deriving ambiguity from real open‑source repositories with executable behavior; (2) using User Agent Data to reveal hidden constraints without inventing new ones or leaking artifacts; and (3) applying standardized black‑box tests plus multi‑dimensional diagnostics across functional, semantic, API, structural, design, and interaction quality. This work addresses a gap in existing benchmarks that ignore interactive, real‑world project construction.  

## Key Contributions  
- Finding 1: ICAE‑Bench provides the first benchmark that models coding agents as collaborative builders rather than isolated solvers.  
- Finding 2: The three‑design framework ensures realistic, reproducible user simulation and fair evaluation of open‑ended repositories.  
- Finding 3: Multi‑dimensional diagnostics capture both functional correctness and higher‑level design qualities.  

## Methodology  
The authors construct a set of real open‑source projects where each repository defines executable behavior that can be used to generate ambiguous requirements. A User Agent Data module extracts constraints from the codebase, feeding them to the coding agent during an interactive dialogue. The evaluation uses black‑box tests and a diagnostic suite measuring functional correctness (pass/fail), semantic similarity (cosine similarity of APIs), API compatibility, structural fidelity (tree comparison), design quality (code readability metrics), and interaction quality (dialogue relevance). Agents are compared across multiple iterations to assess progress under the interactive protocol.  

## Results  
Experiments show that agents trained on standard benchmarks perform significantly worse than those fine‑tuned with ICAE‑Bench’s interactive protocol. The diagnostic suite reveals a strong correlation between interaction quality and final code quality, while functional correctness remains high but design quality varies widely without the interactive guidance.  

## Significance  
This benchmark highlights the importance of interactive, requirement‑driven evaluation for coding agents that must build complete projects from vague intents. It bridges theory and practice by providing a repeatable pipeline for measuring both low‑level execution and holistic project outcomes.  

## Related Concepts  
interactive project building, user agent data, black‑box testing, multi‑dimensional diagnostics, open‑source repository evaluation, vibe‑coding workflows, coding agents, ambiguity resolution, repository integrity.
