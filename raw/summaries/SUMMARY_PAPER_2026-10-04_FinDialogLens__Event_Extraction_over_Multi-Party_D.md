---
title: FinDialogLens: Event Extraction over Multi-Party Dialogue for Missed-Trade Identification in Financial Chatrooms
url: http://arxiv.org/abs/2610.02455v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_20-29-40Z_FinDialogLens_EventExtractionoverMulti_PartyDialog.md
generated_at: 2026-10-04 21:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FinDialogLens addresses the challenge of extracting missed trades from multi-party financial chatrooms by framing the problem as event extraction over complex, interleaved dialogue. The paper presents a hybrid LLM pipeline that combines compact fine-tuned classifiers for detecting RFQ-trigger messages and price/trade outcome metadata with an RFQ-Level segmentation module and a Trade Engine for filling argument roles, achieving 92.1% and 94.3% accuracy on final price and trade outcome extraction respectively. A difficulty-aware routing mechanism further reduces operational costs by 85% in LLM calls while maintaining competitive accuracy at production scale.

## Key Takeaways
- FinDialogLens decomposes the multi-party dialogue event extraction problem into specialized sub-tasks: fine-tuned classifiers detect RFQ-trigger messages and price/trade outcome metadata, an RFQ-Level Module segments per-event windows to isolate concurrent RFQs from different participants, and a Trade Engine fills argument roles to reconstruct the full trade event. This modular scaffold approach outperforms full-chatroom chain-of-thought prompting methods.
- Fine-tuned open-source LLMs with as few as 3 billion parameters achieve performance comparable to GPT-4o on this task when trained with modest in-domain data, demonstrating that domain-specific fine-tuning can close the gap with frontier models for structured extraction tasks in financial dialogue.
- The difficulty-aware router allocates RFQs between a low-cost rule-based engine and the higher-performing LLM-powered Trade Engine, cutting LLM API calls by 85% on final price extraction while recovering half the accuracy gap to the full FinDialogLens pipeline, saving over $300 per day at a 70,000-RFQ-per-day production scale.

## Context
This work sits at the intersection of event extraction, multi-party dialogue understanding, and applied LLM systems engineering. Traditional event extraction research has focused on single-document or single-speaker settings, while financial chatrooms introduce interleaved concurrent events, implicit references, and long-range dependencies that break standard NER or relation-extraction pipelines. By casting trade recovery as a structured event extraction problem over dialogue and introducing a hybrid architecture that pairs lightweight classifiers with large language models, FinDialogLens contributes a practical template for deploying LLMs in high-volume, latency-sensitive enterprise workflows where pure prompting is too expensive and pure rule-based systems are too brittle.

## Implications
For financial institutions and trading desks, FinDialogLens offers a deployable path to automating missed-trade recovery at scale, reducing operational risk and compliance gaps that arise when trades are not captured in real time. The difficulty-aware routing strategy provides a generalizable blueprint for organizations seeking to balance LLM accuracy against inference cost in production systems handling tens of thousands of events daily. For the broader NLP community, the finding that small fine-tuned models can match frontier models on domain-specific extraction tasks underscores the value of targeted data curation and modular pipeline design over monolithic prompting approaches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02455v1)
