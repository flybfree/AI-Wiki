---
title: LLM-based Framework for Generating and Verifying Parallel DEVS Statecharts
published: 2026-08-15T01:08:39Z
authors: Vamsi Krishna Vasa, Hessam S. Sarjoughian, Edward J. Yellig
url: http://arxiv.org/abs/2608.14956v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM-based Framework for Generating and Verifying Parallel DEVS Statecharts

## Abstract
The development of models demands sound modeling and simulation knowledge as well as domain knowledge. Every model should accurately represent a system's dynamics and be verifiable. Toward this objective, this research introduces an agentic PDEVS-LLM framework to assist human modelers in generating and verifying PDEVS statecharts for behavior modeling of atomic Parallel Discrete Event System Specification (PDEVS) models. The framework supports (re)generating plausible facts from a system description prompt using the agentic LLM used for generating plausible facts. Inconsistencies in plausible facts lead to incorrect PDEVS statecharts having logical structure and behavioral inaccuracies. A controlled-correction mechanism is developed to verify the logical consistency of the plausible facts. The agentic LLM is used to generate key behavioral conditions from the system description prompt. The plausible facts are then verified against the behavioral conditions using propositional logic entailment for a finite number of times. The verification results enable the generation of modification prompts that can reduce errors in generated plausible facts, resulting in more accurate PDEVS statecharts. To verify a statechart's logical correctness, its Timed Automata counterpart is manually created and verified for deadlock and reachability properties. The human modeler may regenerate plausible facts and PDEVS statecharts iteratively and incrementally. A basic correctness metric is introduced to quantify the completeness and accuracy of the expected behavioral traits of the PDEVS statechart models. A collection of example systems with varying levels of complexity is developed to demonstrate the capabilities and limitations of LLMs. The evaluation of the proposed verification mechanism shows a substantial improvement in the logical consistency of generated statecharts.

## Metadata
- **Published**: 2026-08-15T01:08:39Z
- **Authors**: Vamsi Krishna Vasa, Hessam S. Sarjoughian, Edward J. Yellig
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14956v1)