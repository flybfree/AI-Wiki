# Summary: 2026-08-07_17-17-18Z_DiffusionLLMsasTargetsandAdversaries_MechanisticSa.md
Saved: 2026-08-09 23:12
Source: 2026-08-07_17-17-18Z_DiffusionLLMsasTargetsandAdversaries_MechanisticSa.md
Model: None

---

## Summary  
The paper investigates diffusion‑based large language models (DLLMs) as both safety targets and adversaries, revealing that their alignment mechanisms are fragile and can be exploited via mechanistic attacks. It demonstrates that safety is sparse and transferable across architectures, enabling high‑success rates for jailbreaks with minimal generation cost.  

## Key Contributions  
- Finding 1: Safety alignment in DLLMs remains sparse and transferable across architectures; direct safety neuron mapping enables transfer attacks.  
- Finding 2: Self‑pruning dramatically increases attack success rates (ASR) from ~2.6 % to 73.8 % on LLaDA, and from 1.9 % to 86.6 % on Dream.  
- Finding 3: SN‑Guided Diffusion achieves near‑perfect prompt separability (AUROC = 1.0) and high transfer ASR up to 77.1 % on Llama‑3‑8B‑Instruct, 86.9 % on Qwen2.5‑7B‑Instruct, and 74.3 % against Gemini‑2.5‑Flash‑Lite, using only 20 generation episodes per prompt.  

## Methodology  
The authors first map safety neurons from autoregressive predecessors to diffusion models via pruning experiments, then develop SN‑Guided Diffusion—a black‑box offline jailbreak that steers the denoising process away from safety‑triggering regions using a weighted safety neuron loss, trained without access to model internals.  

## Results  
Self‑pruning raises ASR dramatically: LLaDA 2.6 % → 73.8 %, Dream 1.9 % → 86.6 %; transfer pruning yields 73.2 % / 86.3 % on Qwen2.5 and Fast‑dLLM; SN‑Guided Diffusion reaches AUROC = 1.0, transfer ASR up to 77.1 % (Llama‑3), 86.9 % (Qwen2.5), 74.3 % (Gemini) with just 20 generations per prompt.  

## Significance  
These findings expose that diffusion alignment is not robust; safety mechanisms can be circumvented efficiently, undermining the promise of diffusion models as safer alternatives to autoregressive LLMs and highlighting the need for more comprehensive mechanistic safeguards.  

## Related Concepts  
- Diffusion Large Language Models (DLLMs)  
- Autoregressive next‑token prediction  
- Safety alignment / jailbreaking  
- Self‑pruning, transfer pruning  
- Weighted safety neuron loss  
- AUROC (Area Under ROC Curve)
