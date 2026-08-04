# Summary: 2026-08-03_06-56-26Z_InvestigatingSocialBiasinNarrativeImageGeneration.md
Saved: 2026-08-04 00:34
Source: 2026-08-03_06-56-26Z_InvestigatingSocialBiasinNarrativeImageGeneration.md
Model: None

---

## Summary  
The paper investigates whether social biases present in text‑to‑image models persist across different visual formats beyond photos, specifically storyboards and comics. It adapts the BBG evaluation framework to assess bias expression in these narrative visual formats. Findings reveal that bias levels increase with narrative complexity, showing higher bias in storyboards and comics compared to photos. This study bridges the gap between static image bias assessments and dynamic narrative media.

## Key Contributions  
- Finding 1: Proprietary T2I models generate on average 25.9 % biased outputs in photo generation.  
- Finding 2: Bias expression rises by 9.6 percentage points in storyboard generation and 18.2 pp in comic generation.  
- Finding 3: Narrative formats expose biases through event sequencing, character positioning, narrative resolution, and textual elements, making them more explicit than subtle visual cues.

## Methodology  
The authors adapted BBG (Bias Benchmark Generator) to image generation by feeding the same prompts into six T2I models across three visual formats—photo, storyboard, comic. They measured bias using a standardized set of demographic queries and evaluated outputs for stereotypical representation. The comparison was conducted with quantitative metrics derived from human annotators rating bias severity; the adapted BBG framework includes prompts that target gender, race, ability, and socioeconomic status to probe representation across panels.

## Results  
Results show average bias rates: 25.9 % in photos, 35.5 % (25.9 + 9.6) in storyboards, and 44.1 % (25.9 + 18.2) in comics. Human annotators rated each output on a 5‑point severity scale, yielding mean bias scores of 2.8 (photos), 3.4 (storyboards), 4.1 (comics). Statistical analysis indicates a significant increase with format complexity.

## Significance  
These findings demonstrate that social biases are not confined to static images but become more pronounced when narratives unfold across panels, affecting real‑world applications like media production and education where visual storytelling is central. The work calls for inclusive evaluation protocols that consider multiple visual formats.

## Related Concepts  
Text-to-image generation, bias in AI models, narrative visual formatting, event sequencing, character positioning, textual elements, BBG framework adaptation, stereotype representation.
