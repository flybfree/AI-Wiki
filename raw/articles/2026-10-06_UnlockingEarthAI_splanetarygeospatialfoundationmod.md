---
title: Unlocking Earth AI’s planetary geospatial foundation models for global public health
date: 2026-10-06
url: https://research.google/blog/earth-ais-planetary-geospatial-foundation-models-for-global-public-health/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/earth-ais-planetary-geospatial-foundation-models-for-global-public-health/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-10-06 10:08
---

# Unlocking Earth AI’s planetary geospatial foundation models for global public health

## Full Article

[Three aerial cityscape panels featuring public health dashboard cards: MMR coverage, Dengue cases forecast, and Cholera emergence zones.]
Unlocking Earth AI’s planetary geospatial foundation models for global public health
October 6, 2026
Arbaaz Muslim, Software Engineer, Google Research, and Gautam Prasad, Software Engineer, Google Research
With Google Earth AI’s Population Dynamics Foundation Model (PDFM), we can address the data gaps and temporal reporting lags of existing epidemiological workflows. In our latest work, we present five partner-driven case studies demonstrating how this model exemplifies the planetary geospatial foundation model paradigm for global public health.
Quick links
Paper
News from Google blog
Share
Copy link
×
Public health decisions rely heavily on timely, granular data. For health conditions, such as cardiovascular disease or postpartum depression, that data shows us where to focus resources and support. For acute disease outbreaks, such as dengue or cholera, it can help inform urgent operational protocols and resource allocation. However, conventional
epidemiological surveillance is often hindered by limitations
in data: multi-year reporting lags, data siloed by rigid geopolitical boundaries, and data sparsity. Even without these limitations, traditional modeling approaches require extensive task-specific data collection and custom data engineering pipelines that are difficult to deploy during rapid outbreaks or in resource-constrained settings.
To address these systemic bottlenecks, we
introduce
a
new paradigm
in public health leveraging planetary geospatial foundation models. Using
Google Earth AI’
s
Population Dynamics Foundation Model
(PDFM) as a proof-of-concept, we demonstrate how self-supervised, pre-trained representations of "place" can be integrated directly into existing health sciences and epidemiological workflows as plug-and-play inputs — enhancing the statistical and machine learning (ML) models epidemiologists already use, rather than building new pipelines from scratch. PDFM compresses privacy-preserving search trends, human mobility, built-environment density, and environmental determinants into location embeddings. Without requiring task-specific fine-tuning, these off-the-shelf location embeddings matched or improved on conventional inputs across a wide variety of disease domains, geographic settings, and epidemiological tasks.
What is PDFM?
Part of Google Earth AI — our suite of geospatial models connecting satellite imagery, weather, anonymous search trends, human mobility, and other population dynamics — PDFM uses self-supervised learning to synthesize the following diverse, privacy-preserving signals into compact, versatile embeddings that serve as “fingerprints” for locations refreshed at a monthly cadence:
Aggregated search trends
: Search frequencies of topics and resources that have garnered community-level interest
Built environment and mobility
: Local density and busyness of places such as pharmacies, clinics, and parks.
Environmental determinants
: High-resolution weather and air quality metrics and statistics.
Rather than requiring researchers to collect and process these raw data streams themselves, PDFM embeddings can be easily plugged into existing ML workflows to provide ready-to-use geospatial context.
Prior work
showed that these embeddings are task-agnostic. Because these everyday signals capture the underlying social, behavioral, and environmental determinants of health, the same embeddings showed strong performance on filling gaps in
a wide variety of CDC health metrics
.
However, establishing a new paradigm for global health carries a higher burden of proof. To meet this standard, we set out to demonstrate the value of PDFM embeddings across a wider variety of health challenges, and in different environments across the globe.
[Flowchart showing how Google Earth AI uses multimodal data to generate population embeddings for public health tasks.]
Overview of Google Earth AI’s PDFM applied to a wide range of global health challenges.
Validation matrix at a glance
To achieve this, our global health research partners facilitated independent evaluations across five distinct public health challenges — spanning diverse epidemiological tasks, resource settings, and disease types:
Case study & domain
Partner institution
Epidemiological task
Geographic scope
Key impact & quantitative results
MMR vaccination
(immunization)
Mount Sinai Health System
; Boston Children’s Hospital
Cross-border extrapolation
US–Canada Border
(146 border counties)
+36% relative gain in explained variance (0.159
0.216, statistically significant) by capturing cross-border mobility and information spillovers.
Cardiovascular disease
(noncommunicable disease)
Department of Population Health, NYU Grossman School of Medicine
Mortality nowcasting & interpolation
Contiguous United States
(3,091 counties)
Comparable accuracy to census-based models for nowcasting (mean absolute error 18.7 vs 19.1 deaths per county; RMSE 46.00 vs 57.69; differences not statistically significant), making PDFM a timely stand-in when census data are outdated or unavailable.
Dengue outbreaks
(vector-borne disease)
University of Oxford and
Tecnológico de Monterrey
Short-horizon probabilistic forecasting
Mexico
(~2,450 municipalities)
Statistically significant 1-month forecast gain (
Δ
Weighted Interval Score = -0.0051, lower is better) via TimesFM integration, concentrated in active transmission hotspots. Accuracy improved in up to 72% of active transmission municipalities.
Postpartum depression
(mental health)
Institute on Human Development and Disability, University of Washington
Individual risk prediction
United States (CDC PRAMS)
(332,970 respondents)
Transferable gain in risk prediction (AUC +0.0020 on a 0.62 baseline in seen states; +0.0038 in unseen states). Encoded area poverty (R² = 0.45). Recovers about 15% of the predictive signal of income and insurance records.
Cholera emergence (
water-borne disease
)
WHO AFRO
Outbreak onset prediction
Democratic Republic of the Congo
(403 health zones, 89 weeks)
Statistically significant relative gains: +9.7% in Area Under the Precision-Recall Curve at 4 weeks; +18.1% Precision@5 (share of the model's five highest-risk zones each week that actually went on to have an outbreak) at 8 weeks, and +19.3% Precision@5 in endemic health zones.
Capturing cross-border dynamics in immunization
Our evaluations show that while epidemiological models are constrained by sovereign borders, the outcomes they track are not. For example, in the 146 U.S. counties situated within 150 km of the Canadian border, domestic-only models often struggle to predict local vaccine uptake.
By supplementing U.S. county embeddings with
Canadian Forward Sortation Area embeddings
, researchers at the
Mount Sinai Health System
and
Boston Children’s Hospital
developed models that captured cross-border behavioral and mobility spillovers. To help public health officials pinpoint communities at risk of measles outbreaks, the researchers used this added cross-border context to increase the share of variation in MMR vaccination coverage explained by the models from 16% to 22% (a 36% increase) and refine coverage estimates by at least 3 percentage points for 4.7 million border residents, revealing local patterns that domestic-only models may miss.
Reducing reporting lags in chronic disease surveillance
Cardiovascular disease (CVD)
claims over 916,000 lives annually in the U.S.
However, unsuppressed official county-level mortality data from the
National Vital Statistics System
(NVSS) typically lags by 1–2 years, and
American Community Survey
(ACS) covariates reflect conditions up to 2–3 years in the past. PDFM is available in more places and has much less of a lag, allowing for the ability to improve our capacity to model disease.
Our partners at
NYU Grossman School of Medicine
tested whether PDFM could stand in for these census-based inputs when estimating current-year CVD deaths across roughly 3,100 U.S. counties. They found no statistically significant differences between PDFM and traditional census data on nowcasting, with PDFM being much fresher and available in far more places:
Comparable to census data
: Models using PDFM predicted 2023 county-level CVD deaths about as accurately as models using ACS demographic and socioeconomic data (an average error of 18.7 vs. 19.1 deaths per county when nowcasting) while cutting large county outlier errors (
RMSE
) by 20% (57.7 → 46.0). The differences were not statistically significant, suggesting that PDFM can serve as a substitute for census inputs.
More timely and more widely available
: ACS covariates pool five years of survey data and are released up to a year after collection. The PDFM embeddings used in this study were built from a single month of data. PDFM is also available in 17 countries, while ACS covers only the U.S.
These results suggest that PDFM can enable health departments to guide prevention resources using current conditions rather than waiting on multi-year survey cycles.
Sharpening forecasts of active outbreak hotspots
Time is especially of the essence when addressing outbreaks of vector-borne diseases like dengue. In partnership with public health researchers at the
University of Oxford
and
Tecnológico de Monterrey
, we coupled PDFM with
TimesFM 2.0
(our open time-series foundation model) to forecast dengue case counts across ~2,450 Mexican municipalities between 2020 and 2025.
The model’s greatest performance gains occurred when predicting one month ahead, improving forecast accuracy in up to 72% of active dengue transmission municipalities, yielding total error reductions 3.4X larger than degradations. This performance occurred precisely where timely vector control and clinical staffing decisions matter most, especially considering the
demonstrated utility
of short term forecasts.
Testing geographic boundaries in clinical screening
Screening for maternal mental health conditions like postpartum depression (PPD) typically relies on clinical intake information, which rarely captures the broader community conditions that shape a mother’s risk and access to care. To test whether geospatial foundation models can help bridge this gap, researchers at the
University of Washington
evaluated PDFM embeddings across 332,970 participants in the
CDC PRAMS
national survey.
In addition to PDFM capturing community-level socioeconomic conditions (R2=0.45), adding the embeddings provided a consistent, statistically significant boost to predicting which mothers were at risk (AUC +0.0020 in seen states; +0.0038 in unseen states). Crucially, this signal held up in states the model had never seen during training—acting as complementary local context that recovers about 15% of the predictive signal of a mother’s own income and insurance records when those details are unavailable.
This transferable context made the biggest difference in how screening resources are directed in new states. In simulations where a health system can follow up with the 20% highest-risk mothers, adding PDFM helped reach 5,640 more rural mothers with postpartum depression each year. Alternatively, in systems aiming to catch 80% of all cases, PDFM cut 17,723 false alarms annually—showing how geospatial embeddings can help health systems either broaden rural outreach or improve follow-up efficiency.
Extending lead times in prospective cholera emergence
Early warning for waterborne epidemics like cholera is critical for prepositioning oral cholera vaccines and clean water supplies. Fortunately, outbreaks are rare: in any given week, fewer than 1 in 100 of the country's 403 health zones sees one begin. Unfortunately, this very same rarity makes them hard to anticipate.
To address a use case defined by the
World Health Organization Regional Office for Africa
using national surveillance data from the Democratic Republic of the Congo’s Integrated Disease Surveillance and Response (IDSR) reporting, we tested whether a lightweight, low-resource version of PDFM (adapted for regions with sparse internet connectivity) could help forecast cholera hotspots.
The benefit depended on how far ahead we looked. One or two weeks out, recent case counts told most of the story and PDFM did not significantly enhance the accuracy. Four to eight weeks out, when there is still time to move supplies, it helped produce:
Sharper shortlists
: Response teams work from a short list of high-risk zones, so each week we checked how many of the model's top five picks went on to have an outbreak. Eight weeks ahead, PDFM raised this from 1.78 to 2.10 correct picks per week, an 18% improvement.
Bigger gains where cholera is endemic
: In the 15 zones that had reported cholera in at least half of all weeks, Precision@5 of eight-week shortlists improved from 0.3333 to 0.3975, a relative gain of 19%.
These findings demonstrate that while short-term tracking can rely on recent clinical data, foundation model embeddings capture underlying environmental, connectivity, and population determinants that supplement historical data, allowing for proactive planning one to two months in advance.
Looking ahead
Geospatial foundation models enable moving from reactive, localized modeling to proactive and time-sensitive health intelligence at planetary scale. Current limitations, such as static snapshots, are driving active research into temporally dynamic embeddings and geographic transfer learning for under-connected regions.
By integrating planetary contextual data into existing public health workflows, we can help take steps to improve how healthcare resources, interventions, and outbreak alerts reach the communities that need them most. Read the
paper
for more details.
PDFM embeddings are
commercially available
in Preview as
Population Dynamics Insights
, a geospatial embeddings dataset from Google Maps Platform. Academics and public health researchers can also
request
no-cost access for select, non-operational research use cases.
Labels:
Earth AI
Global
Health & Bioscience
Quick links
Paper
News from Google blog
Share
Copy link
×
Other posts of interest
[A colorful, high-resolution 3D rendering mapping the neurons of a fruit fly's brain and nerve cord.]
September 3, 2026
A connectomics milestone: Mapping the complete male fruit fly brain
General Science
·
Health & Bioscience
·
Machine Intelligence
·
Open Source Models & Datasets
[MAPL-EMIT-overview-hero]
September 1, 2026
Mapping global methane emissions from space with deep learning
Climate & Sustainability
·
Earth AI
·
Machine Intelligence
[Flowchart detailing the four stages of the Planetary Prediction Engine from data selection to final report generation.]
August 27, 2026
Planetary prediction engine: Automating global models via Earth AI
Earth AI
·
Generative AI
·
Machine Intelligence
×
❮
❯
[PDFMPublicHealth1-Overview]
Flowchart showing how Google Earth AI uses multimodal data to generate population embeddings for public health tasks.

## Metadata
- **Source**: [Original Article](https://research.google/blog/earth-ais-planetary-geospatial-foundation-models-for-global-public-health/)
