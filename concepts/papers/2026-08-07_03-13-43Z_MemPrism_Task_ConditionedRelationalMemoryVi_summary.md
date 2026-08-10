# Summary: 2026-08-07_03-13-43Z_MemPrism_Task_ConditionedRelationalMemoryViewsforL.md
Saved: 2026-08-09 22:35
Source: 2026-08-07_03-13-43Z_MemPrism_Task_ConditionedRelationalMemoryViewsforL.md
Model: None

---

## Summary  
Long‑horizon agents need to reuse past experiences but existing memory systems treat evidence as a static representation, causing a mismatch between stored facts and the current decision. MemPrism solves this by separating persistent storage from task‑time working memory and generating relational views on demand. The view policy selects relation structure, evidence range, outcome condition, and granularity for each task context. Experiments show that this approach consistently improves performance—especially as trajectories grow longer—and reduces token consumption while enabling transfer across different vision‑language models.

## Key Contributions  
- [MemPrism introduces a task‑conditioned relational memory framework that decouples persistent experience storage from decision‑time working memory.]  
- [A lightweight view policy dynamically constructs relational views according to the current task context, selecting relation structure, evidence range, outcome condition, and granularity.]  
- [The learned view policy transfers across different VLMs without additional adaptation, demonstrating a general memory interface for agents.]

## Methodology  
[The authors address representation mismatch by recording interactions as an event stream and using a deterministic composer to render historical facts into a temporary optical working‑memory view that is frozen for the current task policy.]  

## Results  
[On long‑horizon embodied and web‑agent benchmarks, MemPrism consistently improves task performance especially with longer trajectories, while reducing memory token consumption; the learned view policy also transfers across different VLMs without extra adaptation.]  

## Significance  
[This work provides a general memory interface that bridges representation mismatch, enabling efficient reuse of experiences for long‑horizon planning and transferable agents.]  

## Related Concepts  
relational memory, task‑conditioned views, persistent storage, working memory, optical working‑memory view, view policy, evidence range, outcome condition, granularity, VLMs (vision‑language models), episodic memory, long‑horizon planning.
