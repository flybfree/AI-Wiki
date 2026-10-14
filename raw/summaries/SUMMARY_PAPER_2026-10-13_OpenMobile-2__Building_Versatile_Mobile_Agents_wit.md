---
title: OpenMobile-2: Building Versatile Mobile Agents with Scalable Environments and App-Native Tools
url: http://arxiv.org/abs/2610.14157v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-09_17-26-38Z_OpenMobile_2_BuildingVersatileMobileAgentswithScal.md
generated_at: 2026-10-13 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
OpenMobile-2 is a near-frontier mobile agent system that introduces fully open training environments, scalable data pipelines, and a novel hybrid interaction paradigm combining GUI actions with app-native tool calls. The paper presents MobileGym++, a simulated environment featuring 35 realistic commercial-style apps with cross-app workflows, alongside a curated dataset of nearly 12K supervised trajectories and over 2K verifiable reinforcement learning tasks. The resulting agent achieves competitive performance on established benchmarks such as AndroidWorld (79.9) and MobileWorld (50.4), while demonstrating strong transfer to real-device scenarios, nearly doubling performance on SPA-Bench from 31.9 to 59.6.

## Key Takeaways
- MobileGym++ represents a major advance in mobile agent training infrastructure, offering 35 functionally rich commercial-style apps with cross-app workflows and full controllability for reset and verification. Combined with newly configured Android emulator apps, this creates a diverse playground spanning over 110 apps, addressing a critical bottleneck in mobile agent research where realistic, controllable training environments have been scarce.
- The paper contributes the largest open collection of verifiable RL training data for mobile agents, comprising over 2K executable tasks with automatic reward signals, alongside nearly 12K mobile interaction trajectories for supervised fine-tuning. This open-data approach at scale is designed to lower barriers for the broader research community to train and evaluate mobile agents without proprietary data constraints.
- A novel hybrid GUI and app-native tool use paradigm is introduced, where apps expose selected functionalities as callable tools alongside their graphical interfaces, enabling agents to interleave GUI actions and tool calls within a single task. Over 300 carefully scoped tools across 50+ apps are implemented in MobileGym++, and MobileGym++ Bench supports evaluation of both GUI-only and hybrid GUI-tool settings on a shared task suite, enabling systematic comparison of interaction strategies.

## Context
Mobile agents have emerged as a critical frontier in AI research, aiming to automate complex smartphone interactions that span multiple applications, require long-horizon planning, and demand precise GUI manipulation. Prior work has been constrained by limited training environments, closed-source data, and a rigid GUI-only interaction paradigm that does not reflect how modern apps increasingly expose structured APIs. OpenMobile-2 addresses these gaps by providing open, scalable infrastructure and exploring a hybrid interaction model that mirrors the evolving software ecosystem where both visual interfaces and programmatic tool access coexist.

## Implications
For the AI research community, OpenMobile-2 establishes a reproducible, open benchmark and training pipeline that could accelerate progress in mobile agent development by removing data and environment bottlenecks. For industry practitioners and app developers, the hybrid GUI-tool paradigm signals a shift toward designing mobile applications with agent-accessible tool interfaces alongside traditional UIs, potentially reshaping how mobile automation, accessibility, and AI-assisted workflows are built. The near-doubling of real-device performance on SPA-Bench suggests that simulated training environments with app-native tools can meaningfully transfer to practical deployment, offering a viable path toward commercially useful mobile AI assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14157v1)
