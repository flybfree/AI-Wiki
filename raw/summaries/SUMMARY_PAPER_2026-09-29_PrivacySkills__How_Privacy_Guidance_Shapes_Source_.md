---
title: PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents
url: http://arxiv.org/abs/2609.35937v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_15-22-09Z_PrivacySkills_HowPrivacyGuidanceShapesSourceSelect.md
generated_at: 2026-09-29 20:51
model: qwen3.6-35b-a3b
---

## Summary
This study introduces PrivacySkills, a controlled framework designed to evaluate how different forms of privacy guidance influence LLM agents' decisions when selecting information sources for task completion. The research demonstrates that while system-level instructions alone have limited impact, combining skill-level intrusiveness labels with system instructions significantly reduces the agent's reliance on confidential data sources by approximately half compared to baseline conditions without guidance.

## Key Takeaways
- Without privacy guidance, agents frequently access confidential sources even when safer alternatives exist; specifically, agents accessed confidential data in 30% of runs when users were available and this rate jumped to 45% when users were unavailable, indicating a strong preference for direct data retrieval over user interaction or public search.
- The effectiveness of privacy interventions varies by implementation method; system-level instructions produced limited reductions in confidential access, while skill-level metadata labels labeled with intrusiveness information yielded a modest average reduction to 24%, suggesting that granular, task-specific cues are more effective than general prompts.
- Combining system-level instructions with skill-level privacy annotations roughly halves the rate of confidential source access compared to no guidance, highlighting a synergistic effect, whereas framing tasks as urgent had no detectable impact on agent behavior across the evaluated models.

## Context
As LLM agents become increasingly autonomous in handling sensitive user data, understanding the mechanisms that drive privacy violations is critical for developing trustworthy AI systems. This work addresses a gap in existing literature by moving beyond documenting failures to systematically analyzing how specific presentation formats of privacy guidance shape agent decision-making processes across diverse information acquisition pathways.

## Implications
These findings suggest that developers should prioritize embedding granular privacy annotations directly into agent skill specifications rather than relying solely on high-level system prompts to mitigate data exposure risks. Furthermore, the results advocate for standardized evaluation frameworks like PrivacySkills to rigorously test and compare privacy-preserving interventions across different model architectures before deployment

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35937v1)
