# Summary: 2026-08-06_10-51-34Z_MACRO_MarkovChainRoutingofTransformerLayers.md
Saved: 2026-08-06 20:39
Source: 2026-08-06_10-51-34Z_MACRO_MarkovChainRoutingofTransformerLayers.md
Model: None

---

## Summary  
The paper proposes MACRO, a Markov Chain Routing framework that learns task‑specific execution paths through transformer layers without altering model weights. It enables dynamic layer skipping, repeating and residual addition via a context‑dependent policy conditioned on indices, budget phases, displacement, and operator context. The routing is learned from training feedback and decoded with top‑k Viterbi to obtain high‑probability programs. MACRO improves accuracy by 5 % over unrouted baselines and beats Dr. LLM by 7.2 %, while cutting search time ninefold.  

## Key Contributions  
- [Learning a task‑specific Markov policy for layer routing without modifying model parameters.]  
- [Using top‑k Viterbi decoding to obtain high‑probability candidate programs efficiently.]  
- [Achieving +5 % average accuracy gain and +7.2 % over Dr. LLM with 9.4× faster search.]  

## Methodology  
The authors treat the sequence of transformer layers as a Markov chain where each state corresponds to a layer index and transition probabilities are conditioned on contextual cues such as computation budget, directional displacement, and operator context. During training they collect trajectories of hidden states and compute reward‑based policy gradients to update transition weights. At inference the learned distribution is sampled or decoded via Viterbi to produce an optimal route that can perform skip (jump forward/backward), repeat (stay at same layer) and residual addition (add hidden state) operations.  

## Results  
Across reasoning benchmarks on open‑weight LLMs, MACRO yields a 5 % average accuracy boost over unrouted models; the largest gains are observed in small models. It surpasses Dr. LLM by 7.2 % while reducing route search time from 14.8 to 1.6 hours (a 9.4× speed‑up). The code is publicly released at https://github.com/Batorskq/MACRO.  

## Significance  
This work demonstrates that dynamic layer routing can be learned end‑to‑end, offering a scalable alternative to static or weight‑modifying approaches; the efficiency gains make it viable for real‑time inference and large‑scale deployment.  

## Related Concepts  
- Markov chain  
- Viterbi decoding  
- Transformer layers  
- Dynamic routing  
- Skip / repeat / residual operations  
- Context‑conditioned policy  
- Top‑k sampling
