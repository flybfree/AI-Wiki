# Summary: Training a 4B model to produce 81% faster query plans than Postgres
Saved: 2026-10-25
Source: 2026-09-16_Traininga4Bmodeltoproduce81_fasterqueryplansthanPo.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://rohanbansal.com/qorl)

---

## Summary
The article details an experiment demonstrating that a small, open-weights 4B parameter model can be post-trained using supervised fine-tuning and agentic reinforcement learning to generate Postgres query plans that are significantly faster than the database's default optimizer. By leveraging the verifiable nature of query execution time as a reward signal, the author successfully reduced latency by 44.7% across join-heavy queries, effectively outperforming traditional heuristic-based optimizers in specific scenarios.

## Key Takeaways
- **Reinforcement Learning for Optimization:** The core methodology relies on Reinforcement Learning (RL), specifically a custom Group Relative Policy Optimization (GRPO) variant, to train the model. This approach works because query optimization has a single, easily verifiable axis of success: execution time. Unlike subjective tasks, faster plans provide clear feedback for reinforcement learning agents.
- **Overcoming Heuristic Limitations:** Traditional query optimizers struggle with NP-hard problems like join ordering. The study highlights that despite decades of research, standard optimizers (like Postgres) often leave performance on the table. A small language model can bypass these heuristic limitations by learning optimal strategies through trial and error in a simulated environment.
- **Infrastructure and Noise Management:** Achieving reliable results required significant engineering effort to minimize noise. The author constructed a specific measurement rig using concurrent containers to reduce Linux page cache contention and split the RL training across different machines (vLLM on H100 GPUs vs. Postgres containers on local hardware) to ensure stable scoring in an inherently noisy environment.

## Context
This work sits at the intersection of database systems and large language models, addressing a long-standing challenge in computer science: automated query optimization. Historically, databases have relied on cost-based optimizers using static heuristics and statistics. However, as noted by Leis et al., these traditional methods remain imperfect for complex queries. This experiment introduces a modern AI approach—using small, specialized models trained via RL—to tackle a classic NP-hard problem. It reflects a broader industry trend where "small language models" (SLMs) are being fine-tuned for specific, high-stakes technical tasks rather than general chat capabilities.

## Implications
The success of this experiment suggests that AI-driven query optimization could become a viable alternative or complement to traditional database engines. If small models can consistently produce faster plans, it implies that future database systems might integrate lightweight RL-trained components to handle complex join orders dynamically. Furthermore, the methodology demonstrates that RL is highly effective for tasks with clear, measurable outcomes (like latency), potentially opening doors for applying similar techniques to other computational optimization problems in software engineering and infrastructure management.
