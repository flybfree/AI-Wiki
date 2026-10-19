---
title: Multimodal Filesystem Memory For Long-Horizon Embodied Agents
url: http://arxiv.org/abs/2610.22686v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_21-56-00Z_MultimodalFilesystemMemoryForLong_HorizonEmbodiedA.md
generated_at: 2026-10-18 20:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MFM, a multimodal filesystem memory architecture designed to give embodied agents structured, searchable memory across long-horizon tasks. Rather than retaining full interaction histories or compressing them into lossy summaries, MFM maintains complementary memory types—episodic, spatial, semantic, procedural, and working memory—linked through searchable textual records to underlying multimodal episodes. The approach yields measurable performance gains on Minecraft and computer-use benchmarks across three base models, with the strongest results showing a 26% improvement over the best baseline on the Ender Dragon task.

## Key Takeaways
- MFM decomposes agent memory into five complementary stores: episodic memory captures raw observations, actions, and outcomes; spatial memory ties experiences to specific locations; semantic and procedural memory distill general knowledge and reusable action strategies; and working memory holds the agent's current plans. This layered design avoids the failure modes of either unbounded history retention or lossy summarization.
- The architecture uses searchable textual records as a bridge between abstract knowledge and the original multimodal episodes, allowing agents to locate prior experiences through contextual cues and then inspect the original visual and spatial data when textual descriptions lack sufficient detail. Consolidation processes promote experience into higher-level knowledge while preserving references back to source episodes.
- Empirical results demonstrate clear gains: with GPT-6-Astra, MFM completes the "Mine Diamond from Scratch" task and reaches 16 of 24 milestones on the Ender Dragon task versus 12.7 for the best baseline. On CUABench-KiCad, MFM achieves a mean reward of 0.440 compared to 0.400 for the best baseline and 0.267 when no persistent memory is used, confirming that structured memory is a decisive factor in long-horizon performance.

## Context
Long-horizon embodied agents in robotics, game-playing, and computer-use automation face a fundamental memory bottleneck: full interaction logs grow unmanageably large, while compressed summaries discard the visual and spatial details needed for later decision-making. Prior work has explored vector-database retrieval, sliding-window context, or simple scratchpads, but none provide a unified architecture that simultaneously supports raw episodic recall, spatial grounding, procedural skill acquisition, and active planning. MFM addresses this gap by borrowing the filesystem metaphor from operating systems, treating memory as a structured, navigable resource rather than a flat buffer.

## Implications
For practitioners building autonomous agents that must operate over hundreds or thousands of steps—whether in simulation, physical robotics, or software automation—MFM offers a concrete, modular blueprint for memory management that can be layered on top of existing large language models without retraining. The demonstrated improvements across three different base models suggest the architecture is model-agnostic and broadly transferable. As embodied AI systems move toward longer, more complex tasks, structured multimodal memory of this kind may become a standard component of agent toolkits, influencing how developers design retrieval, consolidation, and planning pipelines in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22686v1)
