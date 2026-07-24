# Summary: 2026-07-23_16-34-14Z_What_Where_andHow_DisentanglingtheRolesofTask_Lang.md
Saved: 2026-07-23 21:01
Source: 2026-07-23_16-34-14Z_What_Where_andHow_DisentanglingtheRolesofTask_Lang.md
Model: None

---

## Summary  
This paper investigates how three factors—task (Python vs. Rust), language (the specific syntax of each language), and the underlying model—shape the way code‑model representations are organized. By applying a circuit‑extraction technique to a 2×2 experimental design that combines Python and Rust with two large code models, the authors isolate which factor determines what concepts receive dedicated circuitry, where those circuits appear in the network, and how they evolve across layers. The study finds strong task‑driven agreement on which concepts are circuited, model‑specific placement of those circuits, and a lack of universal structural patterns.  

## Key Contributions
- [Finding 1] Task is the primary driver of which code concepts receive dedicated circuitry, as measured by Spearman’s ρ ≈ 0.64 for both Python (p < 10⁻⁷) and Rust.  
- [Finding 2] The model determines where circuits are instantiated in the network and how they grow across layers: Qwen2.5‑Coder places circuits around layer L17–19, while DeepSeek‑Coder‑V1 does so earlier at L6–7; Qwen also gives atomic concepts an early spike that DeepSeek lacks.  
- [Finding 3] Universality is limited to the “what” (task) dimension; the spatial and temporal layout of circuits varies by model, showing that representational content is not fixed across architectures.  

## Methodology  
The authors employed a circuit‑extraction framework on four cells: Python + Qwen2.5‑Coder‑7B, Python + DeepSeek‑Coder‑V1‑6.7B, Rust + Qwen2.5‑Coder‑7B, and Rust + DeepSeek‑Coder‑V1‑6.7B. They catalogued 58 Python concepts and 57 Rust constructs, extracting the neuronal subgraphs that encode each concept. Linear probes and ablation experiments validated that these circuits are functional representations rather than artifacts of surface syntax.  

## Results  
Spearman’s ρ values confirm task‑dependent circuiting (ρ ≈ 0.64). Qwen’s circuits appear later (L17–19) whereas DeepSeek’s are earlier (L6–7); Qwen also shows an early spike for atomic concepts that DeepSeek does not. Rust constructs receive 2–3× more circuitry than their Python counterparts in both models, indicating language‑specific elaboration. Both models share neurons between languages: 6/7 and 7/7 paired constructs are common, with DeepSeek sharing 1.94× more than Qwen—a pattern not predicted previously. A tight neuron cluster binds nine Rust type‑and‑trait keywords (Jaccard 0.535 vs null 0.112, p < 0.001), revealing a hidden semantic dimension. Ablation and linear probing confirm that these circuits are functionally active.  

## Significance  
The work demonstrates that code representations are not monolithic; they are sculpted by the interplay of task, language syntax, and model architecture. It challenges the notion of universal circuit patterns in neural models, showing that while “what” is largely shared, “where” and “how” differ markedly across implementations. These findings open avenues for designing more efficient, language‑aware code generators and for probing representation learning with finer granularity.  

## Related Concepts  
- Circuit extraction  
- Code model representations  
- Task‑dependent representation  
- Layer‑specific encoding  
- Neuron sharing between languages  
- Jaccard similarity analysis
