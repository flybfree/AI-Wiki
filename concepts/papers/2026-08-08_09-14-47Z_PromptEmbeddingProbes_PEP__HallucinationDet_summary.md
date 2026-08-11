# Summary: 2026-08-08_09-14-47Z_PromptEmbeddingProbes_PEP__HallucinationDetectioni.md
Saved: 2026-08-10 22:52
Source: 2026-08-08_09-14-47Z_PromptEmbeddingProbes_PEP__HallucinationDetectioni.md
Model: None

---

## Summary  
The paper introduces Prompt Embedding Probes (PEP), a white‑box technique that detects hallucinations in frozen large language models by augmenting hidden states with a small number of learnable prompt embeddings, thereby improving detection accuracy over conventional linear probes while keeping the backbone unchanged. PEP is evaluated on TriviaQA, GSM8K, and MedQA using Qwen3 models across multiple scales to assess both in‑distribution performance and broader transferability.

## Key Contributions  
- [Finding 1] PEP achieves higher accuracy than standard linear probes for answer‑level hallucination detection on the three benchmark datasets.  
- [Finding 2] Pre‑generation prediction and cross‑model transfer remain effective when using PEP, indicating that prompt embeddings can strengthen hidden‑state probing without retraining the model.  
- [Finding 3] Robust cross‑dataset transfer remains difficult, highlighting limitations of generalizing detection methods across disparate data distributions.

## Methodology  
PEP extends linear probes by adding a few trainable vectors to each token’s hidden representation. The authors freeze the LLM backbone and only train these embeddings on the target dataset, allowing the probe to learn task‑specific cues while preserving model integrity. This approach yields a lightweight, white‑box detection module that can be inserted into inference pipelines.

## Results  
PEP improves hidden‑state‑based detection over standard linear probes in the main in‑distribution setting across all evaluated models and tasks. Pre‑generation prediction benefits significantly, as does cross‑model transfer within the same dataset family. However, robust generalization to a completely different dataset is limited, reflecting the challenge of out‑of‑distribution probe adaptation.

## Significance  
By requiring only a few trainable parameters, PEP provides a practical, low‑overhead solution for hallucination detection in safety‑critical applications where model retraining is undesirable. The method demonstrates that subtle prompt‑based adaptations can enhance hidden‑state probing while maintaining the frozen backbone of LLMs.

## Related Concepts  
Prompt embeddings, linear probes, hidden states, hallucination detection, frozen LLM, pre‑generation prediction, cross‑model transfer, out‑of‑distribution generalization.
