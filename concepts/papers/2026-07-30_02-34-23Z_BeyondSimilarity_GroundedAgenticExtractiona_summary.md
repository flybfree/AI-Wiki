# Summary: 2026-07-30_02-34-23Z_BeyondSimilarity_GroundedAgenticExtractionandExper.md
Saved: 2026-07-30 20:25
Source: 2026-07-30_02-34-23Z_BeyondSimilarity_GroundedAgenticExtractionandExper.md
Model: None

---

## Summary  
The paper proposes a new framework for extracting intertextual references in Classical Chinese histories that goes beyond simple similarity detection by grounding each reuse in exact character spans and classifying it within a five‑dimensional typology (form, aspect, source‑marking, function, stance). It validates this agentic extraction on an expert‑adjudicated benchmark of 2,533 pairs drawn from the Analects and the Book of Han, then scales the method to the full Twenty‑Four Histories. The study demonstrates that large language models can produce high‑precision extracts while remaining cost‑effective, yet their confidence is unevenly calibrated across dimensions. Crucially, it shows that citation patterns remain stable over centuries despite a gradual shift from literal quoting to more interpretive reuse.

## Key Contributions  
- Finding 1: The proposed agentic extraction pipeline couples full‑text reading with a constrained tool interface to produce precise character‑span annotations and five‑dimensional labels for intertextual reuse.  
- Finding 2: Expert adjudication of a multi‑model candidate set yields a benchmark of 2,533 pairs, establishing ground truth for precision (≈56 %–93 %) and cost‑quality trade‑offs across twelve LLMs.  
- Finding 3: Scaling the validated extractor to all 65,380 comparisons reveals corpus‑level intertextual structures that raw similarity scores cannot capture.

## Methodology  
The authors treat fine‑grained intertextuality extraction as an LLM‑driven agentic task. Input consists of two text units; the model must invoke a tool to locate exact character spans on both sides and assign one of five reuse typologies. The process is constrained by a predefined schema, preventing hallucinated or vague annotations. A curated set of 2,533 pairs from the Analects‑Book of Han comparison is manually adjudicated by three domain experts, whose judgments form the benchmark. The same pipeline is then applied to all pairwise comparisons in the Twenty‑Four Histories (65,380 total), producing a corpus‑wide extraction log.

## Results  
Precision scores across twelve LLMs range from 56 % to 93 %, with a cost spread of roughly 51× at comparable quality. Confidence calibration is uneven: dimensions that rely on surface‑level cues are consistently high, while those requiring inference of authorial intent show lower agreement and higher uncertainty. When aggregated across the full Twenty‑Four Histories, the extraction recovers a stable citation structure spanning eighteen centuries, despite individual passages showing reduced literal quoting.

## Significance  
This work bridges the gap between similarity metrics and meaningful intertextual analysis by providing a reproducible, human‑validated method for extracting precise textual references. It offers a scalable tool for scholars of Classical Chinese literature to map citation networks across time, informing cultural‑attraction models that expect aggregate stability with individual drift.

## Related Concepts  
intertextuality, LLM agentic extraction, character‑span annotation, five‑dimensional reuse typology, expert adjudication, corpus‑level structure, similarity vs. interpretive analysis
