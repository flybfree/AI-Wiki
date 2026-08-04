# Summary: 2026-08-02_18-42-16Z_BeyondRoutingSaturation_ALong_HorizonClass_Increme.md
Saved: 2026-08-04 00:22
Source: 2026-08-02_18-42-16Z_BeyondRoutingSaturation_ALong_HorizonClass_Increme.md
Model: None

---

## Summary  
Multimodal Continual Instruction Tuning (MCIT) enables large language models to acquire new tasks sequentially while preserving prior knowledge, but the task‑identification problem that underlies expert routing is rarely examined beyond short sequences. This paper demonstrates that routing becomes saturated on standard MCIT benchmarks because textual fingerprints and brief 4–10‑task sequences mask long‑horizon cues. To expose this issue, the authors introduce a 34‑task benchmark called FLEX and formulate progressive LoRA routing as soft task‑as‑class Multimodal Class‑Incremental Learning (MCIL), which provides a principled interface for transferring class‑incremental methods to expert routing.

## Key Contributions  
- [Finding 1] Routing is nearly saturated on widely used MCIT benchmarks, indicating that existing task‑identification mechanisms cannot reliably select the correct LoRA expert over long horizons.  
- [Finding 2] Textual fingerprints and short task sequences obscure long‑horizon routing cues, making it difficult for current routing strategies to maintain high accuracy as tasks accumulate.  
- [Finding 3] The FLEX benchmark and MCIL formulation jointly reveal the expanding challenge of expert routing and enable systematic evaluation across a larger expert pool.

## Methodology  
The authors construct FLEX by grouping 34 multimodal tasks that share similar instruction/answer formats but differ in visual content and knowledge domains; outer templates are normalized to reduce leakage. They define progressive LoRA routing as MCIL, where each task corresponds to an incremental routing class whose full score distribution supplies the mixture weights of its LoRA experts, with hard routing serving as a discrete special case. The proposed plug‑in routers can be inserted into existing MCIT frameworks without altering their LoRA experts or generation pipelines.

## Results  
Compared with PureLoRA as a controlled baseline, the four CIL‑based plug‑in routers improve strict LoRA matching by up to 16.3 percentage points and overall MacroScore by up to 4.6 points on FLEX, demonstrating that soft class‑incremental routing can substantially outperform hard rule‑based approaches.

## Significance  
This work clarifies a long‑standing bottleneck in continual multimodal instruction tuning: expert routing degrades as tasks accumulate. By exposing the saturation problem and providing MCIL as a transferable framework, the study offers a roadmap for designing more robust, long‑horizon routing mechanisms that preserve model performance over many sequential task acquisitions.

## Related Concepts  
- Multimodal Continual Instruction Tuning (MCIT)  
- LoRA (Low‑Rank Adaptation) experts  
- Expert routing and task identification  
- Class‑incremental learning (CIL)  
- Soft vs. hard routing  
- FLEX benchmark for long‑horizon evaluation
