---
title: Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research
published: 2026-08-25T09:34:18Z
authors: Eran Hirsch, David Wan, Han Wang, Elias Stengel-Eskin, Mohit Bansal, Ido Dagan
url: http://arxiv.org/abs/2608.24306v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research

## Abstract
Deep research (DR) systems produce long-form cited reports by orchestrating multiple agents that search and synthesize information from the web. Citations are the primary mechanism for evaluating the faithfulness of these reports, yet current DR systems exhibit poor citation recall. Moreover, improving citation recall is challenging because DR systems are complex multi-agent architectures where information passes through agents like a telephone game, and both content and citations can get corrupted along the way. We propose an evaluation method that pinpoints which agent introduced each error by locally testing agent invocations for faithfulness and verifiability relative to their own inputs. Furthermore, we propose a four-type taxonomy to categorize the discovered errors: hallucination, uncited input reliance, uncited output, or insufficient citations. Applying our method to three top-ranked open-source DR systems, we obtain actionable diagnostics. Almost every agent makes a lot of mistakes with the exception being those that summarize a single document. We find that the dominant error type varies systematically across agents, where the orchestrator mistakes are mostly citation-related. We find that 84.7% of final-report errors in AI-Q originate at the orchestrator, roughly 31% of them hallucinations and the rest citation mistakes. Guided by these insights, we demonstrate that two simple interventions raise citation recall by 5% without degrading output quality.

## Metadata
- **Published**: 2026-08-25T09:34:18Z
- **Authors**: Eran Hirsch, David Wan, Han Wang, Elias Stengel-Eskin, Mohit Bansal, Ido Dagan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24306v1)