---
title: AgentSafeEvo: Adversarial Co-Evolution for LLM Agent Safety
url: http://arxiv.org/abs/2610.19422v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_02-13-29Z_AgentSafeEvo_AdversarialCo_EvolutionforLLMAgentSaf.md
generated_at: 2026-10-14 20:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AgentSafeEvo introduces a co-evolutionary reinforcement learning framework designed to improve the safety of large language model agents that interact with external tools across multi-turn tasks. The framework frames safety training as an attacker-defender game where the attacker generates adversarial agent tasks targeting weaknesses in tool use, while the defender learns to complete those tasks safely. Experiments demonstrate that the method enhances adversarial robustness across diverse attack types without degrading general agent capabilities.

## Key Takeaways
- The framework addresses a critical gap in existing adversarial safety research, which has largely focused on language-level safety or indirect prompt injection in web-based tasks. AgentSafeEvo extends adversarial co-evolution to the full agent setting, covering malicious content embedded in user queries, tool descriptions, and environment observations that can manipulate agent decisions and induce unsafe actions across diverse task types.
- A novel mechanism called learnability-guided task weighting uses within-task defender-reward variability to dynamically adjust each task's contribution to both attacker and defender policy updates. This ensures training focuses on tasks where the defender shows meaningful performance variation, making the co-evolution process more efficient and targeted rather than uniformly weighting all adversarial tasks.
- The attacker-defender game is built on reinforcement learning, where the attacker learns to construct adversarial agent tasks that expose weaknesses in the defender's tool-use behavior, and the defender learns to complete tasks safely under these adversarial conditions. Extensive experiments on both agent safety benchmarks and general capability benchmarks confirm that adversarial robustness improves while general agent capabilities are maintained, avoiding the common trade-off seen in safety fine-tuning approaches.

## Context
As LLM agents increasingly deploy in production systems involving tool use, code execution, and multi-step planning, their safety surface expands far beyond simple text generation. Prior adversarial safety methods such as adversarial training and prompt injection defenses have been effective for single-turn language safety but do not adequately address the compound risks introduced by tool interactions, environment observations, and multi-turn decision chains. AgentSafeEvo represents a shift toward treating agent safety as a dynamic, task-level adversarial problem rather than a static input-filtering problem, aligning with the broader research movement toward robust, capability-preserving safety training in agentic systems.

## Implications
For practitioners deploying LLM agents in enterprise workflows, AgentSafeEvo offers a training paradigm that hardens agents against adversarial manipulation of tools and environments without sacrificing task performance, which is essential for safe autonomous operation in domains like software engineering, data analysis, and customer-facing automation. For the research community, the learnability-guided task weighting mechanism provides a generalizable technique for adaptive curriculum construction in adversarial training, potentially transferable to other safety and robustness settings beyond agent tasks. The work signals that co-evolutionary RL can serve as a scalable safety infrastructure for the next generation of agentic AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19422v1)
