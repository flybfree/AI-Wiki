---
title: Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?
published: 2026-09-26T11:37:06Z
authors: Jiahong Dai, Zhuochen Yang, Pengyang Shao, Kelvin Ng, Zhongyi Liu, Chengquan Ju, Yuting He, Bo Hu
url: http://arxiv.org/abs/2609.32495v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?

## Abstract
An agent harness, the code that turns a model into an agent, writes its own record of each run, and that record is all a later reader gets when a run is disputed, investigated or audited. We call a record evidentiary when a reader who was not there can check it without trusting the writer. Across sixteen deployed frameworks, none writes one in full. Hearsay examines the record, not the task: five harnesses run fourteen tasks, three blinded LLM examiners and a human panel read the records, and every excerpt an examiner quotes is checked mechanically for who wrote it. First, the record lets a reader name the fault but not prove how the run went. Examiners name the right fault in 74 to 91% of 140 runs, but the fault can be proved only from two files the benchmark adds; for what happened in between, fewer than one citation in ten lands on anything the harness did not write, and the examiner with the fewest false alarms catches half of the entries we delete, rewrite or fabricate. Second, the remedy is a second author, not a stronger seal on the first. An append-only log of what passes between harness and model, kept outside the harness and read against the record in both directions, reports all 28 omissions and fabrications we made a harness commit as it ran, where a hash chain over the harness's own record passes all 28. Handed the log, examiners keep their fault verdicts but rest more of their citations on what the harness did not write. What makes a record evidence is who writes it, not what is captured.

## Metadata
- **Published**: 2026-09-26T11:37:06Z
- **Authors**: Jiahong Dai, Zhuochen Yang, Pengyang Shao, Kelvin Ng, Zhongyi Liu, Chengquan Ju, Yuting He, Bo Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32495v1)