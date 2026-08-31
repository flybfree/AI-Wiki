---
title: String: An Agentic OS Where Every App Is a Markdown File
published: 2026-08-28T07:44:41Z
authors: Jookyung Song, Nojun Kwak, Simyung Chang
url: http://arxiv.org/abs/2608.28027v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# String: An Agentic OS Where Every App Is a Markdown File

## Abstract
LLM agents have become a new class of software user, but every surface they work through was designed for someone else. Pages are built for human eyes, which can skim and ignore; tool schemas for programs, which pay nothing to carry definitions they never call. An agent has neither luxury: it re-reads, and pays again for, everything it is shown on every turn. We present String, an open-source runtime that gives this user an interface of its own and treats the job as an operating-systems problem. Tool knowledge moves out of the agent's context and into a common layer that renders it back one view at a time as Markdown. A single SFMD (String-Flavored Markdown) document declares an application's views, typed actions, navigation, and credentials, and the runtime handles discovery, validation, execution, state, and secrets behind two core verbs: /open to see and /act to do. Web and app turn out to be two renderings of one architecture: an SFMD site serves styled HTML to browsers and the raw document to agents, so one grammar reaches apps, files, shells, and the web, even legacy HTML, with no per-site integration. Views stay partial by design, and the staging is causal: disclosing one tier of detail a single turn too early costs up to 23 accuracy points, while proper staging drops wrong-action selection from 28% to 2%. Privilege follows provenance: a remote page may call HTTP but never the shell, and caller-supplied text never expands a stored secret. On an 87-task benchmark that pairs each task with curated skills, operationalizing those procedures as on-demand String apps yields comparable aggregate success across six models from frontier to small (+1.3pp) while using 33.5% fewer tokens among completed episodes, and the resident interface stays a constant 53 tokens at any catalog size. We report the design, the evaluation, and what three months of production use taught us.

## Metadata
- **Published**: 2026-08-28T07:44:41Z
- **Authors**: Jookyung Song, Nojun Kwak, Simyung Chang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28027v1)