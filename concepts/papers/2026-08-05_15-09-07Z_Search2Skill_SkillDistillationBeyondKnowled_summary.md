# Summary: 2026-08-05_15-09-07Z_Search2Skill_SkillDistillationBeyondKnowledgeBound.md
Saved: 2026-08-06 20:25
Source: 2026-08-05_15-09-07Z_Search2Skill_SkillDistillationBeyondKnowledgeBound.md
Model: None

---

## Summary  
The paper introduces **Search2Skill**, a framework that enables LLM‑based agents to acquire reusable professional skills even when those skills lie outside the model’s existing knowledge boundaries. By automatically detecting capability gaps, retrieving relevant external evidence, and distilling it into structured skill representations, Search2Skill bridges the gap between what an agent knows and what is required for expert‑level tasks. The authors optimize this process with a **rubric‑based reinforcement learning** scheme that jointly controls when to search, how to search, and how to generate skills. Experiments across eight expert domains demonstrate that this approach consistently outperforms both search‑augmented and trajectory‑based skill‑learning baselines.

## Key Contributions  
- [Finding 1] Search2Skill automatically identifies the agent’s capability gaps and searches external sources to fill them, distilling retrieved evidence into reusable skills beyond the model’s current knowledge.  
- [Finding 2] The framework employs a rubric‑based reinforcement learning scheme that jointly optimizes search timing, search strategy, and skill generation.  
- [Finding 3] Experiments on eight expert‑level domains from three benchmarks show Search2Skill outperforms all baselines under both streaming and held‑out evaluation protocols; the gains stem from skill abstraction rather than raw evidence and skills transfer across model scales.

## Methodology  
The authors first probe the agent’s current proficiency in a target domain to pinpoint capability gaps. These gaps trigger an external search operation, where the system queries curated knowledge bases or web resources using natural‑language prompts. The retrieved snippets are then distilled into concise, reusable skill specifications (e.g., “perform X under Y conditions”). A rubric‑based reinforcement learning loop guides three decision variables: (1) whether to continue searching, (2) which search query to issue, and (3) how to encode the evidence as a skill. The RL agent receives rewards that favor timely, effective searches and accurate skill distillation, allowing it to learn an optimal policy for self‑evolving skills.

## Results  
Across eight expert domains from three benchmarks, Search2Skill achieved higher success rates in both streaming (online) and held‑out evaluations compared with search‑augmented baselines and trajectory‑based methods. The improvement is attributed to the abstraction of raw evidence into structured skills rather than memorizing retrieved text. Moreover, skills learned by one model were successfully transferred to another model of a different scale, indicating robustness beyond the specific training data.

## Significance  
Search2Skill demonstrates that LLM agents can evolve professional expertise autonomously, extending their capabilities far beyond what is encoded in their parameters or training trajectories. By integrating external knowledge and a reinforcement‑learning driven search strategy, the framework opens a path toward truly self‑sustaining expert systems capable of adapting to new domains without human intervention.

## Related Concepts  
- Reusable skills (procedural procedural knowledge)  
- Skill distillation (transforming evidence into structured representations)  
- Reinforcement learning with rubrics (decision‑making guided by explicit criteria)  
- Capability gap detection (identifying mismatches between current and required abilities)  
- External knowledge retrieval (querying databases, web sources)  
- Streaming evaluation (online performance measurement)
