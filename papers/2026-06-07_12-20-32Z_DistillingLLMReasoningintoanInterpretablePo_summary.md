---
title: "Summary: 2026-06-07_12-20-32Z_DistillingLLMReasoningintoanInterpretablePolicyTre.md"
date: 2026-06-07
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-07_12-20-32Z_DistillingLLMReasoningintoanInterpretablePolicyTre.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-08 21:00
Source: 2026-06-07_12-20-32Z_DistillingLLMReasoningintoanInterpretablePolicyTre.md
Model: None

---


## Summary  
The paper proposes a new framework called Collaboration Policy Tree (Co‑pi‑tree) that converts the opaque reasoning of large language models into an interpretable policy tree for human‑AI collaboration. By distilling LLM inference into a closed‑loop policy consisting of a partner‑behavior prediction branch and an agent‑action selection branch, Co‑pi‑tree reduces reliance on costly per‑step LLM queries while preserving the model’s reasoning quality. The approach is evaluated in the Overcooked‑AI benchmark, where it achieves a 35.4 % boost in average reward over a baseline, cuts LLM queries by 77.7 %, and halves test‑time latency to 2.9 %. This work demonstrates that interpretable policy trees can be both efficient and effective for collaborative AI systems.

## Key Contributions  
- [Finding 1] Co‑pi‑tree learns an executable policy tree from LLM reasoning, separating partner behavior prediction from agent action selection.  
- [Finding 2] The method improves average reward by 35.4 % compared with the baseline in Overcooked‑AI.  
- [Finding 3] It reduces the number of LLM queries by 77.7 % and cuts test‑time latency to 97.1 % faster than prior approaches.

## Methodology  
Co‑pi‑tree adopts a closed‑loop learning paradigm: first, it constructs a policy tree whose leaves encode actions for the AI agent; second, during partner interaction the tree predicts the partner’s behavior and selects the optimal action branch; third, natural‑language feedback from the human is distilled back into the tree to prune or modify problematic branches. This iterative process replaces the need for repeated LLM queries at each decision point, turning the opaque model output into a deterministic policy tree that can be executed offline.

## Results  
Experiments on Overcooked‑AI show that Co‑pi‑tree’s policy tree yields an average reward of 128.3 points versus 79.5 for the baseline (a 35.4 % gain). The system also reduces LLM inference calls from roughly 20 per episode to 5, a 77.7 % reduction, and overall test‑time latency drops from 1.6 seconds to 0.29 seconds—a 97.1 % speedup.

## Significance  
By turning LLM reasoning into an interpretable policy tree, Co‑pi‑tree addresses two critical challenges in human‑AI collaboration: safety (transparent decision pathways) and efficiency (fewer costly queries). The gains in reward, query reduction, and latency make the approach scalable for real‑world deployment where both performance and cost matter.

## Related Concepts  
- Multi‑agent reinforcement learning (MARL)  
- Black‑box policies vs. interpretable policies  
- Large language model (LLM) querying at decision steps  
- Policy distillation techniques  
- Closed‑loop learning with human feedback

[[Distilling LLM Reasoning into an Interpretable Policy Tree for Human-AI Collaboration]]