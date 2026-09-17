---
title: A Study of the Reliability of Agentic AI-Generated Programs
published: 2026-09-16T08:21:09Z
authors: Ayesha Shafique, Barton P. MIller, Elisa R. Heymann
url: http://arxiv.org/abs/2609.18298v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Study of the Reliability of Agentic AI-Generated Programs

## Abstract
Agentic-AI based software development offers the promise of faster completion of the software, greater programmer efficiency, and more reliable code. The question is how can we verify these claims in an objective way? In this project, we attempted to answer this question based on three practices. First, we applied a typical best-practices agentic AI workflow for software development. Second, our target programs were ten well-known, release-quality human-written Linux utility programs so that we could compare the AI-generated code against a concrete ground truth. Third, we based our measure of reliability on a widely used testing technique, fuzz random testing. For this testing, we used both classic black box, generational testing and more modern coverage guided (gray box, mutational) testing using AFL++. We found that the AI-generated versions of the utility programs were typically as reliable - often more reliable - than the latest human-generated versions of these programs. While the AI-generated versions did have some failures, they were less common than the code from the standard repositories. Interestingly, the AI-generated code was less likely to have failures such as memory errors (such as buffer overflows) but more likely to have hangs such as infinite loops. In addition, we verified that generating robust and reliable software using agentic AI requires careful practice and human supervision. The quality of the code is highly dependent on the prompts and skills used, and how the human directing the process responds. We also demonstrated that using agentic AI workflow for software development (with its prompts and skills) can become a specification of the code that leads to cost-effective sustainability of the software.

## Metadata
- **Published**: 2026-09-16T08:21:09Z
- **Authors**: Ayesha Shafique, Barton P. MIller, Elisa R. Heymann
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18298v1)