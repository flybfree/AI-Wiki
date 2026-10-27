---
title: SEEK: Skill Extraction with Evolving Knowledge against Frontier Science Agents
url: http://arxiv.org/abs/2610.34365v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_15-19-13Z_SEEK_SkillExtractionwithEvolvingKnowledgeagainstFr.md
generated_at: 2026-10-26 23:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces SEEK (Skill Extraction with Evolving Knowledge), a black-box, self-evolving red-teaming agent designed to extract protected domain skills from science-agent platforms through iterative probing. The authors construct a benchmark of 40 protected skills across eight science-agent platforms and demonstrate that leakage is pervasive, with all platforms leaking at least one skill and four achieving 100% attack success under a single direct request. SEEK outperforms bandit-guided probing by reducing mean first-success rounds by 31.8% to 38.2% and can extract skills even against platforms that block all three benchmark protocols.

## Key Takeaways
- All eight tested science-agent platforms (100%) leak at least one protected skill, and four platforms reach 100% attack success under a single direct request, demonstrating that current science agents do not reliably protect their modular skill capabilities from inference through user-visible interactions.
- SEEK operates as a self-evolving red-teaming agent that consolidates response-derived evidence in persistent memory and evolves reusable attack skills using only user-visible responses, achieving 100% attack success on 12 skills from SpatialAgent and Biomni while reducing mean first-success rounds by 31.8% and 38.2% relative to bandit-guided probing baselines.
- Even against a confidentiality policy that blocks all three benchmark protocols (direct, fixed-strategy, and bandit-guided probing), SEEK still successfully extracts one of six protected skills, showing that adaptive multi-turn attackers can bypass static defense mechanisms.

## Context
Science agents increasingly package domain expertise as reusable modular skills that plan analyses, select tools, and execute workflows, creating a confidentiality risk where the interactions delivering a skill's capability can inadvertently reveal the skill itself. This paper addresses a critical gap in AI safety and intellectual property protection by systematically benchmarking skill leakage across both open- and closed-source platforms and proposing an adaptive attack framework that mirrors real-world adversarial probing scenarios.

## Implications
For practitioners deploying science agents in commercial or research settings, these findings indicate that current confidentiality mechanisms are insufficient against adaptive, multi-turn attackers, and defenses must be evaluated against evolving probing strategies rather than static protocols. Industry stakeholders relying on proprietary skill modules as competitive advantages should anticipate that black-box access alone provides limited protection, necessitating architectural changes or policy-level safeguards to preserve the secrecy of domain-specific capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34365v1)
