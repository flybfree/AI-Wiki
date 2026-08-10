# Summary: 2026-08-06_18-38-14Z_CanMLLMsDecodetheCreativeLeap_IntroducingC4forCros.md
Saved: 2026-08-09 22:20
Source: 2026-08-06_18-38-14Z_CanMLLMsDecodetheCreativeLeap_IntroducingC4forCros.md
Model: None

---

## Summary  
The paper addresses a key limitation of modern multimodal language models: their inability to reliably decode creative leaps that rely on cross‑concept reasoning. By operationalizing creativity as an encoding–decoding pair, the authors introduce C4, a cognition‑inspired evaluation framework for Chengyu‑based Cross‑Concept Creativity, and demonstrate that current MLLMs perform poorly on this task despite strong closed‑model capabilities. The study constructs an extensive benchmark (C4‑Eval) with manually curated cross‑concept relations, bridge paths, and reasoning traces to provide exact answer‑recovery cases across multiple model settings.

## Key Contributions  
- [Finding 1] C4 provides a systematic framework that maps target slots to imageable substitute concepts via a manually annotated third‑party‑reviewed cross‑concept network, enabling batch generation with explicit structure and difficulty indexing.  
- [Finding 2] The strongest closed MLLMs achieve primary accuracy of ~50 % on C4‑Eval items, while open‑source models remain substantially lower, exposing a sizable gap between model performance and human‑level cross‑concept decoding.  
- [Finding 3] Adding constraints improves accuracy sharply, but bridge hints or explicit explanation requests yield only modest gains, indicating that the bottleneck lies in the model’s ability to infer creative meaning rather than simple prompting.

## Methodology  
The authors operationalize item construction as cross‑concept encoding and model inference as decoding. C4 maps each Chengyu slot to an imageable substitute concept along a bridge path constructed from a manually annotated, third‑party‑reviewed network. Difficulty is indexed by the number of bridges and their depth, and answers are generated with exact structure. The C4‑Eval set comprises 184 synthetic items plus 37 human‑created Chengyu figures; each item is instantiated in five task settings, yielding 884 primary answer‑recovery cases. All relations, bridge paths, and reasoning processes were manually constructed and reviewed.

## Results  
Across ten evaluated MLLMs, the best closed models reach 50.7 % and 48.0 % primary accuracy; open‑source models lag well below these levels. Constraint‑only prompting boosts performance noticeably, whereas bridge hints or explicit explanation requests provide only modest improvements. The results confirm that current MLLMs struggle to decode the creative leap encoded in cross‑concept relations.

## Significance  
C4 introduces a cognition‑aligned evaluation paradigm for assessing creative decoding abilities, which are essential for design, communication, and human‑AI collaboration. By quantifying performance on this domain, C4 highlights a persistent gap between model capabilities and human‑level cross‑concept reasoning, offering a benchmark that can guide future research toward more robust creative models.

## Related Concepts  
Cross‑Concept Understanding, Chengyu (Chinese idiom), Cognitive Capacity, Receptive Creativity, MLLM Decoding, Evaluation Framework, Bridge Paths, Primary Accuracy.
