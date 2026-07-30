# Summary: 2026-07-30_HowenablingtwosettingstripledourscoresontheARC-AGI.md
Saved: 2026-07-30 00:04
Source: 2026-07-30_HowenablingtwosettingstripledourscoresontheARC-AGI.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The OpenAI team discovered that enabling two API settings—retained reasoning and compaction—in their harness for GPT‑5.6 Sol dramatically improved performance on the ARC‑AGI‑3 benchmark, raising scores from 13.3 % to 38.3 %, effectively tripling them. This boost was achieved by preserving internal reasoning state across game actions, allowing the model to remember its past thoughts rather than discarding it each turn.

## Key Takeaways  
- Enabling retained reasoning and compaction settings tripled ARC‑AGI‑3 scores for GPT‑5.6 Sol.  
- The original harness forced the model to re‑solve every action, erasing prior reasoning and limiting performance.  
- API‑level harness choices can have a larger impact on benchmark results than model capabilities alone.

## Context  
ARC‑AGI‑3 is an open benchmark that measures how well AI agents learn from generic 2D puzzle games without explicit instructions. It emphasizes fairness by using a simple, tool‑free harness, contrasting with commercial approaches that tailor harnesses to each model’s quirks. The ARC methodology also defines Relative Human Action Efficiency (RHAE), comparing model actions to human performance.

## Implications  
The findings highlight that benchmark scores are not solely reflective of model intelligence but also of engineering decisions around API settings and state management. For researchers and developers, optimizing harnesses—especially preserving reasoning—can be as crucial as advancing model architecture, potentially reshaping how AI capabilities are evaluated in the industry.
