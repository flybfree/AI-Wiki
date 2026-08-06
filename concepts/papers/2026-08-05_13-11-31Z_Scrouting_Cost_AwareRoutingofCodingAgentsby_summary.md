# Summary: 2026-08-05_13-11-31Z_Scrouting_Cost_AwareRoutingofCodingAgentsbyScoutin.md
Saved: 2026-08-05 20:36
Source: 2026-08-05_13-11-31Z_Scrouting_Cost_AwareRoutingofCodingAgentsbyScoutin.md
Model: None

---

## Summary  
The paper introduces SuperScout, a cost‑aware routing system that first “scouts” a software repository to generate a verified handoff of reproduction claims before dispatching them to frontier language models. By separating the costly search phase from the expensive solving phase, SuperScout reduces total compute per solve by roughly one‑fifth while matching the best single model’s success rate on SWE‑bench Pro. The approach relies on a 7B‑parameter searcher that produces structured handoffs with false claims removed via sandbox verification and hidden states that improve routing decisions. This work demonstrates that repository‑level scouting can be an effective cost‑effective preprocessing step for coding agents.

## Key Contributions  
- **Finding 1:** SuperScout matches the best single model’s solve rate (159/266 tasks) at about a fifth of the total cost per solve, outperforming random traffic splitting.  
- **Finding 2:** The searcher’s hidden states enable accurate cost‑aware routing, while the handoff text alone has negligible impact on performance; calibration shows a redistribution of solving ability among fixers.  
- **Finding 3:** Adding new fixers requires no retraining because the router selects from a fixed set of four frontier models based solely on the structured handoff.

## Methodology  
The authors built SuperScout around two components: (1) a 7B‑parameter searcher, SuperScout‑7B, that explores the repository and produces a structured handoff containing reproduction claims; these claims are sandbox‑verified to strip false ones. (2) a resume‑based router that combines the task text with the searcher’s hidden states to dispatch each validated claim to one of four frontier fixers. The system is evaluated under the SWE‑bench Pro budget tier, and its cost per solve is measured by GPU time.

## Results  
On 266 tasks in the Python slice of SWE‑bench Pro, SuperScout achieved a solve rate of 159 (matching the best single model’s 158) while using roughly one‑fifth of the total compute cost. A no‑router ablation that always selects the cheapest fixer with the handoff ties the routed system on this benchmark, indicating that the handoff rather than routing decisions drives performance. Calibration experiments confirm that hidden states improve routing quality, whereas the handoff’s textual content has minimal effect.

## Significance  
SuperScout shows that repository‑level scouting can dramatically lower the cost of solving software issues without sacrificing accuracy, opening a scalable path for deploying multiple frontier fixers in production systems. The approach also provides a clear mechanism—hidden states—that can be leveraged to fine‑tune routing policies.

## Related Concepts  
- Frontier language models for coding assistance  
- Repository‑level issue resolution and scouting  
- Cost‑aware routing of AI agents  
- Structured handoff generation with sandbox verification  
- Hidden state utilization in decision making  
- Calibration studies to understand model behavior shifts
