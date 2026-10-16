---
title: ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews
url: http://arxiv.org/abs/2610.21042v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_00-34-38Z_ReviewPilot_AMulti_AgentSystemforScreeningandDataE.md
generated_at: 2026-10-15 23:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReviewPilot is a conversational multi-agent system designed to automate the full PRISMA workflow for systematic literature reviews, spanning both paper screening and structured data extraction from included studies. The system addresses a critical gap in existing LLM-based deep research tools by recording exclusion decisions with justifications and tracing every extracted value back to its source. Evaluated on epidemiological expert reviews, ReviewPilot outperforms both single-prompt LLM baselines and the AgentSLR framework across three different LLM backends, achieving screening macro F1 scores up to 0.776 and extraction F1 scores up to 0.788.

## Key Takeaways
- ReviewPilot introduces a conversational, multi-agent architecture that allows researchers to tailor inclusion/exclusion criteria and extraction schemas through natural dialogue, while a persistent project memory preserves all configuration changes and revisions throughout the review process. This makes the system adaptable to domain-specific review protocols without requiring re-engineering for each new project.
- Unlike prior LLM-based literature tools that silently discard excluded papers or produce untraceable extracted values, ReviewPilot attaches an explicit reason to every screening decision and a verifiable source citation to every extracted data point. This auditability requirement is essential for systematic reviews, where transparency and reproducibility are foundational to the PRISMA methodology.
- The system was validated not only on epidemiological reviews but also through case studies in biomedicine and human-computer interaction, demonstrating close agreement with human annotators and suggesting that the multi-agent design generalizes across distinct research domains. The authors report performance gains over AgentSLR and single-prompt baselines across three LLM backends, indicating robustness against model-specific biases.

## Context
Systematic reviews remain the gold standard for evidence synthesis across medicine, social sciences, and engineering, yet they are extraordinarily labor-intensive, often requiring hundreds of hours of manual screening and data extraction. The rise of LLM-powered research assistants has raised the possibility of automating portions of this workflow, but existing tools such as AgentSLR and generic deep-research agents lack the structured, auditable decision trails that rigorous review protocols demand. ReviewPilot sits at the intersection of multi-agent orchestration, retrieval-augmented generation, and domain-specific workflow automation, representing a step toward making LLM assistance compatible with the accountability standards that govern published evidence syntheses.

## Implications
For academic researchers and evidence-synthesis practitioners, ReviewPilot offers a practical pathway to reduce the screening and extraction burden of systematic reviews while preserving the transparency that peer reviewers and regulatory bodies require. For the broader AI research community, the paper demonstrates that multi-agent architectures with persistent memory and per-decision provenance tracking can outperform monolithic prompting strategies, suggesting a design principle applicable beyond literature review to any task requiring traceable, multi-step reasoning. The open-source release of the code further lowers the barrier for domain specialists to adapt the system to their own review protocols, potentially accelerating evidence-based decision-making in public health, biomedical research, and technology policy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21042v1)
