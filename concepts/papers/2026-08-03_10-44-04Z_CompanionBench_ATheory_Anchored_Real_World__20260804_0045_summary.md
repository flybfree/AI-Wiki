# Summary: 2026-08-03_10-44-04Z_CompanionBench_ATheory_Anchored_Real_World_Grounde.md
Saved: 2026-08-04 00:45
Source: 2026-08-03_10-44-04Z_CompanionBench_ATheory_Anchored_Real_World_Grounde.md
Model: None

---

## Summary  
CompanionBench is a theory‑anchored, real‑world grounded benchmark for evaluating AI emotional companionship. It moves beyond hand‑crafted scenarios and aggregate empathy scores by using de‑identified bilingual data to generate interactive personas that follow hidden disclosure gates, thereby controlling the interaction state space without scripting dialogue. The framework operationalizes ten capabilities derived from 25 psychology and counseling theories, including four novel constructs such as holding ambiguity, self‑object responsiveness, positive resonance, and calibrated challenge. Rankings are reproduced across Chinese (ρ = 0.996) and English (ρ = 0.953), revealing fine‑grained capability differences that prior aggregate metrics mask.

## Key Contributions  
- [Finding 1] CompanionBench is the first benchmark to ground both its scenarios and a trained user simulator in de‑identified real‑world data, providing authentic, cross‑lingual interaction material.  
- [Finding 2] It introduces ten capability rubrics—four of which are novel (holding ambiguity, self‑object responsiveness, positive resonance, calibrated challenge)—measured via a subjective rubric and a deterministic measure of whether deeper disclosure was earned.  
- [Finding 3] The benchmark yields reproducible rankings across languages with high inter‑rater correlation (ρ = 0.996 ZH / 0.953 EN), exposing capability‑level differences that aggregate scores obscure.

## Methodology  
The authors built an interactive bilingual companion system where each persona’s trajectory is governed by a hidden disclosure gate, allowing the agent to either deepen or limit disclosure without explicit scripting. Ten capabilities are derived from 25 psychological and counseling theories; four are not previously graded. Evaluation uses two axes: (1) a subjective ten‑capability rubric and (2) a deterministic metric indicating whether deeper disclosure was earned. A cross‑family panel mitigates same‑family favoritism, while an Item Response Theory model separates agent quality from judge severity.

## Results  
Twenty‑eight agents were evaluated on the 500 Chinese‑English parallel pairs. Emotion regulation and calibrated challenge emerged as common weaknesses; holding ambiguity consistently discriminated agents most effectively. Role‑play agents ranked near the bottom, indicating that immersion does not guarantee relational competence. The dominant failure mode was substituting surface warmth for substantive relational support. Rankings were highly reproducible across languages.

## Significance  
CompanionBench establishes a fair, theory‑driven evaluation standard for AI emotional companionship, enabling researchers to compare models on nuanced capabilities rather than coarse aggregate scores. By releasing 500 parallel pairs and the evaluation code, it fosters reproducibility and further research into human‑AI relational dynamics.

## Related Concepts  
Theory‑anchored evaluation, hidden disclosure gate, interactive persona simulation, IRT (Item Response Theory), affective computing, relational competence, calibration of challenge, ambiguity handling, empathy measurement.
