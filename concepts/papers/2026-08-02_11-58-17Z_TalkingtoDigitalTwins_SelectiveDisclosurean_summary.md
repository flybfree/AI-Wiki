# Summary: 2026-08-02_11-58-17Z_TalkingtoDigitalTwins_SelectiveDisclosureandBelief.md
Saved: 2026-08-04 00:07
Source: 2026-08-02_11-58-17Z_TalkingtoDigitalTwins_SelectiveDisclosureandBelief.md
Model: None

---

## Summary  
The paper tackles the challenge of measuring what financial media personas deliberately omit from their public posts—selective disclosure—and demonstrates that this hidden information can be turned into a reliable market‑view panel. By constructing “digital twins” from monitored X (Twitter) accounts and conducting repeated, real‑time interviews under a fixed protocol, the authors recover belief proxies for individual stocks even when no explicit recommendation is posted. The design archives interview data before any market return occurs, thereby eliminating look‑ahead bias that plagues many LLM‑based sentiment analyses. Their findings show that these proxy beliefs predict large‑cap stock returns in the expected direction, suggesting a novel way to quantify selective disclosure in real time.

## Key Contributions  
- [Finding 1] The authors develop a repeatable, real‑time interview framework that generates market‑view panels from digital twins without look‑ahead bias.  
- [Finding 2] Selective disclosure by finfluencers can be measured as a panel of belief proxies that are observable before the relevant return window.  
- [Finding 3] The belief proxies derived from these interviews predict the cross‑section of large‑cap stock returns in the expected direction, confirming their utility for market impact analysis.

## Methodology  
The researchers monitored X accounts belonging to financial media personas and built “digital twins” that mirror each persona’s public behavior. They then performed repeated interviews using a fixed protocol, asking the digital twin to articulate its current view on specific stocks. All interview transcripts were archived immediately after generation, ensuring that the data were available only up to the moment of market observation. This approach avoids the classic look‑ahead bias where an LLM would be queried after the fact.

## Results  
The belief proxies extracted from the interviews correlated with the direction of large‑cap stock returns over subsequent trading periods. Statistical tests indicated a statistically significant positive relationship, meaning that when the digital twin’s disclosed view aligned with market moves, it tended to occur in the expected direction. This empirical evidence demonstrates that selective disclosure is not merely anecdotal but can be quantified and used as a predictive signal.

## Significance  
By turning voluntary omissions into measurable panels of belief, this work bridges the gap between social media activity and market dynamics. It provides researchers and practitioners with a tool to quantify how much hidden information influences price movements, potentially improving risk models and trading strategies that rely on sentiment analysis.

## Related Concepts  
- Digital twin: a virtual replica that captures real‑time behavior of an individual or entity.  
- Selective disclosure: the practice of sharing only part of relevant information publicly.  
- Belief measurement: quantifying the strength and direction of an investor’s view on a security.  
- Look‑ahead bias: a statistical artifact where future data are used to inform present analysis.  
- Finfluencer: a social media user who influences financial decisions through public posts.
