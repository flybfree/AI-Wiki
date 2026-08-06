# Summary: 2026-08-05_07-58-53Z_RelevantbutIncomplete_ReferentialDanglingasaParadi.md
Saved: 2026-08-05 22:25
Source: 2026-08-05_07-58-53Z_RelevantbutIncomplete_ReferentialDanglingasaParadi.md
Model: None

---

## Summary  
The paper investigates a failure mode in hard prompt compression called referential dangling, where independent selection of tokens or sentences removes the supporting evidence needed to interpret retained answers. It demonstrates that this flaw causes substantial accuracy loss across multiple multi‑hop question‑answering benchmarks and compressors. The authors propose a lightweight classifier that reinserts omitted sentences essential for answer interpretation while preserving near‑optimal compression ratios. This work bridges theoretical insight with practical mitigation, showing that referential completeness is as crucial as relevance in hard prompt compression.

## Key Contributions  
- Finding 1: Independent scoring can split dependent evidence pairs, leading to referential dangling.  
- Finding 2: At compression ratio 0.30, Beaver leaves the answer path incomplete in 34–54 % of bridge examples across three multi‑hop QA datasets; all six hard compressors exhibit dangling rates up to 60 %, and every document in LongBench‑v2 Single‑Document QA contains at least one dangling reference.  
- Finding 3: Reinserting the top‑ranked omitted sentences improves accuracy by 4.7 points on HotpotQA while increasing the compression ratio only from 0.30 to 0.31, recovering ≈ 88 % of the gap between compressed and full contexts.

## Methodology  
The authors first construct hard compressors that independently score units under a strict token budget, then evaluate them on benchmark bridge sets to detect dangling cases. To address the problem without relying on support annotations, they train a compact classifier using reinforcement‑learning or supervised ranking objectives to predict whether an omitted sentence is needed for answer interpretation; this classifier is deployed at inference time to automatically restore missing content.

## Results  
Beaver shows 34–54 % of bridge examples contain dangling answers when compressed to 0.30, and HotpotQA compressors reach up to 60 % dangling rates. LongBench‑v2 Single‑Document QA documents all have at least one dangling reference. Automatic restoration via the classifier improves accuracy by 4.7 points on HotpotQA while changing the compression ratio only from 0.30 to 0.31, recovering most of the performance gap between compressed and full contexts.

## Significance  
This work reveals a critical limitation in current hard prompt compression that undermines multi‑hop reasoning: referential dangling can erase answer paths even when relevance scores are high. By providing an automatic restoration mechanism, it preserves most compression benefits while eliminating this paradigm‑level failure mode, paving the way for more robust and reliable large‑language model inference.

## Related Concepts  
- Hard prompt compression  
- Referential dangling  
- Bridge examples  
- Multi‑hop question answering  
- Token budget optimization  
- Automatic restoration  
- Qwen3 embeddings  
- HotpotQA  
- LongBench‑v2
