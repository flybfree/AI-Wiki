# Summary: 2026-07-28_12-53-30Z_DecoEvo_Score_DecoupledCo_EvolutionofSolverandRubr.md
Saved: 2026-07-28 22:49
Source: 2026-07-28_12-53-30Z_DecoEvo_Score_DecoupledCo_EvolutionofSolverandRubr.md
Model: None

---

## Summary  
The paper proposes DecoEvo, a novel framework that jointly evolves two complementary skills in text‑space optimization without relying on gold‑standard rubrics. It decouples the solver skill, which is guided solely by criterion‑level feedback, from the rubric‑generator skill, which is updated through independent audits of requirement coverage and response discrimination. This separation prevents the generator from merely making existing criteria easier to satisfy while the solver continues to improve on them. The approach yields measurable gains across multiple benchmarks and LLM backbones compared with prior methods such as SkillOpt.

## Key Contributions  
- **Finding 1:** Decoupled co‑evolution of a solver skill and a rubric‑generator skill eliminates feedback loops that can cause the generator to reinforce already‑satisfied criteria.  
- **Finding 2:** The rubric‑generator is updated via audits of requirement coverage and response discrimination, which are independent of the aggregate solver score, ensuring it targets newly exposed weaknesses.  
- **Finding 3:** DecoEvo outperforms all compared methods on five open‑ended benchmarks using three LLM backbones, achieving a 2.8–5.0 % relative improvement over SkillOpt.

## Methodology  
DecoEvo operates in two parallel loops: the solver receives fine‑grained feedback for each criterion it evaluates, prompting incremental adjustments to its own behavior; simultaneously, an external rubric‑generator audits how well those criteria are covered and discriminative. The generator’s updates focus on criteria that the current solver has not yet satisfied, reducing redundancy. No gold rubrics are used during optimization; instead, coverage metrics and discrimination scores serve as independent signals.

## Results  
Across five benchmark suites (e.g., QA, summarization, reasoning) evaluated with three LLM backbones (GPT‑4, Llama‑3, Mistral), DecoEvo achieved the highest average performance. The improvement over SkillOpt ranged from 2.8 % to 5.0 % relative gain, indicating that decoupled evolution yields more robust and interpretable text‑space artifacts.

## Significance  
By separating solver and rubric evolution, DecoEvo makes optimization transparent: the generated rubrics reflect genuine skill gaps rather than superficial score inflation. This leads to higher-quality, more reliable artifacts for downstream tasks and encourages reproducible research in text‑space adaptation.

## Related Concepts  
- Text‑space optimization  
- SkillOpt (previous co‑evolution framework)  
- Rubric generation  
- Decoupled objectives  
- Coverage audits  
- Response discrimination metrics
