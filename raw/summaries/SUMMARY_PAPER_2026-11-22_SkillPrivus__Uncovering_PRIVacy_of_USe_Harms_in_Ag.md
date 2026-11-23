---
title: SkillPrivus: Uncovering PRIVacy of USe Harms in Agentic Skills
url: http://arxiv.org/abs/2611.26747v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-19_19-43-43Z_SkillPrivus_UncoveringPRIVacyofUSeHarmsinAgenticSk.md
generated_at: 2026-11-22 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillPrivus is a static audit framework designed to evaluate privacy-of-use harms in installable agent skills before they are ever executed. By extracting data operations from both code and natural-language instructions, grounding them in source evidence, and applying Contextual Integrity principles, the framework identifies potential privacy violations in real-world skills from public marketplaces. Applied to 726 skills (563 handling personal data), SkillPrivus flags at least one potential violation in 307 skills (54.5%), with its judgments aligning with three blind human annotators on 83.2% of resolvable cases.

## Key Takeaways
- SkillPrivus operates as a pre-installation static audit tool, meaning it analyzes agent skills without executing them, extracting data operations from both code and natural-language instructions and grounding findings in source evidence. This approach enables proactive privacy assessment rather than reactive detection after a skill has already accessed user data, accounts, or files.
- The framework adapts Contextual Integrity, a privacy theory developed by Helen Nissenbaum, to evaluate whether data flows within agent skills are appropriate given the context of the task. This allows SkillPrivus to flag behaviors such as sensitive attribute inferences, information use beyond the stated task scope, and disclosures to unexpected recipients—harms that arise not from malicious intent but from ordinary skill functionality.
- Empirical validation on 726 real marketplace skills demonstrates that privacy-of-use harms are widespread: 54.5% of skills handling personal data contain at least one flagged potential violation. The 83.2% agreement rate with three blind human annotators on resolvable moves provides credibility to the automated judgments, suggesting the framework captures genuine privacy concerns rather than false positives.

## Context
As AI assistants increasingly rely on installable agent skills—modular packages of instructions and code that grant access to users' files, accounts, and personal data—the attack surface for privacy harm expands dramatically beyond the core model itself. Existing privacy research has largely focused on model training data or inference-time leakage, leaving a gap in understanding how third-party skill extensions introduce privacy-of-use harms through their operational data flows. SkillPrivus addresses this gap by treating skills as auditable artifacts and applying a structured privacy framework to their static content before any user interaction occurs.

## Implications
For practitioners building and deploying agentic AI systems, SkillPrivus offers a practical pre-installation screening mechanism that can be integrated into marketplace review pipelines or enterprise skill vetting processes, reducing the risk of silent privacy violations in everyday skill functionality. For the broader AI governance field, the finding that over half of personal-data-handling skills exhibit potential privacy-of-use harms underscores the need for standardized privacy auditing standards for agent skill ecosystems, analogous to security audits for software packages. Industry stakeholders in AI assistant platforms should consider adopting similar static analysis frameworks as part of their trust and safety infrastructure to protect users from privacy harms that arise not from adversarial attacks but from the mundane operation of installed skills.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.26747v1)
