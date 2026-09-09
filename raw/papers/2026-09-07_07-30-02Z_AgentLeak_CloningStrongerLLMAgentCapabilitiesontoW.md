---
title: AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing
published: 2026-09-07T07:30:02Z
authors: Xiaoting Lyu, Yuhong Wu, Yufei Han, Shichang Liu, Liang Zhang, Bin Wang, Bin Wang, Xiaobo Ma, Wei Wang
url: http://arxiv.org/abs/2609.07131v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentLeak: Cloning Stronger LLM Agent Capabilities onto Weaker Agents Beyond Skill Stealing

## Abstract
Large language model (LLM) agents increasingly achieve long-horizon tasks by combining foundation models with explicit skills and implicit procedural knowledge acquired through execution. The resulting task-solving capabilities have become valuable proprietary assets, raising a new security question: can a substantially weaker attacker-controlled agent acquire the capabilities of a stronger proprietary agent through limited black-box interaction? Existing skill-stealing attacks recover explicit skill artifacts, yet we show that artifact leakage does not necessarily transfer capability: a weaker agent may possess the same skills but still fail because it lacks procedural behaviors implicitly realized by the stronger agent. Our key insight is that the skill execution gap itself forms a leakage surface, where missing behaviors are exposed through observable differences between successful victim executions and failed attacker executions. Based on this, we present AgentLeak, a black-box capability-cloning attack that identifies capability-critical behaviors from these execution differences and incorporates them into attacker-side skills, while keeping the attacker's model, harness, and tools unchanged. Across 20 task scenarios comprising 600 instances, diverse agent systems, and multiple backbone models, AgentLeak improves task pass rates by over 40% compared with direct skill reuse and recovers more than 80% of the victim--attacker capability gap. Our findings reveal a confidentiality risk in LLM agents: protecting explicit artifacts alone is insufficient, as observable execution behavior can leak the procedural knowledge required to reconstruct proprietary task-solving capabilities in low-capability and attacker-controlled agents.

## Metadata
- **Published**: 2026-09-07T07:30:02Z
- **Authors**: Xiaoting Lyu, Yuhong Wu, Yufei Han, Shichang Liu, Liang Zhang, Bin Wang, Bin Wang, Xiaobo Ma, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07131v1)