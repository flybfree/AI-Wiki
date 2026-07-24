# Summary: 2026-07-20_19-47-16Z_StructuredOutputCollapsesAnswerDiversityAcross44La.md
Saved: 2026-07-24 00:25
Source: 2026-07-20_19-47-16Z_StructuredOutputCollapsesAnswerDiversityAcross44La.md
Model: None

---

## Summary  
The paper investigates how structured output requests—such as “Reply with JSON only”—affect answer diversity across 44 language models by re‑examining the One‑Word Census experiment. It finds that forcing a specific format sharpens model responses, increasing the modal (most frequent) answer and decreasing distinct alternatives. The collapse is driven primarily by model registers rather than decoder constraints, with certain formats amplifying or suppressing particular answers. This work shows that structured output can systematically bias language models toward less diverse outputs.

## Key Contributions  
- Finding 1: Structured output prompts cause a significant increase in the modal answer across all categories, reducing distinct answers from 52 to 36.  
- Finding 2: The effect is progressive; six out of forty‑four models shift individually toward the mode while others remain unchanged, indicating both convergence and divergence.  
- Finding 3: Response format influences model behavior beyond simple decoding constraints—e.g., JSON reduces answer surprise by 0.22 bits (p=.0002), XML by 0.19 bits (p=.002), while YAML/CSV show no effect, and an arbitrary bracket wrapper adds +0.13 bits (p=.009).

## Methodology  
The authors re‑run the One‑Word Census with 31 prompts that ask for a single word from a large set of equally valid options, now requiring JSON output without schema enforcement or constrained decoding. They compare responses across 44 language models both in plain chat and under structured output formats, measuring answer diversity via modal frequency, distinct answer count, and surprisal.

## Results  
Modal answers rose to 64 % of the pool, distinct answers fell to 36, and mean surprise dropped from 1.80 to 1.58 bits. Six models moved individually toward the mode; others were unchanged. JSON shifts 53 % of a model’s stable defaults back to crowd responses. Compression effects: JSON –0.22 bits (p=.0002), XML –0.19 bits (p=.002); YAML/CSV no effect; arbitrary bracket wrapper +0.13 bits (p=.009). Schema enforcement at the decoder adds only –0.03 bits.

## Significance  
Structured output is a practical interface that shapes model behavior, leading to more homogeneous answers and less diversity than the unstructured chat baseline. The findings highlight that response formats act as registers influencing model outputs, with measurable impact on performance metrics like surprise and diversity.

## Related Concepts  
Structured output, conditional decoding, response‑format bias, answer diversity, modal collapse, register effects, One‑Word Census, language‑model homogeneity.
