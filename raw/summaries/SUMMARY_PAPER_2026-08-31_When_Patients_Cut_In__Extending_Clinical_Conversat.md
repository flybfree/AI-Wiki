---
title: When Patients Cut In: Extending Clinical Conversational AI Safety to Interruptions
url: http://arxiv.org/abs/2608.29241v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_12-54-50Z_WhenPatientsCutIn_ExtendingClinicalConversationalA.md
generated_at: 2026-08-31 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper investigates how clinical voice agents lose required patient information when patients interrupt mid‑utterance, showing that most benchmarks ignore this scenario and proposing a transcript‑based evaluation across three interruption types in four cell configurations (history‑taking and FAQ). The study finds that competitive FAQ interruptions cause 30/30 provision‑coverage failures for all models except Llama, while brief apology markers improve recovery but inconsistently.  

## Key Takeaways  
- The study reveals that cascaded architectures suffer from content loss when patients interrupt mid‑utterance, especially in information‑gathering cells where target‑question failure varies across models.  
- Competitive FAQ interruptions resulted in 30/30 provision‑coverage failures for all four LLM configurations (Wilson CI 88.6–100%, baseline 0/30 or 4/30), indicating severe robustness gaps.  
- Adding a brief apology marker improves recovery by tens of percentage points but can even reduce it in one model, showing that mitigation strategies are not universally effective.  

## Context  
Clinical conversational AI is moving beyond controlled benchmarks to real‑world patient interactions where interruptions are inevitable; this paper addresses the gap between theoretical performance and practical deployment. It highlights that current evaluation methods assume cooperative turns, missing critical safety issues.  

## Implications  
Practitioners must design systems with interruption resilience as a core metric, report results per cell type, and consider user‑initiated apologies when evaluating LLM configurations; otherwise clinical AI may fail to deliver required information, compromising patient care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29241v1)
