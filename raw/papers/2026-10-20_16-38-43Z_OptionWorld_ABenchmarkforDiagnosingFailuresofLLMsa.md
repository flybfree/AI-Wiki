---
title: OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal Assistants
published: 2026-10-20T16:38:43Z
authors: Ruoyu Zhang, Zhaocen Liu, Weiyi Tian, Melissa Feng, Shilong Liu
url: http://arxiv.org/abs/2610.28491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OptionWorld: A Benchmark for Diagnosing Failures of LLMs as Long-Term Personal Assistants

## Abstract
Long-term assistants must follow unfinished tasks across days as information and circumstances change. Finding information or starting an action, however, does not ensure that the task gets completed. We introduce OptionWorld, a benchmark that traces information acquisition, judgments, actions, and outcomes in simulated daily-life tasks to identify where current LLMs fall short as long-term personal assistants. In runs with archived decision inputs, the key facts remain in the model's last input before the deadline in 35.5% of failed instances. Failure analysis identifies the three most frequent problems: needed information is not obtained or combined, available opportunities to act go unused, and agents impose restrictions that the task does not require. Three follow-up experiments show that supplying missing facts restores task success in some cases; action reminders can restart work while subsequent steps still miss the deadline; and correcting a supplied note that wrongly forbids contact restores permitted inquiry. These findings locate shortcomings in maintaining task state: connecting facts to unfinished work, following through before deadlines, and separating actual restrictions from the agent's assumptions.

## Metadata
- **Published**: 2026-10-20T16:38:43Z
- **Authors**: Ruoyu Zhang, Zhaocen Liu, Weiyi Tian, Melissa Feng, Shilong Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28491v1)