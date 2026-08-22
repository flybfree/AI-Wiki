---
title: An AI tool for prioritizing candidate biomarkers from wearable sensor data
date: 2026-08-22
url: https://research.google/blog/an-ai-tool-for-prioritizing-candidate-biomarkers-from-wearable-sensor-data/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/an-ai-tool-for-prioritizing-candidate-biomarkers-from-wearable-sensor-data/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-08-22 00:16
---

# An AI tool for prioritizing candidate biomarkers from wearable sensor data

## Full Article

[A conceptual diagram illustrating a cyclical AI-driven biomarker discovery process analyzing wearable and clinical data.]
An AI tool for prioritizing candidate biomarkers from wearable sensor data
August 21, 2026
Yubin Kim, Student Researcher
We introduce the Biomarker Discovery Framework, a multi-agent system that supports the discovery of biomarker candidates from wearable sensor data through iterative hypothesis generation, statistical analysis, and literature-grounded reasoning.
Quick links
Paper
Share
Copy link
×
Wearable devices capture continuous physiological signals at population scale. These streams, ranging from heart rate dynamics to sleep patterns, can reveal early physiological changes before symptoms appear. The bottleneck is no longer data collection, but turning these signals into reliable, clinically meaningful biomarkers.
Existing language model-based agent systems automate parts of the scientific workflow, but can often break down on physiological time-series data. These systems optimize for predictive performance while overlooking statistical validity, leading to spurious correlations, leakage, and brittle features.
To this end, we introduce the
Biomarker Discovery Framework
, a multi-agent system that structures candidate biomarker prioritization as an iterative research loop under human supervision. By combining hypothesis generation, parallel statistical analysis, model training, adversarial validation, and literature-grounded reasoning, Biomarker Discovery Framework accelerates the discovery process while maintaining strict statistical rigor and preserving human oversight. Across three cohorts (N = 9,279 participant-observations), Biomarker Discovery Framework recovered known clinical signals, identified convergent biomarkers across independent datasets, and improved downstream prediction when combined with demographic features.
[A conceptual diagram illustrating a cyclical AI-driven biomarker discovery process analyzing wearable and clinical data.]
Overview of the Biomarker Discovery Framework. (a) The system ingests time series data from consumer wearables and clinical labs. (b) A closed-loop architecture orchestrates six phases mirroring the human biomarker prioritization lifecycle. (c) An Orchestrator agent decomposes natural-language research directives into execution plans.
A structured, adversarial pipeline with human oversight
Biomarker Discovery Framework combines deterministic computation for numerical analysis with generative reasoning for hypothesis formation and interpretation. An Orchestrator agent decomposes natural-language research directives into execution plans and guides specialized agents through a six-phase process. Meanwhile, shared memory, a structured fact sheet, and common tools preserve traceability across the workflow:
Data understanding:
Scout agents map the schema, missingness, temporal structure, and clinical endpoint, while leakage controls keep target labels separate from feature construction.
Candidate hypotheses grounding:
Literature and Hypotheses agents retrieve and verify prior evidence, then propose physiologically plausible features and composite measures.
Iterative discovery loop:
Statistical and ML agents execute deterministic code to construct features, estimate associations, adjust for multiple testing, and evaluate predictive signals. A Critic agent identifies weak assumptions and unresolved gaps, prompting further analysis when needed.
Adversarial validation:
Critic and Defender agents stress-test candidates for target leakage, overfitting, confounding sensitivity, construct overlap, instability, and physiological implausibility. A structured 11-check internal battery assigns explicit reporting labels, including screened, conditional, exploratory, rejected, and unstable.
Deep research & assessment:
Mechanism, Novelty, and Strategy agents evaluate biological plausibility, prior literature, and potential translational relevance without treating an association as causal evidence.
Report writing & assembly:
Report agents verify numerical claims against the fact sheet and compile the analyses, figures, literature, and limitations into a draft for expert review.
For example, given a request to prioritize wearable candidates associated with depression severity, Biomarker Discovery Framework profiled the
DWB
dataset, proposed sleep-timing variability features, and estimated an association between sleep-duration variability and
PHQ-8
severity (ρ = 0.252). The workflow then checked stability, leakage, subgroup consistency, and alternative explanations before framing the result as a literature-grounded circadian-instability hypothesis for human review.
[A flowchart detailing a multi-agent AI system for automated biomarker discovery, validation, and report generation.]
Biomarker Discovery Framework Architecture. Specialized sub-agents (Scout, Critic, Defender, Mechanism) operate over a shared state. Biomarker Discovery Framework enforces safety mechanisms to ensure statistical validity, separating feature construction from target signals and requiring candidates to pass an 11-test adversarial filtering stage.
Results: Prioritizing candidate associations across domains
To assess the Biomarker Discovery Framework's capability to extract plausible physiological insights from noisy data, we applied it independently across three large-scale cohorts totaling 9,279 participant-observations, spanning both mental health (
DWB
and
GLOBEM
) and metabolic disease (
WEAR-ME
) domains. The pipeline autonomously identified 41 candidate digital biomarkers for mental health and 25 for metabolic outcomes.
The table below shows a curated sample of candidate associations.
Spearman’s ρ
summarizes the direction and strength of an association. The 95% confidence interval quantifies uncertainty, and the adjusted p-value accounts for multiple comparisons. The mechanism presents a literature-grounded hypothesis rather than a causal conclusion. Importantly, the final column describes the strength of prior evidence — not clinical validation in this study — and the stars denote evidence-tier markers rather than statistical-significance codes.
The Biomarker Discovery Framework did not simply select existing variables; it constructed novel composite features. For instance, in the mental health domain, it identified sleep duration variability and sleep onset variability as top correlates of depression severity. In the metabolic domain, it derived a cardiovascular fitness index (steps divided by resting heart rate) as a non-invasive correlate of insulin resistance, linking it to prior work on glucose regulation and cardiometabolic fitness.
[A data table presenting biomarker candidates, effect sizes, adjusted p-values, and mechanistic hypotheses across three cohorts.]
Effect sizes and uncertainty come from deterministic analysis and mechanistic explanations are literature-grounded hypotheses.
Established
denotes substantial supporting prior literature,
Supported*
indicates the underlying physiological axis is established, but the digital operationalization is new,
Emerging**
means prior evidence is limited & needs held-out confirmation,
R
signifies candidates rejected by the construct-overlap gate.
†
marks wearable-derived features, and
Flagged unstable
identifies held-out estimate reversed direction.
Discovering clinical signals at scale
We deployed the Biomarker Discovery Framework across three distinct large-scale cohorts totaling 9,279 participant-observations, spanning both mental health and metabolic disease domains.
Across the two depression domains, Biomarker Discovery Framework prioritized different operationalizations of a related circadian-instability construct. In DWB, sleep-duration variability was associated with PHQ-8 severity (ρ = 0.252, p < 0.001). In GLOBEM, sleep-onset variability emerged as an exploratory, low-signal association with PHQ-4 (ρ = 0.126, p < 0.001; CV AUC = 0.535). Because the cohorts, endpoints, and feature definitions differ — and no identical candidate was replicated — this pattern should be interpreted as suggestive construct-level convergence, not direct replication.
[Two violin plots displaying sleep duration and onset variability across groups with increasing depression severity.]
Related circadian-instability candidates in two depression cohorts.
Variability increases across symptom-severity groups in both cohorts, but the findings are hypothesis-generating and do not constitute causal evidence or direct cross-cohort replication.
In total, the Biomarker Discovery Framework identified 41 candidate digital biomarkers for mental health and 25 for metabolic outcomes. While the effect sizes reflect the modest magnitudes typical of passive-sensing digital phenotyping, the integration of these Biomarker Discovery Framework-derived features alongside demographic variables improved predictive performance when combined with demographic features (ΔR² = 0.040 for depression, 0.021 for insulin resistance).
[A radar chart and table comparing a proposed AI agent's performance against baselines across multiple data science benchmarks.]
Overview of the Biomarker Discovery Framework.
Left:
The Biomarker Discovery Framework was additionally evaluated on data-science and health benchmarks, achieving competitive performance against per-benchmark strongest baselines.
Right:
In a blinded human expert evaluation, the Biomarker Discovery Framework received the highest mean scores across quality dimensions.
Evaluation by human domain experts
To assess manuscript quality, 15 experts in medicine, biomedical data science, machine learning, bioinformatics, and digital health reviewed blinded reports from the Biomarker Discovery Framework and three contemporary AI research systems (
Google DeepMind’s AI co-scientist
,
Biomni
, and
Google ADK’s Data Science Agent
). Biomarker Discovery Framework, Biomni, and the Data Science Agent were scored together in 21 sessions, and Biomarker Discovery Framework was scored in a separate 13-session set using the same evaluation instrument.
In the blinded evaluation, the Biomarker Discovery Framework received the highest mean scores across all seven quality dimensions. Under the study’s simulated editorial rubric, it was the only system to receive any “Accept” or “Minor Revision” recommendations: 2 Accept, 8 Minor Revision, 8 Major Revision, and 3 Reject. Reviewers estimated that they would retain 56.9% of Biomarker Discovery Framework-generated manuscript content on average, compared with 18.8%–30.4% for the baselines, and ranked the Biomarker Discovery Framework first in 9 of 13 four-system ranking sessions.
[Four charts evaluating various AI agents on report quality, acceptance rates, human effort saved, and task ranking.]
Blinded Human Evaluation. (a) Biomarker Discovery Framework achieved the highest mean expert scores across all seven quality dimensions, excelling in Statistical Validity and Soundness. (b) Editorial decision distribution shows Biomarker Discovery Framework as the only system to receive non-rejection (Accept/Minor Revision) decisions from the expert panel.
Conclusion
As wearable health data continues to scale across populations, the bottleneck in digital medicine is no longer data collection, but rather principled, rigorous hypothesis generation. Scaling model capability alone does not address the problem of scientific rigor. However, when deployed within a meticulously structured architecture that separates deterministic computation from generative reasoning, and forces agents to defensively debate their findings, AI can support structured hypothesis generation, validation, and prioritization under human supervision. By shifting from black-box automation to transparent, human-in-the-loop workflows, we can build AI systems capable of safely accelerating the hypothesis-to-validation cycle in clinical research.
Acknowledgements
This blog post was written by Yubin Kim, Hamid Palangi, and Daniel McDuff from Google Research. This work was spearheaded by MIT PhD student Yubin Kim during a Google internship advised by Daniel McDuff and Hamid Palangi. We are grateful to our co-authors and collaborators from Google Research, Google DeepMind, and academia for their contributions to this work.
Labels:
Generative AI
Health & Bioscience
Quick links
Paper
Share
Copy link
×
Other posts of interest
[PhotoScanIR_Overview]
August 17, 2026
Seeing beyond BMI: Estimating cardiometabolic risk with smartphone imagery
General Science
·
Health & Bioscience
·
Machine Intelligence
[Diagram illustrating five knowledge retrieval states in language models, ranging from encoding failure to direct recall.]
August 12, 2026
Empty shelves or lost keys? Recall is the bottleneck for parametric factuality
Generative AI
·
Natural Language Processing
[AMIE (Video)-hero]
August 11, 2026
Advancing AMIE towards expert-level audio-visual clinical consultations
Health & Bioscience
·
Machine Intelligence
×
❮
❯
[Biomarker-Discovery-Framework-6]
Four charts evaluating various AI agents on report quality, acceptance rates, human effort saved, and task ranking.
[Biomarker-Discovery-Framework-3]
A data table presenting biomarker candidates, effect sizes, adjusted p-values, and mechanistic hypotheses across three cohorts.
[Biomarker-Discovery-Framework-1]
A conceptual diagram illustrating a cyclical AI-driven biomarker discovery process analyzing wearable and clinical data.
[Biomarker-Discovery-Framework-4]
Two violin plots displaying sleep duration and onset variability across groups with increasing depression severity.
[Biomarker-Discovery-Framework-5]
A radar chart and table comparing a proposed AI agent's performance against baselines across multiple data science benchmarks.
[Biomarker-Discovery-Framework-2]
A flowchart detailing a multi-agent AI system for automated biomarker discovery, validation, and report generation.

## Metadata
- **Source**: [Original Article](https://research.google/blog/an-ai-tool-for-prioritizing-candidate-biomarkers-from-wearable-sensor-data/)
