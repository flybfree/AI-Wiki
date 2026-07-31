# Summary: 2026-07-30_15-19-18Z_LLMsstruggletosimulatehumanbeliefupdatesincontroll.md
Saved: 2026-07-30 22:16
Source: 2026-07-30_15-19-18Z_LLMsstruggletosimulatehumanbeliefupdatesincontroll.md
Model: None

---

## Summary  
The authors investigate whether large language models can faithfully replicate the way human participants revise their opinions after encountering online discussion content. By conditioning six LLMs on persona data derived from demographics and personality traits, they compare model‑generated belief updates to the actual stance changes recorded from 391 UK study participants on Prolific. The experiment reveals that only a few models can reproduce the post‑stance distribution when provided with participants’ true starting positions, while all models generate biased or incomplete simulations otherwise. This work directly tests the suitability of LLMs as stand‑in human agents in controlled social‑science settings.

## Key Contributions  
- [Finding 1] Some LLMs (Qwen3‑32B and GPT‑5‑Mini) can match the human post‑stance distribution, but only when given participants’ actual initial stances; all six models fail to simulate those starting positions themselves.  
- [Finding 2] Across every model three systematic biases appear: overrepresentation of neutral positions, more frequent but smaller belief shifts than observed in humans, and a failure to rank Reddit comments by convincingness.  
- [Finding 3] Demographic or personality‑trait personas do not consistently improve LLM fidelity; the effect on simulated beliefs is negligible.

## Methodology  
The researchers selected six state‑of‑the‑art LLMs and created persona profiles for each participant based on collected demographic and personality data. Participants were shown Reddit comments about three topics, updated their stances, and those changes were recorded as ground truth. The LLM simulations were run in a one‑to‑one mapping: the model’s output was compared directly to the human post‑stance distribution. The experiment was performed under controlled conditions with identical persona inputs for both humans and models.

## Results  
When participants’ initial stances were supplied, Qwen3‑32B and GPT‑5‑Mini produced belief update distributions that closely resembled the empirical data, achieving a high pointwise agreement. All other LLMs either deviated significantly or could not reproduce the neutral‑position bias seen in humans. The three observed biases—overrepresentation of neutrality, smaller shifts than human updates, and inability to rank comments by persuasiveness—were present in every model, indicating that the failures are systematic rather than random.

## Significance  
The findings highlight a critical limitation: LLMs used as proxies for human participants can only be reliable when their starting beliefs are explicitly provided. Current multi‑round social‑media simulations rarely supply such realistic initial conditions, making LLM‑based experiments prone to inaccurate representations of belief dynamics. This research underscores the need for better grounding of LLM simulations in authentic pre‑existing attitudes before attempting to model subsequent updates.

## Related Concepts  
- Belief updating and opinion revision  
- Persona conditioning in AI systems  
- Stakeholder simulation fidelity  
- Social media influence on attitudes  
- Demographic modeling and personality traits  
- Reddit comment persuasion and ranking
