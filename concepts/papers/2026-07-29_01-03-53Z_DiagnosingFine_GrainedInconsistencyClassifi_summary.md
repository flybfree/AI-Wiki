# Summary: 2026-07-29_01-03-53Z_DiagnosingFine_GrainedInconsistencyClassificationi.md
Saved: 2026-07-29 20:21
Source: 2026-07-29_01-03-53Z_DiagnosingFine_GrainedInconsistencyClassificationi.md
Model: None

---

## Summary  
The paper tackles the problem of classifying subtle inconsistencies that appear in financial disclosure texts, moving beyond binary conflict detection to a fine‑grained taxonomy of eleven inconsistency types (numerical, temporal, referential, factual, normative, etc.). By treating each type as a distinct label and evaluating multiple models—from frozen embeddings to LoRA‑adapted LLMs—the authors demonstrate that compact supervised encoders can achieve competitive performance while offering practical efficiency advantages over large language models. Their work also reveals that the quality of extracted evidence spans is a critical bottleneck, influencing both classification accuracy and downstream reasoning.

## Key Contributions  
- **Fine‑grained inconsistency taxonomy**: The study introduces an 11‑label classification scheme for SBID‑FD, providing a systematic way to differentiate numerical, temporal, referential, factual, normative, and other inconsistencies.  
- **Model comparison showing encoder efficiency**: A fine‑tuned 300 M encoder reaches 61.9 % accuracy, matching or slightly surpassing LoRA‑adapted Qwen3.5‑9B (61.5 %) and GPT‑5.4 (61.3 %), highlighting that smaller supervised encoders can be as effective as larger generative models under the same evaluation protocol.  
- **Evidence localization remains a bottleneck**: Gold evidence spans boost fine‑tuned encoder performance to 65.3 %, yet automatically predicted spans recover only a partial share of this gain, indicating that precise span extraction is still a limiting factor.

## Methodology  
The authors use a fixed snapshot of the SBID‑FD benchmark (5,940 instances) with paired reference evidence spans for each inconsistency label. They evaluate six approaches under a shared protocol: (1) frozen embedding classifiers, (2) fine‑tuned 300 M encoders, (3) evidence‑augmented classifiers, (4) prompted large language models, and (5) LoRA‑adapted generative models such as Qwen3.5‑9B and GPT‑5.4. All models receive the same input format and are scored on overall accuracy and per‑class performance.

## Results  
The fine‑tuned encoder achieves 61.9 % overall accuracy, while LoRA‑adapted Qwen3.5‑9B scores 61.5 % and GPT‑5.4 scores 61.3 %. Supplying gold evidence spans raises the encoder’s performance to 65.3 %, whereas auto‑predicted spans recover only a modest portion of that improvement. Per‑class analysis shows referential inconsistencies are most affected by localization errors, whereas factual and logical inconsistencies remain challenging even when relevant evidence is provided.

## Significance  
These findings suggest that compact supervised encoders can be practical alternatives to large generative models for financial disclosure analysis, offering comparable accuracy with lower computational cost. However, they also underscore the necessity of high‑quality evidence extraction and robust reasoning across closely related inconsistency categories—a dual focus required for reliable downstream applications.

## Related Concepts  
- **Fine‑grained classification**: Assigning distinct labels to different types of inconsistencies within a text.  
- **Evidence spans**: Sub‑textual segments that serve as ground truth or model input for consistency detection.  
- **LoRA adaptation**: Parameter‑efficient fine‑tuning of large language models.  
- **Embedding classifiers**: Fixed or fine‑tuned low‑dimensional representations used for supervised tasks.
