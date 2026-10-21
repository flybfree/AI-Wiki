---
title: AutoRedClaw: Automated Red-Teaming for Claw-Style Agents
published: 2026-10-19T20:15:39Z
authors: Hao Li, Tongyan Hu, Weidi Luo, Shanghao Shi, Xiaogeng Liu, Aiden Suh, Yulong Cao, Ning Zhang, William Yeoh, Yevgeniy Vorobeychik, Chaowei Xiao
url: http://arxiv.org/abs/2610.27244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoRedClaw: Automated Red-Teaming for Claw-Style Agents

## Abstract
Agent systems are shifting from task-scoped tool-use agents to persistent, personalized assistants such as OpenClaw. These claw-style agents maintain configuration files (e.g., AGENTS.md), long-term memory, and reusable skills. Once poisoned, this persistent state is repeatedly reloaded into the agent's context, creating persistent threats across tasks and sessions. Existing security evaluation systems struggle to evaluate these complex claw-style systems since they rely heavily on manually constructed test cases and environments, which limits their scale and coverage; in addition, these manually designed cases quickly become outdated as agents evolve, and their evaluation settings leave a gap with how claw-style agents are deployed in practice. To address this, we introduce AutoRedClaw, an automated red-teaming framework that generates end-to-end attacks together with the environments needed to execute them. AutoRedClaw combines a strict quality-checking protocol with execution-based validation to ensure the correctness, realism, and effectiveness of generated samples, and adopts task-driven environment construction to keep costs low. To achieve broad coverage, it organizes generation along risk categories, attack strategies, attack stages, and attack surfaces, and uses experience-guided exploration to steer generation toward under-explored regions. AutoRedClaw achieves an effective attack rate above 30% at less than $0.10 per successful sample. From its outputs, we construct RedClaw-Bench, a 330-case benchmark that yields substantially higher attack success rates (ASRs) than AgentDojo, AgentDyn, and DTap. Across seven harnesses and four frontier models, most agent systems exceed 50% ASR, showing that our red-teaming pipeline provides a strong evaluation signal even for the most advanced agent systems. Our code and benchmark are released at https://github.com/SaFo-Lab/AutoRedClaw.

## Metadata
- **Published**: 2026-10-19T20:15:39Z
- **Authors**: Hao Li, Tongyan Hu, Weidi Luo, Shanghao Shi, Xiaogeng Liu, Aiden Suh, Yulong Cao, Ning Zhang, William Yeoh, Yevgeniy Vorobeychik, Chaowei Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27244v1)