# Summary: 2026-08-09_19-51-56Z_TowardsanLLM_basedmethodforquantifyingthesexualcon.md
Saved: 2026-08-10 23:28
Source: 2026-08-09_19-51-56Z_TowardsanLLM_basedmethodforquantifyingthesexualcon.md
Model: None

---

## Summary  
This paper proposes an LLM‑based framework that can automatically quantify thematic content in song lyrics, with a particular focus on sexual explicitness while also capturing broader lyrical dimensions. The authors apply the method to a large reggaeton corpus of 1,259 songs from twelve artists spanning 2002–2025 and compare their scores with Spotify’s own explicit‑flag system.

## Key Contributions  
- [Finding 1] Introduces a reproducible LLM scoring framework that extracts four independent thematic dimensions (eroticism, objectification, profanity, romanticization) from lyrics.  
- [Finding 2] Shows per‑artist variation in lyrical content over time, revealing that some reggaeton artists consistently score higher on sexual‑explicitness measures than others.  
- [Finding 3] Demonstrates a moderate correlation (r ≈ 0.68) between the LLM’s sexual‑explicitness scores and Spotify’s explicit flag, indicating useful alignment while also exposing systematic differences.

## Methodology  
The authors built a prompt that instructs a large language model to generate four numeric scores for each lyric excerpt. The prompt is applied uniformly across all songs in the corpus; no fine‑tuning was required. A subset of 200 songs was manually annotated by human coders to serve as validation and error analysis. Data collection involved downloading official lyrics, cleaning them, and associating each track with its release year.

## Results  
The dataset characterization reveals that average eroticism scores are highest for artists released after 2015, suggesting a generational shift toward more explicit language. Per‑artist comparison shows that three artists consistently exceed the mean on objectification and profanity dimensions. Temporal analysis confirms a clear upward trend in sexual‑explicitness scores from 2002 to 2025. The correlation with Spotify’s flag is positive but not perfect, highlighting both agreement and residual differences.

## Significance  
Providing an objective, LLM‑driven metric for sexual content helps researchers compare lyrical styles across genres and time periods, informs content moderation policies, and offers a baseline for evaluating automated detection systems. The reproducibility of the method encourages broader adoption in music analysis.

## Related Concepts  
- Large Language Models (LLMs)  
- Thematic extraction from text  
- Content scoring and quantification  
- Sexual explicitness measurement  
- Spotify’s automatic explicit‑flag system
