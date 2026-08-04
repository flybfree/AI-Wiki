# Summary: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md
Saved: 2026-08-04 00:40
Source: 2026-08-03_09-42-34Z_ET_Prune_Evidence_AwareDynamicBudgetingforVisualTo.md
Model: None

---

## Summary  
ET-Prune addresses a critical limitation in visual token pruning for text-rich multimodal large language models (MLLMs), where fixed pruning ratios often discard essential evidence needed for correct inference, especially in OCR-centric tasks. The authors introduce ET-Prune, a training-free framework that treats pruning as an evidence allocation problem, dynamically allocating tokens based on the relevance and uncertainty of visual evidence derived from text-rich inputs. By leveraging decoder-side partial query-key blocks to extract question-conditioned evidence, ET-Prune ensures that critical information is preserved while aggressively removing redundant or visually salient but irrelevant regions. This approach enables a more balanced trade-off between inference cost reduction and accuracy preservation.

## Key Contributions  
- [Finding 1] ET-Prune casts pruning as an evidence allocation problem, dynamically allocating tokens based on the relevance and uncertainty of visual evidence derived from text-rich inputs.  
- [Finding 2] The framework uses a decoder-side partial query-key block to derive question-conditioned evidence and safeguards text-like spatial regions, converting evidence uncertainty and density into a sample-specific token floor.  
- [Finding 3] ET-Prune employs three progressive middle-layer events to move the sequence toward this budget, retaining more tokens for diffuse or text-dense evidence while pruning concentrated evidence aggressively.

## Methodology  
ET-Prune avoids fixed token ratios by treating pruning as an optimization of evidence allocation. The model first identifies question-conditioned evidence using a decoder-side partial query-key block, which extracts semantic relevance from the input visual tokens in relation to the query. It then computes evidence uncertainty and density, translating these into a sample-specific token floor that defines the minimum number of tokens required for inference correctness. Three progressive middle-layer events—each corresponding to a stage of pruning decision-making—adjust the sequence toward this budget: the first event identifies diffuse or text-dense evidence requiring preservation; the second refines the allocation based on uncertainty; and the third aggressively removes concentrated, redundant evidence. This dynamic process ensures that only non-critical tokens are pruned while maintaining high accuracy.

## Results  
ET-Prune achieves state-of-the-art results across six backbone-benchmark comparisons at approximately 50% visual-token retention. On OCRBench-v2, it outperforms all pruned baselines by 1.80 and 0.68 percentage points on Qwen3-VL-8B and InternVL3.5-8B, respectively, while maintaining high accuracy. It reaches a circular exact-matching accuracy of 0.8467 on MMBench v1.1 compared to Vanilla’s 0.8437 at 54.45% average visual-token retention. These results demonstrate that ET-Prune provides a favorable observed quality-cost trade-off, significantly improving performance over fixed-ratio pruning methods.

## Significance  
ET-Prune is significant because it introduces an evidence-aware dynamic budgeting strategy that outperforms traditional token-based pruning in text-rich multimodal settings. By aligning pruning decisions with the semantic importance of visual evidence, ET-Prune reduces inference cost without sacrificing accuracy—especially in OCR tasks where small pieces of evidence are crucial. This approach sets a new standard for dynamic, context-sensitive pruning in MLLMs, enabling more efficient and accurate deployment.

## Related Concepts  
- Visual token pruning  
- Multimodal large language models (MLLMs)  
- Evidence allocation  
- Decoder-side partial query-key blocks  
- Text-rich inputs  
- OCR-centric tasks  
- Token floor  
- Middle-layer events
