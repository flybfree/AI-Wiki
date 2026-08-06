# Summary: 2026-08-04_21-31-01Z_HallucinationsontheBoard_Tool_AugmentedEvaluationo.md
Saved: 2026-08-05 20:27
Source: 2026-08-04_21-31-01Z_HallucinationsontheBoard_Tool_AugmentedEvaluationo.md
Model: None

---

## Summary  
The paper introduces ACT-Eval, a tool-augmented evaluation framework designed to assess the factual accuracy and strategic depth of large language model (LLM) chess commentary by decomposing it into atomic claims and validating them using specialized engine tools and expert-verified references. This work addresses a critical gap in LLM performance on chess, where models often generate plausible-sounding but incorrect or incomplete commentary due to hallucinations. The authors demonstrate that even advanced models like GPT-5.4 produce significant factual errors without tool support, while structured evaluation improves reliability. By integrating human calibration and expert annotations, ACT-Eval provides a more nuanced assessment than standard benchmarks.

## Key Contributions  
- [Finding 1] Factual hallucinations in LLM chess commentary are pervasive, with GPT-5.4 producing incorrect sub-claims 22.0% of the time without tool augmentation, and smaller open-weight models exceeding 40%.  
- [Finding 2] Tool-augmented evaluation via ACT-Eval significantly improves factual correctness and move-quality assessment by routing atomic claims to engine-supported tools and expert gold references.  
- [Finding 3] Human calibration confirms that ACT-Eval’s factual judgments align with inter-human agreement, while its coverage scores correlate strongly with human assessments of strategic completeness.

## Methodology  
The authors developed ACT-Eval as a decomposition-based evaluation framework that breaks down chess commentary into atomic claims (e.g., “move X is optimal,” “tactical motif Y is present”). Each claim is then evaluated using two sources: (1) engine-supported tools such as Stockfish or Komodo for move-validity and tactical detection, and (2) expert-annotated gold references that validate strategic and conceptual correctness. The framework produces three scores per position-move pair: factual correctness, coverage of expert ideas, and move-quality judgment. A benchmark of 325 position--move pairs—spanning pedagogical, tournament, and critical positions—was created, with 125 positions containing expert-verified gold atoms and a five-class error taxonomy to guide analysis.

## Results  
The results show that factual hallucinations remain a major issue: GPT-5.4 without tools produces incorrect sub-claims 22.0% of the time, while smaller open-weight models exceed 40%. With ACT-Eval’s tool augmentation, factual accuracy improves substantially, and coverage scores correlate strongly with human strategic assessments. Human calibration confirms that ACT-Eval’s factual judgments fall within the observed range of inter-human agreement (r = 0.91), indicating reliability. However, all models—including GPT-5.4—fail to fully cover expert strategic ideas like long-term positional plans or deep tactical motifs, highlighting a persistent limitation in LLM chess commentary.

## Significance  
This work matters because it provides the first reliable method to evaluate LLM chess commentary beyond surface-level fluency, offering insights into both factual errors and strategic depth. By combining tool support with human expertise, ACT-Eval bridges the gap between superhuman engine evaluations and educational utility, enabling more trustworthy AI-generated chess analysis.

## Related Concepts  
- Hallucinations in LLMs: generation of plausible but false information due to limited domain knowledge.  
- Tool augmentation: using external systems (e.g., engines) to validate LLM outputs.  
- Atomic claims: breaking down complex statements into verifiable components for evaluation.  
- Expert annotation: human validation of strategic and conceptual accuracy in chess commentary.
