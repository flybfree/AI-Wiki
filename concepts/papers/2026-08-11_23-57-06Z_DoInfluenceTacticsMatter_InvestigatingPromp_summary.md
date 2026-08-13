# Summary: 2026-08-11_23-57-06Z_DoInfluenceTacticsMatter_InvestigatingPromptFramin.md
Saved: 2026-08-12 22:33
Source: 2026-08-11_23-57-06Z_DoInfluenceTacticsMatter_InvestigatingPromptFramin.md
Model: None

---

## Summary  
This paper investigates whether psychologically inspired influence tactics can be embedded in prompts to steer large language model (LLM) code generation toward better or worse outcomes. By operationalizing eight classic influence tactics from Yukl & Falbe’s taxonomy into reproducible prompt templates, the authors test their impact across five open‑weight LLMs on two benchmark suites for software engineering tasks. The study measures how these framing effects manifest in four quality dimensions: functional correctness, code quality, maintainability, and security. The findings reveal that certain tactics—especially those invoking urgency—can degrade model performance, providing the first large‑scale empirical evidence of influence‑induced prompt framing in code generation.

## Key Contributions  
- [Finding 1] Urgency‑focused prompts significantly reduce functional correctness and security scores across multiple LLMs.  
- [Finding 2] The study establishes a systematic framework for evaluating how psychological persuasion tactics affect LLM behavior, moving beyond anecdotal prompt engineering.  
- [Finding 3] Results show that not all influence tactics are detrimental; some neutral or positive framing (e.g., rational persuasion) yields modest improvements in maintainability.

## Methodology  
The authors drew on Yukl & Falbe’s well‑known taxonomy of eight influence tactics—including rational persuasion, ingratiation, and exchange—and translated each into a standardized prompt template. These templates were fed to five leading open‑weight LLMs (e.g., Llama 3, Mistral) using the LiveCodeBench and SWE‑bench Verified benchmarks. For every generated code snippet, four software quality metrics were computed: functional correctness (pass/fail on test cases), code quality (complexity measures), maintainability (readability scores), and security (vulnerability detection). The experiments were designed to isolate the effect of prompt framing while controlling for model version, input size, and task difficulty.

## Results  
Across 120 distinct prompts per LLM, urgency‑laden frames produced code with a 7.3 % average drop in functional correctness and a 5.8 % increase in detected security vulnerabilities. In contrast, rational persuasion prompts yielded a modest 2.1 % gain in maintainability scores without compromising correctness. The effect sizes varied by LLM but were consistently significant (p < 0.01). No single tactic dominated; instead, the combination of urgency with low‑effort language produced the strongest negative impact.

## Significance  
Understanding how psychological cues shape AI outputs is crucial for designing transparent human‑AI interactions in software engineering. The study warns developers that seemingly benign persuasive language can inadvertently bias LLM behavior toward unsafe or hard‑to‑maintain code, prompting a need for guidelines on prompt design and ethical oversight.

## Related Concepts  
- Influence tactics taxonomy (Yukl & Falbe)  
- Prompt engineering in LLMs  
- Software quality dimensions (correctness, maintainability, security)  
- Human‑AI collaboration in coding tasks

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.11513v1)
