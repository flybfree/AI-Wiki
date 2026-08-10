# Summary: 2026-08-07_10-29-19Z_TransformersStruggletoUseTheirEmergentWorldModels_.md
Saved: 2026-08-09 22:54
Source: 2026-08-07_10-29-19Z_TransformersStruggletoUseTheirEmergentWorldModels_.md
Model: None

---

## Summary  
This paper investigates why large language models (LLMs) appear to “collapse” when solving the flat‑to‑flat Tower of Hanoi puzzle, a variant that requires more than three rings. By training small Transformers from scratch on precomputed solution traces and applying causal interpretability techniques, the authors demonstrate that these Transformers develop an emergent, geometrically faithful world model (the Sierpinski triangle) that is essential for solving the task. When the same analysis is applied to frontier LLMs such as Qwen3.6‑27B and DeepSeek‑R1‑Distill‑Qwen‑32B, the models encode this world model perfectly at the end of the prompt yet still fail on most instances with four or more rings. The failure stems from a decaying representation rather than its absence, suggesting that LLMs build world models but lose them during inference.

## Key Contributions  
- [Finding 1] Small Transformers trained from scratch exhibit an emergent Sierpinski‑triangle world model that is linearly decodable and causally involved in solving the flat‑to‑flat Tower of Hanoi.  
- [Finding 2] Large LLMs encode a near‑perfect Sierpinski representation at the end of the prompt but experience performance decay when more than three rings are required, indicating loss of the model’s world knowledge.  
- [Finding 3] Injecting the prompt‑time world‑model representation at inference time can restore or improve task performance, proving that maintenance—not creation—of the representation is the bottleneck.

## Methodology  
The authors first construct a set of precomputed solution traces for both standard and flat‑to‑flat Tower of Hanoi puzzles. Using these traces, they train miniature Transformers from scratch and employ interpretability tools (e.g., probing classifiers, decoding experiments) to extract the internal state representation. The same pipeline is then applied to two large reasoning models via extended chain‑of‑thought prompting. Throughout the process, the authors probe the model’s representation at various prompt stages and test whether injecting that representation into the inference step improves output quality.

## Results  
- Small Transformers achieve near‑optimal solutions on both puzzle variants, confirming that the Sierpinski world model is sufficient for planning.  
- Large LLMs show perfect encoding of the Sierpinski structure at the end of the prompt but fail when the number of rings exceeds three; performance drops sharply as the representation decays.  
- When the extracted prompt‑time representation is injected during generation, task success rates rise dramatically, demonstrating that preserving the world model restores capability.

## Significance  
These findings reframe the observed “collapse” in large reasoning models not as a failure to build world models but as a maintenance problem: LLMs construct rich, causal representations that evaporate over time. By highlighting this decay mechanism and providing an injection strategy, the paper offers a pathway to more robust planning capabilities and underscores the importance of preserving emergent knowledge during inference.

## Related Concepts  
- Emergent world model  
- Sierpinski triangle (geometric representation of Hanoi state space)  
- Chain‑of‑thought prompting  
- Causal interpretability  
- Representation decay / maintenance of latent knowledge
