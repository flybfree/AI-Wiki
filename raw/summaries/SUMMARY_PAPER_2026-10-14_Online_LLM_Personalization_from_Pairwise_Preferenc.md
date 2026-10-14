---
title: Online LLM Personalization from Pairwise Preferences Across Users
url: http://arxiv.org/abs/2610.17203v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_17-59-21Z_OnlineLLMPersonalizationfromPairwisePreferencesAcr.md
generated_at: 2026-10-14 01:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel framework for inference-time personalization of large language models by treating the problem as a contextual dueling bandit, where a system sequentially selects from a fixed set of persona-based prompts to match each user's hidden stylistic preferences. The authors release a reproducible benchmark built around a tutoring case study with six teaching styles and LLM-simulated student preferences, and propose a baseline algorithm that learns a mixture prior across users and adapts within each session, achieving 44–48% reduction in excess regret compared to random pair selection.

## Key Takeaways
- The paper formalizes LLM personalization as a variant of the contextual dueling bandit problem, where the learner has no prior preference data, must adapt within each user session, and exploits shared information across users. The objective is cumulative strong regret, which sums the utility gaps of both displayed responses relative to the user's best available option, making it a more demanding metric than standard bandit regret.
- The authors construct a reproducible preference benchmark centered on a tutoring scenario, containing educational questions, LLM-generated answers in six distinct teaching styles, and pairwise judgments from LLM-simulated students with hidden preference profiles. Bradley-Terry models are fitted to these judgments to produce reference utilities, enabling rigorous regret evaluation and reproducible experimentation.
- The proposed baseline algorithm learns a mixture prior over user types from completed sessions and adapts to each new user within the session. On held-out students and topics, it removes 44–48% of the excess regret of random pair selection and achieves more than half the performance of a per-user linear oracle fitted in hindsight, demonstrating meaningful cross-user transfer without requiring per-user training data.

## Context
Personalization of LLM outputs has become a critical challenge as deployment scales to millions of users with diverse communication preferences, yet most existing approaches rely on offline fine-tuning or static system prompts. This paper bridges the gap between bandit learning theory and practical LLM deployment by providing a formal online learning framework, a concrete benchmark, and a transferable algorithm. It addresses the realistic constraint that preference data is sparse, noisy, and revealed only through pairwise comparisons during interaction, which mirrors how real users actually engage with AI systems.

## Implications
For practitioners building personalized AI assistants, tutoring platforms, or content recommendation systems, this work provides both a benchmark for evaluating personalization algorithms and a practical baseline that transfers knowledge across users without requiring per-user data collection. The strong regret formulation and the cross-user mixture prior approach suggest that systems can achieve meaningful personalization with very limited interaction data, which is essential for cold-start scenarios in production deployments. The released code, prompts, and dataset lower the barrier for reproducible research in this emerging subfield of adaptive LLM systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17203v1)
