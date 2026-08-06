# Summary: 2026-08-04_18-00-04Z_FinPerMA_ATheory_Informed_Event_GroundedPersonaliz.md
Saved: 2026-08-05 20:22
Source: 2026-08-04_18-00-04Z_FinPerMA_ATheory_Informed_Event_GroundedPersonaliz.md
Model: None

---

## Summary  
The paper introduces FinPerMA, a theory‑informed benchmark that tests whether LLM agents can maintain and update an individualized user model over long horizons in high‑stakes domains such as financial advising. It focuses on event‑driven preference adaptation after material shocks, which existing benchmarks ignore. The authors combine deterministic impact rules with controlled LLM narration to generate longitudinal investor trajectories and then evaluate how well the agents integrate these events into their persistent memory. Their results show that even frontier models struggle to retain personalized information beyond a modest threshold.

## Key Contributions  
- **Finding 1**: FinPerMA creates an event‑grounded benchmark that evaluates personalized memory against frozen longitudinal investor trajectories, explicitly measuring preference adaptation after shocks.  
- **Finding 2**: The generation pipeline merges deterministic theory‑informed impact rules with controlled LLM narration and automated quality screening; a Post‑Shock checkpoint isolates whether the agent has incorporated the material event into its persistent user model.  
- **Finding 3**: Experiments reveal that no full‑context configuration exceeds ~0.47 overall accuracy or ~39 % on multiple‑choice questions, and simple retrieval often outperforms purpose‑built memory systems, especially after shocks.

## Methodology  
The authors constructed a dataset of 2,994 questions spanning 276 personas representing diverse investor profiles. They applied deterministic impact rules derived from economic theory to generate realistic shock events (e.g., market crashes). Using these events, they prompted frontier LLMs to produce narratives that would update the user’s memory. The system then screened outputs for factual consistency and preference alignment before feeding them into a Post‑Shock checkpoint that assesses whether the event was integrated into the persistent model.

## Results  
Across seven frontier LLMs and up to seven memory configurations, average overall accuracy hovered around 0.47 (≈ 47 %) and multiple‑choice performance peaked near 39 %. Attribution analysis indicated that summary‑based memory preserved factual details but lost the preference signals essential for personalization; simple retrieval consistently outperformed custom memory systems after shock events.

## Significance  
FinPerMA fills a critical gap in LLM research by providing an empirical test of personalized memory under real‑world, event‑driven scenarios. It demonstrates that maintaining accurate, up‑to‑date user models is challenging even for state‑of‑the‑art models, highlighting the need for better integration mechanisms and influencing future design of personal assistants.

## Related Concepts  
event‑grounded benchmarking, theoretical impact rules, longitudinal investor trajectories, preference adaptation, persistent user model, shock integration, retrieval‑based vs. memory‑system performance, personalization in LLM agents
