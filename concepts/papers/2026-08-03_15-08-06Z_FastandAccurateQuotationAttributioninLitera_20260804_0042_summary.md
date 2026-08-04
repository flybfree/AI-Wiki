# Summary: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Saved: 2026-08-04 00:42
Source: 2026-08-03_15-08-06Z_FastandAccurateQuotationAttributioninLiteraryTexts.md
Model: None

---

## Summary  
The paper tackles the problem of attributing quotations to their speakers in literary texts, a task that is both linguistically challenging and computationally expensive. By introducing a joint‑scoring encoder formulation that processes multiple attribution candidates within a single large context window, the authors achieve state‑of‑the‑art accuracy while dramatically reducing inference time compared with existing methods. Their approach leverages pretrained language models to preserve long‑range anaphora signals that are otherwise lost in parallel prediction strategies. The work is released as ModernBookNLP, providing a ready‑to‑use tool for large‑scale literary analysis.

## Key Contributions  
- [Finding 1] The joint scoring formulation enables simultaneous attribution of all quotation speakers within one forward pass, improving overall accuracy to 94.5 % on the PDNC dataset.  
- [Finding 2] Compared with standard independent models and LLM‑based approaches, the new method processes novels 20× faster than comparable encoders and over 1000× faster than LLM pipelines on an A100 GPU.  
- [Finding 3] An analysis shows that joint scoring preserves long‑range anaphora resolution signals present in pretrained encoders, which standard methods discard, thereby enhancing performance on difficult attribution examples.

## Methodology  
The authors adopt an encoder‑based architecture that treats the entire novel as a single input sequence. A shared context window captures all quotation mentions and their surrounding discourse, allowing a unified scoring function to rank speaker candidates jointly. The joint scorer outputs a probability distribution over possible attributions for each quote, which is then refined by a lightweight classifier. This design avoids the sequential bottleneck of processing quotations one‑by‑one, instead exploiting parallelism across the whole text.

## Results  
On the Project Dialogism Novel Corpus (PDNC) containing 35,000 manually annotated quotations from 22 English novels, the joint scoring model attains 94.5 % overall attribution accuracy—the best reported result to date. Benchmarks reveal that the encoder runs 20× faster than standard encoder‑only attribution models and exceeds 1000× speedup over LLM‑based pipelines under identical hardware (A100). Ablation studies confirm that preserving long‑range dependencies is critical for handling complex anaphora patterns.

## Significance  
Accurate quotation attribution is essential for literary analysis, plagiarism detection, and automated summarization. By delivering high accuracy with minimal computational overhead, the joint scoring approach makes LLM‑scale processing feasible for large corpora, enabling researchers to scale up analyses that were previously limited by latency or cost.

## Related Concepts  
- Joint scoring (unified attribution scoring)  
- Anaphora resolution in literary texts  
- Large language model inference costs  
- Context window size and long‑range dependency preservation  
- Pre‑trained encoder representations for downstream tasks
