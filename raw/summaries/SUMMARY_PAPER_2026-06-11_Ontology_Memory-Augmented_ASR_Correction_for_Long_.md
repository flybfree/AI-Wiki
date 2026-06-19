---

title: Ontology Memory-Augmented ASR Correction for Long Text-Speech Interleaved Conversations
url: http://arxiv.org/abs/2606.13464v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-11_15-18-32Z_OntologyMemory_AugmentedASRCorrectionforLongText_S.md
generated_at: "2026-06-11 21:00"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces an ontology memory‑augmented ASR correction framework designed for long, interleaved text‑speech conversations where errors are context‑dependent. The method organizes prior interaction history into a dynamically updatable knowledge graph that stores entities, terminology variants, potential confusions and semantic relations, enabling retrieval‑grounded corrections. Experiments on the RAMC‑Corr dataset show the approach outperforms direct correction in nine out of ten backbone settings.

## Key Takeaways
- The ontology memory stores recurring concepts and surface forms, allowing the system to locate sparse corrective evidence within noisy dialogue streams.  
- Evaluation demonstrates that grounding corrections with contextual nodes yields higher accuracy than methods that rely solely on raw history or current hypotheses.  
- The framework encourages selective edits by linking ASR errors to specific semantic relations stored in the ontology.

## Context
Automatic speech recognition systems increasingly operate on long, multi‑turn dialogues where misrecognitions can propagate if not corrected locally. Traditional correction techniques lack the capacity to retrieve relevant historical knowledge, leading to suboptimal performance and noisy outputs. This work addresses that gap by integrating structured dialogue memory into ASR pipelines.

## Implications
For developers of conversational AI, this ontology‑based approach offers a scalable way to improve error resilience without retraining large models each interaction. Practitioners can leverage the framework to reduce false confidence in long transcripts, enhancing user experience and downstream processing reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.13464v1)
