---
title: Detecting signs of hypertension using wearable sensors
date: 2026-11-05
url: https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-11-05 21:44
---

# Detecting signs of hypertension using wearable sensors

## Full Article

[Diagram of a machine learning workflow using wearable PPG and accelerometer data to predict a hypertension score.]
Detecting signs of hypertension using wearable sensors
November 5, 2026
Paolo Di Achille, Staff Research Scientist, and Ming-Zher Poh, Senior Staff Research Scientist, Google Research
We present a new AI system that leverages standard consumer smartwatch sensors to passively detect signs of high blood pressure.
Quick links
Nature paper
Share
Copy link
×
Hypertension
(i.e., high blood pressure), often called the "silent killer”, affects over one billion people globally, yet more than half of adults with the condition are
unaware they have it
. Because it rarely presents with obvious symptoms, high blood pressure (BP) is typically discovered only through incidental screening. This gap in awareness is particularly severe among
younger adults aged 18 to 44
, where missing diagnoses can delay life-saving early interventions and significantly increase the long-term risk of adverse cardiovascular events like stroke or heart failure.
Office BP measurement serves as the primary
initial screening gateway
for detecting hypertension. In recent years, cuffless wearable devices have emerged as a potential tool to complement episodic office care. However, existing commercial solutions usually require regular calibration using a traditional arm cuff. This means they only track relative changes from a baseline cuff reading rather than identifying absolute hypertensive states, limiting their utility as independent screening tools.
In a
new study
published in
Nature
, we present a multimodal artificial intelligence (AI) system capable of passively detecting signs of hypertension using a consumer smartwatch, without requiring any cuff calibration. Dubbed
AI-PPG-ACC-HTN
, we validated this system against the clinical gold standard of 24-hour ambulatory blood pressure monitoring (ABPM), and it achieves accuracy levels comparable to traditional cuff-based diagnostic workflows for both initial and confirmatory screening. These research findings helped inform the blood pressure trends Health Guardian feature in the Google Health app.
How it works
Instead of attempting to estimate exact, point-in-time systolic and diastolic blood pressure values, which are highly susceptible to transient environmental noise, our system reframes the problem. It focuses on identifying an individual’s underlying, persistent hypertensive state by aggregating passive physiological signatures over multiple days.
The system leverages data from two sensors already active on modern smartwatches:
Photoplethysmography (PPG):
An optical sensor that tracks changes in blood volume at the wrist by measuring reflected light that captures pulse wave contours.
Accelerometry (ACC):
A motion sensor that identifies periods of stillness and captures the
ballistocardiogram (BCG)
, the subtle physical vibrations of the wrist caused by the mechanical ejection of blood from the heart into the aorta.
[Diagram of a machine learning workflow using wearable PPG and accelerometer data to predict a hypertension score.]
The AI system uses photoplethysmography (PPG) and accelerometer (ACC) signals recorded using a consumer smartwatch to create waveform embeddings. The waveform embeddings are aggregated over time (days) into a person-level embedding, which, along with a user’s height, are used to predict their blood pressure status.
To build this system, we used a two-stage machine learning approach:
Stage 1: Self-supervised pre-training (the waveform encoder)
We trained a 1-D deep convolutional neural network using self-supervised contrastive learning. By analyzing a large, unlabeled dataset of 492,347 hours of sensor data from 2,109 consenting participants, the model learned to map overlapping 15-second PPG and ACC waveforms from the same individual close together in a latent space. This allowed the model to discover complex, physiologically rich features of vascular and mechanical cardiac function without requiring manual feature engineering or medical labels.
Stage 2. Person-level aggregation & classification
For each user, these 15-second feature blocks (embeddings) are mean-aggregated across multiple days of wear to wash out ephemeral noise like sudden movements or temperature changes. Finally, the individual's aggregated embedding is combined with their height (which serves as a reliable proxy for arterial path length) and fed into a regularized logistic regression classifier to calculate a continuous hypertension probability score.
Rigorous validation against the clinical gold standard
To evaluate our system, we conducted a prospective, multi-center clinical study across five US sites involving 196 consenting diverse participants who were free from known cardiovascular disease and not taking blood pressure medications.
Importantly, we benchmarked the smartwatch's performance against 24-hour ambulatory blood pressure monitoring (ABPM), the clinical gold standard for hypertension diagnosis. We evaluated the smartwatch system across two clinical use case scenarios: initial screening and confirmatory testing.
Scenario 1: Initial screening
The smartwatch achieved a moderate sensitivity of 65.8% and a high specificity of 90.0%, resulting in a high positive predictive value (PPV) of 80.6%. In comparison, initial office-based screenings showed a sensitivity of 55.3% and a moderate PPV of 77.8% when benchmarked against the gold standard.
[Bar charts comparing sensitivity, specificity, PPV, and NPV across Demographics, Office BPM, and AI-PPG-ACC-HTN models.]
Scenario 2: Confirmatory testing
For individuals who initially screen positive for high blood pressure in a clinic, current guidelines recommend confirmatory out-of-office tracking. We looked at the subset of participants (N=48) who had elevated initial office BP to see how well the smartwatch could confirm sustained hypertension.
Our multimodal system achieved a moderate sensitivity of 78.4%, a high specificity of 90.9% and a high PPV of 96.7%. In comparison, the performance of return office BP measurements showed lower point estimates of sensitivity (67.6%), specificity (63.6%), and PPV (86.2%). Furthermore, the smartwatch approach proved competitive with multi-day home monitoring, which yielded a sensitivity of 89.2%, specificity of 81.8%, and a PPV of 94.3%.
[Bar charts comparing hypertension detection methods show AI-PPG-ACC-HTN achieves the highest specificity (90.9%) and PPV (96.7%).]
Taken together, the results show that our system can detect hypertension with accuracy levels comparable to traditional cuffed BP devices in the existing clinical framework.
Model interpretability
To gain an understanding of what the AI model may be paying attention to, we visualized the average pulse waveforms from users with the highest and lowest predicted probabilities of hypertension.
We observed the following visual differences:
Reduced pulse width:
Waveforms linked to a higher risk of hypertension exhibited a slightly narrower pulse width (figure below, top left panel), indicating a smaller change in blood volume, and may suggest stiffer arteries that are less able to expand.
Pulse wave reflection:
Higher AI risk scores correlated with a slower systolic upstroke (the initial surge of blood) (figure below, highlighted yellow circle in middle panel) and a lower
d/a
ratio (figure below, highlighted yellow circle in right panel). This specific metric compares the initial forward-traveling pulse wave to the reflected wave bouncing back from the body's vascular network.
Mechanical heart vibrations:
The smartwatch accelerometer successfully captured the ballistocardiogram (BCG) signal. In users with higher predicted hypertension, we observed distinct physical modulations in these micro-vibrations, specifically deeper "K waves" and wider "IJK complexes" (figure below, highlighted yellow circle in bottom left panel).
[Plots of pulse and acceleration waveforms and their derivatives, categorized by AI hypertension risk scores.]
Mean pulse waveforms (top left panel), corresponding accelerometer waveforms showing the ballistocardiogram (BCG, bottom left panel), first (middle panel) and second derivatives (right panel) of pulse waveforms from four of the most extreme quintiles of AI-PPG-ACC-HTN scores. Key fiducial points are indicated including the pulse onset (ons), peak (sys), dicrotic notch (dic), diastolic peak (dia) in the PPG waveform, H, I, J, K, L, M, N waves in the BCG waveform, and a, b, c, d, e waves in the second derivative of the PPG waveform.
Outlook
Smartwatch-based hypertension screening is not intended to replace standard clinical arm cuffs or provide a definitive standalone medical diagnosis. Instead, this research points to the potential for a highly scalable, passive tool for
opportunistic screening
. This work represents early feasibility research and methodologies described here are purely exploratory and are not indicative of any existing or upcoming commercial product feature or device capability. By gently prompting at-risk individuals to step into a clinic for formal assessment, this technology holds the potential to significantly close the global awareness gap and catch hypertension before it causes permanent cardiovascular damage.
Acknowledgements
This research was a collaborative effort between Google Research, Beth Israel Deaconess Medical Center, and Harvard Medical School. We thank our paper co-authors Lawrence Cai, Jiang Wu, Mingwu Gao, Bhavna Daryani, Jonathan Wang, Utkarsh Khanna, Ho Ko, Anupam Pathak, Mark Malhotra, Shwetak Patel, Jacqueline B. Shreibati, Stephen P. Juraschek, Pramod Rudrapatna, and Matthew Thompson. We thank key contributors including: Jennifer Block, Anu Gabbita, Sushalini Sunku, Keerthana Natarajan, Alexandros Pantelopoulos, Tuan Phan, Tracy Giest, and Florence Thng.
Labels:
Health & Bioscience
Machine Intelligence
Quick links
Nature paper
Share
Copy link
×
Other posts of interest
[Abstract artwork blending fluid watercolor washes on the left with geometric network nodes on the right, connected by a glowing central light.]
November 4, 2026
Agile Deliberation: How AI helps humans define the gray areas
Data Mining & Modeling
·
Generative AI
·
Human-Computer Interaction and Visualization
·
Machine Intelligence
[A flowing stream of glowing blue geometric shapes consolidates into a bright, interconnected neural network sphere.]
October 27, 2026
The sleep framework: A new way for LLMs to retain knowledge in continual learning
Education Innovation
·
General Science
·
Machine Intelligence
·
Natural Language Processing
[A Nexus AI software interface displaying a chest X-ray with three circled lung areas marked as "TB Suggestive" and "FIR".]
October 23, 2026
Bringing foundational models to the front lines of TB screening
Generative AI
·
Health & Bioscience
×
❮
❯
[Hypertension1_Overview]
Diagram of a machine learning workflow using wearable PPG and accelerometer data to predict a hypertension score.
[Hypertension_Results]
Bar charts comparing hypertension detection methods show AI-PPG-ACC-HTN achieves the highest specificity (90.9%) and PPV (96.7%).
[Hypertension2_Results]
Bar charts comparing sensitivity, specificity, PPV, and NPV across Demographics, Office BPM, and AI-PPG-ACC-HTN models.
[Hypertension3_Results2]
Plots of pulse and acceleration waveforms and their derivatives, categorized by AI hypertension risk scores.

## Metadata
- **Source**: [Original Article](https://research.google/blog/detecting-signs-of-hypertension-using-wearable-sensors/)
