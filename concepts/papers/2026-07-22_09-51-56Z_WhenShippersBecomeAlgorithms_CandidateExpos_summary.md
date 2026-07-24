# Summary: 2026-07-22_09-51-56Z_WhenShippersBecomeAlgorithms_CandidateExposure_Inf.md
Saved: 2026-07-24 01:39
Source: 2026-07-22_09-51-56Z_WhenShippersBecomeAlgorithms_CandidateExposure_Inf.md
Model: None

---

## Summary  
The paper investigates how delegating carrier selection to large language models (LLMs) reshapes freight matching markets, focusing on candidate exposure and the design choices that platform operators make. It uses agent‑based simulations with thirty‑day procurement cycles involving fifty shipper agents interacting with three commercial LLMs—OpenAI’s GPT, Anthropic’s Claude, and Google’s Gemini. The authors identify a concentration risk where a single carrier can dominate market demand despite random candidate lists. Their contribution is a remedy: disclosing each carrier’s remaining daily capacity reduces this concentration and doubles the surplus of shipper options.

## Key Contributions  
- [Finding 1] Agents converge rapidly on the same modal first‑choice carrier, which becomes the dominant option for up to 76 % of requests across all models.  
- [Finding 2] Carrier concentration spikes sharply once candidate lists exceed about ten entries, and the onset varies by model.  
- [Finding 3] Disclosing each carrier’s remaining daily capacity cuts concentration by roughly a third while doubling shipper surplus; vendor diversification, list‑order randomization, and popularity display show no detectable effect.

## Methodology  
The authors constructed an agent‑based simulation of a digital freight matching market with thirty days of activity. Fifty shipper agents, built on GPT, Claude, or Gemini, each maintain a ranked list of candidate carriers drawn uniformly at random from the platform’s pool. The market operates under waterfall tendering rules: shipper requests are processed in order, carriers have daily capacity caps, spot prices react to congestion, and transaction‑based ratings accumulate. The simulation varies two key dimensions—list length (up to 10 or beyond) and information design (e.g., full capacity disclosure versus only estimated quality). This experimental setup isolates the impact of candidate exposure and platform‑controlled information.

## Results  
For a fixed carrier population, the same carrier emerges as the first‑choice modal on day one for every LLM agent, capturing up to 76 % of requests. When lists are limited to ten carriers or fewer, concentration remains moderate; however, beyond this threshold, concentration rises steeply and differs across models. The only design change that measurably mitigates concentration is the disclosure of each carrier’s remaining daily capacity: it reduces concentration by about one‑third and doubles the surplus of shipper options. Vendor diversification, randomizing list order, or showing popularity metrics had no clear effect on outcomes.

## Significance  
The findings reveal that platform information design—specifically how much capacity data is exposed to shippers—is a powerful lever for mitigating market concentration, independent of which LLM powers the agents or whether regulatory restrictions are applied. This insight matters because it suggests that even as LLMs automate freight matching, operators can shape market outcomes through transparent operational policies rather than relying on model governance alone.

## Related Concepts  
- Candidate exposure  
- Waterfall tendering  
- Digital freight matching  
- Large language models (LLMs)  
- Market concentration  
- Capacity disclosure  
- Vendor diversification  
- List‑order randomization  
- Popularity display
