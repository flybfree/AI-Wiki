# Summary: 2026-08-01_15-05-45Z_ATriple_RobustnessAnalysisofRetrieval_AugmentedGen.md
Saved: 2026-08-03 20:30
Source: 2026-08-01_15-05-45Z_ATriple_RobustnessAnalysisofRetrieval_AugmentedGen.md
Model: None

---

## Summary  
The paper investigates why prior evaluations of Retrieval‑Augmented Generation (RAG) for multi‑hop requirements traceability disagree and argues that these disagreements stem from a single corpus, embedding model, or judge rather than inherent differences in the architecture. By fixing a five‑pipeline matrix and systematically varying embedder, source corpus, and evaluator across thousands of runs, the authors conduct a triple‑robustness analysis to reveal hidden performance patterns. Their work demonstrates that citation quality is highly sensitive to where it is measured and that faithfulness judgments can collapse under repeated testing. The study calls for rigorous robustness testing before trusting RAG claims.

## Key Contributions  
- [Finding 1] GraphRAG’s graph walk floods the context window at precision 0.12‑0.23, yet the synthesizer cites selectively at higher precision (0.48‑0.65), showing that ranking can invert when citation quality is measured as an attribution set.  
- [Finding 2] Answer‑level citation winners are corpus‑ and stratum‑conditional but embedder‑robust: GraphRAG ties vanilla on short‑hop DO‑178C queries yet dominates every MuSiQue stratum, while agentic pipelines succeed only on three‑plus hop requirements.  
- [Finding 3] Faithfulness is fragile to retrieval state; GPT‑5.4’s self‑kappa across embedders drops from 0.76 (floor) to 0.137 (verdict change), and re‑judging frozen inputs after eleven weeks yields kappa ≤ 0.14 for both judges.

## Methodology  
The authors fixed a five‑pipeline architecture matrix—embedders (local e5‑small, Azure text‑embedding‑3‑small), corpora (DO‑178C typed‑edge requirements vs. Wikipedia paragraph chains via MuSiQue), and judges (paired GPT‑5.4 × GPT‑4.1). They executed 2 × 4 440 main‑matrix runs, 600 cross‑corpus runs, and collected over 5 000 faithfulness judgments, varying embedder, corpus, and judge independently to isolate each factor.

## Results  
GraphRAG’s precision metrics vary widely: low at 0.12‑0.23 for graph walks but higher at 0.48‑0.65 for citation sets. The synthesized answers cite only a subset of retrieved items, causing ranking inversion when attribution is scored as the retrieval set. Answer‑level wins are corpus‑dependent; GraphRAG matches vanilla on short‑hop DO‑178C but outperforms on all MuSiQue strata, whereas agents win only beyond three hops. Faithfulness declines with hop distance on DO‑178C (p < 0.05 in three judge×embedder combos) and remains stable on Wikipedia chains. Single‑judge LLM faithfulness is unstable: GPT‑5.4’s self‑kappa across embedders is 0.137, far below the test‑retest floor of 0.76; re‑evaluation after eleven weeks yields kappa ≤ 0.14. A learned router on dense embeddings achieves macro‑F1 = 0.86 for hop classification.

## Significance  
These findings reveal that RAG performance is not intrinsic but contingent on the measurement point, making prior rankings potentially misleading. By exposing embedding and corpus effects, the study urges developers to test architectures under multiple conditions before adopting them as reliable solutions.

## Related Concepts  
- Retrieval‑Augmented Generation (RAG)  
- Multi‑hop requirements traceability  
- GraphRAG vs. vector RAG  
- Citation quality measurement  
- Faithfulness and hallucination detection  
- Embedding models (e5‑small, Azure text‑embedding‑3‑small)  
- Judges GPT‑5.4, GPT‑4.1  
- MuSiQue corpus for traceability data
