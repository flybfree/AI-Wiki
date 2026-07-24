# Summary: 2026-07-20_09-29-53Z_LargeLanguageModelsforCitationFunctionClassificati.md
Saved: 2026-07-24 00:17
Source: 2026-07-20_09-29-53Z_LargeLanguageModelsforCitationFunctionClassificati.md
Model: None

---

## Summary  
This paper aims to evaluate the performance of several state‑of‑the‑art large language models (LLMs) on citation function classification, a task that interprets how authors reference prior work. By conducting a systematic comparison across zero‑shot, few‑shot, and fine‑tuning settings, the authors achieve new SOTA results and introduce a novel annotation scheme that distinguishes neutral acknowledgments from evaluative citations. The study fills an identified gap in recent surveys by providing a comprehensive benchmark for citation function classification using LLMs.

## Key Contributions  
- [Finding 1] Fine‑tuned Falcon 7B reaches a 73.3% macro F1 score on the ACL‑ARC dataset, surpassing previous methods and establishing a new SOTA baseline.  
- [Finding 2] The authors introduce AC3, a seven‑category annotation set that differentiates neutral acknowledgments from opinionated citations (criticizing, complimenting, contradicting) across four context‑extraction variants.  
- [Finding 3] A comprehensive comparison of five LLMs—Mistral 7B, Orca 2‑7B, LLaMA 3.1‑8B, Falcon 7B, and SciBERT—across all evaluation strategies is presented, revealing systematic performance differences.

## Methodology  
The researchers approached the problem by leveraging existing large language models to classify citation functions in scholarly texts. They employed the ACL‑ARC dataset for baseline testing and built AC3, a custom annotation set that includes seven categories of citation styles. The study systematically varied model size, prompting style (zero‑shot, few‑shot), and fine‑tuning procedures while also varying context extraction lengths to assess how scope influences classification accuracy.

## Results  
Across all configurations, the fine‑tuned Falcon 7B consistently achieved the highest macro F1 score (73.3%) on ACL‑ARC, outperforming zero‑shot and few‑shot baselines by double digits. The AC3 dataset demonstrated that models trained to recognize evaluative stances improve markedly when given longer contexts, with gains of up to 4% in F1 compared to short‑context evaluations. Other models showed modest improvements under fine‑tuning, but none matched Falcon 7B’s performance.

## Significance  
This work matters because citation function classification is a foundational task for bibliometric analysis, yet prior research has largely treated it as an isolated problem without benchmarking LLMs. By providing the first exhaustive model comparison and a richly annotated dataset (AC3), the study offers a clear benchmark that guides future research on LLM‑based semantic understanding in scholarly communication.

## Related Concepts  
- Citation function classification  
- Large language models (LLMs)  
- Zero‑shot, few‑shot, fine‑tuning evaluation strategies  
- ACL‑ARC dataset  
- Macro F1 score  
- AC3 annotation scheme and context extraction variants
