---
title: Clean Tickets, Wrong Orders: Catching Silent Errors with a Language Model in Your Browser Tab
url: http://arxiv.org/abs/2611.18284v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_15-13-47Z_CleanTickets_WrongOrders_CatchingSilentErrorswitha.md
generated_at: 2026-11-16 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a browser-based demonstration of a fine-tuned 0.8B parameter language model that parses typed restaurant orders into structured tickets, running entirely within the visitor's browser tab via llama.cpp compiled to WebAssembly. The authors focus on detecting "silent errors"—outputs that are syntactically valid and well-formed but semantically incorrect, representing the more dangerous failure mode of order-parsing models. Deployed against all 1,357 PIZZA benchmark test orders, the in-browser model reproduces the server evaluation output for 99.0% of cases and achieves an exact match score of 0.882, while also reporting latency measurements on three consumer laptops.

## Key Takeaways
- The paper distinguishes two failure modes in order-parsing language models: malformed outputs that any downstream system can reject, and "silent errors" where the model produces a clean, well-formed order that the user never actually placed. The authors argue silent errors are the dangerous category because they pass structural validation undetected, making them critical to identify in production systems.
- The entire inference pipeline runs client-side in the browser using llama.cpp compiled to WebAssembly, ensuring that no order text ever leaves the visitor's device. The page parses orders incrementally as the user types, scores each generated ticket using the PIZZA benchmark's matcher ported to TypeScript, and explicitly refuses off-menu items by outputting "?" to acknowledge the model's exposure to the open web.
- The in-browser deployment achieves 99.0% output parity with the server-side evaluation across all 1,357 PIZZA test orders and matches the exact-match score of 0.882, demonstrating that a 0.8B model can be faithfully deployed on consumer hardware without meaningful accuracy loss. Latency benchmarks on three consumer laptops are provided to characterize real-world usability.

## Context
This work sits at the intersection of small language model deployment, privacy-preserving inference, and evaluation methodology for structured text generation tasks. As the industry pushes toward running models on-device for latency and privacy reasons, questions about whether quantized or browser-compiled models preserve the accuracy of their server-side counterparts become practically important. The paper also contributes to the broader conversation about evaluation rigor by highlighting that structural validity checks are insufficient to catch semantic hallucinations, a concern relevant across any domain where language models produce structured outputs such as code, commands, or transactional data.

## Implications
For practitioners building order-parsing, ticketing, or command-understanding systems, this work demonstrates that a sub-billion-parameter model can be deployed entirely client-side with near-identical accuracy to a server deployment, opening a path toward privacy-preserving, low-latency inference on commodity hardware. The explicit framing of silent errors as a distinct evaluation target encourages benchmark designers and application developers to go beyond format-validity checks and incorporate semantic correctness scoring directly into their pipelines. The interactive web demo at wrong.cuyor.com also provides a reproducible, accessible tool for researchers and developers to probe model failure modes hands-on rather than relying solely on aggregate metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.18284v1)
