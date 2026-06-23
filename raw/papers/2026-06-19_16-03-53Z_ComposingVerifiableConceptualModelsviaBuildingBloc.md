---
title: Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows
published: 2026-06-19T16:03:53Z
authors: Noe Y. Flandre, Alexander C. Nwala, Philippe J. Giabbanelli
url: http://arxiv.org/abs/2606.21565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Composing Verifiable Conceptual Models via Building Blocks: Towards Design-Time Verification of Agentic AI Workflows

## Abstract
Agentic AI systems orchestrate multiple LLM-based agents through workflow architectures that coordinate decisions, tools, and external actions. While current platforms emphasize runtime safeguards, little support exists for verifying workflows during system design. From a Modeling \& Simulation perspective, this gap is analogous to composing conceptual models without verifying whether their building blocks interact coherently. We propose a design-time verification approach that models agentic workflows as compositions of reusable building blocks and checks their compatibility through twelve structural rules. We implemented these rules in a software prototype and evaluated them using two openly released datasets: 48 workflows with known design flaws and 168 variants that preserve workflow logic but alter graph structure. Results show that our verifier reliably detects violations even when flawed designs are obscured through structural transformations such as splitting tasks between agents. Future works could combine our verification with community repositories of building blocks to compose safe agentic workflows.

## Metadata
- **Published**: 2026-06-19T16:03:53Z
- **Authors**: Noe Y. Flandre, Alexander C. Nwala, Philippe J. Giabbanelli
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.21565v1)