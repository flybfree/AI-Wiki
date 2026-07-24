# Summary: 2026-07-23_09-35-34Z_AttriMem_Attribution_GuidedProcessFeedbackforAgent.md
Saved: 2026-07-24 02:43
Source: 2026-07-23_09-35-34Z_AttriMem_Attribution_GuidedProcessFeedbackforAgent.md
Model: None

---

## Summary  
The paper tackles the difficulty of constructing effective memory policies for LLM agents, where heuristic or outcome‑based reinforcement learning fails to capture fine‑grained credit for intermediate decisions. AttriMem introduces an attribution‑guided process‑feedback framework that augments global rewards with local token‑level contributions to answer generation. This enables RL to learn a memory‑construction policy using only the final answer as supervision. The approach improves performance across long‑horizon dialogue tasks.

## Key Contributions  
- Heuristic and outcome‑based RL methods cannot identify which intermediate memory contents support the final answer, creating a fine‑grained credit‑assignment bottleneck.  
- AttriMem proposes token‑level attribution scores that generate local rewards to guide memory construction during reinforcement learning.  
- Experiments show superior generalization across benchmarks, different answer models (e.g., GPT, LLaMA), and stable RL optimization.

## Methodology  
The authors formulate a reinforcement‑learning objective where the agent’s memory policy is updated by combining a global success reward with per‑token contribution scores derived from the final answer. They compute these attribution scores using a differentiable function that estimates each token’s impact on output, then inject them as local rewards into the RL update loop, allowing fine‑grained feedback without task‑specific heuristics.

## Results  
On long‑horizon dialogue question answering benchmarks, AttriMem achieves higher accuracy than retrieval‑based, heuristic, and baseline RL methods. It generalizes across diverse answer models (e.g., GPT, LLaMA) and maintains stable training dynamics with lower reward variance compared to other approaches.

## Significance  
By providing a principled mechanism for attributing intermediate memory decisions to downstream performance, AttriMem bridges the credit‑assignment gap in RL. This enables more robust, adaptable memory policies that do not rely on subjective task rules and work across varied downstream objectives.

## Related Concepts  
- Memory construction policy  
- Reinforcement learning  
- Attribution  
- Token‑level reward shaping  
- Fine‑grained credit assignment  
- Long‑horizon dialogue QA
