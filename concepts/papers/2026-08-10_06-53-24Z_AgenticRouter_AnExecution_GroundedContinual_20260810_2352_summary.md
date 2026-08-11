# Summary: 2026-08-10_06-53-24Z_AgenticRouter_AnExecution_GroundedContinualLearnin.md
Saved: 2026-08-10 23:52
Source: 2026-08-10_06-53-24Z_AgenticRouter_AnExecution_GroundedContinualLearnin.md
Model: None

---

## Summary  
The paper introduces **Agentic Router**, an execution‑grounded continual learning framework for LLM agents that perform command‑line network operations such as SONiC. It generates multiple complete actions, predicts their consequences, and selects the best via utility‑risk reranking while storing reusable operational lessons in memory. The approach separates a proposal side that abstracts guidance from a selection side that adapts consequence prediction with LoRA updates. Experiments show improved feasible‑action coverage and top‑1 execution success across multi‑turn SONiC sessions.

## Key Contributions  
- Execution‑grounded dual‑path architecture that jointly optimizes action generation and selection.  
- Retrieval‑based guidance memory that captures reusable lessons without modifying the proposal LLM.  
- Session‑level LoRA adaptation of consequence predictor using real SSH feedback to boost conditional selection.

## Methodology  
The authors model each SONiC operation as a sequence of commands. First, they feed the user query to a Qwen3 proposal model to produce several full action sequences. A consequence predictor estimates success probability and risk for each candidate; these predictions are reranked using a utility‑risk score. The system also maintains an in‑memory knowledge base of past successful operations; this memory is consulted to generate guidance that improves coverage. For selection, they fine‑tune the predictor with LoRA updates derived from actual SSH outcomes logged during sessions.

## Results  
Across 12 multi‑turn SONiC sessions using three Qwen3 proposal models, Agentic Router increased feasible‑action coverage by an average of **18 %** and top‑1 execution success from **64.2 %** to **79.5 %**. The dual‑path design contributed roughly half the gain; memory guidance added ~5 %, while LoRA adaptation added another ~8 %.

## Significance  
By grounding continual learning in real execution outcomes, Agentic Router reduces operational risk and improves reliability of LLM agents without retraining large models, offering a scalable path to safer CLI automation.

## Related Concepts  
Continual learning, reinforcement learning from human feedback (RLHF), retrieval‑augmented generation, LoRA fine‑tuning, execution monitoring, SONiC protocol, utility‑risk scoring.
