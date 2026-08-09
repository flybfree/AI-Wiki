---
title: Science One Framework: A verifiable autonomous research framework via Chain-of-Evidence
date: 2026-08-09
url: https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-09 00:01
---

# Science One Framework: A verifiable autonomous research framework via Chain-of-Evidence

## Full Article

Science One Framework: A verifiable autonomous research framework via Chain-of-Evidence
July 30, 2026
Rui Meng, Research Scientist, and Tomas Pfister, Director, Google Cloud
Introducing the Science One Framework, an experimental research prototype designed to eliminate hallucinations by natively building verifiable evidence chains, and CoE Audit, an automated protocol to evaluate the integrity of AI-generated papers.
Quick links
Paper
Share
Copy link
×
Large language models (LLMs) are increasingly being deployed not just as coding assistants but as autonomous agents capable of conducting end-to-end scientific research workflows. Recent systems (e.g., Sakana’s
AI-Scientist
,
AutoResearchClaw
,
DeepScientist
,
AI-Researcher
) can review literature, formulate hypotheses, execute experiments and write complete manuscripts that are comparable to human-authored papers. However, as the surface-level quality of these AI-generated manuscripts improves, a critical structural problem has emerged: verifiability. Because current autonomous research pipelines generate text iteratively, errors introduced at any stage are amplified. Some existing systems can generate
non-existent citations
, exhibit
misalignments
between the described methods and the actual code, and report experimental scores that are
not fully reproducible
from the provided code.
In our
paper
, we tackle this problem by introducing Chain-of-Evidence (CoE), a new verifiability framework for AI-driven research. We instantiate CoE with the Science One Framework, an autonomous research prototype that natively builds and maintains evidence chains, and the CoE Audit, a set of automated evaluation metrics that measures the integrity of AI-generated papers against their underlying code and evidence. Our results show that baseline systems hallucinate up to 21% of their references and frequently misalign their code and text, whereas the Science One Framework achieves zero phantom references and fully verifiable scores while achieving state-of-the-art performance on frontier benchmarks like
MLE-Bench
and
Parameter-Golf
.
Chain-of-Evidence: A framework for verifiable research
The CoE is a conceptual framework that defines what makes a research artifact trustworthy, much as
ACID
defines what makes a database transaction reliable. Rather than prescribing how to build a research agent, the framework specifies the properties its outputs must have. It follows a single principle with two halves: every claim in a research artifact must carry a recorded evidence chain (completeness), and each chain must genuinely support the claim it is attached to (correctness). A claim may be a reference, a reported number, a method description, or a conclusion, that must link back to corresponding evidence, such as a peer-reviewed paper, an experimental log line, the code that actually ran, or the results table.
A hallucinated reference points to a paper that does not exist. An unreproducible score does not reappear when the code is re-run. A misdescribed method claims one algorithm in the paper while the code implements another. Each is a claim whose chain back to its evidence is broken; the CoE Audit makes these breaks measurable.
The Science One Framework
To demonstrate that verifiable AI research is possible without sacrificing problem-solving performance, we designed the
Science One Framework
. Unlike previous agents that generate a paper and try to link facts retroactively, the Science One Framework instantiates the CoE framework by construction through three main modules:
Problem investigator (literature grounding):
To prevent hallucinated references, the Science One Framework builds a citation graph via the
Semantic Scholar API
. It reads up to 100 full-text PDFs per topic to produce a structured research brief. Every reference in the final paper originates from this grounded API call entirely eliminating reliance on model memory.
Discovery engine (parallel explore-exploit):
The Science One Framework systematically explores and exploits ideas across multiple parallel branches. In each isolated cycle, a Solver agent implements a solution and a task-specific evaluator scores it. High-performing branches are iteratively refined, and all raw evaluator outputs are compiled into a strict, read-only record.
Paper writer and claim verifier:
Before rendering the manuscript, the Science One Framework builds a structured representation of every factual claim with an inline evidence tag binding it to a specific workspace artifact. A dedicated Claim Verifier checks every claim against its declared source. Claims that outrun their evidence are reconciled with the source — restated conservatively rather than removed, keeping the paper aligned with what the work supports.
[Science-One-1-final]
The Science One Framework pipeline. Problem Investigator grounds literature via retrieved PDFs. Discovery module explores and evaluates solutions. Paper writing & verification module writes and verifies the paper with a Claim Verifier ensuring all claims match their evidence source.
CoE Audit: Measuring verifiability
To rigorously evaluate the Science One Framework prototype against state-of-the-art baselines (e.g.,
Sakana AI's AI Scientist v2
,
AutoResearchClaw
,
DeepScientist
,
AI-Researcher
), we developed the CoE Audit. This post-hoc evaluation protocol acts as an automated forensic reviewer, running four strict integrity checks on the generated artifacts (paper, solution, code and references):
Score verification:
Extracts the reported score from the paper and compares it against a completely independent re-run of the submitted code.
Specification violation:
Inspects the solution code to ensure it actually solves the task rather than exploiting the evaluator metric or reading ground-truth answer files.
Reference verification:
Cross-checks every bibliography entry against academic APIs to catch non-existent phantom references.
Method-code alignment:
Uses LLM judges to compare the paper's method section side-by-side with the code to ensure the text faithfully describes the implemented algorithm.
[Science-One-2]
Overview of the CoE Audit framework and its four core integrity checks.
Results
We applied the CoE Audit to 75 papers generated across five systems-optimization tasks (
Prism
,
Cloudcast
,
EPLB
,
LLM-SQL
, and
transaction scheduling
) from the
Automated Design of Research Systems
(ADRS) benchmark.
The Science One Framework significantly outperformed existing baselines in verifiability. The CoE Audit applies the same independent protocol to every system, re-checking each reference against live scholarly databases, and under it, Science One Framework led on all four integrity checks. None of its references were phantom: every one pointed to a real, retrievable paper, compared to hallucination rates as high as 21% in baselines, because the Problem Investigator retrieves every reference rather than generating it from memory. It also achieved perfect score verification and the highest method-code alignment. In contrast, baseline systems frequently described sophisticated algorithms (like "hybrid neuro-symbolic solvers") when their submitted code was a simple, deterministic heuristic.
[Science-One-3-Final]
CoE Audit results across five systems.
Crucially, implementing strict verifiability did not compromise the agent's scientific capabilities. The Science One Framework
matched or exceeded
human expert performance on all five ADRS tasks, achieving the best overall score among all systems on two of them (Cloudcast and EPLB).
[Science-One-4-Final]
Comparison of solver performance across five MLE-Bench tasks and Parameter Golf.
To test its generalization, we deployed the Science One Framework on six highly complex external tasks:
MLE-Bench
: Across five difficult Kaggle competitions spanning medical imaging, fine-grained recognition and 3D perception, Science One Framework achieved two Gold Medals (including a winning score on 3D Object Detection where baselines failed entirely) and two Silver Medals.
Parameter-Golf
: We tested Science One Framework in a live LLM-training competition with strict hardware and file-size constraints. While baseline systems failed to produce valid submissions, Science One Framework successfully adhered to all constraints and achieved a state-of-the-art score (as of April 27, 2026). Note that Science One Framework discovers genuine and novel algorithmic techniques rather than just tweaking superficial hyperparameters.
Looking forward
As autonomous research systems scale to solve increasingly difficult scientific problems, solver quality alone will no longer be enough to differentiate them. What will separate their outputs is whether the resulting research can be trusted. Our findings demonstrate that verifiability must be treated as a first-class architectural constraint. By building evidence chains at the time a claim is produced rather than attempting to reconstruct grounding after the fact, The Science One Framework demonstrates that AI agents can produce rigorous, trustworthy and highly competitive scientific research. We hope the Chain-of-Evidence framework and its audit will serve as valuable tools for the community as we continue to build the next generation of AI scientists.
Acknowledgements
We would like to thank Bhavana Dalvi Mishra, Jiefeng Chen, Chun-Liang Li, Palash Goyal, Mihir Parmar, Yiwen Song, Yale Song, Raj Sinha, Parthasarathy Ranganathan, Burak Gokturk and Jinsung Yoon for their valuable contributions to this work.
Disclaimer
The Science One Framework is an experimental research prototype, not production-ready tools.
Labels:
General Science
Machine Intelligence
Natural Language Processing
Quick links
Paper
Share
Copy link
×
Other posts of interest
[Four smartphone screenshots display a conversational Symptom Checker research app collecting neck pain symptoms, showing a diagnosis summary, and prompting a feedback rating.]
July 22, 2026
SymptomAI: Towards a conversational AI agent for everyday symptom assessment
General Science
·
Health & Bioscience
·
Natural Language Processing
·
Responsible AI
[RL_for _QEC-2]
July 22, 2026
Towards a quantum computer that learns from its errors
Machine Intelligence
·
Quantum
[Interpolation-effect-1]
July 15, 2026
Towards demystifying the creativity of diffusion models
Algorithms & Theory
·
Generative AI
·
Machine Intelligence
×
❮
❯
[Science-One-1-final]
[Science-One-2]
[Science-One-3-Final]
[Science-One-4-Final]

## Metadata
- **Source**: [Original Article](https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/)
