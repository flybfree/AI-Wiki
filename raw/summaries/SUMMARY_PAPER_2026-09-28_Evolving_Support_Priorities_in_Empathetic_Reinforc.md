---
title: Evolving Support Priorities in Empathetic Reinforcement Learning
url: http://arxiv.org/abs/2609.34249v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_03-55-21Z_EvolvingSupportPrioritiesinEmpatheticReinforcement.md
generated_at: 2026-09-28 23:17
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses a fundamental mismatch in empathetic reinforcement learning where fixed reward specifications fail to capture the dynamic evolution of support priorities as dialogues progress. The authors propose Context-Adaptive Rubric Evolution (CARE), a framework that generates context-adaptive rubrics at each turn by adjusting weights across cognitive, affective, and proactive empathy dimensions along with their fine-grained criteria. CARE serves as an adaptive reward interface trained via supervised fine-tuning and preference-based reinforcement learning, achieving state-of-the-art results on SentientBench, EQBench3, and EMPA benchmarks while demonstrating systematic adaptation to dialogue stages and user emotions.

## Key Takeaways
- Existing empathetic RL methods suffer from static reward functions that ignore how support needs change with the dialogue state, whereas CARE dynamically reweights cognitive, affective, and proactive empathy dimensions at every turn to align rewards with evolving context.
- The CARE rubric generator is trained using turn-level rubric supervision and human preference data through a pipeline of supervised fine

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34249v1)
