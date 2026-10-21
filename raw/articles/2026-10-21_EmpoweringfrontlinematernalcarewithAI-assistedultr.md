---
title: Empowering frontline maternal care with AI-assisted ultrasound
date: 2026-10-21
url: https://research.google/blog/empowering-frontline-maternal-care-with-ai-assisted-ultrasound/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/empowering-frontline-maternal-care-with-ai-assisted-ultrasound/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-10-21 11:32
---

# Empowering frontline maternal care with AI-assisted ultrasound

## Full Article

[Bar chart comparing the mean absolute error between the AI model and expert clinical standards across multiple cohorts.]
Empowering frontline maternal care with AI-assisted ultrasound
October 21, 2026
Angelica Willis, Research Engineer, Google Research, and Nichole Young-Lin, Clinical Lead, Google for Health
A prospective multi-center study demonstrates how AI-based blind sweep ultrasound assessment can enable non-sonographer operators with low-cost probes to deliver expert-level gestational age assessments, marking a significant step toward expanding life-saving maternal care globally.
Quick links
Paper
Share
Copy link
×
The World Health Organization (WHO)
estimates
that more than 250,000 preventable deaths occur worldwide each year due to pregnancy-related complications. While prenatal ultrasound can
improve
outcomes and
reduce
fetal and maternal mortality,
two-thirds
of people globally lack access to diagnostic medical imaging like ultrasound. Current methods that support maternal health rely heavily on specialized clinical training, leaving millions in low-resource settings without access to a single ultrasound during their entire pregnancy.
We saw an opportunity to conduct research towards addressing this real-world need, by developing machine learning systems that interpret "
blind sweep
" ultrasounds. This way of scanning allows frontline healthcare workers without specialized sonography training to perform scans by simply gliding low-cost, portable ultrasound probes across the abdomen in a standardized pattern.
play silent looping video
pause silent looping video
unmute video
mute video
Blind sweep sequence protocol diagram in order of their appearance in the data collection protocol.
Because many regions face critical shortages of experts, and traditional sonographer training is both expensive and requires a multi-year commitment, enabling these health workers to perform assessments with minimal training has the potential to significantly expand prenatal screening coverage.
Combining the minimal training requirement with AI interpretations could ultimately mean a successfully developed tool that has the potential to increase availability of ultrasound-based pregnancy assessment, and thereby improve access to higher quality maternal health.
In “
Generalization of AI-Based Gestational Age Assessment Using Blind Sweep Ultrasonography
”, published in
JAMA Network Open
, we evaluated how effectively an AI model for gestational age assessment (how far along the pregnancy is) generalizes across diverse clinical settings and hardware. While our
previous research
validated the model's performance on unseen patients from the same retrospective cohort it learned from, this new prospective study shows how the AI system performs reliably running live on mobile devices in real clinics, with only novice operators and unfamiliar ultrasound equipment, and minimal fine-tuning.
“
The gestational age is basically how far along a woman is in pregnancy. All of our screening, a lot of our treatments, a lot of our indications for delivery are all based on this master timeline that you get from the gestational age
.”
-
Nichole Young-Lin, OB-GYN Physician
Evaluating performance across diverse clinical settings
For a medical AI system to safely scale globally, it must demonstrate generalizability — maintaining accurate diagnostic performance when introduced to new clinical settings with different patient populations, clinical workflows, and ultrasound hardware variations than those on which the model was trained.
In this study, our original AI model was minimally tuned on only one of our target populations, and then prospectively tested across both target environments:
Northwestern Medicine
: An urban, high-resource academic medical center in Chicago, IL, United States.
Jacaranda Health:
An urban community clinic network in Nairobi, Kenya.
Originally trained on ultrasound data collected in North Carolina and Zambia using a set of Sonosite, GE, and Butterfly Networks commercial ultrasound probes, the research AI system was paired with Clarius C3, a commercial handheld transabdominal probe. All of these sites differed in various care dimensions, including when women first come in for prenatal care, how many routine ultrasounds they receive, and how gestational age is usually dated.
To evaluate efficient system tuning, the study leveraged a small pilot dataset of 120 participants from Chicago — approximately 6% of the original training set—to adapt the model to new probe hardware and extend the gestational age prediction range beyond 36 weeks. To understand generalizability, no data from the Nairobi site was used for fine-tuning, maintaining the Kenyan clinical validation as a strictly independent, external test. To evaluate comprehensive utility, the study also included multiple gestation pregnancies, which could present tracking and measurement challenges for both human operators and automated systems.
[Bar chart comparing the mean absolute error between the AI model and expert clinical standards across multiple cohorts.]
Our blind sweep model, trained on 1,968 participants (North Carolina, US, and Zambia) was fine-tuned on scans from 120 participants from Chicago, Illinois. It was then tested prospectively in Chicago (n=192) and Nairobi (n=193), with no fine-tuning on Nairobi data. The model was non-inferior to expert sonographers at determining gestational age, in both settings, with a combined mean absolute error of 4.18 vs. 4.48 days.
Key findings: Matching the expert standard
We compared the AI system’s ability to estimate fetal age from blind sweep ultrasounds to formula-based estimation from the clinically standard expert approach. This expert approach relies on an expert sonographer locating multiple specific cross-sections of the fetus(es) to take precise biometry measurements, a difficult-to-scale task that requires years of training and is highly operator-dependent.
Evaluating a primary cohort of 385 participants between 16 and 36 weeks of pregnancy, the diagnostic study demonstrated strong AI system results:
Clinically non-inferior accuracy
: Across both cohorts, the AI model achieved a mean absolute error (MAE) of 4.18 days in estimating gestational age, successfully demonstrating non-inferiority to the standard clinical procedure performed by expert sonographers, which had an MAE of 4.48 days.
Cross-setting generalization
: In Chicago, the adapted model achieved an MAE of 4.10 days. In Nairobi, with zero local optimization, the model achieved a comparable MAE of 4.27 days.
[Flowchart outlining the AI model's training, fine-tuning, and validation process across multiple global clinical sites.]
The AI system's gestational age error (MAE 4.18 days) was non-inferior to expert sonographer biometry (4.48 days), and stayed consistent from Chicago (4.10 days) to Nairobi (4.27 days), where the model had no local fine-tuning.
Beyond accuracy, exploratory metrics showed that the research AI system was resilient in complex scenarios. For instance, in cases of fetal weight extremes (above the 90th percentile), the model outperformed traditional biometry formulas, demonstrating robustness against variations in fetal size.
Lessons learned during prospective deployment
In addition to highlighting an immense opportunity to expand ultrasound access through AI, the prospective multi-center study allowed us to actively observe and optimize how AI behaves in live clinical environments. By deploying our system directly into everyday clinical workflows, we gained practical insights that help us design for real world use. For example, we observed the importance of swappable batteries over plug-in docking stations for keeping devices charged between consecutive patients.
These studies also demonstrated how deploying AI systems like this will also require building deep trust with both clinicians and patients. One important way to ultimately achieve this would be by building clear safeguards into the app, like model confidence estimates produced by our model to reject poor-quality sweeps and convey model uncertainty to the clinician user.
Looking ahead: Expanding access to care with AI
These study findings indicate that AI-based systems can analyze standardized “blind sweeps” images acquired by operators without specialized sonography training. The AI estimate of fetal age had accuracy comparable to the current standard of care from expert operators and more expensive traditional, cart-based ultrasound machines. Demonstrating technical generalizability across diverse clinical settings, hardware, and changing populations, marks a key step in highlighting their potential to expand access to this critical capability for maternal health.
By empowering minimally trained community health workers to perform reliable ultrasonography assessments, this research demonstrates the potential to expand prenatal coverage for millions in under-resourced areas. Studying the capabilities of this scalable technology lays the groundwork for more resilient, accessible healthcare systems, ensuring that every mother, regardless of location, has the chance for a healthy pregnancy and a safe delivery.
This point-of-care research represents a potential application of our broader vision for expanding healthcare accessibility through AI. The insights gained from this research inform the development of our next-generation, multimodal medical intelligence research. Through our continued work, we strive to provide the development community and scientists with the answers they need to improve clinical care and make it helpful and accessible to all.
Acknowledgements
Thank you to our co-authors across Google Research, Jacaranda Health and Northwestern University Feinberg School of Medicine: Chace Lee, Justin Krogue, Anneka Wickramanayake, Stacey Caron, Priscah Cheruiyot, Amber Watters, Alicia Martín, Tiya Tiyasirichokchai, Akib Uddin, Yun Liu, Patricia Strachan, Sunny Jansen, Alyssa Santi, Preeti Singh, Catherine Arguelles, Kenneth Hudson, David Melnick, Mahesh Vaidyanathan, Mozziyar Etemadi, Yossi Matias, Avinatan Hassidim, Greg Corrado, Shruthi Prabhakara, Daniel Golden, Ryan G. Gomes, and Shravya Shetty. Thank you to Pi-Chuan Chang and Dale Webster for reviewing this work.
Labels:
Health & Bioscience
Machine Perception
Quick links
Paper
Share
Copy link
×
Other posts of interest
[Diagram of a Self-Improving Search cycle going from a Lab in the Loop, to a Model, to a Complex Space, to an Agent.]
October 16, 2026
Grounding AI agents in biological reality: Building blocks for autonomous wet labs
General Science
·
Health & Bioscience
·
Robotics
[USS0291-Google Research Anthem Film_Thumbnail4 (1)]
October 14, 2026
Research@ 2026: 10 ways we're amplifying human ingenuity
General Science
·
Generative AI
·
Health & Bioscience
[Three aerial cityscape panels featuring public health dashboard cards: MMR coverage, Dengue cases forecast, and Cholera emergence zones.]
October 6, 2026
Unlocking Earth AI’s planetary geospatial foundation models for global public health
Earth AI
·
Global
·
Health & Bioscience
×
❮
❯
[FrontlineMaternalCarewithAI3_KeyFindings]
Flowchart outlining the AI model's training, fine-tuning, and validation process across multiple global clinical sites.
[FrontlineMaternalCarewithAI2_ModelOverview]
Bar chart comparing the mean absolute error between the AI model and expert clinical standards across multiple cohorts.

## Metadata
- **Source**: [Original Article](https://research.google/blog/empowering-frontline-maternal-care-with-ai-assisted-ultrasound/)
