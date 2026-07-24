# Summary: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Saved: 2026-07-24 03:02
Source: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Model: None

---

## Summary  
The paper investigates how much information a low‑rank LoRA adapter actually writes into the frozen backbone of a large language model, quantifying this effect in bits rather than in parameter counts. By extending compression‑based memorization analysis to the “frozen‑base” setting, the authors measure directly the capacity of adapters and show that it is far smaller than full fine‑tuning would suggest. Their findings reveal that adapter memory depends on where the parameters are placed within the model and whether the base remains frozen, providing a quantitative metric for privacy‑sensitive adaptation. The work thus transforms an anecdotal folklore into a measurable quantity that can guide design choices.

## Key Contributions  
- [Finding 1] Adapter writes only a few bits per trainable parameter, well below the capacity of full fine‑tuning.  
- [Finding 2] The amount of writable capacity is not tied to the number of adapter parameters but to their location (MLP vs. attention) and the structure of the frozen base.  
- [Finding 3] Privacy leakage correlates with the bits an adapter writes, not with its nominal parameter count; supervised fine‑tuning adapters copy data verbatim while reinforcement‑learning adapters do not.

## Methodology  
The authors employ a compression‑based memorization analysis that measures how much of the original model’s weights are altered by an adapter. In the frozen‑base scenario, the base parameters remain unchanged, so any deviation is captured solely in the adapter’s low‑rank matrices. By comparing the compressed representation before and after training, they compute the number of bits written per parameter, allowing a direct bit‑level accounting of adaptation capacity.

## Results  
Experiments on Qwen2.5 fine‑tunes show that adapters typically write 0.1–0.3 bits per trainable parameter, roughly an order of magnitude smaller than full fine‑tuning. Moving the same budget from attention layers to MLP layers increases writable capacity by nearly a factor of two, whereas removing the frozen base collapses this capacity almost entirely. Moreover, privacy leakage measured via compression analysis rises with the bits written rather than with parameter count: supervised adapters exhibit verbatim copying (high leakage), while RL‑trained adapters show negligible leakage.

## Significance  
By quantifying what fine‑tuning actually writes into a model’s weights, the paper provides a concrete design constraint that can be used to enforce privacy and efficiency goals. This metric helps developers decide whether an adapter is acceptable for sensitive data or whether alternative strategies (e.g., full fine‑tuning) are needed.

## Related Concepts  
LoRA, parameter‑efficient fine‑tuning (PEFT), frozen‑base models, compression‑based memorization analysis, adapter capacity, supervised learning, reinforcement learning.
