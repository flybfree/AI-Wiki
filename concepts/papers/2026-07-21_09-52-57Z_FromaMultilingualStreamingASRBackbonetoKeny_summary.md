# Summary: 2026-07-21_09-52-57Z_FromaMultilingualStreamingASRBackbonetoKenyan_Lang.md
Saved: 2026-07-24 00:42
Source: 2026-07-21_09-52-57Z_FromaMultilingualStreamingASRBackbonetoKenyan_Lang.md
Model: None

---

## Summary  
The paper presents a data‑centric engineering study that adapts NVIDIA’s multilingual ASR Streaming model Nemotron 3.5 to three Kenyan languages—Kikuyu, Dholuo and Kalenjin—while preserving the streaming architecture (FastConformer RNN‑T, prompt conditioning, decoder) for low‑latency inference. By fine‑tuning a Kenyan Swahili checkpoint on carefully curated corpora, the authors retain cache‑aware components and avoid discarding the streaming pipeline, delivering language‑specific systems that can be served in production. The work reports internal WER/CER scores (42.97 % Kikuyu, 33.98 % Dholuo, 68.74 % Kalenjin) and documents negative findings such as non‑speech label over‑generation and cloud job failures.

## Key Contributions  
- [Finding 1] Fine‑tuning the streaming backbone retains its FastConformer RNN‑T architecture and decoder, enabling continued low‑latency inference without a full model rewrite.  
- [Finding 2] The adapted models achieve modest but measurable performance: Kikuyu WER 42.97 %, Dholuo WER 33.98 % (CER 9.59 %/no‑space CER 8.13 %), and Kalenjin v1‑v WER 68.74 % on a limited diagnostic subset.  
- [Finding 3] The study introduces a true‑streaming evaluation protocol that isolates artifact preservation, low‑rate continuation, and validation‑based checkpoint selection.

## Methodology  
The authors approached the problem through a series of data‑centric steps: (1) auditing the corpus for orthographic consistency and missing audio; (2) applying Unicode normalization to standardize symbols; (3) performing split checks and duration filtering to remove outliers; (4) implementing low‑rate continuation for streaming continuity; (5) selecting checkpoints via a validation manifest that excludes gradient‑contaminated rows; (6) conducting isolated serving tests to verify artifact preservation. All these operations were performed while keeping the FastConformer RNN‑T and prompt‑conditioned decoder intact.

## Results  
Internal evaluation sets, kept separate from training data, yielded WER scores of 42.97 % for Kikuyu and 33.98 % for Dholuo; Kalenjin v1‑v reached 68.74 % on a clean‑v3 diagnostic subset (excluding long pauses, digit references, and short tokens). Negative findings included over‑generation of non‑speech labels, boundary‑sensitive WER errors, and cloud job lifecycle failures that halted streaming jobs.

## Significance  
This work provides an auditable account of adapting a multilingual ASR backbone to African languages without discarding the streaming constraints that are essential for real‑time applications. By documenting data‑centric adaptation pipelines—corpus curation, normalization, and true‑streaming evaluation—the authors demonstrate that inclusive NLP can be achieved while maintaining low latency and model integrity.

## Related Concepts  
ASR (automatic speech recognition), multilingual streaming models, FastConformer RNN‑T architecture, prompt conditioning, WER (word error rate), CER (character error rate), Unicode normalization, data‑centric adaptation, validation‑based checkpoint selection, true‑streaming evaluation, artifact preservation.
