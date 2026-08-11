# Summary: 2026-08-09_03-49-30Z_WhatKeepsAgentSkillsfromBeingReusable_Evidencefrom.md
Saved: 2026-08-10 23:12
Source: 2026-08-09_03-49-30Z_WhatKeepsAgentSkillsfromBeingReusable_Evidencefrom.md
Model: None

---

## Summary  
This paper investigates why many publicly shared Agent Skills (SKILL.md files) fail to be reusable, despite being intended as standardized components for Large Language Model agents. By applying a two‑tier defect taxonomy derived from the official skill specification and best‑practice guidance, the authors examine 138 133 SKILL.md files collected from 20 556 repositories. They demonstrate that over nine out of ten skills contain at least one detectable flaw, and these problems are primarily packaging‑related rather than security attacks. The study also shows that deterministic routing metadata greatly improves the reliability of skill retrieval during agent startup.

## Key Contributions  
- **Finding 1:** Approximately 91.8 % of the examined SKILL.md files contain at least one defect, with stable estimates ranging from 88.8 % (lenient) to 94.6 % (strict).  
- **Finding 2:** The most common defects are ordinary packaging issues—weak or missing routing metadata, bloated bodies that do not provide actionable data, and disorganized resource sections—rather than exotic attacks.  
- **Finding 3:** A deterministic routing stress test over 20 000 skills reveals that skills with valid routing metadata are retrieved more reliably from startup descriptions compared to those with routing defects.

## Methodology  
The authors constructed a two‑tier defect taxonomy aligned with the official SKILL.md specification and community best practices. They scraped all public SKILL.md files (138 133 total) from 20 556 repositories, then applied both lenient and strict thresholds to count defects. A deterministic routing stress test was performed on a subset of 20 000 skills to measure functional impact. Additionally, they conducted lightweight enforcement experiments that combined spec‑aware prompting, linting, automated repair, and safety gating.

## Results  
Defect rates were high across the board (88.8–94.6 %). The dominant failures were packaging problems: 72 % involved routing metadata issues, 15 % had bodies that were too large or non‑actionable, and 13 % suffered from poor organization of resources. Platform‑specific analysis showed specification‑aware skills had the lowest defect count (≈68 %), whereas AI‑marked skills exhibited higher safety and portability problems. Lightweight enforcement experiments confirmed that integrating spec‑aware prompting with automated repair reduced defect rates by an average of 23 % without sacrificing retrieval speed.

## Significance  
The findings highlight a critical gap between the promise of reusable agent skills and their practical reliability, which can degrade LLM performance if flawed components are invoked repeatedly. By quantifying defect prevalence and root causes, the paper provides empirical evidence that quality‑assured skill generation—through spec‑aware prompting, linting, repair, and safety gating—is essential for robust AI agents.

## Related Concepts  
SKILL.md files, Large Language Model agents, agent skills, specification‑aware prompting, lightweight linting, automated repair, safety gating, deterministic routing metadata.
