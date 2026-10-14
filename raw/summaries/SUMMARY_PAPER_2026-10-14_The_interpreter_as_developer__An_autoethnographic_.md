---
title: The interpreter as developer: An autoethnographic design study of building a computer-assisted interpreting tool through human-LLM co-creation
url: http://arxiv.org/abs/2610.16460v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_09-19-55Z_Theinterpreterasdeveloper_Anautoethnographicdesign.md
generated_at: 2026-10-14 00:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an autoethnographic design study in which a professional interpreter with no programming background built a local-first computer-assisted interpreting (CAI) system through collaborative "vibe coding" with an LLM architect and a coding agent. The study demonstrates how tacit professional knowledge—such as segmentation strategies and booth infrastructure requirements—was externalized into functional design after generic defaults proved inadequate in real use, and it reports telemetry from a fully instrumented public scientific event showing a median translation latency of 0.94 seconds across 971 utterances sustained by a fully local processing chain.

## Key Takeaways
- The study reframes the interpreter not as a passive end-user of CAI tools but as a lead-user developer who, through generative AI co-creation, can externalize deeply tacit professional knowledge (e.g., segmentation logic, booth infrastructure constraints) into working software design, challenging the prevailing paradigm where CAI tools are built for interpreters rather than by them.
- A firmly human-led division of labor is central to the design process: the interpreter retains interpretive authority while the LLM and coding agent handle implementation, producing three distinct mechanisms of in-booth appropriation that govern how the tool is integrated into live interpreting practice without displacing human judgment.
- Empirical telemetry from a demanding public scientific event demonstrates that a fully local (non-cloud-dependent) processing chain can sustain a median translation latency of 0.94 seconds across 971 utterances, showing that practical, privacy-preserving CAI systems are achievable without reliance on external API infrastructure.

## Context
The broader AI landscape increasingly positions large language models as collaborative coding agents, yet most human-AI co-creation research focuses on software engineers or domain experts with technical training. This paper extends that paradigm to a profession—simultaneous interpreting—that has historically been excluded from the design loop of its own tooling, and it does so through a fully local-first architecture that sidesteps the privacy and latency concerns that cloud-based AI captioning systems raise for professional interpreters. By documenting the complete development dialogues, the study contributes a rare empirical account of how non-programmers can leverage LLMs to build domain-specific tools, adding to the growing literature on vibe coding and lead-user innovation in generative AI.

## Implications
For the interpreting profession, this work suggests that generative AI can democratize tool development, enabling interpreters to shape their own CAI systems and thereby raising the bar for technological literacy as a component of interpreter training curricula. For the CAI industry, the findings challenge vendors to shift from building tools for interpreters to co-creating with them, potentially yielding systems that better encode professional tacit knowledge and respect the human-led division of labor essential to interpreting ethics. For AI-assisted software development more broadly, the case illustrates that domain expertise combined with LLM-mediated coding can produce production-grade, locally deployed systems, offering a template for other professions seeking to build their own AI-augmented tools without traditional programming expertise.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16460v1)
