---

title: Learning the Error Patterns of Language Models
published: "2026-05-27T11:28:38Z"
authors: Jinwoo Kim, Taylor Berg-KirkPatrick, Loris D'Antoni
url: http://arxiv.org/abs/2605.28328v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Learning the Error Patterns of Language Models



**Source**: [Original Paper](http://arxiv.org/abs/2605.28328v1)
## Abstract
When generating outputs for domains with specific validity constraints (e.g., a program should compile), LLMs often fail in a small number of focused ways: for example, by using Python function names when generating TypeScript. We observe that these error patterns can be represented using a small number of constraints that can be learned in practice. We propose \emph{prefix filters}, which are per-domain-and-LLM symbolic functions, as objects to capture the error patterns, Palla as an algorithm to learn prefix filters efficiently in practice, and implement Palla. Prefix filters learned by Palla i) help us quantitatively analyze the error patterns of LLMs, and ii) can be used to constrain the outputs of a model via constrained sampling algorithms. For example, Palla boosts compile rates for Qwen2.5-1.5B on TypeScript generation, by over 60%, allowing Qwen2.5-1.5B to achieve similar performance to Llama3.1-8B unconstrained.

## Metadata
- **Published**: 2026-05-27T11:28:38Z
- **Authors**: Jinwoo Kim, Taylor Berg-KirkPatrick, Loris D'Antoni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28328v1)