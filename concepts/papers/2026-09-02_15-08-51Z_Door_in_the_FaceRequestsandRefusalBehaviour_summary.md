# Summary: 2026-09-02_15-08-51Z_Door_in_the_FaceRequestsandRefusalBehaviourinLarge.md
Saved: 2026-09-02 23:36
Source: 2026-09-02_15-08-51Z_Door_in_the_FaceRequestsandRefusalBehaviourinLarge.md
Model: None
Canonical original paper: [http://arxiv.org/abs/2609.02707v1](http://arxiv.org/abs/2609.02707v1)

---

## Summary  
The paper investigates whether the door‑in‑the‑face (DITF) persuasion technique—where a large request is first refused and then followed by a smaller, related request—works on language models. It compares model compliance when asked directly versus after a refusal, finding that the effect varies dramatically across different model families and only applies to requests that are thematically related. The study also shows that unrelated refusals have little impact, suggesting the concession itself is essential but not sufficient for success.

## Key Contributions  
- [Finding 1] The door‑in‑the‑face technique works for certain frontier models (e.g., Anthropic Opus 5) but backfires for OpenAI, Google, and Haiku 4.5, reducing compliance by roughly 15–23 points.  
- [Finding 2] A control experiment demonstrates that refusing a large request on an unrelated topic has less effect than a related one across all nine models, indicating the concession matters everywhere but the specific follow‑up request is crucial.  
- [Finding 3] The technique does not transfer to refusals drawn from public benchmarks; rewriting refused instructions into explanation requests removes refusal in 263 of 265 cases.

## Methodology  
The authors selected nine production LLMs (Anthropic frontier models, OpenAI, Google, Haiku 4.5) and performed a controlled experiment: each model first refuses a large request, then receives a smaller version of the same request. Compliance is measured by whether the model provides an answer to the small request after the refusal versus when asked directly. A control condition compares unrelated topic refusals to evaluate the role of relatedness.

## Results  
Anthropic Opus 5 shows 65.8 % compliance after DITF compared with only 29.3 % when asked directly, a gain of about 36 points. In contrast, OpenAI and Google models exhibit a drop to 15.5–23.0 % compliance after the technique, indicating backfiring. Haiku 4.5 follows the same pattern as the non‑frontier models. The control confirms that unrelated refusals reduce compliance by less than 1 point on all models, while related refusals produce measurable effects.

## Significance  
These findings reveal that persuasion techniques are not universally applicable to large language models; their success hinges on model architecture and family, as well as the thematic relationship between requests. The study underscores the need for domain‑specific design when leveraging human influence strategies in AI interactions.

## Related Concepts  
door‑in‑the‑face technique, large language models, refusal behavior, compliance rates, model families, relatedness of requests, public benchmarks.
