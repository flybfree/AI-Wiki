# Summary: 2026-07-21_09-52-57Z_FromaMultilingualStreamingASRBackbonetoKenyan_Lang.md
Saved: 2026-07-24 00:58
Source: 2026-07-21_09-52-57Z_FromaMultilingualStreamingASRBackbonetoKenyan_Lang.md
Model: None

---

## Summary  
The paper aims to adapt NVIDIA Nemotron 3.5 ASR Streaming 0.6B, a multilingual streaming model, to Kenyan languages—Kikuyu, Dholuo, and Kalenjin—while preserving its caching‑aware FastConformer RNN‑T architecture, prompt conditioning, and streaming decoder. It does so through a data‑centric fine‑tuning pipeline that starts from a Kenyan Swahili checkpoint and maintains the full‑parameter training process without discarding any streaming constraints. The study documents an end‑to‑end engineering workflow from corpus auditing to isolated serving. Results show modest WER improvements for Kikuyu (42.97%) and Dholuo (33.98%), with Kalenjin still a work in progress, highlighting the challenges of African language ASR.

## Key Contributions  
- [Finding 1] The adaptation retains the streaming decoder and FastConformer RNN‑T architecture while fine‑tuning on Kenyan languages.  
- [Finding 2] A data‑centric pipeline includes Unicode normalization, split checks, low‑rate continuation, and true‑streaming evaluation to avoid overfitting to internal sets.  
- [Finding 3] Checkpoint selection uses a mixed‑source validation manifest, reducing the risk of over‑optimistic scores derived from non‑independent data.

## Methodology  
The authors begin with a Kenyan Swahili‑adapted Nemotron 3.5 checkpoint that includes cache‑aware FastConformer RNN‑T and prompt conditioning. They perform full‑parameter fine‑tuning on curated audio‑text pairs, preserving the streaming decoder’s ability to handle low‑rate continuation. Throughout the process they conduct corpus auditing (Unicode normalization, split verification), filter out short or non‑speech utterances, apply duration filtering, and select checkpoints based on validation performance rather than arbitrary iteration numbers. The final system is served in an isolated environment that preserves streaming artifacts such as no‑space CER and boundary‑sensitive WER.

## Results  
Kikuyu achieves a 42.97 % WER and Dholuo records a 9.59 % CER (no‑space) under its frozen historical label policy; Kikuyu’s no‑space CER is 7.79 %. Kalenjin, still in progress, reaches 68.74 % WER on a clean‑v3 diagnostic subset that excludes long pauses, digit‑bearing references, and targets shorter than three tokens. The scores are not independent generalizations because the validation manifest mixes test origins. Negative findings include non‑speech label contamination, over‑generation of short utterances, boundary‑sensitive WER errors, and cloud job‑lifecycle failures.

## Significance  
This work provides an auditable account of adapting a multilingual streaming model into language‑specific systems without discarding its streaming constraints. It demonstrates that data‑centric fine‑tuning can yield modest performance gains while maintaining the operational integrity required for real‑world deployment in African contexts, informing future ASR research and engineering efforts.

## Related Concepts  
- Streaming ASR  
- FastConformer RNN‑T  
- Prompt conditioning  
- Cache‑aware models  
- Multilingual backbones  
- Unicode normalization  
- Low‑rate continuation  
- True‑streaming evaluation  
- WER / CER metrics  
- African language orthography challenges
