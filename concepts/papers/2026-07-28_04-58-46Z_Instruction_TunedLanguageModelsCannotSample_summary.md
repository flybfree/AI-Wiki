# Summary: 2026-07-28_04-58-46Z_Instruction_TunedLanguageModelsCannotSamplefromDis.md
Saved: 2026-07-28 22:31
Source: 2026-07-28_04-58-46Z_Instruction_TunedLanguageModelsCannotSamplefromDis.md
Model: None

---

## Summary  
The paper investigates why instruction‑tuned language models cannot generate diverse responses from the distributions they are trained to model, showing that these models collapse to a single answer on repeated prompts. It introduces the KNOWS/DOES split, explaining that models can describe distributions (KNOWS) but cannot sample from them (DOES). The authors propose Prompt‑Perturbed Argyle as a mitigation technique that reduces error by 21 % compared to persona aggregation without adding cost. This work demonstrates a fundamental gap between what LLMs can articulate and what they can actually produce.

## Key Contributions  
- [Finding 1] Instruction‑tuned models collapse to a single output on more than half of items in a public‑opinion benchmark, with identical answers across repeated queries.  
- [Finding 2] The collapse is sharp: the model’s internal probabilities concentrate on one option and is amplified by instruction tuning, which degrades the sampling primitive visible in logits.  
- [Finding 3] Prompt‑Perturbed Argyle (PPA) reduces the error between generated responses and human survey data by 21 % relative to baseline persona aggregation while incurring no additional computational cost.

## Methodology  
The authors employ a public‑opinion survey dataset where each question is asked twice: once directly as a persona query (DOES) and once with an auxiliary instruction asking the model to describe the response distribution (KNOWS). They measure response similarity, compute logit concentration, and compare performance across three model families—base models versus instruction‑tuned variants. PPA is implemented by perturbing the prompt that asks for a description of the distribution.

## Results  
Over 50 % of items yielded identical answers under repeated persona queries, indicating a degenerate sampling primitive. The model’s probability mass concentrates on a single option, and the KNOWS/DOES split halves the error against human survey data when the model is asked to describe the distribution. PPA reduces this error by an additional 21 % with no added cost.

## Significance  
This research reveals that instruction‑tuned LLMs cannot be used as reliable proxies for human survey respondents, exposing a flaw in alignment training that degrades sampling capabilities. The KNOWS/DOES split and PPA offer a clear diagnostic and practical remedy, potentially reshaping how we deploy language models in response‑generation tasks.

## Related Concepts  
KNOWS/DOES split, degenerate sampling primitive, logit concentration, instruction tuning, persona aggregation, response distribution modeling, Prompt‑Perturbed Argyle.
