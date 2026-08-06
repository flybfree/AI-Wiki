# Summary: 2026-08-05_05-14-39Z_Multi_ObjectiveRankingforLive_Streaming_BalancingF.md
Saved: 2026-08-05 22:24
Source: 2026-08-05_05-14-39Z_Multi_ObjectiveRankingforLive_Streaming_BalancingF.md
Model: None

---

## Summary  
The paper tackles the challenge of ranking live‑streaming recommendations where user behavior is sparse and delayed, with segment‑specific biases. It introduces a multi‑objective ranking framework that balances fresh signals (immediate feedback) and delayed signals (later interactions), using a segment‑aware targeting module to optimize scores across different lifecycle stages. The solution employs a Multi‑gate Mixture‑of‑Experts architecture that jointly models correlated targets while reducing model parameters by 41.9 %.

## Key Contributions  
- [Finding 1] A delayed window approach that extends feedback collection beyond immediate responses, capturing later user actions such as follows and likes.  
- [Finding 2] A multi‑model architecture that combines fresh and delayed signals with a segment‑aware targeting module to optimize ranking scores for each user stage.  
- [Finding 3] Multi‑gate Mixture‑of‑Experts (MMoE) integration that jointly models correlated targets, achieving a 41.9 % reduction in model parameters compared to independent models.

## Methodology  
The authors collect both fresh and delayed interaction data across the user lifecycle—watching, chatting, following, and spending. This heterogeneous dataset is fed into separate but integrated models: one that processes immediate feedback and another that ingests later signals. A segment classifier assigns each viewer a stage (e.g., new, engaged, churned) to tailor ranking scores accordingly. The MMoE layer employs gating mechanisms to share representations across the two models, thereby reducing parameter count while preserving expressiveness.

## Results  
Online A/B testing on the primary platform shows a +0.09 % increase in Daily Active Viewers (DAV), generating millions more annual active viewer days. Highly engaged viewers experience a +0.56 % rise in capped Average Revenue Per User (ARPU). Newer and less‑engaged viewers see an additional +0.15 % DAV boost from segment‑aware targeting, while the MMoE enhancement contributes +0.08 % overall DAV and +0.27 % new follows. A separate test on Twitch mobile live feed yields a +1.12 % increase in positive user‑channel interactions (clicks, follows, likes), demonstrating cross‑use‑case applicability.

## Significance  
This work provides a scalable, low‑latency ranking system that simultaneously balances multiple business objectives—maximizing viewership and revenue across diverse user populations. By leveraging delayed feedback and segment‑aware strategies, the approach improves both engagement metrics and monetization without sacrificing performance. The parameter‑efficient MMoE design makes the solution deployable at scale, offering a practical alternative to larger, less efficient models.

## Related Concepts  
- Multi‑objective optimization  
- Delayed feedback modeling  
- Segment‑aware targeting  
- Mixture‑of‑Experts (MMoE) with gating  
- A/B testing for online experiments  
- ARPU and DAV metrics
