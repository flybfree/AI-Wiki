# Summary: 2026-08-10_10-52-20Z_ReducingPretraining_GenerationMismatchinDiffusionL.md
Saved: 2026-08-11 00:02
Source: 2026-08-10_10-52-20Z_ReducingPretraining_GenerationMismatchinDiffusionL.md
Model: None

---

## Summary  
Diffusion language models suffer from a mismatch between their pretraining process and the generation interface, as random corruption can affect both prompt and continuation tokens together, breaking the clean‑prefix alignment needed for prompt‑conditioned output. The authors introduce PCD (Prefix‑Conditioned Diffusion), an objective that preserves the autoregressive prefix while applying diffusion only to the unknown suffix, thereby restoring a local training interface similar to block‑diffusion queries at inference time. By separating intra‑sample conditioning from inter‑sample mixing, PCD isolates the alignment signal without requiring new decoders or inference modes. This work demonstrates that aligning pretraining with generation can recover measurable performance gains in diffusion LLMs.

## Key Contributions  
- [Finding 1] Native dLLM pretraining randomly corrupts prompt and continuation tokens together, weakening the clean‑prefix interface required for prompt‑conditioned generation.  
- [Finding 2] PCD combines autoregressive prefix supervision with no‑shift suffix denoising to keep the prefix untouched while applying diffusion only to the unknown continuation.  
- [Finding 3] The method separates intra‑sample prefix conditioning from inter‑sample objective mixing, allowing the alignment signal to be identified independently of batch‑level mixing.

## Methodology  
The authors modify three components of the training pipeline: they change the attention mask so that only the suffix receives diffusion noise, adjust the corruption mask to avoid shifting any token in the prefix, and construct labels that retain the original autoregressive target for the prefix while providing a denoised version for the suffix. No new decoder, verifier, or inference mode is introduced; instead, PCD re‑uses the existing dLLM architecture and simply aligns its training context with how block‑diffusion models are queried at evaluation time.

## Results  
Experiments on LLaDA2‑Mini and Qwen‑1.7B backbones show that PCD consistently outperforms stable native dLLM baselines. On the six‑benchmark average, PCD improves performance by 4.2 % relative gain (+2.56 points) for LLaDA2‑Mini, while in the primary Qwen comparison it yields a 14.2 % relative gain (+4.86 points). These gains persist across both models and indicate that the alignment achieved is not limited to a single architecture.

## Significance  
Aligning pretraining with prompt‑conditioned generation can recover a measurable portion of the dLLM continuation gap without altering inference, which is crucial for practical deployment of diffusion language models. The findings suggest that careful design of training objectives can mitigate the mismatch between how data are corrupted during learning and how they are queried at output time.

## Related Concepts  
Diffusion language model, autoregressive LM, clean‑prefix interface, prefix conditioning, block‑diffusion models, latent diffusion, dLLM mismatch, training objective alignment, intra‑sample vs. inter‑sample mixing.
