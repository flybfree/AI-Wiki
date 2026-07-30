# Summary: 2026-07-29_08-20-11Z_Living_HarnessIsanInteractive_AgentEvolver.md
Saved: 2026-07-29 20:30
Source: 2026-07-29_08-20-11Z_Living_HarnessIsanInteractive_AgentEvolver.md
Model: None

---

## Summary  
The paper introduces **Living‑Harness**, a self‑evolving agent harness that continuously updates the procedural scaffolding of large language model (LLM) agents based on feedback from completed interaction trajectories. By converting each episode’s success or failure into evidence, Living‑Harness generates two complementary forms of knowledge: an episodic memory of trigger conditions and recovery actions, and a state graph encoding repair edges between system states. The evolved harness guides future interactions while keeping tools and base context static, enabling procedural repairs to accumulate across multiple evolution cycles. This approach improves the reliability and performance of interactive agents without requiring retraining from scratch.

## Key Contributions  
- [Finding 1] Living‑Harness creates a dynamic, feedback‑driven harness that evolves incrementally rather than being rebuilt after each failure.  
- [Finding 2] The system produces both episodic memory and a state graph, providing rich procedural knowledge for future task execution.  
- [Finding 3] On eight benchmark environments (τ²‑Bench and MultiWOZ‑2.4), Living‑Harness raises Pass@1 by 10.07 % and 9.91 % over the strongest interactive baselines, demonstrating robust cross‑model reuse.

## Methodology  
Living‑Harness follows a domain‑level Evolution‑SOP (Standard Operating Procedure) that abstracts each completed trajectory into structured evidence. The authors first parse the episode to identify trigger conditions and failure patterns, then encode these as episodic memory entries. Simultaneously, they construct a state graph where nodes represent system states, edges denote repair actions, and transition rules dictate how the harness is updated. The resulting harness state is retrieved at runtime to steer the LLM’s tool usage and workflow without altering static tools or context.

## Results  
The experiments compare Living‑Harness against baseline interactive agents on eight environments derived from τ²‑Bench and MultiWOZ‑2.4. Pass@1, a metric for correct first‑step response, improves by 10.07 % in τ²‑Bench tasks and 9.91 % in MultiWOZ‑2.4 tasks. Moreover, the evolved harness state can be reused across different model backbones via retrieval‑only mechanisms, showing that procedural knowledge is portable.

## Significance  
Living‑Harness addresses a critical limitation of static agent harnesses: they cannot adapt to recurring failure patterns after deployment. By continuously updating procedural scaffolding from real interaction data, the approach enhances reliability and efficiency across diverse interactive settings, paving the way for more robust, long‑lived AI agents.

## Related Concepts  
- Large Language Model (LLM) agents  
- Agent harness / procedural scaffolding  
- Evolutionary SOP (Standard Operating Procedure)  
- Episodic memory in reinforcement learning  
- State graph representation of repair edges  
- Pass@1 evaluation metric for interactive tasks
