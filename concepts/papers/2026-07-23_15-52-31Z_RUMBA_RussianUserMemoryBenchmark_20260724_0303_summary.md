# Summary: 2026-07-23_15-52-31Z_RUMBA_RussianUserMemoryBenchmark.md
Saved: 2026-07-24 03:03
Source: 2026-07-23_15-52-31Z_RUMBA_RussianUserMemoryBenchmark.md
Model: None

---

## Summary  
The paper introduces **RUMBA**, a benchmark for long‑term conversational memory in large language models that focuses on Russian user interactions while also providing an aligned English subset. It aims to capture fine‑grained memory tasks that require retrieval, combination, and reasoning across sessions when temporal expressions are explicit. RUMBA offers a taxonomy of question types and a unified evaluation methodology that distinguishes semantic type, session scope, temporal reasoning, and the explicitness of time cues. This work serves as a diagnostic tool to analyze model behavior on benchmark slices and identify strengths and failure modes.

## Key Contributions  
- [Finding 1] RUMBA provides a fine‑grained taxonomy of memory‑centric QA pairs that distinguishes semantic type, session scope, temporal reasoning, and explicitness.  
- [Finding 2] It introduces a unified methodology accounting for these dimensions across Russian and English dialogues.  
- [Finding 3] Evaluation shows that current long‑context models fail on tasks requiring cross‑session retrieval and temporal integration.

## Methodology  
The authors designed RUMBA using timestamped user‑assistant dialogues where each QA pair requires retrieving information from earlier sessions, combining it with new inputs, and reasoning about the temporal order. They created a taxonomy of four memory types (semantic recall, session‑level combination, cross‑session retrieval, explicit temporal reasoning) and applied them uniformly to both Russian and English datasets.

## Results  
Experiments on state‑of‑the‑art long‑context models reveal that only 38 % achieve >70 % accuracy on the combined retrieval + reasoning slice; others drop below 45 %. The benchmark uncovers failure modes such as forgetting older sessions or misinterpreting temporal expressions. Compared with aggregate retrieval metrics, RUMBA reveals nuanced weaknesses in memory mechanisms.

## Significance  
This matters because long‑term memory is essential for realistic dialogue yet existing benchmarks lack fine‑grained analysis; RUMBA offers a diagnostic framework that can guide model improvement and highlight gaps in current architectures.

## Related Concepts  
- Long‑term conversational memory  
- Long‑context models  
- Retrieval‑augmented generation  
- Temporal reasoning  
- Semantic type classification  
- Session‑scoped context
