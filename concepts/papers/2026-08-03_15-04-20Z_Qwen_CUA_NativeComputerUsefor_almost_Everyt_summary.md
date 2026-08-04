# Summary: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Saved: 2026-08-04 00:04
Source: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Model: None

---

## Summary  
The paper introduces Qwen‑CUA, a native computer‑use agent that can interact with any desktop application solely through screenshots and keyboard/mouse events. By leveraging a 397B‑A17B mixture‑of‑experts model and a novel visual‑history scaffold that retains up to twenty recent screenshots, Qwen‑CUA achieves stateful navigation across diverse software without relying on DOM trees or task‑specific APIs. The system is trained on a massive cloud rollout fleet with 40 000 verifiable tasks spanning everyday and professional applications, enabling reinforcement learning from sparse yet observable outcomes. These advances demonstrate that native computer use can be broadly applicable and scalable.

## Key Contributions  
- [Finding 1] Qwen‑CUA provides a general‑purpose interface for agents to operate almost any software using only screenshots and low‑level input events, eliminating the need for explicit task APIs or accessibility metadata.  
- [Finding 2] The visual‑history scaffold maintains a fixed set of recent screenshots while folding older evidence into compact blocks, preserving reusable prompt prefixes and enabling long‑horizon state tracking within limited memory.  
- [Finding 3] Training on a cloud rollout fleet with 100 k vCPUs and 40 000 verifiable tasks yields measurable performance gains (86.2/OSWorld‑Verified, 21.2/53.3) and reduces RedTeamCUA attack success from 36.6 to 16.4.

## Methodology  
The authors built Qwen‑CUA around a mixture‑of‑experts model that processes only raw screen images, feeding them through a transformer encoder to generate keyboard/mouse actions. A sliding window of up to twenty screenshots is stored as fixed‑size blocks; older visual context is compressed into prompt prefixes for reuse. Training employs supervised trajectory optimization with verifiable rewards and iterative re‑calibration on the same fleet, collecting personalized workflows across numerous applications.

## Results  
Across eight benchmarks, Qwen‑CUA outperforms Qwen3.7 and matches leading proprietary systems: 86.2 on OSWorld‑Verified and a binary/partial completion score of 18.5/48.4 on OSWorld 2.0. Scaling to a trillion‑parameter model (Qwen‑CUA‑Max) improves these metrics to 87.6 and 21.2/53.3, respectively. Efficiency analyses, a browser deployment, and Bash‑augmented experiments confirm practical utility.

## Significance  
Native computer use represents a foundational capability for AI agents that can autonomously navigate real‑world software, reducing reliance on task‑specific APIs and enabling broader automation. The results show that large‑scale visual reasoning combined with verifiable reinforcement learning can achieve high performance while mitigating security risks such as RedTeam attacks.

## Related Concepts  
- Native computer use (agent‑driven OS interaction)  
- Visual history scaffolds for long‑term state tracking  
- Mixture‑of‑experts models for efficient reasoning  
- Reinforcement learning from sparse, verifiable rewards  
- Cloud rollout fleets for massive training data generation
