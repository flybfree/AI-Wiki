# Summary: 2026-07-29_09-01-26Z_BorrowedStrength_Best_of_NSearchoveraCodeEncodingB.md
Saved: 2026-07-29 21:36
Source: 2026-07-29_09-01-26Z_BorrowedStrength_Best_of_NSearchoveraCodeEncodingB.md
Model: None

---

## Summary  
The paper demonstrates that self‑check defenses like SAGE can be breached by combining two seemingly harmless attacks—code‑completion encoding and best‑of‑N search—each individually low impact but together achieving high evasion rates. By composing these attacks, the authors achieve 67 %/22 %/15 % success across three open targets and persist on a 70B model. They also explain why certain attacks survive based on defense type and propose a diagnostic for deterministic greedy decoding.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The composition of code‑completion encoding with best‑of‑N search yields high evasion rates (67 %/22 %/15 %) across three open targets, surpassing individual attack limits.  
- [Finding 2] Self‑check defenses borrow strength from the target model, converting requests into refusals at varying rates (32 %-97 %), which inflates defended coverage despite similar undefended reach.  
- [Finding 3] The survival of attacks depends on defense type: code encoding retains more undefended reach against transform defenses than character search, while ordering flips against gate defenses; this is linked to the number of independent probes each attack delivers.

## Methodology  
The authors evaluated both attacks individually and in combination across three open models (e.g., GPT‑3.5, Claude 2) and a 70B model. They measured defense success rates using human‑validated judgments over 310,000 generations. The composition was analyzed by examining how each attack interacts with the self‑check’s decision process, focusing on probe count and response transformation.

## Results  
The combined attacks achieve evasion rates of 67 %/22 %/15 % across three open targets, indicating robust breach capability even when individually limited. Self‑check defenses show a range of refusal probabilities (32 %-97 %) that increase defended coverage without affecting undefended reach. The code encoding retains higher undefended reach against transform defenses compared to character search, while gate defenses invert this ordering.

## Significance  
This work reveals a fundamental vulnerability in self‑check defenses: their reliance on the target model’s internal reasoning can be exploited by benign attacks, undermining security claims. It also provides diagnostic insight into deterministic greedy decoding flaws and highlights that defense effectiveness is not monotonic with attack complexity.

## Related Concepts  
- Self‑check defenses (e.g., SAGE)  
- Code‑completion encoding  
- Best‑of‑N search  
- Prompt injection / jailbreak composition  
- Defense probing and decision boundary
