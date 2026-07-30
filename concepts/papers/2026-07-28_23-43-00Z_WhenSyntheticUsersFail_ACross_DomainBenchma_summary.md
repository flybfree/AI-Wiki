# Summary: 2026-07-28_23-43-00Z_WhenSyntheticUsersFail_ACross_DomainBenchmarkofLLM.md
Saved: 2026-07-29 21:33
Source: 2026-07-28_23-43-00Z_WhenSyntheticUsersFail_ACross_DomainBenchmarkofLLM.md
Model: None

---

## Summary  
This paper investigates the limits of using large language models (LLMs) as synthetic users in market‑ and policy‑driven surveys, asking when such substitutes are reliable and when they fail. By applying a single cross‑domain protocol to four LLMs across two demographic families and an 8B‑to‑frontier capability range, the authors benchmark them against non‑LLM baselines on real human data from the General Social Survey and World Values Survey. The study reveals two persistent failures: (i) no LLM can outperform baseline models at the individual level, especially on cross‑cultural values; and (ii) LLMs systematically over‑determine demographic identities, inflating between‑segment gaps. These findings suggest that synthetic‑user evidence is often unsafe for decision support.

## Key Contributions  
- [Finding 1: No LLM beats even the strongest baseline on individual‑level predictions]  
- [Finding 2: All LLMs fall well below human performance on cross‑cultural value items, with gaps persisting under distance‑aware and proper‑scoring metrics]  
- [Finding 3: LLMs systematically over‑determine demographics, treating identity as far more predictive than it is in real respondents, a distortion that appears across question groups]

## Methodology  
The authors designed a unified evaluation framework that (1) prompts each LLM with demographic cues and survey‑simulation protocols identical to those used for human respondents; (2) runs the same protocol on two independent datasets—U.S. general social attitudes (General Social Survey) and cross‑cultural values (World Values Survey); (3) compares every model against a suite of non‑LLM baselines trained on held‑out human data; (4) measures performance using standard metrics such as accuracy, proper scoring, and distance‑aware evaluation; (5) conducts a decision‑impact analysis to quantify how inflated segment gaps affect real‑world targeting decisions.

## Results  
At the individual level, every LLM’s accuracy is lower than that of the best baseline across all questions. On cross‑cultural value items, even the most capable models are several percentage points below human performance, and the gap remains when proper scoring accounts for distance between respondents’ values. The demographic over‑determination issue manifests in nearly every question group: LLMs assign higher confidence scores to identity categories than real people do, leading to inflated between‑segment gaps of 2–4×. In a segment‑targeting simulation, this causes the model to misdirect teams toward incorrect segments in half of U.S. cases and most cross‑cultural cases, creating artificial splits that do not exist.

## Significance  
These results expose critical risks when synthetic users replace human respondents: they can produce systematically biased or inaccurate insights that drive flawed market strategies or policy decisions. By making the benchmark and evaluation framework publicly available on request, the paper equips practitioners with a tool to pre‑emptively assess whether their synthetic‑user pipelines are safe for high‑stakes applications.

## Related Concepts  
- Large Language Models (LLMs) as synthetic users  
- Survey simulation protocols  
- Proper scoring and distance‑aware evaluation  
- Demographic over‑determination bias  
- Segment targeting in market research
