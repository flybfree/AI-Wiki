---
title: Which Agent's Skill Should Change? Group-Relative Credit Assignment for Evolving Multi-Agent Teams
url: http://arxiv.org/abs/2610.27227v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_19-55-19Z_WhichAgent_sSkillShouldChange_Group_RelativeCredit.md
generated_at: 2026-10-20 22:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces GRSE (Group-Relative Skill Evolution), a method for credit assignment in multi-agent language-model teams that determines which agent's skill should be revised by comparing multiple executions of the same question under identical skill libraries. Unlike prior approaches that credit skills merely for being present in successful trajectories, GRSE contrasts group executions to isolate true causal responsibility, yielding more accurate skill updates. On HotpotQA and LoCoMo benchmarks with two open-weight actors, GRSE outperforms the closest prior method (MASkills) on most categories, with the largest gains on multi-hop reasoning tasks, and demonstrates robustness against corrupted skill libraries by correctly identifying and correcting harmful skills.

## Key Takeaways
- GRSE addresses a fundamental flaw in existing skill-evolution methods: presence in a successful trajectory does not imply responsibility. A harmful skill that happens to appear in a successful run still receives positive credit under prior methods like MASkills, leading to incorrect reinforcement of bad behavior. GRSE instead uses group-relative comparison, inspired by GRPO's reward-normalization logic, to contrast multiple executions and assign credit only to agent-skill pairs that genuinely caused the outcome difference.
- On HotpotQA and LoCoMo benchmarks, GRSE achieves the largest performance gains on multi-hop questions (+6.7 and +3.2 F1 points over MASkills), and its improvements are grounded in better retrieval rather than hallucinated answers without evidence. Additionally, learned skills transfer across multi-hop tasks, suggesting the method produces generalizable behavioral improvements rather than task-specific memorization.
- GRSE demonstrates strong robustness to corrupted skill libraries: when starting from planted harmful skills, it correctly credits every planted skill with the right sign and recovers the performance of a clean library (+6.3 points), whereas MASkills misattributes two harmful skills and actually falls below its own starting performance, highlighting the practical danger of naive presence-based credit assignment.

## Context
Multi-agent systems built on language models increasingly rely on reusable skill libraries rather than weight updates to improve team performance, making credit assignment a critical bottleneck for autonomous self-improvement. This paper sits at the intersection of reinforcement learning credit assignment, multi-agent coordination, and prompt-based skill evolution, extending ideas from GRPO (Group Relative Policy Optimization) into the domain of discrete skill revision. It matters because as agentic systems scale to teams of specialized LLMs, the ability to correctly identify which component caused a failure or success becomes the linchpin of safe, self-directed improvement without human oversight.

## Implications
For practitioners deploying multi-agent LLM pipelines, GRSE offers a practical mechanism to audit and repair skill libraries automatically, reducing the risk of compounding errors from misattributed credit that silently degrade team performance over time. For the research community, the group-relative comparison paradigm suggests a general recipe for causal attribution in any system where multiple components contribute to a shared reward, potentially informing safer alignment strategies and more reliable autonomous agent training. The demonstrated robustness to corrupted libraries is particularly relevant for production systems where skill libraries may accumulate harmful entries through prior errors, providing a principled recovery path rather than requiring manual curation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27227v1)
