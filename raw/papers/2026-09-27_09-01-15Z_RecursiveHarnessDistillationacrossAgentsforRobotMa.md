---
title: Recursive Harness Distillation across Agents for Robot Manipulation
published: 2026-09-27T09:01:15Z
authors: Seungyeon Kim, Junhoo Lee, Minkyu Kim, Baekseung Kim, Nojun Kwak
url: http://arxiv.org/abs/2609.33378v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recursive Harness Distillation across Agents for Robot Manipulation

## Abstract
A central goal in robotics is to enable manipulation across changing tasks and environments. Vision-language-action (VLA) models provide broad manipulation capabilities but can struggle when execution requires diagnosing failures and adapting behavior. Strong agents can discover effective interventions through interaction with these policies. We propose Recursive Harness Distillation to accumulate this experience as reusable guidance across agents. A strong agent distills its experience into a playbook for a light agent, then recursively refines the playbook using the light agent's execution feedback. The resulting playbook enables agents to reuse accumulated intervention knowledge in new task instances without updating model parameters. In real-world manipulation, the harness improves success from 37.3% to 64.0%. On SimplerEnv Bridge, the light agent with the playbook achieves 66.7% success, compared with 41.7% for the GR00T-only baseline, and outperforms the strong agent without a playbook. The same playbook also benefits the strong agent, which reaches 79.2% success. These results demonstrate the feasibility of harness distillation for robotics: intervention experience can be accumulated, refined through execution, and reused across agents to improve manipulation.

## Metadata
- **Published**: 2026-09-27T09:01:15Z
- **Authors**: Seungyeon Kim, Junhoo Lee, Minkyu Kim, Baekseung Kim, Nojun Kwak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33378v1)