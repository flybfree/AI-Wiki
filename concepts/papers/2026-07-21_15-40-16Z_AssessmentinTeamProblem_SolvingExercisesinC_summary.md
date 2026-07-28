# Summary: 2026-07-21_15-40-16Z_AssessmentinTeamProblem_SolvingExercisesinComputin.md
Saved: 2026-07-24 01:00
Source: 2026-07-21_15-40-16Z_AssessmentinTeamProblem_SolvingExercisesinComputin.md
Model: None

---

## Summary  
The paper proposes two automated assessment techniques for team problem‑solving exercises (TTXs) used in computing education: a clustering algorithm that groups teams with similar approaches and an LLM‑based rubric evaluator. By applying these methods to data from 81 participants across two countries, the authors demonstrate how they can be integrated into the open‑source INJECT platform to provide faster, scalable feedback. The work bridges the gap between rich TTX data capture and practical performance evaluation, offering a research‑to‑practice solution that is both technically feasible and educationally valuable.

## Key Contributions
- Finding 1: Clustering of team responses into comparable groups yields valid and reliable assessment scores with minimal computational demand, enabling rapid instructor feedback.  
- Finding 2: Large language models can evaluate teams against standardized rubrics; GPT‑5.2 shows substantially lower disagreement with human scores than GPT‑4o.  
- Finding 3: The clustering and LLM methods have been successfully embedded into the INJECT TTX learning platform, supporting scalable deployment in teaching practice.

## Methodology  
The authors collected interaction logs from two TTX scenarios involving 81 student teams (four per country). Each log contained actions, communication transcripts, and timestamps. They first applied a hierarchical clustering algorithm to the action sequences, generating clusters that represent similar problem‑solving strategies. For each cluster, they computed aggregate metrics aligned with predefined rubrics. Separately, they fed the same transcriptions into GPT‑4o and GPT‑5.2, which generated rubric scores based on the same criteria. The human instructors then assigned final scores using a standardized rubric for validation.

## Results  
Clustering produced 12 distinct groups; intra‑group variance was low (average coefficient of variation ≈ 0.08) and inter‑group variance was high, confirming the method’s ability to separate teams with comparable approaches. The clustering approach required only a few seconds per team on a standard laptop, meeting low computational requirements. GPT‑4o disagreed with instructor scores in 32 % of cases, whereas GPT‑5.2 disagreed in only 8 %, indicating superior LLM performance. All tools were integrated into INJECT, which now offers automated clustering dashboards and LLM score generation for each scenario.

## Significance  
Automated assessment reduces instructor workload while maintaining fidelity to learning objectives, supporting evidence‑based feedback loops. The findings provide a replicable framework that can be extended to larger cohorts or other educational contexts, fostering the adoption of data‑driven evaluation in TTXs and beyond.

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
