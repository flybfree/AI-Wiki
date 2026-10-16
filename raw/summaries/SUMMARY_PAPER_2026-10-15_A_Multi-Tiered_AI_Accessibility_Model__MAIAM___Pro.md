---
title: A Multi-Tiered AI Accessibility Model (MAIAM): Proportionate Access and Capability Limits for Comprehensive Frontier AI Safety
url: http://arxiv.org/abs/2610.20921v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_20-52-28Z_AMulti_TieredAIAccessibilityModel_MAIAM__Proportio.md
generated_at: 2026-10-15 22:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

This paper proposes the Multi-Tiered AI Accessibility Model (MAIAM), a framework that separates the question of how capable an AI system may become from the question of who may access a given capability and under what conditions. Rather than treating AI release as a binary choice between API-only access and open-weight publication, MAIAM sorts access into three tiers based on purpose, safety, and capability, arguing that accessibility should be proportional to the risk a system poses. The authors demonstrate that publishing frontier-class model weights eliminates all post-release safety levers available to developers, and they combine MAIAM with a SAFE AI Operating Point to create a two-part governance framework consisting of a Capability Boundary and an Accessibility Boundary.

## Key Takeaways

- MAIAM introduces three access tiers: Tier 1 (AI for Learning) is broadly accessible but deliberately capability-bounded; Tier 2 (AI for Exploration) serves research and development under registration, identity, and usage controls that tighten as capability increases; Tier 3 (Full-Scale Frontier AI) is available only through structured, recorded, and accountable access channels. The tiering principle is that accessibility must scale proportionally with capability, safety risk, and potential consequence.

- The authors argue that publishing frontier-class weights forfeits every safety lever a developer retains after release. They cite evidence that safety fine-tuning can be stripped from open-weight models for only a few hundred dollars, meaning that evaluating the base model provides little information about the safety properties of its derivatives. This undermines the assumption that open-weight release is inherently transparent or safe.

- The paper provides concrete criteria for assigning a system to a tier along four axes: capability, autonomy, domain-consequence, and usage/safety. It further integrates MAIAM with the SAFE AI Operating Point to form a two-part governance structure: a Capability Boundary that fixes the safety limits not to be crossed, and an Accessibility Boundary that fixes who may obtain a capability below that limit. The authors stress that capability limits alone are insufficient for safety; a tiered access regime administered by regulating bodies is also required.

## Context

The current AI policy debate has largely been framed as a binary dispute between closed API access and open-weight publication, a framing that conflates two distinct governance questions: how capable a system should be allowed to become, and who should be permitted to use a given capability. This conflation has left regulators and developers without structured tools for managing access across the full spectrum of AI capabilities. As frontier models grow more capable and autonomous, the stakes of uncontrolled access rise sharply, making a principled, tiered framework like MAIAM a necessary contribution to AI safety governance literature.

## Implications

For policymakers and regulatory bodies, MAIAM offers a concrete administrative structure for governing AI access that moves beyond the open-versus-closed dichotomy and instead ties access rights to measurable capability, autonomy, and domain-consequence thresholds. For AI developers and safety researchers, the finding that safety fine-tuning can be trivially stripped from open weights challenges the assumption that open-weight release is a neutral or transparent act, suggesting that post-release safety assurance requires active institutional oversight rather than passive availability. Industry practitioners deploying frontier systems will need to consider tiered access protocols as regulatory frameworks mature, and the paper signals that capability boundaries and accessibility boundaries must be jointly administered to achieve comprehensive frontier AI safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20921v1)
