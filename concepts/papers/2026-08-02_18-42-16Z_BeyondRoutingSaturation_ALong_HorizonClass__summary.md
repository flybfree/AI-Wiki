# Summary: 2026-08-02_18-42-16Z_BeyondRoutingSaturation_ALong_HorizonClass_Increme.md
Saved: 2026-08-04 00:19
Source: 2026-08-02_18-42-16Z_BeyondRoutingSaturation_ALong_HorizonClass_Increme.md
Model: None

---

## Summary  
This paper investigates why expert routing becomes saturated in multimodal continual instruction tuning (MCIT) systems, where tasks are added sequentially but textual fingerprints often leak task identity. It proposes a 34‑task long‑horizon benchmark called FLEX that weakens these fingerprints and normalizes outer templates to expose the hidden challenge of long‑range routing. The authors introduce progressive‑LoRA routing as soft task‑as‑class multimodal class‑incremental learning (MCIL), treating each task as an incremental routing class while preserving hard‑routing as a special case.  

## Key Contributions  
- Routing performance plateaus on standard MCIT benchmarks due to overlapping textual fingerprints and short expert pools.  
- FLEX reveals this saturation by grouping tasks with similar instruction/answer formats but diverse visual domains, normalizing outer templates across all tasks.  
- The paper introduces progressive‑LoRA routing via soft task‑as‑class MCIL, providing a principled interface to transfer class‑incremental learning methods to expert routing.  

## Methodology  
The authors first construct FLEX, which creates 34 tasks with controlled instruction and answer formats while varying visual knowledge domains; outer templates are standardized to reduce leakage. They then formulate progressive‑LoRA routing as MCIL: each task defines an incremental routing class whose full score distribution supplies LoRA mixture weights, enabling soft routing that can be interpreted as a continuous blend of experts. The framework is applied without modifying existing LoRA experts or generation pipelines; four established CIL methods are adapted to four MCIT systems using plug‑in routers.  

## Results  
Compared with the baseline PureLoRA, the plug‑in routers achieve up to 16.3 percentage points improvement in strict LoRA matching and raise overall MacroScore by as much as 4.6 points across FLEX tasks. These gains demonstrate that soft task‑as‑class MCIL routing can substantially alleviate saturation when long‑horizon tasks are present.  

## Significance  
By exposing the saturation of expert routing in MCIT, this work opens a path to more stable continual learning by treating each new task as an incremental class rather than forcing hard assignment. The FLEX benchmark and MCIL formulation provide reusable tools for researchers aiming to improve long‑horizon instruction tuning without sacrificing model efficiency or generation quality.  

## Related Concepts  
MCIT, expert routing, LoRA, task‑as‑class learning, class‑incremental learning (CIL), soft vs. hard routing, long‑horizon tasks, fingerprint reduction, MCIL, progressive‑LoRA, plug‑in routers.
