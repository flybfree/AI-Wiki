# Summary: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
Saved: 2026-08-10 23:28
Source: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
Model: None

---

## Summary  
The paper proposes a Full‑bandwidth Transformer that widens the vertical feedback channel in autoregressive transformers via latent feedback, allowing non‑verbalized computation to re‑enter the stack while preserving the standard architecture and parallel teacher forcing. It introduces a scheduled multi‑pass objective that adds this feedback late in pretraining and mixes deeper passes for stability. The model is trained up to 400 B tokens with 1 B parameters, achieving performance comparable to models trained on roughly 1.5× more tokens while incurring negligible per‑token decoding overhead.

## Key Contributions  
- Introduces latent feedback that fuses the previous top‑layer hidden state with the sampled token embedding through a gated linear unit and feeds it back as the next input.  
- Implements a scheduled multi‑pass training objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper feedback passes to maintain stability without breaking parallel teacher forcing.  
- Demonstrates that full‑bandwidth transformers achieve validation loss improvements, 5‑shot language‑model evaluation parity or superiority, enhanced math and coding generation, and better instruction‑tuned performance.

## Methodology  
The authors address the narrow vertical feedback inherent in standard autoregressive transformers by adding a feedback path from the top hidden states back into the stack at each decoding step. This preserves the KV cache and language‑modeling objective while enabling non‑verbalized computation to re‑enter with a renewed depth budget. Training employs a multi‑pass schedule: early passes lack latent feedback, later passes include it gradually, mixing a small fraction of deeper feedback passes to stabilize training.

## Results  
Validation loss is reduced compared with baseline full‑bandwidth transformers; 5‑shot language‑model evaluation matches or exceeds standard models trained on more tokens. Math and coding generation tasks see measurable gains, as does instruction‑tuned performance. Per‑token decoding overhead remains negligible, allowing shorter reasoning traces at equal or better accuracy. The model reaches 400 B tokens with a 1 B parameter budget.

## Significance  
This work enables more efficient training of large transformers by reducing the token cost for high‑quality generation while improving reasoning depth without sacrificing parallelism. It opens a path to larger models that achieve comparable or superior performance with fewer compute resources, which is crucial for scalable AI research and deployment.

## Related Concepts  
Autoregressive transformer architecture, KV cache, teacher forcing, latent feedback, gated linear unit, multi‑pass training schedule, full‑bandwidth transformer.
