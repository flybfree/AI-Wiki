---
title: Advancing AMIE towards expert-level audio-visual clinical consultations
date: 2026-08-11
url: https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-08-11 12:20
---

# Advancing AMIE towards expert-level audio-visual clinical consultations

## Full Article

Advancing AMIE towards expert-level audio-visual clinical consultations
August 11, 2026
Anil Palepu, Senior Research Scientist, and Mike Schaekermann, Research Lead, Google
We advance AMIE, our research medical AI system, to conduct real-time video consultations, with a first-of-its-kind demonstration of expert-level performance in a randomized controlled study with simulated consultations.
Quick links
Paper
Share
Copy link
×
When a physician meets a patient, the consultation extends far beyond the words exchanged. The physician observes the patient's gait, registers visible signs of discomfort, notes their breathing, and guides the patient through physical examination maneuvers. This continuous stream of visual and auditory information is seamlessly integrated with the spoken clinical history. These non-verbal visual and auditory cues are central to effective diagnosis, patient trust, and clinical communication.
AI systems capable of clinical reasoning and dialogue have the potential to dramatically increase access to medical expertise and care, fostering a future where physicians can focus their time on the most meaningful aspects of patient interactions. In early work, the Articulate Medical Intelligence Explorer (
AMIE
), our research AI system for clinical reasoning and dialogue, demonstrated expert-level performance in
text-based diagnostic dialogue
and proved effective as a
differential diagnosis aid for clinicians
. Recently, we advanced AMIE’s capabilities
beyond diagnosis
towards
treating and managing disease over time
.
We have also extended AMIE's capabilities towards specialist-level evaluations in
oncology,
cardiology
and
ophthalmology
, and
multimodal diagnostic reasoning
over
images and clinical documents
, in simulated settings with patient actors. In parallel, we have begun translating these research advances towards clinical practice, through a framework for
physician-centered oversight
, as well as our first real-world clinical studies including a
clinical feasibility study
with
Beth Israel Deaconess Medical Center
, and an
ongoing nationwide randomized study
in partnership with
Included Health
.
Despite these advances, a fundamental constraint in our research remained that text-based interfaces discard the visual and auditory dimensions of clinical practice. Patients must translate complex physical symptoms into written descriptions, a process that discards diagnostic information and can negatively affect patients with limited digital or health literacy. Text-only systems cannot independently observe the visual and auditory cues that inform clinical reasoning, nor can they guide patients through the physical examination maneuvers that shape differential diagnosis.
Today, in “
Towards expert-level medical AI for real-time video consultations
”
, we present AMIE in a real-time video configuration, AMIE (Video), that addresses these limitations. Built on
Gemini
and
Project Astra
, AMIE (Video) conducts synchronous clinical video consultations, perceiving non-verbal clinical cues, guiding patient actors through virtual physical examinations, and reasoning diagnostically, all in real time. In a multi-arm randomized study with 100 scenarios, 300 live consultations, and a group of 30 board-certified primary care physicians (PCPs), we present the first demonstration of an AI system exhibiting expert-level performance in real-time clinical video consultations.
[Video preview image]
Watch the film
Link to Youtube Video
AMIE (Video): An asynchronous multi-agent architecture
Conducting an effective clinical conversation over video requires balancing competing demands: the system must respond to patients at natural conversational speed while simultaneously performing careful clinical reasoning and continuously processing visual and auditory streams. Currently, a single agent cannot satisfy all these requirements. Deep reasoning takes time, but conversational pauses erode patient trust and rapport.
To address this challenge, AMIE (Video) uses an asynchronous multi-agent architecture that divides labor across three specialized agents working continuously in parallel:
Talker agent:
The patient-facing agent drives responsive, low-latency spoken interaction. It maintains natural conversational flow while incorporating guidance from the other agents.
Planner agent:
Operating in the background, this agent continuously refines the system's clinical reasoning, updating differential diagnoses and management plans while identifying information gaps, and re-prioritizing diverse clinical goals.
Perception agent:
This agent continuously reviews the audio and visual streams, identifying clinically relevant non-verbal cues (such as visible signs of distress, physical findings, or auditory signals) and contextualizing these observations within the ongoing conversation.
This decoupled design allows AMIE (Video) to maintain natural conversational latency while performing diagnostic reasoning and audio-visual perception that would otherwise introduce unacceptable delays. Automated evaluations confirm that each agent in this three-agent architecture makes important contributions towards improvements on clinical metrics, such as competency in history-taking, clinical reasoning and treatment recommendations, as well as on metrics related to dialogue quality, including patient-centered communication skills and response latency.
[AMIE (Video)-1]
Overview of AMIE for real-time clinical video consultations, the evaluation study and key findings.
Guiding development with automated evaluation
A key challenge in building audio-visual medical AI is characterizing a system's perceptual and reasoning capabilities at scale. To guide development, we derived a taxonomy of clinical audio-visual competencies relevant to telehealth from the medical literature, covering non-verbal visual cues, auditory signals, and physical examination maneuvers. We then built an automated evaluation suite structured around this taxonomy.
This evaluation framework combines targeted single-turn audio-visual assessments with multi-turn simulated audio consultations. The single-turn audio-visual assessments test specific instances of clinical perception and reasoning (e.g., correctly identifying anatomical laterality or recognizing signs of respiratory distress). And the multi-turn simulated audio consultations assess end-to-end conversational performance while injecting visual cues as textual descriptions into the simulation (for example, an AI patient simulator for a Parkinson’s scenario prompted to show their handwriting may inject a verbal description of “[holding up paper to camera showing cramped, tiny script]”). Together, these complementary evaluations enabled rapid iteration on system design and richly characterized capabilities and failure modes of AMIE (Video) prior to human evaluation.
Evaluation through a randomized video study
To evaluate clinical competence in the more challenging and realistic setting of an end-to-end audio-visual clinical consultation, we conducted a large-scale, randomized
Objective Structured Clinical Examination
(OSCE) study with a synchronous video consultation interface.
To cover a breadth of medical conditions in our evaluation, the study spanned 100 clinical scenarios covering five body systems, including cardiopulmonary, abdominal, head/eyes/ears/nose/throat (HEENT), neurological/psychiatric, and musculoskeletal conditions. Fifteen trained patient actors carried out 300 standardized consultations across three study arms:
AMIE (Video):
The video configuration of AMIE conducting real-time video consultations.
AMIE (Text):
A text-only version serving as a baseline to isolate the contribution of audio-visual capabilities.
PCP (Video):
Ten board-certified PCPs consulting via the same video interface.
An independent panel of 20 experienced primary care physicians evaluated all consultations using established clinical rubrics, including both general clinical competency scales and detailed case-specific scoring criteria tailored to each scenario.
[AMIE (Video)-2]
Video consultation quality of AMIE and PCPs as assessed by diagnostic accuracy as well as clinical evaluator ratings and patient actor preferences.
Key results
Expert-level clinical performance:
Across core clinical competencies, history-taking thoroughness, diagnostic accuracy, management appropriateness, and communication quality, clinical evaluators rated AMIE (Video) on par with PCPs. AMIE (Video) also matched or exceeded AMIE (Text) on these dimensions.
Strength in physical observation and examination:
AMIE (Video) was rated significantly higher, on average, than both PCPs and AMIE (Text) eliciting physical signs and proactively guiding patient actors through virtual examination maneuvers. This advantage was also reflected in case-specific perception and examination rubric scores.
Patient actors preferred the video experience:
Patient actors strongly preferred the synchronous video interface over text-based chat, rating it as significantly easier to use and more effective for communicating health concerns. They also rated AMIE (Video) favorably on empathy, rapport, and confidence in care compared to both PCPs and AMIE (Text).
[AMIE (Video)-3]
Modality ablation comparing AMIE’s video configuration to AMIE using text chat only. Results are based on ratings from clinical evaluators and preferences from patient actors.
Limitations and responsible development
This research has important limitations and it is critical to interpret these results within the context of these limitations. This study was conducted entirely with professional patient actors in simulated clinical settings, not with real patients presenting with their own health conditions. Patient actors, however skilled, cannot fully replicate the complexity and unpredictability of real clinical encounters, and the scenarios were limited to conditions that can be authentically portrayed through acting, omitting important clinical presentations where audio-visual perception would be diagnostically consequential. Beyond the scope of the study, targeted automated evaluations revealed occasional perceptual and reasoning errors, despite overall high-quality conversation and diagnostic accuracy, and the system still exhibits intermittent technical issues that can disrupt conversational naturalness. Given the prototype nature of Project Astra, this includes technical considerations that future development may address at a system level that go beyond the specific medical application explored in this work. Assessing these findings in studies with real patients and real clinical conditions is an essential next step before any conclusions about real-world utility can be drawn.
Looking ahead
This work demonstrates that the transition from text-based to audio-visual clinical AI is achievable at expert-level quality. AMIE (Video) engages with the perceptual richness of clinical practice, observing non-verbal cues, guiding physical examination, and conversing naturally through spoken dialogue — capabilities that more closely approximate the experience of a telehealth video encounter.
Important questions remain on the path towards responsible real-world evidence. Our findings need to be validated with real patients, expanded to encompass clinical presentations that cannot be enacted, and supported by robust safety frameworks. We have already taken early steps in this direction: a
real-world feasibility study
with Beth Israel Deaconess Medical Center provided initial evidence for the safety and utility of text-based AMIE in clinical practice, and our
ongoing nationwide randomized study
with Included Health is further evaluating AI in real-world virtual care. Together, these research experiences will help inform how audio-visual capabilities might be responsibly integrated into clinical practice. While much remains to be done, these results mark an important milestone towards AI systems that could one day augment care by engaging with the sensory complexity of clinical practice.
Acknowledgements
The research described here is joint work across many teams at Google Research and Google Deepmind. We are grateful to all our co-authors - Mahvish Nagda, Jihyeon Lee, Matthew Thompson, CJ Park, Tim Strother, Valentin Liévin, Roma Ruparel, Akshay Goel, Teya Bergamaschi, Suhana Bedi, Meet Shah, Pavel Dubov, Liviu Panait, Toshiyuki Fukuzawa, Sam Schmidgall, Craig Schiff, Joseph Xu, Aliya Rysbek, Yana Lunts, Jan Freyberg, Rebecca Hemenway, Sunny Virmani, David Racz, Carey Radebaugh, Joëlle Barral, Kavi Goel, Dale R. Webster, Katherine Chou, Avinatan Hassidim, Yossi Matias, James Manyika, Gregory Wayne, Tao Tu, Yun Liu, Ethan Goh, Christina Chen, Ryutaro Tanno, and Cameron Chen.
Labels:
Health & Bioscience
Machine Intelligence
Quick links
Paper
Share
Copy link
×
Other posts of interest
[Science-One-1-final]
July 30, 2026
Science One Framework: A verifiable autonomous research framework via Chain-of-Evidence
General Science
·
Machine Intelligence
·
Natural Language Processing
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
×
❮
❯
[AMIE (Video)-3]
[AMIE (Video)-2]
[AMIE (Video)-1]

## Metadata
- **Source**: [Original Article](https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/)
