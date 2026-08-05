---
title: CARE-Bench: Benchmarking Patient-Facing LLM Triage
published: 2026-08-04T14:26:45Z
authors: Yining Hua, Hongbin Na, Cyrus Ayubcha
url: http://arxiv.org/abs/2608.03731v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CARE-Bench: Benchmarking Patient-Facing LLM Triage

## Abstract
Patient-facing medical LLMs and agents increasingly answer symptom questions before clinician contact, where the key safety question is what action the user should take next. We introduce CARE-Bench, a source-grounded benchmark that evaluates sequential patient-facing triage as a four-label per-turn current-action task. CARE-Bench contains 500 cases and 1,059 evaluated patient-disclosure prefixes reconstructed from medical dialogue, consultation, and follow-up-question sources. We evaluate 11 models on 269 held-out rounds under unprompted and minimally prompted open-ended protocols, using a fixed GPT-5.5 mapper to code each response into the four-label action space. Unprompted macro-F1 remains low, ranging from 31.2 to 50.4. Prompting improves 10 of 11 models, with prompted macro-F1 ranging from 46.9 to 63.4, but substantial threshold errors remain. Prompted models often recommend care before needed clarification is obtained; when the correct action was to ask for more information, only 33.5% of prompted outputs preserved the step. The persistence of these errors after prompting suggests that patient-facing triage is not a simple prompting problem and supports explicit evaluation of action timing before deployment.

## Metadata
- **Published**: 2026-08-04T14:26:45Z
- **Authors**: Yining Hua, Hongbin Na, Cyrus Ayubcha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03731v1)