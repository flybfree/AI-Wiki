# Summary: 2026-07-17_18-47-31Z_RetrievalisEnough_Training_FreeInterpretabilitywit.md
Saved: 2026-07-24 00:00
Source: 2026-07-17_18-47-31Z_RetrievalisEnough_Training_FreeInterpretabilitywit.md
Model: None

---

## Summary  
The paper introduces HARP (Hypothesis‑driven Agentic Retrieval and Probing), a training‑free interpretability framework that leverages an LLM agent, a vector database of activations paired with textual context, and a suite of activation‑manipulation tools. By iteratively retrieving samples, forming hypotheses, and validating them with linear probes, HARP uncovers insights that appear to go beyond what is recoverable from the original training data. The approach demonstrates that interpretability can be achieved without any model‑training cost, challenging the assumption that expensive training‑based methods are necessary for deeper understanding.

## Key Contributions  
- [Finding 1] Training‑free methods can achieve performance comparable to costly training‑based approaches such as SAEs and activation oracles.  
- [Finding 2] Retrieval of activation contexts enables hypothesis formation that is validated via linear probes, revealing insights not present in the original dataset.  
- [Finding 3] The system’s design is substantially cheaper and more flexible; new datasets can be indexed on demand whenever existing ones prove insufficient.

## Methodology  
The authors equip an LLM agent with a vector database containing activations paired with their textual contexts, along with tools for projecting out directions in latent space, computing activation differences, and averaging activations. The agent repeatedly queries the database to obtain representative samples, constructs hypotheses about the underlying concept or behavior, and then tests these hypotheses by building linear probes that measure how strongly each hypothesis aligns with the retrieved data. This hypothesis‑driven loop continues until a high level of confidence is reached, all without any training step.

## Results  
HARP outperforms both activation oracles and SAE‑based agents on four interpretability benchmarks: concept discovery, concept detection, model steering, and secret elicitation. The training‑free design also yields lower computational overhead and greater adaptability; when the original database is insufficient, additional activations can be indexed without retraining. These results suggest that prior methods do not extract insights beyond their training data.

## Significance  
The work shows that interpretability can be achieved with minimal cost, encouraging a shift toward retrieval‑augmented frameworks rather than expensive training pipelines. It also motivates the creation of benchmarks that explicitly require new methods to demonstrate genuine insight extraction, thereby guiding future research away from “training‑only” explanations.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Linear probing for activation interpretation  
- Self‑Attention Explanation (SAE) oracles  
- Hypothesis‑driven AI agents  
- Vector databases and on‑demand indexing  
- Concept discovery in neural networks
