---
title: Extending FunctionGemma for Practical On-Device Mobile Function Calling
published: 2026-09-21T20:12:22Z
authors: Ali Rezagholizadeh, Soheila Samiee
url: http://arxiv.org/abs/2609.25373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Extending FunctionGemma for Practical On-Device Mobile Function Calling

## Abstract
On-device assistants require function-calling models that map natural language to local system actions, but existing resources emphasize web APIs or narrow mobile-action catalogs. We extend FunctionGemma 270M-it to practical Android workflows by introducing MOBILEACTIONSEXTENDED, a synthetic, schema-validated dataset of ~9,500 conversations covering fifteen device-control categories, including messaging, phone calls, camera/screenshot, brightness control, device-status queries, flashlight control, and application management. We fine-tune the 270M model with TRL supervised fine-tuning under completion-only loss, producing an extended specialist and a combined model trained jointly with Google's MOBILEACTIONSGOOGLE. On MOBILEACTIONSEXTENDED, end-to-end accuracy improves from 29.3% for the base model and 17.2% for Google's Mobile-Actions variant to 76.5%. The combined model retains 76.5% on MOBILEACTIONSEXTENDED and reaches 82.3% on MOBILEACTIONSGOOGLE, down from the 90.3% of Google's Mobile-Actions specialist, representing an 8.0-percentage-point trade-off in return for doubling category coverage. We release the dataset, fine-tuned models, reproducible training/evaluation pipeline, and an Android demo, highlighting compact local function calling as a practical path towards low-latency and privacy-preserving mobile assistants.

## Metadata
- **Published**: 2026-09-21T20:12:22Z
- **Authors**: Ali Rezagholizadeh, Soheila Samiee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25373v1)