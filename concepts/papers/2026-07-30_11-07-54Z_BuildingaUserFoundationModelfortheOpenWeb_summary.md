# Summary: 2026-07-30_11-07-54Z_BuildingaUserFoundationModelfortheOpenWeb.md
Saved: 2026-07-30 20:33
Source: 2026-07-30_11-07-54Z_BuildingaUserFoundationModelfortheOpenWeb.md
Model: None

---

## Summary  
The paper proposes a user foundation model for the open web, where user identity is fragmented across short, non‑persistent browsing sessions and historical data are often represented as aggregated counters. It addresses the limitation of prior models that assume stable, persistent identities by learning representations directly from these sparse histories using self‑supervised techniques. The approach improves downstream production tasks such as click prediction and bid win‑rate modeling. Experiments demonstrate statistically significant gains in real‑time bidding metrics.

## Key Contributions  
- [Finding 1] A user foundation model can be trained on fragmented open‑web browsing data without requiring persistent user identity.  
- [Finding 2] Self‑supervised pre‑training with masked language modeling combined with a sequence‑level contrastive objective yields robust embeddings for short, disjointed sessions.  
- [Finding 3] An LLM‑in‑the‑loop optimizer that selects the best code‑level “lifters” from a curated catalog improves encoder performance.

## Methodology  
The authors pre‑train a Transformer encoder using masked language modeling on user browsing sequences, then apply a sequence‑level contrastive objective to encourage similarity between related events. Fine‑tuning is performed on a click prediction task. Optimization leverages an LLM that iteratively proposes code edits (lifters) and selects the most beneficial ones from a catalog, embodying the LLM‑as‑optimizer paradigm in an industrial setting.

## Results  
The encoder improves RIG by +1.197% for the production bid win‑rate model and +1.354% for the CTR ranker. A seven‑day live A/B test confirms a +2.13% increase in CTR and a –1.13% reduction in eCPC, both with 80 % confidence intervals excluding zero.

## Significance  
This work shows that user foundations can thrive on open‑web data, challenging the assumption of persistent identity and providing a scalable solution for real‑time bidding and recommendation systems where historical signals are sparse and fragmented.

## Related Concepts  
User foundation model, self‑supervised learning, masked language modeling, sequence contrastive learning, LLM‑as‑optimizer, RIG (revenue impact gain), eCPC (effective cost per click).
