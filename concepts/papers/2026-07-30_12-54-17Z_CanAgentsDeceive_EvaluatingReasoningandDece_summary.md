# Summary: 2026-07-30_12-54-17Z_CanAgentsDeceive_EvaluatingReasoningandDeceptionin.md
Saved: 2026-07-30 20:36
Source: 2026-07-30_12-54-17Z_CanAgentsDeceive_EvaluatingReasoningandDeceptionin.md
Model: None

---

## Summary  
The paper aims to evaluate whether large language models can deceive in high‑stakes settings by using a social deduction game, Secret Hitler, as a controlled proxy for adversarial behavior. It introduces ParliamentBench, an open‑source benchmark framework that measures reasoning and deception across 16 LLMs playing each other or humans. The study isolates three metrics: social deduction performance, reasoning ability, and deceptive consistency. Frontier models outperform baselines, while many struggle with sustained deception.

## Key Contributions  
- Finding 1: Frontline LLMs (GPT‑5.4, Kimi K2.5, Grok 4.1 Fast, DeepSeek 3.1 Terminus) achieve top performance across both cooperative and deceptive roles.  
- Finding 2: Most models fail to maintain a consistent deceptive persona, with deception retention dropping below 50% over the game.  
- Finding 3: The benchmark shows that deception is not uniformly strong; some models perform close to random (≈33%) while others reach near simple algorithmic levels (≈45%).

## Methodology  
ParliamentBench simulates Secret Hitler, a social deduction game where players must deduce hidden roles using limited information. LLMs are deployed as agents that generate statements, cast votes, and provide reasoning. The framework runs 1 600 simulated matches across pairwise LLM‑LLM, LLM‑human, and human‑human games, comparing outcomes to large online game datasets. Three metrics isolate social deduction (vote accuracy), reasoning (logical consistency of statements), and deceptive consistency (maintaining the hidden role). Experiments measure performance via success rates and retention.

## Results  
The top four models consistently outperform baselines, with average deception scores above 70 % in short games but falling below 50 % over full matches. Weakest models reach near‑random levels. Human baseline shows moderate performance (~60 %). Deception retention is the weakest metric for many models.

## Significance  
Understanding agent deception informs safety of LLMs in critical domains; this benchmark provides a reproducible test to assess and compare deceptive capabilities, highlighting gaps between capability and consistency.

## Related Concepts  
Social deduction games (Secret Hitler), large language model reasoning, deception detection metrics, information asymmetry, benchmarking frameworks for AI agents.
