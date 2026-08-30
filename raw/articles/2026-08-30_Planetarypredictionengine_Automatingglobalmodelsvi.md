---
title: Planetary prediction engine: Automating global models via Earth AI
date: 2026-08-30
url: https://research.google/blog/planetary-prediction-engine-automating-global-models-via-earth-ai/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/planetary-prediction-engine-automating-global-models-via-earth-ai/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-08-30 00:13
---

# Planetary prediction engine: Automating global models via Earth AI

## Full Article

[Flowchart detailing the four stages of the Planetary Prediction Engine from data selection to final report generation.]
Planetary prediction engine: Automating global models via Earth AI
August 27, 2026
Rama Pasumarthi, Staff Software Engineer, and Shravya Shetty, Distinguished Engineer, Google Research
As part of
Google Earth AI
, we introduce the planetary prediction engine (PPE), an experimental research capability that autonomously executes the full geospatial modeling workflow — from data discovery to model training — achieving improvements across diverse prediction tasks in public health, food security, environmental risk, and socioeconomics.
Quick links
Paper
Share
Copy link
×
Addressing humanity's most pressing global challenges — from forecasting regional food security and environmental disaster risks to tracking real-time disease outbreaks and mapping socio-economic vulnerability — requires high-fidelity geospatial modeling. However, building these models is hindered by a fragmented data ecosystem that requires specialized teams to spend weeks on manual data curation, feature engineering, and specialized spatial validation. While existing
AutoML
and LLM-based agents effectively automate standard machine learning pipelines, they rely on pre-curated tabular data and lack the specialized capabilities needed to autonomously handle geospatial workflows. Consequently, planetary-scale analytics remains a significant bottleneck, a limitation that is especially severe when rapid response is critical during humanitarian crises.
Today we introduce the
planetary prediction engine
(PPE), the latest experimental research capability within our broader
Google Earth AI
initiative that turns planetary information into actionable insights. Previously, we demonstrated Earth AI’s
reasoning capabilities
in intelligently bringing together diverse geospatial assets. As an autonomous AI system, PPE executes the full geospatial prediction workflow, from planetary-scale data discovery and cleanup to training and evaluation, directly from natural-language queries. Given a geospatial predictive query, PPE will autonomously retrieve relevant data, engineer features, train and evaluate predictive models, and generate a comprehensive report. We demonstrate that by delivering improvements over diverse benchmarks without manual intervention, PPE effectively reduces the time needed to build complex planetary prediction models from weeks that include manual data engineering to mere minutes that result in autonomous insight.
How the planetary prediction engine works
The PPE decomposes the predictive workflow into three modular stages, each orchestrated by an LLM:
Stage 1: Intelligent geospatial data selection.
Given a natural-language query, the PPE translates the prompt into strict geographic constraints (spatial granularity, join-keys, temporal scope). It then conducts grounded signal discovery, formulating domain hypotheses and identifying both direct and causal proxy signals validated against published literature. PPE systematically retrieves covariates from established geospatial repositories including
Data Commons
and
Google Earth Engine
. For signals not available in established repositories, the system performs live open-web discovery, searching government portals and academic repositories at inference time.
Stage 2: Multimodal dataset curation.
The assembled covariates are fused with pre-trained geospatial foundation model embeddings,
Population Dynamics Foundation Models
(PDFM) for socio-demographic latent states and
AlphaEarth
for satellite imagery semantics. The system implements a strict “Feature Gate” that enforces automated target leakage mitigation, evaluating every candidate covariate against four anti-leakage criteria (filtering out mathematical sub-components, shared survey data, downstream causal effects, and future temporal data) to ensure the integrity of downstream evaluations.
Stage 3: Automated model building and prediction.
Here, PPE shifts from data curation to model optimization and evaluation. The system searches over multiple model families such as regularized linear models,
gradient-boosted decision trees
(GBDT), and
multi-layer perceptrons
, with custom logic to prevent overfitting (Overfitting Guard Protocol) that pre-assesses dataset risk and implements a self-correction loop to detect and recover from generalization failures.
Critically, each stage operates independently on well-defined inputs and outputs to prevent data bottlenecks. Data artifacts are passed between stages via opaque handles rather than serialized into LLM prompts, avoiding context-window limitations.
[Animation detailing the four stages of the Planetary Prediction Engine from data selection to final report generation.]
The PPE’s end-to-end workflow. The system decomposes the predictive workflow into three modular stages: (1) Intelligent data selection, (2) dataset curation, and (3) AutoML & prediction to produce the final predictions and report. Off-the-shelf LLMs serve as orchestrators within each stage.
Improvements over diverse benchmarks across tasks
We evaluated the PPE across a multidimensional matrix of machine learning paradigms, geographies, and scientific domains.
Spatial regression: US public health and environment
Across 21
CDC health indicators
, the PPE’s intelligent data selection and multimodal fusion achieve a mean
R²
of 76.8% vs 60.0%, compared to a manual expert pipeline. We observe similar gains for predicting
FEMA national risk indicators
(mean R² of 64.9% vs. 60.0% baseline) and
Social Vulnerability Index
(mean R² of 66.2% vs. 58.6% baseline).
Super-resolution downscaling: Nigeria food security
In data-scarce regions, coarse regional reporting often obscures local vulnerability. By autonomously integrating localized market shocks, food price anomalies, and microclimate indicators, PPE doubles baseline accuracy when downscaling food security from the provincial state (ADM1) level to the
local government area
(ADM2) level (R² 66.1% vs. 31.5%), providing humanitarian organizations with actionable, high-fidelity vulnerability maps.
[Side-by-side maps of Nigeria comparing ground truth and predicted Food Consumption Group prevalence for December 2025.]
Super-resolution food security downscaling in Nigeria (ADM1 State Level → ADM2 LGA Level).
Epidemiological nowcasting: DRC Ebola outbreak
For real-time prediction of new disease transmission hotspots during the
2026 Bundibugyo ebolavirus outbreak
in the Democratic Republic of the Congo, the PPE achieves a
Recall@10
of 83.3%, correctly identifying 15 of 18 newly invaded health zones across five sequential weekly forecasts. This represents a +10.3 percentage point absolute improvement over the published state-of-the-art
Bayesian modeling baseline
(~73%), driven by fusing epidemiological signals with PDFM embeddings and PPE-selected geospatial covariates.
The power of multimodal fusion with intelligent data selection
A key finding across all experiments is the synergistic value of combining structured statistical covariates with latent foundation model embeddings. Neither modality alone captures the full picture: statistical covariates provide explicit, interpretable signals, while
Population Dynamics Embeddings
and
AlphaEarth Foundations embeddings
encode complex non-linear patterns learned from large pre-training datasets. Our ablation studies consistently show that multimodal fusion along with intelligent data selection outperforms baseline approaches, confirming that these representations are complementary rather than redundant. In future work, we want to expand these capabilities to include more geospatial data sources, and foundation model embeddings such as
Remote Sensing Foundations multimodal embeddings
.
[Bar chart showing the Planetary Prediction Engine outperforming baseline approaches across five spatial tasks.]
Improvements from PPE’s multimodal fusion and intelligent data selection over baseline approaches.
Conclusion
The PPE demonstrates that autonomous AI systems can match or improve performance across a wide range of geospatial prediction tasks: from estimating chronic disease prevalence in the United States, to improving resolution of food insecurity in Nigeria and nowcasting active viral outbreaks in the Democratic Republic of the Congo. By combining intelligent data discovery, multimodal foundation model fusion, and automated model optimization, the PPE lowers the technical barrier to planetary-scale analytics, enabling rapid deployment when time-sensitive decisions are critical.
We believe this experimental research represents a meaningful step toward democratizing geospatial prediction. By shifting the focus from manual data engineering to high-level hypothesis direction, the planetary prediction engine helps researchers, humanitarian organizations, and policymakers build models without needing specialized engineering teams. While PPE is an early-stage research project, we’re excited to explore more use cases and see how this approach can help organizations better anticipate and solve complex global challenges.
Acknowledgements
We thank and acknowledge the contributions from all of the co-authors of the paper. We are grateful to the
UN World Food Programme
(WFP) and Vulnerability Analysis and Mapping (VAM) team for the data and research support. We also thank the
Institut National de Recherche Biomédicale
(INRB) for their collaboration on the DRC Ebola nowcasting, and the teams behind Data Commons, Google Earth Engine, Population Dynamics Foundation Models, and AlphaEarth for providing the foundational data and model infrastructure that power the PPE.
Labels:
Earth AI
Generative AI
Machine Intelligence
Quick links
Paper
Share
Copy link
×
Other posts of interest
[Overview diagram of the GlucoFM framework detailing data preprocessing, JEPA-style pre-training architecture, and clinical forecasting applications.]
August 26, 2026
GlucoFM: Foundation model for continuous glucose monitoring
Health & Bioscience
·
Machine Intelligence
[Workflow diagram of AgentHands system generating annotated text, gesture events, and timestamped speech from a user's question and gaze.]
August 25, 2026
AgentHands: Generating interactive hand gestures for spatially grounded agent conversations in XR
Human-Computer Interaction and Visualization
·
Machine Intelligence
[A conceptual diagram illustrating a cyclical AI-driven biomarker discovery process analyzing wearable and clinical data.]
August 21, 2026
An AI tool for prioritizing candidate biomarkers from wearable sensor data
Generative AI
·
Health & Bioscience
×
❮
❯
[PlanetaryPredictionEngine3_Results]
Bar chart showing the Planetary Prediction Engine outperforming baseline approaches across five spatial tasks.
[PlanetaryPredictionEngine2_NigeriaFoodSecurity]
Side-by-side maps of Nigeria comparing ground truth and predicted Food Consumption Group prevalence for December 2025.
[PlanetaryPredictionEngine1_Workflow]
Animation detailing the four stages of the Planetary Prediction Engine from data selection to final report generation.

## Metadata
- **Source**: [Original Article](https://research.google/blog/planetary-prediction-engine-automating-global-models-via-earth-ai/)
