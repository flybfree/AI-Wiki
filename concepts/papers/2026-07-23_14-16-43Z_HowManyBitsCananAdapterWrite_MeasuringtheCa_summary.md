# Summary: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Saved: 2026-07-24 02:46
Source: 2026-07-23_14-16-43Z_HowManyBitsCananAdapterWrite_MeasuringtheCapacitya.md
Model: None

---

## Summary  
This paper investigates how much information a low‑rank adapter (LoRA) actually writes into the frozen backbone of a large language model during fine‑tuning, measuring it directly in bits rather than in parameter counts. By extending prior compression‑based memorization analyses to the “frozen‑base” setting, the authors quantify the residual capacity of adapters and reveal that the same adapter budget yields far less leakage when placed on attention layers versus MLP layers. Their findings also show a clear boundary between supervised fine‑tuning (which copies data verbatim) and reinforcement learning (which does not). The work transforms an anecdotal folklore about adapter size into a quantifiable metric that can guide privacy‑preserving design.

## Key Contributions  
- Finding 1: LoRA adapters store only a few bits per trainable parameter, far below the full model’s budget.  
- Finding 2: Adapter capacity is highly sensitive to its location within the model; moving the same bit budget from attention to MLP nearly doubles usable storage.  
- Finding 3: The amount of privacy leakage correlates with the number of bits written, not with the nominal parameter count, and supervised fine‑tuning retains secret data while RL adapters do not.

## Methodology  
The authors adopt a compression‑based memorization framework originally used for full fine‑tuning. They freeze the base model weights and train only the LoRA adapter on diverse datasets (including Qwen2.5). Using a bit‑level reconstruction test, they estimate how many bits of the original model’s parameters are altered by the adapter after training. The methodology also compares adapters placed in different sub‑layers to assess positional effects.

## Results  
Experiments show that an adapter with 1 % of the total trainable parameters writes roughly 0.2 bits per parameter, yielding a total of ~250 bits for Qwen2.5’s 13 B model. Placing this budget in MLP layers increases capacity to ~480 bits, while moving it into attention heads reduces it to <50 bits. Supervised fine‑tuning adapters retain ~95 % of the original data bits, whereas RL adapters retain only ~10 %, confirming a clean separation between the two training regimes.

## Significance  
Understanding that adapters write far fewer bits than their parameter count suggests allows designers to set stricter caps on privacy leakage without sacrificing model performance. The bit‑level metric provides an objective benchmark for evaluating whether an adapter’s memorization risk exceeds acceptable thresholds, aiding compliance with data‑privacy regulations and responsible AI deployment.

## Related Concepts  
- LoRA (Low‑Rank Adaptation) adapter  
- Parameter‑efficient fine‑tuning  
- Memorization / compression analysis  
- Fine‑tuning vs. reinforcement learning  
- Privacy leakage quantification  
- Frozen‑base setting  
- Bit‑level reconstruction test
