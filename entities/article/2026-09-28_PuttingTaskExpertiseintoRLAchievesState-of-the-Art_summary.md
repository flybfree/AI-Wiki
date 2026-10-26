# Summary: Putting Task Expertise into RL Achieves State-of-the-Art Performance on Text-to-SQL
Saved: 2026-10-25
Source: 2026-09-28_PuttingTaskExpertiseintoRLAchievesState-of-the-Art.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://thinkingmachines.ai/news/putting-task-expertise-into-rl/)

---

## Summary
The article describes a method for achieving state-of-the-art performance on Text-to-SQL tasks by fine-tuning models using reinforcement learning with verifiable rewards (RLVR), rather than relying on complex agentic scaffolding. The authors argue that traditional multi-stage prompting systems fail to bridge the gap between AI and human performance because they do not improve the model's underlying reasoning capabilities. By training on an expert-verified dataset and applying specific reward-shaping techniques, the proposed approach enables models to reach human-level accuracy without external orchestration.

## Key Takeaways
- **Limitations of Scaffolding:** Current state-of-the-art approaches use "agentic scaffolding" (e.g., schema linking, query generation, self-correction) to improve performance. However, these methods keep the model fixed and only optimize prompts, leaving a significant 11-point gap between AI and human performance on benchmarks like BIRD.
- **Human-Level Performance via RLVR:** The authors demonstrate that fine-tuning models with reinforcement learning using verifiable rewards can achieve human-level accuracy (92.96% on BIRD) without scaffolding. This suggests that direct training on task-specific reasoning is more effective than complex orchestration layers.
- **Critical Data and Reward Improvements:** Success depends on two specific technical adjustments: creating an expert-verified training set to remove label errors that poison RLVR, and implementing reward-shaping techniques to address common failure modes in RLVR for SQL generation.

## Context
Text-to-SQL is a critical capability for industries relying on relational databases, where humans currently write billions of custom queries monthly. While LLM pretraining data contains extensive SQL examples, models struggle with the ambiguity and contextual complexity of real-world enterprise schemas, which can contain millions of columns. Historically, AI progress in this domain has been incremental, moving from ~70% to ~82% accuracy on benchmarks through prompt engineering and multi-step agent systems like OpenHands or MetaGPT. These systems mimic human workflows by breaking tasks into discrete stages but do not fundamentally enhance the model's internal reasoning skills regarding database structures.

## Implications
This research suggests a paradigm shift in how AI agents are built for structured data tasks: moving from external orchestration to internal capability enhancement. By proving that models can learn complex reasoning through RLVR, the article implies that future AI systems may require less complex scaffolding and fewer API calls, potentially reducing costs and latency for high-volume applications. It highlights the importance of high-quality, expert-verified training data in reinforcement learning, warning that noisy labels can severely degrade performance. For enterprises, this could mean more reliable automated querying tools that handle ambiguous business questions without needing extensive human-in-the-loop correction or complex prompt engineering pipelines.
