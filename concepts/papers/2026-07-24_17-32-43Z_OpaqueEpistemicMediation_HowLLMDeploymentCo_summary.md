# Summary: 2026-07-24_17-32-43Z_OpaqueEpistemicMediation_HowLLMDeploymentConfigura.md
Saved: 2026-07-26 21:55
Source: 2026-07-24_17-32-43Z_OpaqueEpistemicMediation_HowLLMDeploymentConfigura.md
Model: None

---

## Summary  
This paper investigates how the deployment configuration of commercial large language models influences their epistemic stance toward pseudo‑scientific claims. By comparing four major LLM families—Claude, Grok, GPT, and Gemini—across multiple temporal snapshots and both API and web interfaces, the authors reveal that credibility scores are not intrinsic to a model but depend on system prompts, safety layers, routing, and silent updates. The study demonstrates that these configurations can dramatically alter whether pseudo‑science is validated or dismissed, creating an opaque epistemic mediation problem for users and researchers. The work argues that this lack of transparency constitutes a public concern demanding new forms of accountability.

## Key Contributions  
- Finding 1: Grok’s Fast versions consistently assign credibility scores of 70–75 to pseudo‑science derived from Frank Salter’s biosocial framework, whereas all other models score only 15–40.  
- Finding 2: A silent patch reversed Grok’s behaviour overnight, shifting validation from chaotic to stable high scores without any public documentation.  
- Finding 3: The same Grok model identifier produced radically divergent outputs via API (75) and web interface (5.5) three months later, and refusal to rate the claim—observed in Claude Opus 4.1 and GPT‑5.1 Chat—eroded in successor versions.

## Methodology  
The authors collected data by prompting each LLM family with a fixed pseudo‑scientific statement from Salter’s biosocial framework at four points between October 2025 and February 2026. Prompts were sent via both API endpoints and the model’s native web UI, capturing output scores or refusals. Control prompts testing established scientific consensus (evolutionary biology) and refuted Lamarckian claims were also used to isolate effects specific to pseudo‑science.

## Results  
Experimental results show that Grok Fast models rate pseudo‑science with high credibility (70–75), while Claude, GPT, and Gemini score it low (15–40). The silent patch caused an abrupt shift in Grok’s behaviour. Despite using the same model identifier, API responses varied from 75 to 5.5 on the web interface after three months. Refusal to rate the claim appeared only in Claude Opus 4.1 via the web and intermittently in GPT‑5.1 Chat via API, both of which were later reduced in newer versions.

## Significance  
These findings expose how deployment configurations—system prompts, safety layers, routing decisions, and undocumented updates—shape an LLM’s epistemic stance, making validation opaque to users and researchers. The paper underscores that credibility scores are contingent rather than inherent, raising concerns about trust, misinformation, and the need for transparent accountability mechanisms in AI systems.

## Related Concepts  
- Epistemic stance  
- Deployment configuration  
- Safety layers  
- System prompts  
- Silent updates  
- Credibility scoring  
- Pseudo‑science validation  
- API vs. web interface behavior
