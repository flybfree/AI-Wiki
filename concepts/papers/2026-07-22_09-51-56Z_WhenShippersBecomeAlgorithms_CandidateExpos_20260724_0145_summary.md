# Summary: 2026-07-22_09-51-56Z_WhenShippersBecomeAlgorithms_CandidateExposure_Inf.md
Saved: 2026-07-24 01:45
Source: 2026-07-22_09-51-56Z_WhenShippersBecomeAlgorithms_CandidateExposure_Inf.md
Model: None

---

## Summary  
This paper investigates how the delegation of carrier selection to large‑language‑model (LLM) agents reshapes freight matching markets and which platform design choices drive that transformation. By running agent‑based simulations with three commercial LLMs, the authors reveal that rapid convergence toward a single dominant carrier, sharp concentration of demand once candidate lists grow beyond ten entries, and a simple information disclosure—showing each carrier’s remaining daily capacity—can alleviate these problems. The study argues that platform‑level information design is the primary lever for mitigating market inefficiencies, independent of which LLM is chosen or how it is regulated.

## Key Contributions  
- [Finding 1] Agents quickly converge on a single modal first choice, capturing up to 76 % of requests within the first day.  
- [Finding 2] Carrier concentration spikes sharply when each shipper’s candidate list exceeds roughly ten carriers; the onset and intensity vary across model families.  
- [Finding 3] Disclosing remaining daily capacity reduces concentration by one‑third and doubles shipper surplus, whereas vendor diversification, randomizing list order, or popularity display have no detectable effect.

## Methodology  
The authors constructed an agent‑based simulation of a digital freight matching market for thirty days. Fifty shipper agents were instantiated using three commercial LLMs (OpenAI GPT, Anthropic Claude, Google Gemini). Each agent maintains its own randomly drawn list of up to ten candidate carriers and selects the first carrier that has remaining capacity on a given day. The platform enforces waterfall tendering, daily capacity caps for carriers, spot‑price dynamics reflecting congestion, and an accumulation of ratings based on completed transactions. This setup reproduces typical features of freight marketplaces while allowing systematic variation in information design.

## Results  
Across all simulated markets the same carrier became the modal first choice for every LLM within a single day, indicating rapid convergence (Finding 1). As the number of displayed candidates grew beyond ten, concentration intensified: one model produced a dominant carrier with 76 % demand, another with 58 %, and a third with 42 %. The effect was not driven by true quality differences—displayed ratings never affected delivery outcomes—but rather by the sheer size of the candidate pool. When the platform added a simple disclosure of each carrier’s remaining daily capacity, concentration fell by roughly one‑third and shipper surplus doubled (Finding 3). Vendor diversification, randomizing list order, or highlighting popular carriers showed no statistically significant impact.

## Significance  
These findings demonstrate that the architecture of information presented to shippers—rather than the underlying LLM technology or regulatory oversight—determines market concentration. By exposing precise capacity data, platforms can restore a more balanced distribution of load‑allocation risk and improve overall efficiency. The study underscores that future policy on AI in freight markets should prioritize transparent, actionable information design over banning or restricting model choice.

## Related Concepts  
- LLM‑mediated marketplaces  
- Information design / data disclosure  
- Vendor diversification  
- Waterfall tendering  
- Capacity limits and congestion pricing  
- Rating accumulation in digital platforms
