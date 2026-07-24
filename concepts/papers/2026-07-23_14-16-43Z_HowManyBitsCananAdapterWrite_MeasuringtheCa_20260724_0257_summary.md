# Summary: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Saved: 2026-07-24 02:57
Source: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Model: None

---

## Summary  
The paper investigates how much data a low‑rank adapter actually writes into the underlying frozen model during parameter‑efficient fine‑tuning, measuring it in bits rather than parameters. It extends memorization analysis to the fixed‑base setting and reveals that adapters store far fewer bits per trainable parameter than full fine‑tuning would suggest. The study shows that adapter capacity depends on where the budget is placed within the model architecture.

## Key Contributions  
- Finding 1: Adapters write only a couple of bits per trainable parameter, far less than the total bits available in full fine‑tuning.  
- Finding 2: Capacity varies with location; moving the same adapter budget from attention to MLP yields nearly twice the stored information.  
- Finding 3: The amount of privacy leakage correlates directly with bits written, not with nominal parameter count, and adapters trained on reinforcement learning do not record supervised knowledge.

## Methodology  
The authors treat adapters as a black‑box that writes into the frozen base model. They quantify this by measuring the number of bits changed in the underlying weights after training, using bit‑wise analysis across multiple fine‑tuning runs on Qwen2.5. By comparing adapter‑only updates to full fine‑tuning updates, they isolate the incremental write capacity. Experiments also separate supervised and reinforcement learning fine‑tunes.

## Results  
Experiments show that a 1 % adapter update corresponds to ~0.02 bits per parameter, while moving the same adapter budget into MLP yields ~0.04 bits per parameter—about twice as much. Privacy leakage measured via membership inference rises linearly with bits written, confirming the bit‑based metric. Supervised fine‑tuning adapters retain verbatim model knowledge (high bits), whereas RL adapters show negligible writes.

## Significance  
Understanding that adapters write only a few bits per parameter debunks folklore that they memorize large amounts of data. This quantitative measure enables designers to set safe limits on adapter capacity, ensuring privacy compliance without over‑fitting the base model.

## Related Concepts  
- Parameter-efficient fine-tuning (PEFT)  
- Low-rank adapters (LoRA)  
- Memorization analysis  
- Bit‑wise capacity measurement  
- Privacy leakage via membership inference
