---
title: Transfer learning for genomic prediction in underrepresented populations
date: 2026-09-05
url: https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-05 00:10
---

# Transfer learning for genomic prediction in underrepresented populations

## Full Article

[Three heatmaps showing prediction accuracies for unique genetic traits across varying UKB and BBJ sample sizes.]
Transfer learning for genomic prediction in underrepresented populations
September 3, 2026
Joey Poomarin Phloyphisut, Software Engineer, and Cory McLean, Senior Staff Software Engineer, Google Research
We evaluate ways to improve cross-population genetic risk prediction and find that while transfer learning from European cohorts improves prediction in small underrepresented populations, it degrades accuracy once target cohort sample sizes grow, especially for traits with population-specific genetic architectures.
Quick links
Share
Copy link
×
Polygenic risk scores
(PRSs) are used to predict disease risk from genetic variants. They usually incorporate the influence of hundreds to millions of genetic variants. However, their adoption for clinical decision making is currently low, partly because historical
genome-wide association studies
(GWASs) have
overwhelmingly evaluated European cohorts
, resulting in severe accuracy drops when applied to non-European populations. These accuracy differences arise because of cross-population differences in genetic architectures, population structure, and
variant allele frequencies
.
Moreover, conducting
de novo
GWASs across hundreds of thousands of individuals is cost-prohibitive for most healthcare systems. Transfer learning from existing European-centric GWAS, augmenting these large-scale results with target-population-specific GWAS, provides a potential solution.
To that end, in this blog post we describe a study evaluating PRS performance in a target non-European population while varying the size of both the target population and European populations used to create the predictive model across eight clinical traits. Specifically, we evaluate transferability of PRS ascertained in hundreds of thousands of European individuals within the
UK Biobank
(UKB) to samples within
Biobank Japan
(BBJ), a deeply-phenotyped cohort of nearly 200 thousand Japanese individuals. Our primary objective is to provide systematic, empirical guidelines on how cross-population GWAS and PRS model training should be performed to optimize predictive performance in a target population.
Effects of GWAS population size on target ancestry PRS performance
The presence of two large-scale, deeply genotyped and phenotyped datasets (UKB and BBJ) enables dataset ablation experiments to systematically evaluate PRS performance as a function of sample size. We selected eight clinically relevant traits measured in both populations for evaluation: body mass index (BMI), systolic blood pressure, diastolic blood pressure, red blood cell count, white blood cell count, high-density lipoprotein cholesterol (HDL), low-density lipoprotein cholesterol (LDL), and blood glucose. In UKB, the estimated fraction of trait variance explained by the measured genetic variants (single nucleotide polymorphism
heritability
) ranged from 0.07–0.28.
Three methods were used to evaluate the PRS performance transferability:
UKB - Discovery GWAS +
elastic net
:
Explores the direct variants transferability between European and Japanese populations. For each trait, we first identified European-specific genetic associations by running GWAS on the full UKB European population, filtering the results for independent variants also present in the BBJ Japanese dataset. Using these variants as inputs, we computed target-population PRSs by training elastic net models on various combinations of BBJ and UKB samples. Specifically, we paired 12–13 BBJ sample sizes with seven UKB sample sizes. This produced 96–104 PRS models per trait.
Meta-analysis
+ elastic net:
Explores the impact of mixing Japanese population data during variant discovery. First, we ran GWAS on the full UKB European population and a sampled BBJ Japanese dataset. We then combined these genetic associations using meta-analysis to generate the final variant set. Using these variants, we trained elastic net models on a mixed UKB / BBJ dataset to determine target population PRSs.
PRS-CSx
:
Explores a
PRS-CSx
model designed to handle
linkage disequilibrium
diversity between populations. We applied PRS-CSx on full UKB European samples and sampled BBJ Japanese samples for each trait. Since PRS-CSx models provide two different scores for each population from one sample, we also split the validation set to find optimal linear combinations between two scores.
In all experiments, the PRS models were evaluated on the same held-out set of BBJ samples.
[A flowchart outlining three genomic prediction models—ElasticNet, Meta-Analysis, and PRS-CSx—using BBJ and UKB datasets.]
Experiment design for cross-ancestry genomic prediction. a)
The main experiments explore the impact of different numbers of European and Japanese samples on elastic net performance when applied to variants discovered through a large-scale European GWAS.
b)
Meta-analysis experiments integrate population-specific GWAS results into the generation of variants used for elastic net model development.
c)
PRS-CSx experiments fit the PRS-CSx model on a variety of population-specific sample sizes.
[A table listing sample sizes across UKB and BBJ datasets for eight physical and hematological traits.]
Sample sizes in UKB and BBJ for the eight traits explored in this study.
More data is not always better for cross-population PRS prediction
For each experiment, we quantified model performance using
Pearson correlation
. As expected, European discovery data provides a helpful baseline when target population data is limited or non-existent. However, the target-population-specific models outperform at sample sizes of 15k or more, as it appears that co-training with external European data limits the target population accuracy gains achieved through higher sampling.
[A line graph showing HDL prediction correlation improving and crossing over as BBJ and UKB sample sizes increase.]
PRS performance for HDL cholesterol in BBJ samples as a function of BBJ and UKB sample sizes: This titration curve demonstrates how incorporating out-of-sample data can actually degrade predictive performance in a target population. Beyond the crossover point at 15,000 BBJ samples, the inclusion of more than 5k UKB samples reduces prediction performance compared to training solely on target-population data.
This surprising observation held across all phenotypes we examined. When the target sample size is extremely small (e.g., 5,000 samples), pooling European UKB data during training provides a valuable statistical boost. As the target sample size used to train the PRS model increases, the benefit of out-of-population pooling diminishes.
While the trend holds across phenotypes, the crossover point at which the success of using European data diminishes depends heavily on the specific trait being studied. We can quantify the extent of “shared genetics” using genetic correlation of the same trait across populations. We observe that “conserved” traits, or those with higher genetic correlations between the two populations, retain the benefits of pooling UKB European training data up to much larger target sample sizes (25-40k+ samples) before target-population-specific training data reaches parity.
[Five heatmaps showing prediction accuracies for shared genetic traits across varying UKB and BBJ sample sizes.]
PRS
performance in BBJ samples as a function of BBJ and UKB sample sizes for traits with shared genetic architectures across populations: As the BBJ sample size grows past 40k, the optimal UKB sample size decreases from maximum.
In sharp contrast, lipid levels (HDL, LDL) and blood glucose exhibit much smaller BBJ sample sizes beyond which optimal UKB sample sizes are smaller than maximum, and that optimal sample size is also smaller. These highly population-specific traits do not benefit as much from UKB data, since that data is farther out-of-distribution.
[Three heatmaps showing prediction accuracies for unique genetic traits across varying UKB and BBJ sample sizes.]
PRS performance in BBJ samples as a function of BBJ and UKB sample sizes for traits with unique genetic architectures across populations: Unlike conserved traits, these more population-specific phenotypes exhibit early crossing points.
The impact of meta-analysis and PRS-CSx
The above experiments restricted PRS model input variants to those discovered in the UKB European population, excluding any trait-associated variants unique to BBJ samples. To extend the analyses to capture these, we created two additional prediction methods.
First, we ran GWAS on each BBJ sample size. The first new method performed a cross-population meta-analysis using the full UKB GWAS and the sample-size-specific BBJ GWAS to identify candidate variants, and then fit an elastic net on those variants. The second method used
PRS-CSx
to combine the two sets of GWAS summary statistics.
By tracking the net performance gain of meta-analysis and PRS-CSx across varying discovery sample sizes, we observed differences in performance across BBJ sample sizes.
The influence of meta-analysis is low for conserved traits, largely due to reduced statistical power in the much smaller BBJ GWAS sample sizes. However, for population-specific traits like HDL and LDL, and to a lesser extent blood glucose, meta-analysis substantially outperforms single-population discovery. The gains are primarily due to modifying the elastic net variant input: including UKB European samples during training slightly improved prediction when using 10,000 or fewer BBJ samples. This improvement was not seen with larger BBJ samples.
Because PRS-CSx dynamically weights population-specific models, its performance is theoretically less sensitive to conserved vs population-specific traits. However, we observed that the model requires more data than elastic net models to perform well. For target sample sizes under 25k, PRS-CSx performs worse than the strongest corresponding elastic net model in all phenotypes except BMI. As sample sizes approached 100k, PRS-CSx matched or exceeded the best performing model across all phenotypes except blood glucose.
[Eight line graphs comparing Pearson correlation for three predictive models across varying trait sample sizes.]
Relative performance of UKB discovery, meta-analysis, and PRS-CSx models as a function of BBJ sample size: The BBJ-specific GWAS results used by meta-analysis and PRS-CSx are identified in the subsampled BBJ dataset. The UKB GWAS results used by all models are based on the entire UKB European dataset.
Conclusion
Systematic evaluation of cross-population genomic prediction reveals that larger out-of-population datasets are not always beneficial when applying polygenic risk scores (PRSs) to underrepresented ancestries. Specifically, while transfer learning from the large European cohort of UK Biobank provided a statistical boost at low target population sizes (under 15,000 samples in Biobank Japan), it actually degraded predictive accuracy as the BBJ sample size grew. This performance crossover is trait-dependent: genetically conserved traits (such as BMI) retain the benefits of external data pooling up to larger sample sizes, whereas population-specific traits (such as lipids and blood glucose) show diminished benefits with fewer samples. Importantly, advanced multi-ancestry methods like PRS-CSx require substantial target-population samples to outperform simpler approaches, while cross-population meta-analysis offers robust benefits for population-specific traits at smaller sizes. Ultimately, these findings emphasize that optimizing predictive performance in diverse populations will require both the expansion of local, diverse biobanks and careful selection of modeling strategy that is tailored to both trait heritability and sample size.
Acknowledgments
We sincerely thank
Biobank Japan
and our collaborators at
RIKEN
and
The Institute of Medical Science
The University of Tokyo
for enabling this research, as well as additional Google collaborators: Babak Behsaz, Andrew Carroll, Farhad Hormozdiari, and Taedong Yun. Our thanks also go to Hiroki Kayama and Joe Ledsam for institutional support, and Michael Brenner and Katherine Chou for their leadership support.
Labels:
General Science
Machine Intelligence
Quick links
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
[TimesFM-3 architecture diagram illustrating time series patching, transformer layers, and multivariate forecast output.]
August 31, 2026
TimesFM-3: A zero-shot foundation model for multivariate forecasting
Data Management
·
Machine Intelligence
·
Product
×
❮
❯
[BBJ_GenomicPrediction1-ExperimentalDesign]
A flowchart outlining three genomic prediction models—ElasticNet, Meta-Analysis, and PRS-CSx—using BBJ and UKB datasets.
[BBJ_GenomicPrediction6-UKBDiscovery]
Eight line graphs comparing Pearson correlation for three predictive models across varying trait sample sizes.
[BBJ_GenomicPrediction5-SharedGeneticTraits]
Five heatmaps showing prediction accuracies for shared genetic traits across varying UKB and BBJ sample sizes.
[BBJ_GenomicPrediction6-UniqueGeneticTraits]
Three heatmaps showing prediction accuracies for unique genetic traits across varying UKB and BBJ sample sizes.
[BBJ_GenomicPrediction2-Samples]
A table listing sample sizes across UKB and BBJ datasets for eight physical and hematological traits.
[BBJ_GenomicPrediction3-PRS4HDL]
A line graph showing HDL prediction correlation improving and crossing over as BBJ and UKB sample sizes increase.

## Metadata
- **Source**: [Original Article](https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/)
