# Summary: 2026-07-22_18-26-57Z_SalesLoop_ReinforcementLearningfromPerformanceFeed.md
Saved: 2026-07-24 02:10
Source: 2026-07-22_18-26-57Z_SalesLoop_ReinforcementLearningfromPerformanceFeed.md
Model: None

---

## Summary  
The paper tackles the gap between high‑performing offline lead‑ranking models and their real‑world performance in a CRM system. It proposes **SalesLoop**, a reinforcement‑learning framework that continuously updates rankings based on actual conversion outcomes, thereby closing the feedback loop between prediction and business results. By introducing a position‑weighted reward and a discriminative GRPO objective, SalesLoop learns to surface high‑intent leads more effectively than static baselines. The approach has been validated in a 160‑day production A/B test with millions of leads across two Chinese markets.

## Key Contributions  
- **Finding 1:** Identifies three core mismatches—offline‑online metric mismatch, pointwise‑listwise objective misalignment, and temporal distribution drift—that cause offline accuracy to degrade in production.  
- **Finding 2:** Introduces a performance‑aware reward that combines conversion outcomes with ranking position and conversion velocity, enabling the model to value leads that convert quickly even if they are lower in rank.  
- **Finding 3:** Implements Discriminative GRPO, an adapted Group Relative Policy Optimization objective tailored for listwise ranking, which optimizes relative performance across the entire leaderboard.

## Methodology  
SalesLoop builds a closed‑loop RL system where the model’s prediction is treated as an action, and the observed conversion outcome serves as feedback. The reward function is defined as \(R = \sum_i w_{\text{pos}}^{(i)} \cdot \mathbf{1}_{\text{converted}}(i) \times v_{\text{conv}}(i)\), where \(w_{\text{pos}}\) decays with rank and \(v_{\text{conv}}\) reflects conversion speed. The discriminative GRPO objective minimizes the KL divergence between the predicted ranking distribution and the empirical ranking while maximizing a listwise loss that rewards higher‑ranked conversions relative to lower ones.

## Results  
In an A/B test involving 16.5 million leads and 280 sales specialists, SalesLoop achieved NDCG@K +7.9 % and P@K +15.8 % over the strongest static baseline. Cumulative lift was statistically significant at +4.7 % (p=0.047) for Top‑10 recall and +8.7 % (p=0.002) for conversion rate. The ranking backbone maintained a 44.1 % Top‑10 recall in production, surfacing high‑intent leads that convert at 2.3× the rate of specialist baselines.

## Significance  
SalesLoop demonstrates that reinforcement learning can directly improve CRM lead rankings by aligning model objectives with real conversion dynamics, reducing reliance on static offline metrics and delivering measurable revenue impact for sales teams.

## Related Concepts  
- Reinforcement Learning (RL)  
- Group Relative Policy Optimization (GRPO)  
- Discriminative ranking  
- NDCG@K, P@K metrics  
- Closed‑loop feedback systems
