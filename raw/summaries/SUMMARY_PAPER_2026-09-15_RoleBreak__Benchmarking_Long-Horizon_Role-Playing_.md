---
title: RoleBreak: Benchmarking Long-Horizon Role-Playing Robustness in Spoken Dialogue
url: http://arxiv.org/abs/2609.16614v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-15_04-19-53Z_RoleBreak_BenchmarkingLong_HorizonRole_PlayingRobu.md
generated_at: 2026-09-15 20:15
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces RoleBreak, an open benchmark designed to evaluate the robustness of long-horizon role-playing in spoken dialogue systems, addressing limitations in existing character-centric and short-duration datasets. Through extensive evaluations across nine speech-to-speech configurations, the study reveals that while current models maintain semantic role adherence better than vocal emotion, they struggle significantly with consistency over extended interactions, often failing within just ten turns despite LLM scaling efforts.

## Key Takeaways
- Current spoken dialogue models exhibit a significant disparity in capabilities, demonstrating substantially stronger semantic role adherence compared to the accurate generation of expressive vocal emotions, indicating a persistent gap in multimodal expressiveness despite advancements in language understanding.
- Long-horizon robustness remains critically brittle; even the most advanced systems evaluated encounter persona and safety failures after an average of only 10.4 and 11.6 turns respectively, and while scaling the underlying LLM improves semantic consistency, it yields negligible improvements in vocal emotion generation.
- User vocal cues exert a direct influence on role-playing behavior independent of linguistic content, as evidenced by findings that variations in user emotional tone affect system responses even when the textual input remains fixed, highlighting the importance of cross-modal interaction dynamics in spoken dialogue.

## Context
As speech-to-speech models gain traction for

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16614v1)
