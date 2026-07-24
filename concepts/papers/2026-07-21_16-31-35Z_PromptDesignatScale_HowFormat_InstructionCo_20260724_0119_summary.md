# Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md
Saved: 2026-07-24 01:19
Source: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md
Model: None

---

## Summary  
The paper investigates how three prompt‑design choices—instruction formatting, the number of simultaneous instructions in a system prompt, and context length—affect both instruction adherence and hallucination in large language models (LLMs). By systematically varying these factors on a single, reproducible synthetic dataset, the authors uncover strong interactions that were previously undocumented. The study demonstrates that even modest increases in rule count or context size can cause perfect‑response rates to drop to zero across all models, while also reshaping model preferences for plain text versus markdown. These findings provide empirical evidence that prompt engineering is not a one‑size‑fits‑all practice and highlight the need for careful design at scale.

## Key Contributions  
- [Finding 1] Instruction‑following accuracy collapses to zero by N=80 rules regardless of format or placement, indicating a hard ceiling on rule count.  
- [Finding 2] Recall accuracy degrades sharply after ~64–128k tokens and varies dramatically across formats, with some models showing up to 48‑point spread at the context ceiling.  
- [Finding 3] Refusal rates rise sharply near each model’s context limit (0 % to 90 %) and are unrelated to sycophancy or fabrication, which remain negligible.

## Methodology  
The authors constructed “Book of Veyra,” an 8,780‑entity corpus deterministically generated from a fixed seed. They executed two controlled experiments: Experiment 1 varied the number N of simultaneous instructions (10–160) across four formats (markdown, plain text, prose, tabular) and instruction placement (system vs. user turn). Experiment 2 extended context length from 2k to 512k tokens while keeping other factors constant. All experiments were run on five distinct LLMs, generating a total of 5,760–9,600 model calls per experiment.

## Results  
- Perfect‑response rate drops to zero by N=80 for every configuration; placement effects match or exceed format effects at high N in most models.  
- Recall remains stable up to ~128k tokens but then declines sharply and is highly format‑dependent, with one 35B model reaching a 48‑point spread at 128k tokens.  
- Hallucination never occurs (0/5,760 probes); sycophancy stays ≤ 8.3%. Refusal rates increase to 79–90% near each model’s context ceiling.

## Significance  
These results reveal that prompt design decisions have measurable, non‑linear impacts on LLM behavior, especially as instruction complexity and context size grow. Practitioners must consider these interactions when scaling prompts for real‑world applications, avoiding hidden performance cliffs that can degrade reliability.

## Related Concepts  
- Instruction following decay  
- Hallucination vs. sycophancy  
- Context length limits  
- Prompt formatting (markdown, plain text)  
- System prompt placement
