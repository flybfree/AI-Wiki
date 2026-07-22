# Summary: 2026-07-21_17-59-21Z_CopyLess_GroundMore_OvercomingRepetitiveCopyinginL.md
Saved: 2026-07-21 22:04
Source: 2026-07-21_17-59-21Z_CopyLess_GroundMore_OvercomingRepetitiveCopyinginL.md
Model: None

---

## Summary  
The paper tackles a pervasive failure mode in long‑context language models that generate reasoning traces: repetitive copying of prompt text instead of productive problem solving. By isolating key evidence from irrelevant distractor context, the authors diagnose this as an insufficient grounding issue and introduce GEAR (Grounding Evidence‑Aware Reward) to reshape reinforcement learning rewards. Their contribution is a novel reward‑shaping method that simultaneously encourages overlap with relevant evidence while penalizing overlap with distractors, enabling training on automatically annotated natural‑language data. This approach yields measurable gains in accuracy and reduces both repetitive copying and unnecessary thought steps across model scales.

## Key Contributions  
- Finding 1: Repetitive copying is a widespread problem in frontier long‑context LLMs and worsens as context length increases.  
- Finding 2: The root cause is insufficient grounding; models indiscriminately copy from the prompt, especially when distractor content is present, leading to higher error rates.  
- Finding 3: GEAR, an evidence‑aware reward shaping scheme, adds a grounding reward for correct overlap with key evidence and a distractor penalty for overlap with irrelevant context.

## Methodology  
The authors first decompose each prompt into two components: task‑relevant key evidence and extraneous distractor text. Using an automated pipeline they annotate arbitrary documents to produce training data where the relevance of each segment is explicitly labeled. They then train long‑context models via reinforcement learning, augmenting the standard accuracy signal with GEAR’s grounding reward and distractor penalty. The combined objective guides the model to attend to and incorporate only the essential evidence while avoiding unnecessary copying.

## Results  
Experiments across multiple model scales and benchmark suites show that GEAR improves average accuracy by up to +4.6 points compared with baseline RL using only accuracy rewards, with larger gains observed at longer contexts. Additionally, the method reduces repetitive copying in generated traces and shortens average thinking length, indicating more efficient reasoning.

## Significance  
Accurate grounding of evidence is essential as long‑context evaluation evolves from simple retrieval to complex multi‑step reasoning. By providing a concrete reinforcement learning strategy that explicitly rewards proper grounding, GEAR addresses a critical gap in current models, paving the way for more reliable and efficient long‑context generation.

## Related Concepts  
Long‑context reasoning, evidence‑aware reinforcement learning, grounding, repetitive copying, distractor context, RL reward shaping, key evidence.
