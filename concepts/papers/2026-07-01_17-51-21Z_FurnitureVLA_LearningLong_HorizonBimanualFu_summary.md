# Summary: 2026-07-01_17-51-21Z_FurnitureVLA_LearningLong_HorizonBimanualFurniture.md
Saved: 2026-07-01 23:01
Source: 2026-07-01_17-51-21Z_FurnitureVLA_LearningLong_HorizonBimanualFurniture.md
Model: None

---


## Summary  
This paper presents FurnitureVLA, the first systematic investigation of real‑scale bimanual furniture assembly using a Vision‑Language‑Action (VLA) model. The authors formalize the multi‑subtask task, develop a scalable simulation pipeline and a VR teleoperation system to collect high‑quality expert demonstrations, and propose a progress‑enhanced VLA that predicts both actions and a continuous progress signal for long‑horizon assembly up to 7 subtasks and 1550 control steps. Their design factors improve average success rates dramatically compared with baselines, and they validate the approach on a real Kinova Gen3 platform with only a modest performance drop.

## Key Contributions  
- [Introduce FurnitureVLA as a systematic study of real‑scale bimanual furniture assembly using Vision‑Language‑Action models, providing a formal task definition, scalable simulation pipeline, and VR teleoperation system for expert data collection.]  
- [Propose a progress‑enhanced VLA that jointly predicts discrete actions and a continuous progress signal, enabling automatic subtask transitions and mitigating compounding errors in long‑horizon assembly.]  
- [Identify perception and control design factors that critically affect precision in real‑scale assembly, achieving an 80% average simulation success (up from 48%) and a +21% gain over baselines.]

## Methodology  
The authors first formalize the furniture assembly task as a sequence of up to seven subtasks, each requiring precise perception and control. They build a simulation environment that generates expert demonstrations using a VR teleoperation interface, allowing single‑operator bimanual control while capturing high‑quality state data. The progress‑enhanced VLA is trained end‑to‑end: the model outputs both an action token sequence and a scalar progress value, which guides subtask switching and error correction during inference. Design factors such as sensor placement, visual grounding cues, and controller latency are systematically varied to understand their impact on precision.

## Results  
Across three furniture types (a table, a chair, and a bookshelf), FurnitureVLA improves average simulation success from 48% to 80%, representing a 21‑percentage‑point gain over the best baselines. In the hardest task, performance drops only 16% relative to the baseline, demonstrating robustness. These gains are attributed to the progress‑enhanced VLA’s ability to maintain continuity and reduce error accumulation.

## Significance  
FurnitureVLA advances robotics by tackling a complex, long‑horizon bimanual task that is beyond current single‑arm or toy‑scale approaches. By integrating perception, language guidance, and continuous progress prediction, the model demonstrates practical applicability to real‑world furniture assembly, offering a template for future multi‑task manipulation systems.

## Related Concepts  
- Vision‑Language‑Action (VLA) models  
- Bimanual manipulation  
- Progress‑enhanced reinforcement learning  
- Subtask decomposition and transition management  
- VR teleoperation for data collection
