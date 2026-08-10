# Summary: 2026-08-07_03-24-59Z_Stockmark_Nemotron_3_Nano_Omni_JapanDocReader_Stru.md
Saved: 2026-08-09 22:36
Source: 2026-08-07_03-24-59Z_Stockmark_Nemotron_3_Nano_Omni_JapanDocReader_Stru.md
Model: None

---

## Summary  
The authors introduce Stockmark‑Nemotron‑3‑Nano‑Omni‑JapanDocReader, a Japanese document understanding model built on the reasoning‑oriented Nemotron‑3‑Nano‑Omni‑30B‑A3B. Their central contribution is to inject structured Japanese document parsing capability into this multimodal system while preserving its existing VQA (visual question answering) ability as much as possible. To achieve this, they employ three training regimes: parsing‑centric SFT that uses only structured parsing data, mixed SFT that combines parsing and VQA data, and parsing‑centric RL that optimizes a task‑level reward for parsing. The work demonstrates how capability injection can be combined with forgetting control to improve one task without destroying another.

## Key Contributions  
- [Finding 1] Injecting Japanese structured document parsing capability into a reasoning‑oriented multimodal model while preserving its VQA competence.  
- [Finding 2] Mixed SFT mitigates the VQA forgetting that occurs with pure parsing‑centric SFT, maintaining comparable parsing performance.  
- [Finding 3] DAPO‑based RL on top of the mixed SFT checkpoint further boosts structured document parsing beyond the ceiling set by SFT.

## Methodology  
The authors approached the problem by first constructing a dual data stream: a Japanese Document VQA Stream and a programmatic Structured Document Parsing Stream. They injected the parsing capability via prompt engineering and forgetting control, ensuring that the model’s attention mechanisms could be selectively suppressed for tasks unrelated to parsing. Training was performed in three stages: (1) parsing‑centric SFT using only the structured stream, (2) mixed SFT alternating between both streams with a balanced loss, and (3) RL fine‑tuning on top of the mixed checkpoint using DAPO, where reward variance is controlled by variance‑based prompt filtering to avoid catastrophic forgetting. This pipeline enables systematic evaluation of how each training method influences both parsing accuracy and VQA quality.

## Results  
Parsing‑centric SFT yields a noticeable increase in structured document parsing scores but also causes measurable degradation in VQA performance, indicating strong task‑specific forgetting. Mixed SFT restores the original VQA level while preserving the improved parsing results of the first stage. Applying DAPO‑based RL on this mixed checkpoint further raises parsing accuracy beyond what pure SFT could achieve, demonstrating that RL can unlock additional gains when combined with careful reward design and prompt filtering.

## Significance  
This work matters because it provides a principled framework for task‑specific capability injection in large multimodal models, allowing researchers to enhance one domain (Japanese structured document parsing) without sacrificing the model’s broader capabilities. By integrating forgetting control techniques such as DAPO and variance‑based reward shaping, the authors demonstrate that fine‑grained RL can be effective even on long‑reasoning tasks, opening avenues for more efficient and robust document understanding systems.

## Related Concepts  
- Capability injection  
- Forgetting control  
- Structured document parsing  
- VQA (visual question answering)  
- SFT (Supervised Fine‑Tuning) – parsing‑centric and mixed variants  
- RL fine‑tuning with DAPO  
- Reward design for long‑reasoning tasks  
- Variance‑based prompt filtering
