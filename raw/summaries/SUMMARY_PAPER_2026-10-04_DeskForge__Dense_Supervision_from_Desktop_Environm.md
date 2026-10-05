---
title: DeskForge: Dense Supervision from Desktop Environments for Computer-Use Agents
url: http://arxiv.org/abs/2610.02320v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_18-00-05Z_DeskForge_DenseSupervisionfromDesktopEnvironmentsf.md
generated_at: 2026-10-04 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DeskForge introduces a controllable desktop environment that composes real applications and systematically varies their states, layouts, and appearances to generate large-scale, densely annotated supervision data for training computer-use agents. By fine-tuning four vision-language models on 200K grounding examples drawn from a 1.2M-observation corpus, the authors demonstrate substantial improvements in GUI grounding accuracy across five external benchmarks and meaningful gains in long-horizon task completion on WebArena-Infinity and OpenApps.

## Key Takeaways
- DeskForge-1M is a corpus of 1.2 million annotated desktop observations containing 159.7 million element instances, constructed by programmatically composing real applications and varying application states, content, window layout, appearance, and resolution. The environment fuses screenshots, accessibility trees, and window geometry into dense element annotations while recording the outcome of each executed action, providing a level of supervision density that existing training data lacks.
- Fine-tuning on just 200K grounding examples from DeskForge-1M yields consistent improvements across all four tested vision-language models on all five external GUI grounding benchmarks. For Qwen3.5-4B specifically, accuracy increases by 11.51 percentage points on ScreenSpot-Pro and 10.11 points on OSWorld-G, demonstrating that controlled synthetic variation in real desktop scenes transfers effectively to unseen evaluation conditions.
- The grounding improvements translate directly into downstream task performance: under a fixed planner, the fine-tuned action models solve significantly more long-horizon tasks, with Qwen3.5-4B increasing from 31 to 50 out of 119 WebArena-Infinity tasks and from 3 to 15 out of 100 OpenApps tasks, showing that better element grounding is a critical bottleneck in end-to-end computer-use agent performance.

## Context
Computer-use agents represent a rapidly growing frontier in applied AI, aiming to automate interactions with graphical user interfaces across operating systems and applications. A persistent bottleneck in this field is the scarcity of high-quality, densely annotated training data that reflects the visual complexity of real desktop environments, where overlapping windows, similar-looking controls, and multi-application layouts challenge even state-of-the-art vision-language models. DeskForge addresses this data gap by treating the desktop itself as a controllable generative environment rather than relying on static screenshots or limited human annotations, positioning it within the broader trend of synthetic data generation for embodied and interactive AI agents.

## Implications
For practitioners building autonomous agents that interact with desktop software, DeskForge offers a reproducible and scalable pipeline for generating training supervision without manual annotation, potentially reducing the cost and labor currently required to build GUI-grounding datasets. The open release of the framework code, dataset, and fine-tuned models lowers the barrier for researchers and companies to improve their own computer-use agents, and the demonstrated transfer from synthetic variation to real-world benchmarks suggests that controllable environment composition could become a standard data-engineering strategy for training agents that must operate in complex, visually cluttered software environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02320v1)
