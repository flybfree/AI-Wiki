# Summary: 2026-07-28_16-44-38Z_Knowledge_GuidedMultimodalReasoningoverInteracting.md
Saved: 2026-07-28 23:00
Source: 2026-07-28_16-44-38Z_Knowledge_GuidedMultimodalReasoningoverInteracting.md
Model: None

---

## Summary  
The paper introduces PRISM‑AH, a knowledge‑guided multimodal reasoning framework designed to detect video‑level ambivalence and hesitancy (A/H) that precede health‑behaviour change. By treating A/H as a temporal conflict across facial, vocal, linguistic, and bodily cues, the authors propose a lightweight streaming model that scores cross‑modal dissonance, predicts hesitation signals, and leverages expert‑derived evidence to improve detection beyond zero‑shot baselines.

## Key Contributions  
- Introduces PRISM‑AH, a knowledge‑guided multimodal reasoning framework for recognizing ambivalence/hesitancy at the video level.  
- Develops a lightweight streaming model that scores cross‑modal dissonance across short time windows and predicts hesitation surprise signals.  
- Leverages an expert cue taxonomy and large language model reasoning to fuse evidence only when validation performance improves.

## Methodology  
The authors align frozen vision, audio, and text encoders into short overlapping windows, feeding the resulting feature streams into a streaming model that computes cross‑modal dissonance scores. Dense window‑level annotations serve as an auxiliary supervision signal for calibration, while a decision threshold is tuned to achieve macro F1 on a held‑out set. A knowledge‑guided large language model then reasons over structured evidence using the expert cue taxonomy; its verdict is fused with the streaming output only after validation performance shows improvement.

## Results  
On the labelled public test partition of 525 videos, PRISM‑AH attains a macro F1 of 0.6133 compared with a zero‑shot baseline of 0.2827. The reasoning gain is validated to transfer from validation to the larger test set, demonstrating consistent performance improvements.

## Significance  
Accurate video‑level detection of ambivalence and hesitancy enables early identification of individuals at risk for delayed health behaviour change, supporting timely interventions in public health communication strategies.

## Related Concepts  
Ambivalence/hesitancy, multimodal conflict, streaming models, knowledge‑guided large language model reasoning, macro F1 metric, expert cue taxonomy.
