---
title: When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills
url: http://arxiv.org/abs/2610.37734v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-27_13-21-17Z_WhenSkillsTellAgentsNottoAsk_ALarge_ScaleStudyofOv.md
generated_at: 2026-11-01 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents the first large-scale empirical study of oversight-loosening directives embedded in agent skills, analyzing 1.53 million English-language skills from the GitSkills repository. The authors find that approximately 88,000 skills (about one in seventeen) contain directives that instruct agents to proceed without approval, bypass verification checks, or continue working without checking in, and that these directives are disproportionately associated with skills that execute shell code, install packages, or use sudo.

## Key Takeaways
- Roughly 88,000 out of 1.53 million skills contain at least one oversight-loosening directive, with permission flags being the most common mechanism and 70.1% of these directives applying unconditionally rather than being scoped to specific contexts such as CI pipelines. This means a single line in a widely copied skill can silently remove a safety checkpoint from every agent that loads it.
- Skills that run shell code, install packages, or use sudo have 1.7 to 1.8 times the odds of containing a loosening directive compared to skills with equivalent amounts of oversight language, and this association persists across all robustness checks. Crucially, these higher-risk skills do not compensate by adding more tightening directives, meaning the net oversight burden is reduced precisely where the operational risk is greatest.
- Loosening directives propagate through a small number of upstream skill families rather than through independent edits by adopters: 2.4% of skill families account for half of all copies of loosening-carrying skills, and 1.1% of distinct loosening units account for half of all occurrences. Existing open-source skill scanners detect at most 46% of these directives with precision below 0.4, whereas an LLM prompted with the authors' structured codebook achieves 61% recall at 0.71 precision.

## Context
Agent skills, structured as reusable instruction packages centered on a SKILL.md file, have become a dominant mechanism for extending the capabilities of AI agents across coding assistants, automation platforms, and enterprise workflows. Despite their ubiquity, the oversight directives embedded within these skills—lines that tell an agent to skip approval, bypass verification, or proceed autonomously—had never been systematically studied before this work. The paper fills a critical gap in understanding how safety and governance controls are silently modified at scale through the skill ecosystem.

## Implications
For practitioners deploying agent skills in production, the findings suggest that current scanning tools are insufficient to catch most oversight-loosening directives, leaving a significant blind spot in agent governance pipelines. The concentration of loosening in a tiny fraction of upstream skill families means that auditing a small number of widely adopted skills could dramatically reduce systemic risk. For the broader field, the work establishes a codebook and detection methodology that can be adopted by skill registries, CI/CD pipelines, and agent platforms to enforce oversight integrity as agent ecosystems continue to grow.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37734v1)
