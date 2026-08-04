# Summary: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Saved: 2026-08-04 00:57
Source: 2026-08-03_15-04-20Z_Qwen_CUA_NativeComputerUsefor_almost_Everything.md
Model: None

---

## Summary  
The paper introduces Qwen‑CUA, a native‑computer‑use agent that can interact with virtually any desktop software using only screenshots and keyboard/mouse actions. By leveraging a 397B‑A17B mixture‑of‑experts model, Qwen‑CUA maintains a short visual history of up to twenty screenshots while preserving reusable prompt prefixes for long‑horizon tasks. The authors demonstrate that the system can complete complex workflows across everyday and professional applications with high accuracy and robustness. Scaling the same architecture to a trillion‑parameter model yields further gains, establishing native computer use as a broadly capable foundation.

## Key Contributions  
- [Finding 1] Qwen‑CUA achieves state‑of‑the‑art performance on eight OSWorld benchmarks, outperforming Qwen3.7 and matching leading proprietary systems.  
- [Finding 2] The agent reduces RedTeamCUA attack success from 36.6 % to 16.4 %, showing improved security against adversarial manipulation.  
- [Finding 3] A scalable recipe for native computer use can be extended to models with over one trillion parameters, yielding Qwen‑CUA‑Max.

## Methodology  
The authors built a cloud rollout fleet equipped with nearly 100 000 vCPUs and tens of thousands of concurrent environments. They constructed roughly 40 000 verifiable tasks that span everyday utilities to professional software, collecting personalized long‑horizon workflows. Training employed complete trajectory optimization with verifiable rewards and trajectory slicing; supervised data were refreshed iteratively while reinforcement‑learning tasks were recalibrated. The system observes only screenshots and generates keyboard/mouse events, avoiding DOM trees or task‑specific APIs.

## Results  
Qwen‑CUA scores 86.2 on OSWorld‑Verified and 18.5/48.4 binary/partial completion on OSWorld 2.0; Qwen‑CUA‑Max improves to 87.6 and 21.2/53.3 respectively. These results indicate strong competence across diverse computational tasks while maintaining efficiency.

## Significance  
Native computer use provides a universal interface for AI agents, enabling them to perform almost any software operation without explicit API knowledge. The work demonstrates that large‑scale, verifiable interaction and hybrid tool use are scalable foundations for future general‑purpose agents.

## Related Concepts  
native computer use, verifiable interaction, hybrid tool use
