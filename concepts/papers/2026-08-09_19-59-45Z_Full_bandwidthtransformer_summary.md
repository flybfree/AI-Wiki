# Summary: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
Saved: 2026-08-10 23:28
Source: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
Model: None

---

## Summary  
The paper proposes a **full‑bandwidth transformer** that widens the vertical feedback channel in autoregressive transformers, allowing non‑verbalized computation to re‑enter the stack with a fresh depth budget while preserving the standard architecture and KV cache. It does this by fusing the previous top‑layer hidden state with the sampled token embedding through a gated linear unit at each decoding step. To train such models without breaking parallel teacher forcing, the authors introduce a scheduled multi‑pass objective that gradually mixes deeper feedback passes for stability. The result is a model that can achieve performance comparable to or better than standard transformers trained on roughly 1.5 × more tokens while incurring negligible per‑token decoding overhead.

## Key Contributions  
- [Finding 1] Introduces the full‑bandwidth transformer architecture, which adds latent feedback via a gated linear unit that re‑injects the previous top‑layer hidden state at every decoding step.  
- [Finding 2] Designs a scheduled multi‑pass training objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper feedback passes to maintain stability and teacher forcing.  
- [Finding 3] Shows empirically that full‑bandwidth transformers improve validation loss, 5‑shot language‑model evaluation, math and coding generation, and instruction‑tuned performance, matching or exceeding standard models trained on ~1.5 × more tokens.

## Methodology  
The authors keep the conventional transformer stack, KV cache, and language‑modeling objective unchanged. At each decoding step they compute a gated linear unit that combines the sampled token embedding with the latent feedback from the previous top layer, producing a new input for the next layer. Training is performed in multiple passes: early passes rely only on shallow feedback, while later passes gradually incorporate deeper feedback layers. This schedule allows the model to learn richer vertical interactions without sacrificing parallel generation.

## Results  
Trained 1 B‑parameter full‑bandwidth transformers up to 400 B tokens demonstrate that latent feedback reduces validation loss and boosts downstream metrics: 5‑shot language‑model accuracy, math reasoning, coding generation, and instruction‑tuned performance all improve. The per‑token decoding overhead is negligible; the model matches or approaches standard transformers trained with roughly 1.5 × more tokens and even produces shorter reasoning traces at equal or better accuracy.

## Significance  
This work demonstrates that deeper vertical computation can be efficiently integrated into autoregressive models, reducing token cost while enhancing quality. By preserving parallel training dynamics and only adding a lightweight feedback mechanism, full‑bandwidth transformers open the door to more expressive, scalable language models without sacrificing inference speed or memory efficiency.

## Related Concepts  
autoregressive transformer, attention depth, KV cache, teacher forcing, latent feedback, gated linear unit, multi‑pass training objective, reasoning traces.
