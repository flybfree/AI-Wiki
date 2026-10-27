---
title: Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation
url: http://arxiv.org/abs/2610.35426v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_13-33-07Z_Intent_PreservingAdversarialUserSimulationforMulti.md
generated_at: 2026-10-27 00:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces StressSim, an intent-preserving adversarial user simulator framework designed to stress-test multi-turn LLM agents by generating challenging yet valid user interactions that reduce task success without altering the user's underlying goal. The framework uses a genetic prompt-optimisation loop to evolve adversarial planner prompts, and evaluation on MultiWOZ and tau-bench domains demonstrates that StressSim exposes robustness gaps missed by standard simulators, with pass^4 scores dropping by up to 69% on frontier models while maintaining goal preservation within 10%.

## Key Takeaways
- StressSim optimises a high-level adversarial plan for each task instance through a genetic prompt-optimisation loop that leverages rollout traces, granular task-completion signals, and validity feedback. This approach favours conversations that reduce agent task success while preserving the user's original goal, distinguishing it from hand-designed non-collaborative behaviours or standard cooperative simulators that overestimate agent performance.
- On tau-bench retail and airline domains, StressSim caused pass^4 scores to decrease by up to 69% on gemini-3.8-flash and 62% on gpt-5.6-sol, revealing substantial robustness gaps in frontier LLMs that standard evaluation pipelines fail to detect. Goal preservation performance degraded by at most 10%, confirming that adversarial stress-testing does not distort user intent.
- The framework achieves these results through lightweight prompt optimisation alone with a budget of 20 rollouts per task, requiring no model fine-tuning. Sensitivity analysis indicates that increasing the optimisation budget further decreases task success, suggesting diminishing returns and practical feasibility for deployment.

## Context
Multi-turn agent evaluation has become a critical bottleneck in assessing the reliability of LLM-based assistants deployed in customer service, travel booking, and retail scenarios. Standard evaluation pipelines rely on LLM-based simulated users that tend toward excessive cooperativeness, inflating reported agent performance and masking failure modes that would surface in real-world interactions. StressSim addresses this gap by introducing a principled adversarial simulation methodology that sits between fully cooperative simulators and hand-crafted adversarial scripts, offering a scalable middle ground for rigorous agent evaluation.

## Implications
For practitioners deploying multi-turn agents in production environments, StressSim provides a practical, fine-tuning-free method to uncover hidden failure modes before agents face real users, potentially reducing costly post-deployment debugging and improving user trust. For the broader AI evaluation community, the paper demonstrates that adversarial stress-testing can be achieved through prompt-level optimisation rather than architectural changes, making it accessible to teams without extensive compute resources. The findings also raise important questions about the validity of current benchmark scores reported for frontier models, suggesting that reported pass rates may substantially overstate real-world agent reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35426v1)
