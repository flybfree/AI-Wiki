# Summary: 2026-07-31_15-35-57Z_ARB_AMatchedAuthorship_RewritingBenchmarkDatasetfo.md
Saved: 2026-08-03 10:23
Source: 2026-07-31_15-35-57Z_ARB_AMatchedAuthorship_RewritingBenchmarkDatasetfo.md
Model: None

---

## Summary
The paper introduces the Authorship-Rewriting Benchmark (ARB), a novel dataset designed to evaluate the robustness of AI-text detectors against sophisticated rewriting attacks that preserve human authorship styles. The authors address a critical gap in current evaluation methodologies by demonstrating that standard benchmarks, which compare raw human text against direct Large Language Model (LLM) generation, fail to predict detector performance when human content is modified by an LLM. By creating matched variants of texts across four distinct generation and rewriting scenarios, the study reveals a significant discrepancy in how detectors handle different types of textual modification. The core contribution lies in providing a rigorous testing ground that exposes the vulnerability of existing detection tools to "human-to-LLM" rewriting processes, which are increasingly common in real-world applications where users seek to evade detection while maintaining their original voice.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap

## Key Contributions
- **Identification of a Critical Vulnerability**: The study demonstrates that state-of-the-art detectors suffer massive performance drops (60-78 percentage points) when human-authored text is rewritten by an LLM, despite performing well on direct LLM-generated content.
- **Creation of the ARB Dataset**: The authors introduce a new benchmark comprising 1,800 source texts and four matched variants per source (Human, Free-LLM, H2L, and LLM2L) generated using four open-weight models, enabling precise comparative analysis.
- **Evidence of Non-Transferability**: The research proves that detector efficacy measured on conventional human-vs-LLM benchmarks does not transfer to scenarios involving LLM-assisted rewriting of human text, challenging the validity of current evaluation standards.

## Methodology
The authors constructed the ARB dataset by selecting 1,800 human-written source texts from three diverse corpora: XSum, WritingPrompts, and OpenWebText. For each source item, they generated four matched variants using four open-weight LLMs (Llama-3.2-3B, Qwen2.5-7B, Mistral-7B, and Gemma-2-9B). These variants included the original human text, direct generation from the LLM (Free-LLM), LLM-rewritten human text (H2L), and LLM-rewritten LLM text (LLM2L). The authors then evaluated five prominent AI-text detectors—FastDetectGPT, Binoculars-falcon-7b, RADAR, BERT-Defense, and RoBERTa-Defense—at a strict operating point of 1% false positive rate to ensure fair comparison of true positive recall across all regimes.

## Results
The experimental results highlight a stark contrast in detector performance depending on the source of the text modification. FastDetectGPT and Binoculars-falcon-7b achieved high recall rates (91.2% and 93.5%) for direct LLM generation but plummeted to 30.8% and 15.1% respectively when detecting human text rewritten by an LLM. In contrast, these detectors remained relatively robust when LLM-generated text was further rewritten by the same model, showing only a minor decline in recall. RADAR exhibited a similar pattern of significant degradation for H2L texts, while BERT-Defense and RoBERTa-Defense performed poorly across all categories, maintaining less than 3% recall.

## Significance
This research is significant because it exposes a fundamental flaw in the current ecosystem of AI-text detection. As users increasingly employ LLMs to paraphrase their own writing to avoid detection, existing tools are largely ineffective. The findings necessitate a re-evaluation of benchmark standards and highlight the urgent need for detectors that can distinguish between original human authorship and LLM-modified human text, rather than just detecting raw machine generation.

## Related Concepts
- AI-Text Detection
- Large Language Models (LLMs)
- Paraphrasing and Rewriting Attacks
- Benchmark Datasets
- False Positive Rate (FPR)
- True Positive Recall (TPR)
- Authorship Attribution
