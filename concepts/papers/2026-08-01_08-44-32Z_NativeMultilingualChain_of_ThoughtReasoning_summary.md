# Summary: 2026-08-01_08-44-32Z_NativeMultilingualChain_of_ThoughtReasoninginLow_R.md
Saved: 2026-08-03 20:22
Source: 2026-08-01_08-44-32Z_NativeMultilingualChain_of_ThoughtReasoninginLow_R.md
Model: None

---

## Summary  
The paper addresses the problem that large language models often collapse to English when performing multi‑step reasoning in low‑resource Southeast Asian languages, creating a cold‑start bottleneck for policy optimization and risking catastrophic forgetting during fine‑tuning. To overcome this, the authors propose OSCD (Onramp-Sequence Cross-Distillation), an algorithm that injects high‑resource reasoning traces into low‑resource vocabularies through a translator‑agent loop while aligning semantic embeddings of both source and target reasoning traces. This joint approach preserves linguistic diversity and enables stable generation without relying on external translation. The method is evaluated on AIME25 and HMMT25 benchmarks, showing substantial gains.

## Key Contributions  
- OSCD integrates an agentic translator that projects high‑resource reasoning trajectories into low‑resource language subspaces during fine‑tuning rollouts.  
- Joint‑embedding semantic alignment bridges cross‑lingual representation gaps between reference and target‑language traces.  
- The approach yields up to 3.2× overall improvement in native Southeast Asian languages for mathematical reasoning, with the semantic‑alignment component alone contributing ~6.4% linguistic debiasing.

## Methodology  
The authors begin with a pre‑trained multilingual model trained on high‑resource data. During fine‑tuning, an auxiliary translator agent generates reference sentences in the target language from English reasoning traces. OSCD then projects these references into the low‑resource vocabulary space while simultaneously updating embeddings of both source and target tokens through a joint‑embedding loss that enforces semantic similarity. The combined loss ensures that generated outputs remain faithful to the original logical chain without translating each token individually.

## Results  
Experiments on AIME25 (Arithmetic Inference in Multiple Languages) and HMMT25 (Higher‑Level Math Metric Test 25) show that OSCD outperforms translation‑only baselines by an average of 3.2× on native language scores, with the semantic‑alignment subcomponent adding another ~6.4% improvement. The gains are consistent across five low‑resource Southeast Asian languages, indicating broad applicability.

## Significance  
By eliminating cross‑lingual collapse and preserving native linguistic structures, OSCD enables policy systems to reason reliably in under‑represented languages without costly external translation services. This reduces reliance on human translators and mitigates catastrophic forgetting, making large language models more equitable and efficient for global deployment.

## Related Concepts  
- Large Language Models (LLMs)  
- Chain-of-Thought reasoning  
- Cross‑lingual representation alignment  
- Agentic translation loops  
- Joint loss functions  
- Low‑resource language fine‑tuning  
- Linguistic debiasing
