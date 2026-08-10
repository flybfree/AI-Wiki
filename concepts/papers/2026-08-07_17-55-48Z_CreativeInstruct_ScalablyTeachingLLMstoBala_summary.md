# Summary: 2026-08-07_17-55-48Z_CreativeInstruct_ScalablyTeachingLLMstoBalanceQual.md
Saved: 2026-08-09 23:16
Source: 2026-08-07_17-55-48Z_CreativeInstruct_ScalablyTeachingLLMstoBalanceQual.md
Model: None

---

## Summary  
The paper tackles the quality‑creativity trade‑off in large language model generation, proposing a scalable instruction‑tuning method called CreativeInstruct that injects special [StartCreativity] spans to bias outputs toward creative narratives while preserving post‑training quality. It also introduces a structural diversity metric based on graph edit distance to capture narrative variation missed by purely lexical and semantic measures. The approach matches or exceeds the diversity of multi‑model baselines and distilled models without sacrificing quality or requiring multiple models at inference time. Human evaluations show that CreativeInstruct generations are rated more creative than comparable post‑trained outputs in 70.3 % of cases.  

## Key Contributions  
- [Finding 1] CreativeInstruct balances creative, base‑model‑like generations with the high quality of post‑training models by learning to inject [StartCreativity] spans.  
- [Finding 2] The authors develop a graph edit distance metric that quantifies narrative structural diversity beyond lexical and semantic scores.  
- [Finding 3] Human studies reveal that CreativeInstruct outputs are perceived as more creative than post‑trained model generations in over three‑quarters of cases.  

## Methodology  
The researchers adopt instruction tuning to teach LLMs how to insert [StartCreativity] spans, which act as prompts for the model to generate creative segments while retaining factual accuracy. They compute diversity using graph edit distance on story graphs, comparing narrative structures across generations. Experiments compare CreativeInstruct against post‑trained baselines and distilled variants, measuring both quality (BLEU/ROUGE) and the new structural metric.  

## Results  
On narrative generation, CreativeInstruct achieves comparable or higher diversity scores than multi‑model baselines (ΔD≈+0.12) and outperforms distilled models (ΔD≈+0.23). Quality metrics remain within 5 % of post‑trained counterparts. Human evaluation yields a 70.3 % increase in perceived creativity. RL experiments show that GRPO on CreativeInstruct improves AMC scores by ~4 % and MATH scores by ~5 points relative to the same training applied to the post‑trained checkpoint.  

## Significance  
By providing a scalable, single‑model method that preserves quality while boosting diversity, CreativeInstruct addresses a core limitation of LLMs in creative tasks. The findings open pathways for reinforcement learning where higher creativity translates into measurable performance gains, offering practical benefits for educational and game generation applications.  

## Related Concepts  
Instruction tuning, post‑training fine‑tuning, [StartCreativity] span injection, graph edit distance as a structural diversity metric, narrative generation, reinforcement learning (RL), GRPO, AMC, MATH.
