# Summary: 2026-07-28_17-27-47Z_Instruction_TunedModelsLocallyReuseHumanSyntaxMore.md
Saved: 2026-07-28 23:01
Source: 2026-07-28_17-27-47Z_Instruction_TunedModelsLocallyReuseHumanSyntaxMore.md
Model: None

---

## Summary  
The paper investigates whether instruction‑tuned large language models locally reuse human syntax more than humans do, measuring syntactic convergence via substitution‑paradigm data across sixteen open‑weight Llama and Gemma models (1B–70B). It finds that model generations align with preceding human turns more strongly than with unrelated random primes, especially for low‑frequency CFG rules. Instruction tuning amplifies this alignment relative to pretrained baselines. The study also reports higher lexical and semantic similarity in model outputs compared to human responses.

## Key Contributions  
- Finding 1: Instruction‑tuned models show greater CFG‑rule overlap with the preceding human turn than with an unrelated random prime.  
- Finding 2: The actual‑versus‑random difference is larger for lower‑frequency rules, indicating stronger convergence on rare syntactic patterns.  
- Finding 3: Instruction tuning increases natural‑output overlap with the prime turn and all eight architecture pairs exhibit greater alignment after instruction tuning compared to pretrained variants.

## Methodology  
The authors employ substitution‑paradigm data from human dialogues, replacing one speaker’s turns in pre‑existing conversations. At each matched position they compare model‑generated responses (1,901 positions per model) with the actual preceding turn and a sampled unrelated prime. CFG rule reuse is quantified by measuring overlap of context‑free grammar rules across the two contexts.

## Results  
All instruction‑tuned models exhibit higher actual‑versus‑random CFG overlap than unrelated primes; this gap widens for low‑frequency rules. Instruction tuning raises natural‑output similarity with the prime turn, and every architecture pair shows greater alignment after instruction tuning than its pretrained counterpart. However, relative to pretrained models, instruction‑tuned outputs overlap more with random primes and show a smaller actual‑versus‑random increment when target rule‑set size is held constant.

## Significance  
These findings demonstrate that large language models mimic human syntactic convergence locally, challenging the notion that such alignment requires conscious awareness. They also reveal that instruction tuning can both enhance and sometimes dilute this behavior depending on model architecture, offering insights into how training instructions shape linguistic adaptation.

## Related Concepts  
Syntactic convergence, context‑free grammar (CFG) rule reuse, substitution‑paradigm methodology, instruction‑tuning, natural‑language generation, lexical/semantic similarity, open‑weight models.
