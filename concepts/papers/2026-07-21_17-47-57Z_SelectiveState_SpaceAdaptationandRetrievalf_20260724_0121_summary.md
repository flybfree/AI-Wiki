# Summary: 2026-07-21_17-47-57Z_SelectiveState_SpaceAdaptationandRetrievalforLangu.md
Saved: 2026-07-24 01:21
Source: 2026-07-21_17-47-57Z_SelectiveState_SpaceAdaptationandRetrievalforLangu.md
Model: None

---

## Summary  
The paper proposes a family of adaptive state‑space modules that replace the static low‑rank updates of LoRA by making adaptation dynamic at both token and context levels, thereby improving language model reasoning. It introduces MaLoRA for recurrent token‑level scaling and MaRA for cross‑segment retrieval selection before generation. Experiments on multiple frozen backbones and two reasoning benchmarks show consistent gains across all cells of the 3 × 2 grid. The improvements are significant relative to LoRA baselines, with up to an 18 % boost on the hardest cell.

## Key Contributions  
- [Dynamic token‑level adaptation via MaLoRA that uses a recurrent state‑dependent scaling factor across tokens.]  
- [Context‑level retrieval via MaRA that tracks segment memory and selects the most relevant pieces for answering.]  
- [Consistent improvement across diverse models (Qwen‑2.5‑7B, Llama‑3.1‑8B, Gemma‑2‑9B) and reasoning tasks (MuSiQue, 2WikiMultihopQA), outperforming LoRA.]

## Methodology  
The authors address the limitation of static low‑rank adapters by introducing two complementary granularities of state‑space recurrence: MaLoRA introduces a dynamic scaling factor that evolves token‑by‑token, while MaRA maintains cross‑segment memory to retrieve pertinent context before model generation. They evaluate these modules on frozen backbones with standard reasoning benchmarks to measure task‑specific gains.

## Results  
Across Qwen‑2.5‑7B, Llama‑3.1‑8B, Gemma‑2‑9B and the MuSiQue/2WikiMultihopQA benchmarks, the combined adapters raise F1 by 6.8 points (+10.5 % relative) on average and reach up to 9.3 points (+18.2 % relative) on the hardest cell versus LoRA; token‑level gains also benefit RULER QA‑2 under length stress.

## Significance  
This work demonstrates that selective, state‑space adaptation can substantially boost reasoning performance without retraining the model, offering a scalable path for task‑specific improvements across diverse language models and tasks.

## Related Concepts  
- Low‑rank adaptation (LoRA)  
- Mamba architecture  
- Recurrent modulation  
- Context retrieval  
- Multi‑granularity adaptation  
- F1 score  
- MuSiQue benchmark  
- 2WikiMultihopQA
