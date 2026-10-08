---
title: From Expert-Guided Proof Search to Automated Open-Problem Solving
url: http://arxiv.org/abs/2610.09769v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_09-52-46Z_FromExpert_GuidedProofSearchtoAutomatedOpen_Proble.md
generated_at: 2026-10-07 21:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Bolzano, a multi-agent open-source system designed for automated mathematical proof search that combines parallel prover agents with a dedicated verifier agent while maintaining a human-readable research state. The system was first validated on expert-selected problems yielding 8 expert-verified proofs, then scaled to solve approximately 200 open problems out of roughly 3,800 extracted from four sets of papers without problem-specific human guidance, including answering four open questions from papers accepted to STOC 2026 as confirmed by the original authors.

## Key Takeaways
- Bolzano employs a multi-agent architecture with parallel prover agents working alongside a verifier agent, and crucially maintains a human-readable research state that allows researchers to inspect, understand, and build upon the system's progress incrementally rather than treating proof search as a black box.
- The system demonstrated a meaningful progression from expert-guided use to fully automated operation: initial manual use on carefully selected problems produced 8 verified results, while subsequent autonomous runs on approximately 3,800 open problems extracted from four paper collections solved around 200 of them, representing a roughly 5% success rate on genuinely open research questions.
- The STOC 2026 experiment provides strong external validation: Bolzano answered four open questions raised in papers accepted to a top theoretical computer science conference, and these answers were confirmed by the original paper authors, demonstrating that the system can contribute meaningfully to frontier research rather than merely reproducing known results.

## Context
This work sits at the intersection of large language models, automated theorem proving, and multi-agent AI systems, addressing a critical bottleneck in mathematical research where progress depends on efficient proof search, incremental improvements, and careful verification. The paper contributes to the growing body of research on AI-assisted mathematics by demonstrating that a structured multi-agent framework can move beyond toy problems or well-known conjectures to tackle genuinely open questions in published research, bridging the gap between AI capability and real-world mathematical practice.

## Implications
For mathematical researchers and theoretical computer scientists, Bolzano offers a practical open-source tool that can systematically scan literature for open problems and attempt automated solutions, potentially accelerating discovery and reducing the manual burden of proof search. For the broader AI research community, the progression from expert-guided to fully autonomous operation, validated by confirmation from STOC 2026 authors, provides a credible template for deploying multi-agent systems on real research tasks while maintaining verifiability and human oversight. The open-source nature of the system also invites community contribution and benchmarking, which could accelerate progress in automated reasoning and formal verification across disciplines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09769v1)
