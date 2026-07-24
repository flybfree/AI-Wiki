# Summary: 2026-07-17_01-55-17Z_SkillCorpus_ConsolidatingandEvaluatingtheOpenSkill.md
Saved: 2026-07-23 23:51
Source: 2026-07-17_01-55-17Z_SkillCorpus_ConsolidatingandEvaluatingtheOpenSkill.md
Model: None

---

## Summary  
The paper introduces SkillCorpus, a comprehensive framework that aggregates, curates, and evaluates the fragmented open‑source skill ecosystem for large language model agents. By filtering millions of candidate skills through a multi‑stage pipeline, it creates a high‑quality corpus organized by taxonomy and quality facets, then pairs each skill with a retrieval‑selection stack to match tasks. The study demonstrates that integrating this curated corpus yields measurable performance gains across three benchmark suites, confirming that the benefits are bounded both by coverage limits and by harness constraints. This work provides the first end‑to‑end evaluation of when a community‑driven skill corpus can improve real agent tasks.

## Key Contributions  
- [Finding 1] SkillCorpus consolidates ~821 k raw skills into 96 401 curated items using a taxonomy and three quality dimensions (utility, robustness, safety).  
- [Finding 2] The retrieval‑selection stack consistently matches task‑relevant skills to agents, achieving up to +7.5 percentage points on the SkillsBench benchmark.  
- [Finding 3] Gains are limited by coverage gaps in the skill ecosystem and by the specific harness used for evaluation.

## Methodology  
The authors built a multi‑stage pipeline: (1) crawling of public repositories, (2) deduplication and quality filtering via automated metrics, (3) classification into a 16‑class taxonomy, (4) scoring each skill on utility, robustness, and safety, (5) building a fine‑tuned retrieval system that selects skills per task. They evaluated the pipeline across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones, including a frontier robustness check.

## Results  
Across all experiments, SkillCorpus integration produced consistent improvements: +7.5 pp on SkillsBench, +4.2 pp on GDPVal, and +3.8 pp on QwenClawBench. The gains correlate with the proportion of tasks whose required skill is present in the curated set; when coverage exceeds ~90 % of needed skills, marginal gains diminish. Robustness checks showed no degradation under adversarial prompts.

## Significance  
SkillCorpus clarifies that a well‑curated community corpus can boost real‑world LLM agents, but its impact is bounded by how much the skill set covers and which evaluation harness is used. This insight guides researchers on when to invest in expanding or refining open skill repositories rather than simply adding more raw data.

## Related Concepts  
- Agent skills (SKILL files)  
- Retrieval‑augmented generation  
- Open‑source skill ecosystem  
- Curated corpora for LLM evaluation  
- Coverage vs. harness boundaries
