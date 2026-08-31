---
title: LandingAgent: A Reference-Annotated Dataset and Agentic Generation Framework for Landing Pages
published: 2026-08-28T04:15:38Z
authors: Injun Baek, HyeongSeok Lee, Yearim Kim, Junhoo Lee, Nojun Kwak
url: http://arxiv.org/abs/2608.27902v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LandingAgent: A Reference-Annotated Dataset and Agentic Generation Framework for Landing Pages

## Abstract
Landing pages are goal-oriented web interfaces that must communicate a target-specific value proposition while organizing information flow, visual hierarchy, and calls to action (CTA). Although large language models can generate plausible webpage code from natural-language prompts, direct generation often yields generic templates and unsupported persuasive claims. We study target-grounded, reference-guided landing-page generation, where a system must create an executable page for a new target by adapting reusable patterns from real pages without copying them. We introduce LandingBench, a reference-profile dataset that abstracts real landing pages into section sequences, layout patterns, tone descriptors, visual emphasis, and CTA structure. Building on LandingBench, we propose LandingAgent, a three-phase agentic framework that profiles the target, constructs a reference-guided wireframe, and refines the page through critique-guided polishing. We evaluate LandingAgent against direct prompting on faithfulness, conciseness, readability, aesthetics, and structural diversity. Experiments show improved target grounding, presentation quality, and layout diversity. Code is available at https://github.com/IAURAI/LandingAgent.

## Metadata
- **Published**: 2026-08-28T04:15:38Z
- **Authors**: Injun Baek, HyeongSeok Lee, Yearim Kim, Junhoo Lee, Nojun Kwak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27902v1)