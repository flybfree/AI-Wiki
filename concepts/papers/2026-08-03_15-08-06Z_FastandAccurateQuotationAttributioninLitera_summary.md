# Summary: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Saved: 2026-08-04 00:04
Source: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Model: None

---

## Summary  
The paper addresses the challenge of attributing quotations to their speakers in literary texts, proposing a joint scoring method that processes multiple attributions within a shared context window. It achieves state‑of‑the‑art accuracy while being orders of magnitude faster than LLM‑based approaches. The proposed formulation leverages shared representations across all quotation mentions within a single large context window, reducing the need for multiple passes over the text and cutting computational load dramatically. This work introduces ModernBookNLP, a toolkit integrating the new model.

## Key Contributions  
- Joint scoring formulation enables simultaneous attribution of all quotations in a novel using a single large context window.  
- State‑of‑the‑art overall attribution accuracy of 94.5 % on PDNC while processing novels 20× faster than standard methods and >1000× faster than LLM approaches.  
- Release of ModernBookNLP, a modified BookNLP fork that replaces its attribution model with the new joint scoring system.

## Methodology  
The authors adopt an encoder‑based architecture that treats all quotation mentions as part of one continuous input stream. By sharing a large context window across the entire novel, they allow the model to capture long‑range dependencies crucial for anaphora resolution. This approach reduces the need for multiple passes over the text, thus cutting computational load dramatically. The joint scoring function predicts speaker labels jointly with each quotation, optimizing for both accuracy and efficiency.

## Results  
On the Project Dialogism Novel Corpus (PDNC) containing 35,000 annotated quotations from 22 novels, the best model reaches 94.5 % overall attribution accuracy. Benchmarks show processing speed: 20× faster than conventional independent‑prediction methods and >1000× faster than LLM‑based solutions on an A100 GPU.

## Significance  
This work bridges the gap between computational efficiency and high‑quality linguistic analysis, making large‑scale literary attribution feasible. By preserving long‑range signal in pretrained encoders, it improves performance on challenging examples where prior methods fail.

## Related Concepts  
- Anaphora resolution: linking mentions to their antecedents.  
- Large language models (LLMs): neural networks trained on massive text corpora for generation and classification.  
- Joint scoring: a multi‑task formulation that optimizes shared representations across all quotation attributions.  
- Context window: the length of input sequence processed simultaneously by an encoder.
