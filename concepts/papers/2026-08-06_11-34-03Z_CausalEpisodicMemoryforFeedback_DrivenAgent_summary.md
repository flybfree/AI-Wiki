# Summary: 2026-08-06_11-34-03Z_CausalEpisodicMemoryforFeedback_DrivenAgentRepair.md
Saved: 2026-08-06 20:40
Source: 2026-08-06_11-34-03Z_CausalEpisodicMemoryforFeedback_DrivenAgentRepair.md
Model: None

---

## Summary  
The paper investigates whether a frozen LLM can retain and reuse successful repair outcomes to boost subsequent Text‑to‑SQL tasks without retraining, addressing the problem of “forgetting” corrections after each failure. It proposes MERIT (Causal Episodic Memory for Feedback‑Driven Agent Repair), a training‑free system that stores a dual‑polarity memory of oracle‑verified fixes and observed dead‑ends, retrieving only those memories that are causally linked to earlier episodes. The approach combines a deterministic classifier with a hybrid lexical‑dense retriever before the frozen model generates each revision. Experiments on Spider and BIRD show measurable gains in execution accuracy compared with stateless iterative repair, while also revealing trade‑offs between memory usage and inference cost.

## Key Contributions  
- Finding 1: MERIT achieves higher Text‑to‑SQL execution accuracy (69.79 % on Spider, 48.44 % on BIRD) than baseline stateless repair, indicating that retained causal memories can improve downstream performance.  
- Finding 2: The benefit of negative memory is modest, and the value of type conditioning plus lexical‑dense ranking varies with dataset characteristics, suggesting that not all retrieved entries are equally useful.  
- Finding 3: Schema‑local experience yields the most consistent improvement across tasks, whereas broader memory representations often do not translate into reliable gains.

## Methodology  
MERIT is built as a training‑free agent that maintains an online dual‑polarity memory: one branch records oracle‑verified corrections (positive memories) and another stores unsuccessful query directions (negative memories). Before each revision, a deterministic classifier assigns a coarse failure type, which conditions a hybrid lexical‑dense retriever. The retrieved items are then fed to the frozen Qwen2.5‑7B‑Instruct model that generates the next repair step. Oracle feedback is used only for initial verification; later episodes rely solely on stored memories.

## Results  
On Spider, MERIT lifts accuracy from 66.34 % (stateless) to 69.79 %, a gain attributed to successful retrieval of earlier fixes. On BIRD, the improvement is smaller—from 47.35 % to 48.44 %—and the system cannot be distinguished from untyped dynamic retrieval without higher inference cost (Reflection‑style memory reaches 51.24 %). Ablation studies confirm that negative memories contribute little, type conditioning and ranking are dataset‑dependent, and schema‑local experience is most beneficial.

## Significance  
These results clarify when causal episodic memory aids repair: it helps on tasks where prior fixes map directly to current queries (Spider), but may be less effective or costly on more diverse datasets (BIRD). The work also highlights the trade‑off between memory efficiency and inference overhead, guiding future research on retrieval‑augmented generation for LLM agents.

## Related Concepts  
- Causal episodic memory: storing past outcomes that causally influence later actions.  
- Dual‑polarity memory: maintaining both successful corrections (positive) and observed dead‑ends (negative).  
- Oracle feedback: external validation used only for initial verification, not for ongoing learning.  
- Retrieval‑augmented generation: hybrid retrieval before model output to inject stored knowledge.  
- Schema‑local experience: memory that is specific to a task’s schema, yielding consistent benefits.
