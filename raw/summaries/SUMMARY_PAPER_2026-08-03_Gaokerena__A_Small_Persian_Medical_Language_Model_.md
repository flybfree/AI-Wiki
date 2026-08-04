---
title: Gaokerena: A Small Persian Medical Language Model Family
url: http://arxiv.org/abs/2608.00932v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_02-17-10Z_Gaokerena_ASmallPersianMedicalLanguageModelFamily.md
generated_at: 2026-08-03 20:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Gaokerena, a compact Persian medical language model family designed for deployment on consumer‑grade hardware. The authors report that training a baseline model on a 90‑million‑token Persian medical corpus and physician Q&A pairs boosts performance on the translated medical MMLU benchmark from 46.28 % to 49.31 %, while an enhanced version with chain‑of‑thought reasoning reaches 52.98 %. Both models also include uncertainty heads that estimate confidence solely from internal hidden states.

## Key Takeaways
- The baseline model’s performance improves by over three points on a medical benchmark, showing the value of large‑scale Persian medical text and expert Q&A data.
- Adding chain‑of‑thought reasoning and reinforcement learning with AI feedback yields a higher score despite using less data, indicating that reasoning strategies can compensate for dataset size.
- Custom uncertainty heads provide confidence estimates without external context, offering an internal safety signal for model deployment.

## Context
Medical question‑answering systems are increasingly powered by large language models, yet most research focuses on English resources. Persian, as a widely spoken low‑resource language in Iran’s healthcare sector, remains underrepresented, creating a gap between AI capabilities and local clinical needs. This work addresses that gap with a focused, lightweight model family.

## Implications
The results suggest that domain‑specific fine‑tuning can bring modest but meaningful gains to Persian medical NLP tasks. However, the models still fall short of clinical reliability, underscoring the need for further data collection and rigorous safety testing before real‑world use. Practitioners should view these findings as a stepping stone toward localized AI health tools rather than final solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00932v1)
