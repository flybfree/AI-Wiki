# Summary: 2026-07-29_19-43-40Z_GoodRankers_BadObjectives_BilinearContrastiveCriti.md
Saved: 2026-07-30 23:10
Source: 2026-07-29_19-43-40Z_GoodRankers_BadObjectives_BilinearContrastiveCriti.md
Model: None

---

## Summary  
The paper investigates why bilinear contrastive critics, which are widely used as rankers for best‑of‑K action selection in reinforcement learning, can produce poor or unsafe rankings despite their popularity. It shows that the raw bilinear scores suffer from norm drift and cosine saturation, leading to off‑support actions being selected with high regret. The authors propose a controlled support decomposition and demonstrate that true value‑calibrated objectives (e.g., Bellman TD‑Q) outperform these critics in several navigation tasks.  

## Key Contributions  
- [Finding 1] Unbounded bilinear scores amplify embedding norms, causing large off‑support values to dominate the ranking despite cosine bounding.  
- [Finding 2] A controlled support decomposition reveals that most raw bilinear regret stems from norm drift rather than intrinsic ranking flaws.  
- [Finding 3] Contrastive critics remain useful for compatibility rankers but fail as reliable action selectors without value‑calibrated scalar feedback.  

## Methodology  
The authors employ a mixed approach: first, they analyze the behavior of bilinear contrastive critics through theoretical decomposition (support vs. raw score contributions) and empirical simulation. They then conduct extensive experiments across four OGBench navigation tasks—PointMaze, AntMaze, HumanoidMaze, and an exact‑Q* toy problem—comparing bilinear critics with Bellman TD‑Q controllers. The study also includes a training/readout decomposition to isolate the impact of cosine normalization on ordering quality.  

## Results  
Simulator rollouts show that bilinear critics incur single‑step selection costs on PointMaze and exact‑Q* but perform poorly (well‑powered nulls) in AntMaze and HumanoidMaze, where self‑correction is possible. Cosine‑bounded critics still select off‑support actions from most pools with comparable regret to raw bilinear scores. The top score decile of contrastive scores is weakly calibrated or inverted across tasks, and they do not order fixed‑query actions by value. In contrast, Bellman TD‑Q succeeds even in parameter‑matched function‑class control.  

## Significance  
This work clarifies a critical limitation of bilinear contrastive critics: their rankers are valuable for compatibility but unsafe for autonomous action selection without proper value calibration. The findings guide researchers toward hybrid objectives that combine ranking with scalar value signals, improving both safety and performance in complex navigation environments.  

## Related Concepts  
- Bilinear contrastive critic  
- Cosine bounding  
- Norm drift  
- Support decomposition  
- Bellman TD‑Q (value‑calibrated objective)  
- Best‑of‑K action selection  
- Off‑support actions  
- Scoring calibration
