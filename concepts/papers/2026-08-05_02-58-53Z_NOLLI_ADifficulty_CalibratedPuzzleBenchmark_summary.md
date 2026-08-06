# Summary: 2026-08-05_02-58-53Z_NOLLI_ADifficulty_CalibratedPuzzleBenchmarkforDiag.md
Saved: 2026-08-05 20:29
Source: 2026-08-05_02-58-53Z_NOLLI_ADifficulty_CalibratedPuzzleBenchmarkforDiag.md
Model: None

---

## Summary  
The paper introduces NOLLI, a calibrated puzzle benchmark that systematically diagnoses the English‑Korean performance gap by generating 15 puzzle types (7,500 unique tasks) whose difficulty is tuned to match a reference model’s accuracy bands. By separating direct translations, Hangul‑jamo script adaptations, and Korean‑only cultural/orthographic tasks, NOLLI isolates presentation language from deeper cognitive demands. The benchmark evaluates frontier models and reveals that overall English‑Korean accuracy is statistically equivalent within ±10 pp, yet writing‑system‑intensive puzzles expose larger gaps. This work provides a calibrated tool for understanding where Korean performance lags.

## Key Contributions  
- Finding 1: NOLLI calibrates difficulty behaviorally across puzzle types, creating a benchmark where each generator is tuned to achieve target accuracy bands for a reference model.  
- Finding 2: The three‑level design includes direct translations, script adaptations over Hangul jamo (sub‑syllabic letters), and Korean‑only tasks grounded in culture or orthography.  
- Finding 3: Writing‑system‑intensive tasks such as Korean Cipher show sharper gaps (up to 68.7 pp) than cryptarithmetic, indicating difficulty in multi‑step sub‑syllabic execution; Jamo Composition predicts Korean Cipher accuracy.

## Methodology  
The authors procedurally generated 15 puzzle types with 25 tasks each, ensuring every instance is regenerated and has a unique solution while maintaining deterministic scoring. They tuned each generator until a reference model lands within predefined target accuracy bands, thereby calibrating difficulty rather than assuming it grows linearly with task size. The benchmark was evaluated on 15 frontier models (open‑weight and Korean‑developed) using TOST to compare English‑Korean accuracy.

## Results  
Overall English‑Korean accuracy is statistically equivalent within a ±10 pp margin, suggesting presentation language alone does not cause the gap. However, Korean Cipher accuracy lags behind English by up to 68.7 pp, whereas cryptarithmetic over the same jamo shows no systematic penalty; Jamo Composition scores correlate with Korean Cipher performance. Crucially, a size measure (number of items) fails to increase difficulty in seven puzzle types, making structural size an unreliable proxy for empirical difficulty.

## Significance  
These findings diagnose the English‑Korean performance gap as rooted in multi‑step sub‑syllabic execution and rule‑application deficits rather than linguistic complexity; they provide a calibrated benchmark for future research on cross‑lingual skill transfer and model calibration.

## Related Concepts  
- Difficulty calibration  
- Hangul jamo (sub‑syllabic letters)  
- Multi‑step cognitive tasks  
- Cross‑lingual accuracy parity  
- Structural size vs. empirical difficulty
