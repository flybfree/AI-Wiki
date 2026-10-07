---
title: Can Agents Work for Everyone? Cross-User Reliability for Mobile GUI Agents in Personalized User Interfaces
url: http://arxiv.org/abs/2610.07972v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_08-38-30Z_CanAgentsWorkforEveryone_Cross_UserReliabilityforM.md
generated_at: 2026-10-06 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether mobile GUI agents can reliably complete tasks across different users when application interfaces are shaped by individual histories and preferences. It introduces PAIR to create controlled user-conditioned app states and RePAIR to train agents using cross-user differences in subgoal outcomes. Across six agents, the authors find large reliability gaps in personalized interfaces and show RePAIR improves success on unseen users.

## Key Takeaways
- The paper shows that mobile GUI agent performance is not stable across users: task success varies substantially, and subgoal achievement drops by 6.98 to 15.4 percentage points in user-conditioned UI contexts compared with less personalized settings.
- Personalization makes failures more severe when targets come from a user’s own content, with subgoal gaps increasing to 8.77 to 22.0 percentage points, indicating that agents struggle to distinguish intended personal items from similar alternatives.
- A major failure mode is selecting the wrong item before the intended target is exposed, and RePAIR addresses this by learning from cross-user variation, improving user-conditioned SAR by 5.87 points, all-success by 7.50 points, and overall task success by 9.42 points over supervised fine-tuning.

## Context
Mobile GUI agents are moving from static benchmark apps toward real devices where interface layout, content, and interaction history differ by user. This paper matters because it treats personalization as a reliability problem rather than a cosmetic variation, providing evaluation and training methods that expose cross-user failure modes.

## Implications
For practitioners, these findings suggest that GUI agents should be evaluated across user-conditioned states, not only across fixed tasks, before deployment on personal devices. The RePAIR result indicates that explicitly modeling cross-user differences can make agents more robust, which is important for assistants, accessibility tools, and automated mobile workflows that must work for many individual users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07972v1)
