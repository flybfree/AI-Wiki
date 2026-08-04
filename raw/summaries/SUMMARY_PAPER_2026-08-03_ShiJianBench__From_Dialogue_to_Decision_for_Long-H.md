---
title: ShiJianBench: From Dialogue to Decision for Long-Horizon Evaluation of Investment Advisors
url: http://arxiv.org/abs/2608.01204v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_12-41-47Z_ShiJianBench_FromDialoguetoDecisionforLong_Horizon.md
generated_at: 2026-08-03 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ShiJianBench, an offline evaluation framework that tracks how conversational investment advisors shape long‑term investor behavior by matching advisor responses to simulated user trajectories under fixed market feedback. Experiments on Chinese fund data from 2021 to 2026 reveal a stable group of LLM advisors that excel at personalized content while also delivering effective long‑horizon outcomes, highlighting the gap between high‑quality replies and real impact.

## Key Takeaways
- The framework uses a multi‑agent investor simulator with evolving state variables, memory, and dialogue‑grounded updates to capture how advisor language influences decisions over time.  
- Advisor policies are judged on three dimensions: investor‑side trajectory outcomes, service‑side compliance, and content‑side quality, all under a hard gate.  
- The results show that the best LLM advisors combine strong personalization with measurable long‑term behavioral improvements, indicating that response quality alone is insufficient for effective intervention.

## Context
Current AI research often measures conversational agents by isolated metrics such as response accuracy or immediate user satisfaction, overlooking how those interactions ripple into downstream actions. This work addresses a critical blind spot in AI safety and impact assessment by modeling the full decision chain from dialogue to investment behavior.

## Implications
For practitioners, ShiJianBench provides a concrete benchmark for evaluating conversational advisors that matters beyond chat quality, guiding design toward interventions that truly affect long‑term outcomes. The methodology can be adapted across domains where user guidance influences complex decisions, reinforcing the need for holistic performance evaluation in AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01204v1)
