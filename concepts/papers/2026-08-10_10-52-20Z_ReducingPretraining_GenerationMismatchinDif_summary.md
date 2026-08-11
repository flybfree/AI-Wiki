# Summary: 2026-08-10_10-52-20Z_ReducingPretraining_GenerationMismatchinDiffusionL.md
Saved: 2026-08-10 23:46
Source: 2026-08-10_10-52-20Z_ReducingPretraining_GenerationMismatchinDiffusionL.md
Model: None

---

## Summary  
Diffusion language models suffer from a mismatch between the clean‑prefix prompt used at generation time and the corrupted continuation that is generated during pretraining, which degrades performance. The authors introduce PCD (Prefix‑Conditioned Diffusion), an objective that aligns training with inference by supervising the autoregressive prefix while applying diffusion only to the unknown suffix. By reshaping attention masks, corruption masks, and label construction, PCD creates a local training interface that mirrors how block‑diffusion models are queried at evaluation time without requiring a new decoder or inference mode. This alignment recovers a measurable portion of the continuation gap across several large language models.

## Key Contributions  
- [Finding 1] Diffusion language model pretraining often corrupts both prompt and continuation tokens, breaking the clean‑prefix interface needed for prompt‑conditioned generation.  
- [Finding 2] PCD combines autoregressive prefix supervision with no‑shift suffix denoising to preserve the original prompt while only diffusing the unknown continuation.  
- [Finding 3] The method separates intra‑sample prefix conditioning from inter‑sample objective mixing, allowing the local alignment signal to be isolated from optional batch‑level mixing.

## Methodology  
PCD modifies three components of the standard dLLM pipeline: it updates the attention mask so that only the continuation tokens are masked for diffusion, constructs a corruption mask that never shifts the prefix tokens, and builds labels that reflect the autoregressive generation of the clean prefix. The model then runs diffusion exclusively on the suffix portion, leaving the prefix untouched. This design eliminates the need for an autoregressive decoder or a separate inference mode; instead, it reuses the existing dLLM pipeline. By treating intra‑sample conditioning and inter‑sample mixing as distinct signals, PCD can be tuned independently to improve alignment without affecting batch statistics.

## Results  
On LLaDA2‑Mini, PCD improves the six‑benchmark average by 2.56 points (a 4.2 % relative gain) over native dLLM stable baselines. For Qwen‑1.7B, it yields a +4.86 point improvement in the primary mechanism comparison—a 14.2 % relative gain. These gains are consistent across both models and demonstrate that aligning pretraining with prompt‑conditioned generation can close part of the continuation gap without altering inference.

## Significance  
The alignment achieved by PCD suggests that diffusion language models retain a sizable portion of their generative potential when their training context matches how they are queried at inference. By fixing the mismatch between prompt and corrupted continuation, researchers gain better controllable generation without sacrificing the parallel denoising advantage of diffusion, opening pathways for more reliable and efficient dLLM applications.

## Related Concepts  
Diffusion language models, autoregressive language models, prefix conditioning, block‑diffusion models, latent diffusion, dLLM (denoising language model), prompt‑conditioned generation, attention masks, corruption masks, label construction.
