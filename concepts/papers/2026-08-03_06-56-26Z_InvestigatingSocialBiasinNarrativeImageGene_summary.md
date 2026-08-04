# Summary: 2026-08-03_06-56-26Z_InvestigatingSocialBiasinNarrativeImageGeneration.md
Saved: 2026-08-04 00:27
Source: 2026-08-03_06-56-26Z_InvestigatingSocialBiasinNarrativeImageGeneration.md
Model: None

---

## Summary  
This paper investigates how social biases manifest in text‑to‑image (T2I) generation across different visual narrative formats—photo, storyboard, and comic panels—to reveal whether the hidden prejudices that appear only in static images become more explicit when characters and events are sequenced. By adapting an existing bias evaluation framework to image generation, the authors demonstrate that proprietary models produce a higher proportion of biased outputs in narrative media than in conventional photo generation.

## Key Contributions  
- [Finding 1] Proprietary T2I models generate on average 25.9 % biased outputs in photo generation, but this rises to 35.5 pp in storyboard and 43.7 pp in comic generation, indicating a systematic increase with narrative complexity.  
- [Finding 2] Bias expression differs across formats: photos rely on subtle visual cues, while storyboards and comics expose bias through event sequencing, character positioning, narrative resolution, and accompanying text.  
- [Finding 3] The study underscores that evaluating T2I systems must consider diverse visual formats beyond photographs to capture the full spectrum of social bias.

## Methodology  
The authors repurpose BBG (Bias Benchmark for Generative Models), a text‑based evaluation tool, by converting its prompts into image generation tasks. Six widely used proprietary models are evaluated on three narrative visualizations: single‑panel photos, multi‑panel storyboards, and sequential comic strips. Each model is tested with the same set of bias‑inducing prompts across all formats to ensure comparable conditions.

## Results  
Across the six models, photo generation averaged 25.9 % biased outputs (measured by demographic disparity in facial features). Storyboard generation showed a 9.6 percentage‑point increase, reaching 35.5 pp bias, while comic generation exhibited an even larger rise of 18.2 pp to 43.7 pp. Qualitative analysis revealed that biases in storyboards and comics are more overt: characters from under‑represented groups appear disproportionately in negative roles, event order favors dominant narratives, and textual captions reinforce stereotypes.

## Significance  
These findings reveal that social bias is not confined to static images; it becomes more pronounced when narrative structure is introduced. Ignoring narrative formats could lead to the deployment of biased media that subtly or overtly marginalize certain groups. The work calls for comprehensive evaluation protocols that include diverse visual storytelling techniques.

## Related Concepts  
- Text‑to‑image (T2I) generation  
- Social bias in AI outputs  
- Visual cues and implicit representation  
- Event sequencing in narratives  
- Character positioning as a bias indicator  
- Narrative resolution influencing perception  
- BBG framework adaptation for image generation
