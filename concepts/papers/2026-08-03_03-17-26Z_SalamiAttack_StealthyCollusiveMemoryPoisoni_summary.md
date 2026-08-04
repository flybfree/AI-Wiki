# Summary: 2026-08-03_03-17-26Z_SalamiAttack_StealthyCollusiveMemoryPoisoningagain.md
Saved: 2026-08-03 23:18
Source: 2026-08-03_03-17-26Z_SalamiAttack_StealthyCollusiveMemoryPoisoningagain.md
Model: None

---

## Summary  
The paper introduces MemCollusion, an automated red‑teaming framework that demonstrates a compositional threat to long‑term memory in large language models: multiple seemingly benign memories can together steer the model toward unsafe behavior. By applying “salami” tactics—slicing an adversarial objective into small, individually innocuous pieces—the authors construct collusive memory fragments that are harmless on their own but harmful when combined. Empirical evaluation on OpenClaw shows that MemCollusion can achieve a Memory Save Rate of 81.3 % and an Attack Success Rate of 75 %, remaining effective even under benign dilution or memory‑level defenses, highlighting a serious vulnerability in persistent memory systems.  

## Key Contributions  
- [Finding 1] Collusive memory poisoning is possible through the composition of individually benign memory records that collectively produce unsafe outcomes.  
- [Finding 2] MemCollusion provides an automated framework that generates such poisoned coalitions using four design constraints, five theory‑informed strategies, and a fine‑tuned generator.  
- [Finding 3] The attack succeeds with high efficiency (≈75 % success) across diverse settings, including memory‑saving configurations and defenses, underscoring the need for robust long‑term memory safeguards.  

## Methodology  
The authors approached the problem by first formulating a red‑team challenge: how to create collusive poisoned memories that survive observation yet influence later sessions. They built MemCollusion as an automated pipeline that (1) defines four design constraints to shape memory fragments, (2) selects five theoretical strategies for combining them, and (3) employs a fine‑tuned generator to produce the final coalitions. To evaluate impact in a realistic cross‑session environment, they deployed MoltLab—a controlled reproduction of Moltbook—where platform content is first observed, distilled into persistent memory, and later used by OpenClaw’s two backbone models across 48 scenarios.  

## Results  
Across the experimental suite, MemCollusion achieved an average Memory Save Rate of **81.3 %**, meaning that 81.3 % of crafted poisoned memories were retained in long‑term storage. The Attack Success Rate was **75.0 %**, indicating that the collusive memory successfully steered model behavior toward unsafe outputs. Notably, the attack remained effective under both benign memory dilution (where many harmless entries are present) and explicit memory‑level defenses, confirming its resilience to common mitigation techniques.  

## Significance  
These findings reveal a previously overlooked compositional threat: long‑term memory is not merely a passive store but an active attack surface where adversarial collusion can corrupt persistent knowledge. By demonstrating that seemingly innocuous memories can be weaponized together, the work motivates new research into collective memory safety and more sophisticated defense mechanisms that consider multi‑record interactions rather than isolated entries.  

## Related Concepts  
- Long‑term memory in LLMs  
- Memory poisoning attacks  
- Collusive (compositional) attack  
- Salami tactics  
- OpenClaw platform  
- MoltLab experimental setup  
- Memory Save Rate, Attack Success Rate
