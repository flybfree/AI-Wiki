---
title: Beyond Maliciousness: Static and Runtime Attack-Surface Profiling of Agent Skills
url: http://arxiv.org/abs/2610.19264v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_22-34-07Z_BeyondMaliciousness_StaticandRuntimeAttack_Surface.md
generated_at: 2026-10-14 21:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a two-phase attack-surface profiling methodology for agent skills—Markdown instruction documents that grant a tool-using agent authority upon installation—combining static bundle analysis with instrumented sandbox execution and model-based trace assessment. Applied to 6,309 marketplace listings, the study reveals that half carry shell-execution capability, a permission model exists but is largely inert, and declarations made by authors are frequently inaccurate, establishing that capability-oriented profiling must complement maliciousness detection.

## Key Takeaways
- Half of the 6,309 analyzed agent-skill listings carry evidence of shell-execution capability, with 35% showing filesystem read access, 31% each for filesystem write and network egress, and 13% for credential access; seven listings in ten possess at least one elevated capability. This represents the attack surface a user implicitly accepts at install time, almost none of which is visible during installation.
- The existing permission model is close to inert: authors may declare pre-approved tools in frontmatter, but this removes confirmation prompts rather than restricting reach. Only 770 of 6,061 parseable listings declare anything at all, the vocabulary cannot express credential or environment access, and nothing validates declarations against the actual bundle. Furthermore, 59% of declaring listings understate their bundle's true capabilities, with ClawHub under-declaring on 88% of its declarations versus 31% for skillsmp.
- Triage at the marketplace boundary cannot rely on what a listing declares; it must rest on what the bundle can actually do. The authors position capability-oriented attack-surface profiling as a necessary complement to existing maliciousness-detection approaches, arguing that absence of malicious intent does not equate to absence of risk.

## Context
As tool-using AI agents proliferate through marketplaces that distribute reusable instruction bundles, the security community has largely focused on detecting malicious or adversarial content within those bundles. This paper shifts the lens from intent-based threat detection to capability-based risk measurement, treating every installed skill as a potential expansion of the agent's operational authority regardless of authorial intent. It addresses a gap in the agent-security literature where static scanning and runtime sandboxing have been studied separately but not integrated into a unified profiling pipeline for marketplace-scale corpora.

## Implications
For practitioners deploying agent frameworks, the findings demonstrate that current marketplace permission declarations provide negligible security assurance and that install-time trust decisions are made almost entirely blind to the capabilities a skill bundle actually grants. Industry standards for agent-skill distribution will likely need to incorporate automated capability profiling at the marketplace boundary rather than relying on author self-declarations. For the research community, the methodology establishes a template for auditing agent ecosystems at scale and reframes the security question from "is this skill malicious?" to "what can this skill do, and should the user have been told?"

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19264v1)
