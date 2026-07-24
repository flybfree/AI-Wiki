# Summary: 2026-07-22_18-26-57Z_SalesLoop_ReinforcementLearningfromPerformanceFeed.md
Saved: 2026-07-24 02:12
Source: 2026-07-22_18-26-57Z_SalesLoop_ReinforcementLearningfromPerformanceFeed.md
Model: None

---

## Summary  
The paper addresses the gap between offline model accuracy and real‑world sales lead ranking performance in CRM systems, identifying three gaps: metric mismatch, objective misalignment, and temporal distribution drift. It proposes SalesLoop, a reinforcement learning framework that creates a closed feedback loop using performance‑aware rewards and discriminative GRPO. The method improves NDCG@K by 7.9 % and P@K by 15.8 % over static baselines. A 160‑day production test with 280 specialists shows statistically significant lift of +4.7 % and +8.7 %.

## Key Contributions  
- Finding 1: Offline‑online metric mismatch is a core issue.  
- Finding 2: Pointwise‑listwise objective misalignment hinders ranking.  
- Finding 3: Temporal distribution drift degrades model relevance.  

## Methodology  
The authors introduce a performance‑aware reward that combines conversion outcomes with rank position and speed of response, feeding this into Discriminative GRPO—a variant of Group Relative Policy Optimization designed for listwise ranking. This creates a closed loop where the model’s predictions are continuously optimized based on real sales results rather than static offline metrics.  

## Results  
SalesLoop achieves NDCG@K +7.9 % and P@K +15.8 % over the strongest static baseline. In production, it reaches Top‑10 % recall of 44.1 % and delivers high‑intent leads at a conversion rate 2.3× higher than specialist baselines. The A/B test over 16.5 M leads and two provincial markets yields cumulative lift +4.7 % (p=0.047) and +8.7 % (p=0.002).  

## Significance  
By aligning model training with actual business outcomes, SalesLoop reduces reliance on offline proxies, improves sales efficiency, and provides measurable ROI for CRM systems.  

## Related Concepts  
- Reinforcement Learning  
- Group Relative Policy Optimization (GRPO)  
- Discriminative RL  
- NDCG@K  
- P@K  
- Closed feedback loop  
- Ranking backbones
