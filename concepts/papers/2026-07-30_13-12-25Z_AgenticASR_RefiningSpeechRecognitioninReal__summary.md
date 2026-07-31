# Summary: 2026-07-30_13-12-25Z_AgenticASR_RefiningSpeechRecognitioninReal_WorldSc.md
Saved: 2026-07-30 20:36
Source: 2026-07-30_13-12-25Z_AgenticASR_RefiningSpeechRecognitioninReal_WorldSc.md
Model: None

---

## Summary  
The paper proposes AgenticASR, an agentic approach to refine speech recognition output in real time by removing disfluencies and resolving self‑corrections while preserving the speaker’s intent. It introduces an ASR‑Refiner architecture that continuously revises text as audio streams arrive, enabling clean transcription for downstream tasks. This work addresses the limitation of conventional ASR that cannot revise emitted text once it has been generated.

## Key Contributions  
- [Finding 1] The formulation of Agentic Speech Recognition (AgenticSR) as a bounded active‑context editing task.  
- [Finding 2] Design and release of AASR‑Bench, a bilingual benchmark with atomic rubrics for evaluating clean transcription quality.  
- [Finding 3] Demonstration that the Refiner architecture outperforms standard ASR front‑ends on AASR‑Bench and yields human‑AI agreement.

## Methodology  
The authors adopt an online ASR‑Refiner that maintains a sliding active context window; as new audio arrives, the system updates its output span, allowing continual emission and revision. The pipeline integrates a stateful encoder‑decoder model trained jointly to predict both speech tokens and refined text, with loss functions encouraging alignment between acoustic predictions and clean transcription.

## Results  
AgenticASR achieves top scores on AASR‑Bench across multiple ASR front‑ends, surpassing baseline systems by up to 6.2 % in rubric scores. Human–AI agreement studies show >85 % concordance with expert judgments. Ablation experiments reveal that extending context length improves refinement but degrades latency; online inference offers a trade‑off between speed and quality.

## Significance  
By enabling intent‑preserving, clean transcription during ongoing speech, AgenticASR reduces downstream processing effort and opens new applications in interactive dialogue and assistive technologies.

## Related Concepts  
- Automatic Speech Recognition (ASR)  
- Disfluency removal  
- Self‑correction resolution  
- Online learning / continual inference  
- Human evaluation rubrics
