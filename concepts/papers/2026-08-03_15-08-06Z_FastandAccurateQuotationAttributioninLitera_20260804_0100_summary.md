# Summary: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Saved: 2026-08-04 01:00
Source: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Model: None

---

## Summary  
The paper tackles the problem of attributing quotations to their speakers in literary texts, a task that is both linguistically challenging and computationally expensive. It introduces an encoder‑based “joint scoring” framework that processes multiple quotation mentions within a single large context window, thereby reducing the per‑example computational load compared with independent models or large language model (LLM) pipelines. The authors demonstrate state‑of‑the‑art attribution accuracy on the Project Dialogism Novel Corpus while achieving dramatically faster inference times. Their work also releases an updated version of BookNLP that integrates this new system, making it readily available for downstream literary analysis.

## Key Contributions  
- **Joint Scoring Framework**: A novel encoder architecture that jointly scores all quotation attributions in one pass, preserving long‑range anaphora signals.  
- **State‑of‑the‑art Accuracy**: Achieves 94.5 % overall attribution accuracy on the PDNC dataset, surpassing previous methods.  
- **Computational Efficiency**: Processes novels 20× faster than standard models and >1000× faster than LLM‑based approaches on an A100 GPU.

## Methodology  
The authors adopt a shared encoder that reads the entire novel (or a large segment) as context, feeding it into a transformer‑like model. Instead of predicting each quotation’s speaker separately, the joint scoring module outputs a single probability distribution over possible speakers for all annotated quotations simultaneously. This approach leverages the same pretrained language knowledge present in standard encoders, allowing the system to capture long‑range dependencies that are critical for accurate attribution.

## Results  
On the Project Dialogism Novel Corpus (35,000+ manually annotated quotations from 22 novels), the joint scoring model reaches an overall attribution accuracy of 94.5 %, which is the best reported in this domain. Benchmarks show that compared with a baseline encoder‑only system, the new method reduces inference time by a factor of 20 and, when measured against LLM pipelines, improves speed by over 1000× while maintaining or improving accuracy. The release includes ModernBookNLP, a fork of BookNLP where the quotation attribution component is replaced with this joint scoring model.

## Significance  
Accurate quotation attribution is essential for literary analysis, translation, and automated summarization, yet current solutions are either too slow for large corpora or lack precision. By delivering high accuracy with orders‑of‑magnitude speedups, the paper enables scalable processing of entire novels without resorting to costly LLM inference. The released ModernBookNLP integration lowers the barrier for researchers who wish to apply this technology directly in downstream literary pipelines.

## Related Concepts  
- Anaphora resolution  
- Joint scoring (joint attention)  
- Large language model (LLM) inference cost  
- Transformer encoder architecture  
- Project Dialogism Novel Corpus (PDNC)  
- BookNLP framework
