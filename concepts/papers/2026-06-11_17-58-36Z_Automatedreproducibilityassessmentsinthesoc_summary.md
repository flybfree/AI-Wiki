# Summary: 2026-06-11_17-58-36Z_Automatedreproducibilityassessmentsinthesocialandb.md
Saved: 2026-06-11 23:02
Source: 2026-06-11_17-58-36Z_Automatedreproducibilityassessmentsinthesocialandb.md
Model: None

---


## Summary  
This paper demonstrates that large language models (LLMs) can be used to automatically evaluate the reproducibility of empirical claims in the social and behavioral sciences, a domain where independent reanalysis is traditionally required but resource‑intensive. The authors construct an LLM pipeline that processes 76 published studies with predefined effect‑size claims and compares its outputs to both the original findings and human reanalyses. By quantifying both quantitative recovery (effect‑size tolerance) and qualitative alignment, they show that LLMs can serve as a scalable audit tool. Their contribution is a systematic empirical evaluation of LLM performance on reproducibility assessment tasks in this field.

## Key Contributions  
- LLM can automate reproducibility assessments in social and behavioral sciences, reducing reliance on manual reanalysis.  
- The pipeline recovers the original effect sizes within ±0.05 Cohen’s d for 41% of studies (out of 69 successful cases).  
- Qualitative conclusions match those of the original study in 96% of cases, outperforming human reanalysts who achieve this at 74%.

## Methodology  
The authors selected a corpus of N = 76 published empirical claims from behavioral and social‑science literature. Each claim includes an estimated effect size (e.g., Cohen’s d). The LLM pipeline was trained to generate its own estimate and a qualitative verdict on whether the reanalysis supports the original conclusion. Human reanalysts were also asked to produce estimates and conclusions for comparison, creating a three‑way benchmark.

## Results  
For seven studies the LLM could not generate a viable effect‑size estimate, likely due to ambiguous or insufficient data in those papers. In the remaining 69 studies, the LLM recovered the original effect size within the ±0.05 tolerance for 41% of cases. Crucially, the LLM’s qualitative conclusion aligned with the original study in 96% of instances. Human reanalysis recovered original effect sizes only in 34% of studies and matched the original conclusion in 74%. These numbers illustrate a clear advantage of the LLM approach.

## Significance  
Automated reproducibility assessment is essential for maintaining scientific integrity, yet it remains costly and limited by human bandwidth. By showing that LLMs can achieve comparable or superior performance on both quantitative and qualitative dimensions, this work provides a scalable foundation for systematic auditing of empirical results in the social sciences.

## Related Concepts  
- Reproducibility assessment  
- Large language models (LLMs)  
- Effect size (Cohen’s d)  
- Social and behavioral sciences  
- Qualitative conclusions  
- Automated audit tools
