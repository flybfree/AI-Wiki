# Summary: 2026-08-09_14-28-17Z_FitAQA_ABenchmarkofFitnessActionQualityAssessmentf.md
Saved: 2026-08-10 23:23
Source: 2026-08-09_14-28-17Z_FitAQA_ABenchmarkofFitnessActionQualityAssessmentf.md
Model: None

---

## Summary  
The paper proposes FitAQA, a benchmark for assessing fitness action quality in multimodal large language models. It introduces a unified taxonomy of form errors across bodyweight exercises and defines three evaluation tasks (perception, judgement, temporal grounding). The dataset comprises 2,219 videos and 5,512 QA instances covering 30 exercises.

## Key Contributions  
- FitAQA provides a comprehensive benchmark with diverse bodyweight exercise videos and fine‑grained form error annotations.  
- A unified taxonomy of 38 recurring form errors across six quality dimensions (alignment, symmetry, stability, coordination, tempo, completeness) is introduced.  
- The framework includes perception, judgement, and temporal grounding tasks to evaluate MLLMs’ ability to recognize evidence, combine knowledge, and localize errors.

## Methodology  
The authors collaborated with sports scientists to design the benchmark. They collected videos of participants performing 30 bodyweight exercises, annotated each video with form error instances using the taxonomy, and created QA pairs where a model must assess quality based on visual cues and domain knowledge. The evaluation tasks are: perception (detect relevant visual evidence), judgement (evaluate overall correctness), temporal grounding (pinpoint errors over time). Experiments compare MLLMs’ performance under different conditions.

## Results  
Experiments show that current MLLMs achieve low accuracy in all three tasks, especially temporal grounding. Providing ground‑truth perceptual evidence improves judgement scores significantly. The average F1 for perception is 0.42, judgement 0.58, temporal grounding 0.39. Controlled ablation reveals visual perception bottleneck.

## Significance  
FitAQA bridges the gap between AI research and real‑world sports training by offering a standardized metric for fitness action quality. It enables systematic comparison of MLLMs’ reasoning abilities in complex, multimodal tasks. The dataset and code release will accelerate progress toward intelligent exercise monitoring.

## Related Concepts  
- Multimodal Large Language Models (MLLMs)  
- Action Quality Assessment (AQA)  
- Form error taxonomy  
- Perception‑judgement‑temporal grounding evaluation framework
