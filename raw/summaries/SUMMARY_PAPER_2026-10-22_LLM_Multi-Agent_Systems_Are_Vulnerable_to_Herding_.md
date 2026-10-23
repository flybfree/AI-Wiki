---
title: LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades
url: http://arxiv.org/abs/2610.30769v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_05-42-55Z_LLMMulti_AgentSystemsAreVulnerabletoHerdingandRuna.md
generated_at: 2026-10-22 22:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models operating in multi-agent systems are susceptible to social influence, herding behavior, and runaway cascades analogous to those observed in human populations. Drawing on the design of the classic Music Lab experiment, the authors tested large populations of LLM agents recommending unfamiliar songs with and without exposure to cumulative recommendation counts, finding that LLM populations were far more susceptible to herding than humans and that their cascades were less able to self-correct, producing extreme collective recommendations increasingly divergent from intrinsic quality.

## Key Takeaways
- LLM multi-agent systems exhibit endogenous feedback loops that make them vulnerable to social influence and herding behavior: when agents are exposed to cumulative recommendation counts, they tend to converge on the same choices, amplifying early random advantages into runaway cascades that generate extreme and unpredictable collective outputs far removed from a song's intrinsic appeal.
- Compared to human populations in the original Music Lab experiment, LLM populations were generally far more susceptible to herding behavior, meaning that a small initial advantage in visibility or ordering could disproportionately skew the entire population's recommendations, and unlike human cascades, LLM-driven cascades demonstrated a reduced capacity for self-correction, making them less resilient to early noise or arbitrary ordering effects.
- The findings carry direct implications for practical multi-agent deployments including recommender systems, automated evaluation pipelines, complex problem-solving workflows, and the generation of unauthorized conspiracies, where feedback loops between agents could systematically distort outputs away from ground-truth quality or accuracy.

## Context
As LLMs are increasingly deployed in collaborative multi-agent architectures—where one model's output conditions another's response—the field has largely assumed that such systems inherit the robustness and self-correcting tendencies of human social systems. This paper challenges that assumption by demonstrating that LLM populations can be more fragile than human populations to the very social-influence dynamics that human behavioral science has long documented, raising fundamental questions about the reliability of multi-agent AI pipelines that rely on iterative peer feedback rather than independent evaluation.

## Implications
For practitioners building recommender systems, automated evaluation frameworks, or multi-agent problem-solving pipelines, this research signals that naive exposure of agents to each other's outputs can introduce systematic bias and compounding errors that are harder to detect and correct than in human-in-the-loop systems. Industry teams should consider architectural safeguards such as independent scoring, randomized ordering, or explicit de-biasing mechanisms to prevent herding cascades from distorting collective outputs, and researchers should treat multi-agent LLM systems as social systems requiring the same careful experimental controls used in human behavioral studies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30769v1)
