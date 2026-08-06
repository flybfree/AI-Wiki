# Summary: 2026-08-05_10-59-53Z_SuppressionSticks_LocalityIsFragile_AClosed_LoopTa.md
Saved: 2026-08-05 22:29
Source: 2026-08-05_10-59-53Z_SuppressionSticks_LocalityIsFragile_AClosed_LoopTa.md
Model: None

---

## Summary  
The paper investigates how task‑vector subtraction affects multitask vision‑language‑action (VLA) policies across ten LIBERO‑Goal skills, revealing that the intervention is fast but locally fragile. It proposes a closed‑loop target‑and‑control audit to evaluate the locality of model editing interventions and quantify their impact on both targeted and unrelated tasks.

## Key Contributions  
- [Finding 1] Subtraction yields three regimes: target‑control separation for five skills, resistance for three, and global collapse for two.  
- [Finding 2] On held‑out initial states, suppressible targets achieve only ~52 % baseline‑normalized control retention while each edit harms at least one nominally unrelated control, indicating non‑local interference.  
- [Finding 3] A matched‑norm control reveals a local sign asymmetry around one Goal anchor; multi‑vector outcomes vary with anchor and scale, showing that cosine similarity does not capture this variation.

## Methodology  
The authors construct a closed‑loop audit by applying per‑skill task‑vector subtraction to VLA policies trained with different action heads (continuous‑regression, discrete‑token, flow‑matching). They evaluate performance on held‑out initial states and compare against baseline controls, measuring success rates, control retention, and cosine similarity. A single‑skill relearning probe is used to test whether the observed masking corresponds to unlearning or merely behavioral suppression.

## Results  
Across ten skills, five exhibit clean separation (targets suppressed while unrelated controls remain intact), three show resistance (targets are not suppressed but related controls degrade), and two collapse globally. The mean baseline‑normalized control retention after subtraction is 52 %. Cosine similarity of the task vectors does not explain these regimes. The matched‑norm control demonstrates a local sign asymmetry around one Goal anchor, with multi‑vector outcomes depending on both anchor and scale.

## Significance  
This work demonstrates that task‑vector arithmetic is a fast but brittle editing operation, underscoring the need for closed‑loop target‑and‑control evaluation when assessing locality in embodied model editing. It provides empirical evidence that interventions can unintentionally affect unrelated tasks, urging more rigorous assessment methods to avoid hidden side effects.

## Related Concepts  
task‑vector arithmetic, VLA policies, task‑vector subtraction, locality, closed‑loop audit, signed asymmetry, cosine similarity, Goal anchors, multi‑vector outcomes, single‑skill relearning probe, masked vs. unlearned behavior
