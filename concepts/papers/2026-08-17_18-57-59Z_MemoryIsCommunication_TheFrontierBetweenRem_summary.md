# Summary: 2026-08-17_18-57-59Z_MemoryIsCommunication_TheFrontierBetweenRememberin.md
Saved: 2026-08-18 21:25
Source: 2026-08-17_18-57-59Z_MemoryIsCommunication_TheFrontierBetweenRememberin.md
Model: None

---

## Summary  
The paper investigates how bounded agents balance memory usage and peer communication to achieve a given decision performance, proposing the remembering–signaling frontier as the efficient boundary between these resources. It argues that when history can reduce task loss equally, larger reductions from memory should correspond to less needed peer messages. The authors formalize this trade‑off under cooperative tasks and test it empirically with referential games.

## Key Contributions  
- Finding 1: A theoretical frontier (remembering–signaling frontier) defines the set of achievable (memory rate, message rate) pairs for a fixed task loss threshold.  
- Finding 2: Empirically, in target‑repetition conditions, agents that rely more on memory transmit shorter successful messages.  
- Finding 3: Predictability from hidden cyclic rules does not shorten messages, indicating that the benefit of history is independent of rule predictability.

## Methodology  
The authors construct a theoretical model where agents allocate a fixed information budget between storing task‑relevant history and sending peer observations. They derive constraints on memory and message rates to meet a performance threshold, then simulate these trade‑offs in referential games with varying memory and message frequencies.

## Results  
Simulations confirm the frontier’s shape; higher memory usage yields lower message rates when loss reduction is high, matching the prediction that larger historical gains reduce communication needs. Message length correlates inversely with memory reliance only under target repetition, not under cyclic rule predictability.

## Significance  
The work bridges cognitive psychology and information theory, offering a quantitative framework for understanding how humans allocate memory versus social signaling in cooperative decision‑making.

## Related Concepts  
Memory; signaling; bounded agents; information budget; frontier analysis; referential games; task loss reduction; communication efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17053v1)
