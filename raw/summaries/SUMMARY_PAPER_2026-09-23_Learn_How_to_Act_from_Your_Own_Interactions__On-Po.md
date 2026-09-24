---
title: Learn How to Act from Your Own Interactions: On-Policy Self-Distillation for GUI Agents
url: http://arxiv.org/abs/2609.27307v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_03-38-11Z_LearnHowtoActfromYourOwnInteractions_On_PolicySelf.md
generated_at: 2026-09-23 22:18
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces GUI-SD-v2, an advancement of the On-Policy Self-Distillation (OPSD) method designed to improve how Graphical User Interface (GUI) agents handle complex, multi-turn interactions with software environments. By addressing the limitations of current self-teachers—specifically their struggle with long-horizon reasoning and privilege-following—the authors propose a two-stage training framework that enhances both the agent's ability to follow instructions and its capacity to retain task-relevant information.

## Key Takeaways
- **Overcoming OPSD Limitations:** While existing OPSD methods have succeeded in basic GUI grounding, they often struggle with multi-turn tasks because self-teachers provide insufficient guidance for complex sequences. GUI-SD-v2 addresses these limitations by focusing on the quality of supervision provided during long-horizon interactions.
- **Two-Stage Training Framework:** The proposed method utilizes a two-stage framework where the first stage strengthens privilege-following by jointly optimizing rollouts with and without privileged guidance from identical states. This ensures the agent can learn to act effectively even when explicit "privileges" are not provided.
- **Selective Reasoning and Memory Distillation:** In the second stage, the model selectively distills step-specific reasoning and memory guidance through a privilege-conditioned self-teacher. This allows the agent to maintain critical information across multiple steps, which is essential for completing complex user instructions.
- **Superior Benchmark Performance:** Extensive experiments on AndroidWorld and MobileWorld demonstrate that GUI-SD-v2 consistently outperforms current state-of-the-art methods in both Pass@1 and Pass@3 success rates, proving its effectiveness in real-world software environments.

## Context
This research is significant because it addresses a major hurdle in the development of autonomous agents: the ability to perform complex, multi-step reasoning without massive amounts of human-labeled data. As AI moves toward practical applications like automated app usage and web navigation, methods that allow models to learn effectively from their own interactions are essential for scalability.

## Implications
For researchers and practitioners, this work provides a clear path forward for training reliable GUI agents by improving the quality of self-generated supervision rather than just increasing data volume. By demonstrating that improved "privilege-following" leads to better long-horizon reasoning, it suggests that future developments in autonomous software interaction will rely heavily on these sophisticated distillation techniques to achieve human-like reliability and consistency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.27307v1)
