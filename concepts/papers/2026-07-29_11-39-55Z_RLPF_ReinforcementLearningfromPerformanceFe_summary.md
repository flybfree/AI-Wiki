# Summary: 2026-07-29_11-39-55Z_RLPF_ReinforcementLearningfromPerformanceFeedbackf.md
Saved: 2026-07-30 20:21
Source: 2026-07-29_11-39-55Z_RLPF_ReinforcementLearningfromPerformanceFeedbackf.md
Model: None

---

## Summary  
The paper addresses the gap between mere correctness and runtime efficiency in code generation, arguing that most training signals stop at test‑passing without rewarding speed or resource usage. It introduces RLPF (Reinforcement Learning from Performance Feedback), a staged reward system that orders failed programs by execution progress and ranks successful ones by their relative improvement toward an expert reference. Fine‑tuning Qwen3‑32B on PerfCodeBench with this reward boosts correct‑and‑runnable solutions dramatically, moving the model from 11.1 % to 54.6 % success while improving relative efficiency from 8.1 % to 38.6 %. The results demonstrate that code agents can learn optimization beyond simple correctness.

## Key Contributions  
- RLPF introduces a staged reward: failed programs are scored by how far they progress before crashing or timing out, and correct programs receive rewards proportional to their improvement relative to an expert reference.  
- The approach yields substantial gains on PerfCodeBench—correct‑and‑runnable solutions rise from 11.1 % to 54.6 %, and relative efficiency improves from 8.1 % to 38.6 %.  
- A composite reward outperforms both correctness‑only (11.1 %) and runtime‑only baselines, showing that the full feedback is more reliable than single‑metric signals.

## Methodology  
The authors design a reinforcement‑learning framework where the environment provides feedback based on execution outcomes. For programs that fail to compile or run, the reward reflects the distance traveled toward a successful state; for programs that succeed, the reward quantifies how much faster they are relative to an expert reference. This staged reward is then used to fine‑tune Qwen3‑32B via RL, allowing the model to learn both correctness and efficiency objectives.

## Results  
On PerfCodeBench, the RLPF‑fine‑tuned model achieves 54.6 % correct‑and‑runnable solutions and improves relative efficiency by a factor of roughly four (8.1 % → 38.6 %). The composite reward outperforms correctness‑only (11.1 %) and runtime‑only baselines, and its optimization behavior modestly transfers to EffiBench‑X, indicating broader applicability.

## Significance  
By integrating execution feedback into the training signal, RLPF enables code agents to prioritize both correctness and performance, moving beyond binary pass/fail evaluation toward practical, resource‑aware system code generation. This could lead to more efficient AI assistants, automated codebases, and tools that understand real‑world runtime constraints.

## Related Concepts  
- Reinforcement Learning (RL)  
- Staged reward design  
- Performance feedback  
- Composite rewards  
- PerfCodeBench benchmark  
- Execution progress ordering  
- Relative improvement ranking
