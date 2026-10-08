---
title: AgentTime: Can Agents Estimate and Control Their Own Runtime?
published: 2026-10-07T12:26:24Z
authors: Michael Ofengenden, Maksym Andriushchenko
url: http://arxiv.org/abs/2610.09944v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentTime: Can Agents Estimate and Control Their Own Runtime?

## Abstract
An essential control of AI agents is their ability to manage runtime. This ability requires a sense of time-awareness, to predict and estimate wall-clock time and to control their own actions. Prior work has focused on time-awareness, but duration-following and control in native agent harnesses remain unexplored. We present AgentTime, a benchmark for testing whether agents can work for a requested duration, predict their runtime, and estimate elapsed time afterward. It comprises 222 tasks from 18 sources spanning coding, computer use, agentic work, and automated research. Duration-following experiments append a single instruction specifying how long to work, with requests ranging from about a minute to multiple days. Accuracy on these instructions varies substantially: Fable 5.1 in Claude Code deviates from requested runtimes by a typical factor of 2.9$\times$, compared with only 1.2$\times$ for GPT-6 Astra in Codex. However, matching the requested runtime does not, by itself, establish continued work on the task. Among 158 reviewed Astra runs with classifiable transcripts, 14 explicitly slept after appearing to finish. In forecasting experiments, predictions tend to overestimate natural runtimes. In retrospective experiments, removing temporal information more than doubles deviation for Sol and Astra and nearly doubles it for Fable. An agent's ability to complete a task does not guarantee that it can control its own time or work for the whole requested duration. For agents to run reliably, safely, and autonomously over long horizons, we require the evaluation of both.

## Metadata
- **Published**: 2026-10-07T12:26:24Z
- **Authors**: Michael Ofengenden, Maksym Andriushchenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09944v1)