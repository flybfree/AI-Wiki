# Summary: 2026-08-09_05-50-30Z_MathShikkha_AControlledStudyofAnswer_OnlyandChain_.md
Saved: 2026-08-10 23:13
Source: 2026-08-09_05-50-30Z_MathShikkha_AControlledStudyofAnswer_OnlyandChain_.md
Model: None

---

## Summary  
The paper investigates whether teacher‑generated Bangla chain‑of‑thought (CoT) supervision improves performance of small language models on mathematical reasoning tasks compared to ordinary answer‑only fine‑tuning. It constructs a dataset called MathShikkha with GPT‑5.4 rationales and conducts controlled experiments across four 4B–7B student models using matched protocols that differ only in the training target. The study finds that CoT yields no statistically significant in‑domain gain for three stronger backbones but markedly boosts the weakest model, while also affecting out‑of‑domain accuracy and reasoning adherence. Overall, rationale supervision’s value is situational, emphasizing language fidelity and auditability over raw reasoning improvement.  

## Key Contributions  
- Finding 1: CoT provides no statistically significant in‑domain performance gain for three stronger Bangla models (paired bootstrap CIs include zero; McNemar p ≥ 0.17), despite generating many more tokens.  
- Finding 2: For the weakest 4B model, CoT improves in‑domain accuracy by 18.56 points with p < 0.0001, indicating a sizeable benefit for smaller backbones.  
- Finding 3: On the contamination‑audited BanglaMATH benchmark, CoT outperforms answer‑only supervision across all four models by 20–28 points (p < 0.0001), and it preserves or improves out‑of‑domain accuracy whereas answer‑only reduces it.  

## Methodology  
The authors built MathShikkha, a Bangla mathematical reasoning dataset generated with GPT‑5.4 to produce rationales for each problem. They fine‑tuned four student models (two 4B and two 7B) under a matched protocol: same data split, response‑only loss masking, identical decoding and scoring procedures; only the training target differed between answer‑only and CoT conditions. The study compared in‑domain reasoning scores on MathShikkha and out‑of‑domain performance on the contamination‑audited BanglaMATH benchmark, using statistical tests (bootstrap CIs, McNemar test) to assess significance.  

## Results  
In‑domain results: answer‑only fine‑tuning achieved baseline scores; CoT showed no significant difference for models 7B and 4B (paired bootstrap 95% CI includes zero); however, the 4B model improved by 18.56 points (p < 0.0001). Out‑of‑domain results: answer‑only reduced accuracy below base model for three models; CoT maintained or increased accuracy across all four. Human evaluation with two annotators and Cohen’s κ of 0.76–1.00 found no significant improvement in reasoning content, but higher target‑language adherence and inspectable reasoning.  

## Significance  
This work demonstrates that chain‑of‑thought supervision is not universally beneficial for small language models; its impact depends on model capacity and downstream task distribution. The findings highlight the importance of evaluating both in‑domain performance and out‑of‑domain robustness, as well as the value of generating interpretable rationales for low‑resource languages like Bangla.  

## Related Concepts  
- Chain-of-Thought (CoT) prompting / supervision  
- Small language model fine‑tuning  
- In‑domain vs. out‑of‑domain evaluation  
- Bootstrapped confidence intervals and McNemar tests  
- Target‑language adherence in multilingual tasks
