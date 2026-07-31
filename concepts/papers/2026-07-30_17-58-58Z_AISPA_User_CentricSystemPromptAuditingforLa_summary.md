# Summary: 2026-07-30_17-58-58Z_AISPA_User_CentricSystemPromptAuditingforLargeLang.md
Saved: 2026-07-30 22:24
Source: 2026-07-30_17-58-58Z_AISPA_User_CentricSystemPromptAuditingforLargeLang.md
Model: None

---

## Summary  
AISPA (Artificial Intelligence System Prompt Assurance) is a user‑centric framework that systematically audits system prompts used to steer foundation models. By evaluating each prompt against eight human‑relevant dimensions, the authors classify instructions as either protective of users or problematic and reveal how commercial AI products handle these prompts. The study demonstrates that while many firms embed protective guidance, the audit uncovers deep inconsistencies in coverage, length, and the coexistence of harmful instructions.

## Key Contributions  
- [Finding 1] System prompt design varies substantially across products and developers, with some organizations averaging over 60 protective instructions per product while others average fewer than 5.  
- [Finding 2] Protective instructions are widely adopted but shallow in scope: 98.9% of products contain at least one, yet only 24% cover all eight dimensions of the AISPA taxonomy.  
- [Finding 3] System prompts have grown steadily longer and more protective of users, suggesting user protection is becoming a visible concern, yet problematic instructions remain pervasive—roughly 40% of products contain at least one instruction that works against user interests—and they frequently coexist within the same prompt.  

## Methodology  
The authors applied AISPA to a large‑scale audit of commercial AI systems. They collected system prompts from 88 different products, totaling 3,249 instructions. For each prompt, AISPA extracts and scores the eight user‑focused dimensions (e.g., safety, fairness, privacy) to determine whether the instruction is protective or problematic. The classification yields a binary label per instruction, enabling statistical analysis across products.

## Results  
The audit produced four core findings: (1) heterogeneous prompt design; (2) high adoption but low comprehensive coverage of all dimensions; (3) increasing length and protective intent in prompts; (4) persistent presence of harmful instructions. Quantitative results show that 98.9% of products include at least one protective instruction, only 24% satisfy the full eight‑dimension checklist, and about 40% contain a problematic instruction. The analysis also notes that protective and problematic instructions often appear together in a single prompt.

## Significance  
These findings expose a critical trust gap: developers hide system prompts from users and regulators, while user protection efforts remain uneven. AISPA’s systematic approach provides a benchmark for auditing AI systems, encouraging transparency, standardization, and independent oversight to align commercial AI with ethical expectations.

## Related Concepts  
system prompts, foundation models, user‑centric auditing, trust and accountability gap, prompt design, AI safety, large language model applications.
