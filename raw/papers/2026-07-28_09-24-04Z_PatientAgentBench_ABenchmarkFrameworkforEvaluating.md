---
title: PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents
published: 2026-07-28T09:24:04Z
authors: Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou, Mohammad Abuzar Hashemi, Prasad Kasu, Deepak Bansal, Daniel Lopez-Martinez, Anchal Nema, Ramya Ganesan, Will Kimbrough, Alex Woody, Yadunandana Rao, Dilek Hakkani-Tur, Wilko Schulz-Mahlendorf
url: http://arxiv.org/abs/2607.25485v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PatientAgentBench: A Benchmark Framework for Evaluating Patient-Facing Health AI Agents

## Abstract
Health AI is evolving from answering questions to agentic systems that converse with patients, reason about health records, and act on their behalf. Primary care guards against diagnostic errors and unsafe care; agents assisting in this domain warrant evaluation against the same risks. Current benchmarks focus on medical knowledge, assessed through isolated question-answering or clinician-facing tasks. PatientAgentBench benchmarks patient-facing agentic healthcare; it evaluates a foundation model, wrapped in an agent with a sandbox of healthcare tools, conversing with a simulated patient. Each conversation is scored by an LLM-as-a-Jury across six dimensions via over a hundred conversation-agnostic, clinician-grounded criteria. To validate alignment, licensed clinicians annotated shared conversations, yielding 79-93% adjacent agreement between jury and expert raters, on par with or exceeding clinician inter-rater agreement. We benchmarked 10 models across four families on the same 1,200 scenarios and found clinical gaps. Triage quality is the most discriminating dimension: pass rates rise from 32% for the weakest models to 88% for the strongest, with agents often acting on administrative requests without clinical screening. Clinical safety and workflow accuracy follow the same pattern: the weakest models fail often, fabricating unexecuted actions, while frontier models fail on only 1-3% of cases, from unverified tool outputs and omitted crisis resources in an emergency. More capable models narrow these gaps but do not close them; the strongest scores only 4.25 of 5 overall. These failures surface only in sustained, tool-using conversations against realistic patient records, confirming that static benchmarks are insufficient as healthcare agentic systems gain autonomy. We release the framework as a reproducible, clinician-validated evaluation standard to help the field close this gap.

## Metadata
- **Published**: 2026-07-28T09:24:04Z
- **Authors**: Korosh Vatanparvar, Ashutosh Joshi, Maria Xenochristou, Mohammad Abuzar Hashemi, Prasad Kasu, Deepak Bansal, Daniel Lopez-Martinez, Anchal Nema, Ramya Ganesan, Will Kimbrough, Alex Woody, Yadunandana Rao, Dilek Hakkani-Tur, Wilko Schulz-Mahlendorf
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25485v1)