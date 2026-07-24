# Summary: 2026-07-23_17-35-20Z_X__3__OPD_DistillingReasoningintoLargeAudio_Langua.md
Saved: 2026-07-24 02:59
Source: 2026-07-23_17-35-20Z_X__3__OPD_DistillingReasoningintoLargeAudio_Langua.md
Model: None

---

## Summary  
The paper introduces X$^3$-OPD, a cross‑modal on‑policy distillation framework that transfers logical reasoning from powerful text teachers to large audio‑language student models, addressing the gap in deep reasoning for multimodal systems. It builds a three‑tier symmetric corpus covering speech‑rendered textual reasoning, event‑based acoustic reasoning, and spoken‑dialogue reasoning grounded in prosody. The method lets the student generate its own reasoning trajectories while receiving teacher guidance via matched inputs and verified answers. Experiments show that X$^3$-OPD markedly improves audio‑grounded reasoning and chain‑of‑thought quality across several benchmarks.

## Key Contributions  
- X$^3$-OPD framework for cross‑modal on‑policy distillation of reasoning between text and audio‑language models.  
- Construction of a three‑tier symmetric corpus integrating speech, event, and dialogue reasoning modalities.  
- Demonstration that the method boosts audio‑grounded reasoning accuracy while preserving existing capabilities under domain shift.

## Methodology  
The authors train a large audio‑language student model to produce intermediate reasoning steps conditioned on its acoustic perception. A powerful text teacher supplies token‑level guidance using paired textual inputs and correct answers, and an on‑policy loss aligns the student’s trajectory with the teacher’s output. The three‑tier corpus provides diverse data: (1) textual reasoning rendered into speech, (2) audio‑event grounding in complex acoustic scenes, and (3) spoken‑dialogue reasoning involving prosodic cues.

## Results  
On MMSU, MMAU, BIG Bench Audio, and MMAR, X$^3$-OPD improves chain‑of‑thought accuracy by up to 12.4 % relative to baseline models while maintaining or slightly enhancing standard perception metrics. The model retains its original capabilities under domain shift, indicating effective transfer without overfitting.

## Significance  
This work bridges the reasoning gap between text and audio‑language models, enabling multimodal agents that can reason from non‑linguistic events and prosody. It demonstrates a scalable on‑policy distillation technique applicable to other cross‑modal tasks beyond reasoning.

## Related Concepts  
- Cross‑modal distillation  
- On‑policy alignment  
- Reasoning trajectories  
- Three‑tier corpus  
- Audio‑grounded chain‑of‑thought
