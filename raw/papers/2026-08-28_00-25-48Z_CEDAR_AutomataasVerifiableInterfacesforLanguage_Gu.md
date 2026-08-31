---
title: CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action
published: 2026-08-28T00:25:48Z
authors: Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi
url: http://arxiv.org/abs/2608.27797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CEDAR: Automata as Verifiable Interfaces for Language-Guided Embodied Action

## Abstract
Natural-language tasking of embodied agents is rarely just goal specification: users also impose constraints that must persist while the world changes. Code-generating LLM agents can produce plausible behaviors for such instructions, but their free-form programs provide no stable object to verify, compose with new constraints, or repair from a failing trace. We present CEDAR, a counterexample-guided framework that grounds instructions as regular languages over environment event traces. CEDAR uses a language model for semantic judgments and execution traces for correction, then represents both skills and specifications as deterministic finite automata. This turns constraints into executable finite-state objects: a learned skill can be intersected with a learned sleep at night or stay in this biome specification, yielding a controller that enforces the learned constraint by construction rather than by repeated prompting. In Minecraft, with the same simulator/API observations available to a program-generating baseline, CEDAR maintains temporal and spatial constraints that the baseline fails to preserve and amortizes reuse of learned skills, reducing cumulative LLM queries. These results suggest that regular languages offer a practical verification layer between natural-language instructions and embodied-agent policies.

## Metadata
- **Published**: 2026-08-28T00:25:48Z
- **Authors**: Lekai Chen, Alvaro Velasquez, Ashutosh Trivedi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27797v1)