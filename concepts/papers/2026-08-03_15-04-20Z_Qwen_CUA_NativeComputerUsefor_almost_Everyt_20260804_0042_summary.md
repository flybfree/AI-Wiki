# Summary: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Saved: 2026-08-04 00:42
Source: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Model: None

---

## Summary  
The paper introduces Qwen‑CUA, a native computer‑use agent that can operate any software solely through screenshots and keyboard/mouse events, using a 397B‑A17B mixture‑of‑experts model. It demonstrates state‑of‑the‑art performance on OSWorld benchmarks while reducing RedTeam attacks, establishing native computer use as a broadly capable agent foundation.

## Key Contributions  
- [Finding 1] Qwen‑CUA achieves full software interaction without APIs or DOM metadata, relying only on visual screenshots and low‑level input.  
- [Finding 2] The system maintains up to 20 active screenshots and folds older visual history into fixed‑size blocks for long‑horizon state tracking.  
- [Finding 3] Qwen‑CUA reduces RedTeamCUA attack success from 36.6 % to 16.4, showing robust security in native use.

## Methodology  
The authors built a cloud rollout fleet with ~100,000 vCPUs and generated roughly 40,000 verifiable tasks across everyday and professional software. They collected personalized long‑horizon workflows, optimized complete trajectories using verifiable rewards and trajectory slicing, and performed iterative training runs that refreshed supervised data to recalibrate reinforcement‑learning objectives.

## Results  
Across eight benchmarks Qwen‑CUA outperforms Qwen3.7: OSWorld‑Verified score 86.2 (vs. ~85.x) and binary/partial completion 18.5/48.4 on OSWorld 2.0. Scaling to a trillion‑parameter model yields Qwen‑CUA‑Max with scores 87.6 and 21.2/53.3, respectively.

## Significance  
These results prove that native computer use can be achieved at scale, providing a foundation for agents that can perform almost any task through verifiable interaction and hybrid tool use, which are key research directions for future AI systems.

## Related Concepts  
native computer use, mixture‑of‑experts models, long‑horizon state tracking, trajectory slicing, reinforcement learning with verifiable rewards, RedTeam attacks, OSWorld benchmark.
