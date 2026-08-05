---
title: 'AI/ML Foundations Lesson 12 - Prompting: Guiding Model Behavior'
date: 2026-05-06
status: draft
tags: [lesson, prompting, prompt-engineering, llm, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-04-28_What_is_generative_AI__-_IBM.md
  - raw/articles/2026-05-04_WhatisgenerativeAI_-IBM.md
  - raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
  - raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 12: Prompting: Guiding Model Behavior



**Source**: [Original Article](https://example.com/placeholder)

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-13-agents-and-agentic-workflows.md|AI/ML Foundations Lesson 13 - Agents and Agentic Workflows]] — 2 title terms overlap; shared tags: foundations, lesson, llm; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 2 title terms overlap; shared tags: foundations, lesson, llm; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-16-deployment-scaling-and-what-comes-next.md|AI/ML Foundations Lesson 16 - Deployment, Scaling, and What Comes Next]] — 2 title terms overlap; shared tags: foundations, lesson, llm; 5 backlinks

## Navigation
- Previous: [[ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|Lesson 11: Large Language Models: The Modern AI Interface]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-13-agents-and-agentic-workflows.md|Lesson 13: Agents and Agentic Workflows]]


Time budget: 90 to 120 minutes

## Lesson overview

Prompting is the practical skill of telling a large language model, or LLM, what you want it to do. In real systems, prompting often blends with context engineering, which means choosing the right instructions, examples, source text, and constraints so the model has the information it needs. A prompt can be a question, an instruction, an example, a constraint, or a mix of all four. In everyday use, the prompt is the interface between the person and the model.

This lesson looks at the basic prompting ideas you will use again and again: instructions, context, examples, constraints, zero-shot and few-shot prompting, revision, and when to add retrieval or other system support. The goal is not to find a magic phrase. The goal is to learn how to give the model enough direction to be useful.

The main idea is simple: prompting is a repeatable skill, and clearer prompts usually produce better output, but the right context matters just as much.

## Learning goals

By the end of this lesson, you should be able to:

- explain what prompting is and why it matters
- show how instructions, examples, constraints, and context shape model output
- distinguish zero-shot and few-shot prompting at a high level
- treat prompt refinement as an iterative skill
- recognize how prompting fits into everyday LLM use

## 1) A prompt is the input that steers the model

A prompt is the text you give the model to guide its response.

It can be short, like “Summarize this,” or detailed, like “Summarize this for a non-technical manager in three bullets and avoid jargon.” The prompt is the steering wheel for the interaction. It tells the model what kind of response you want and what boundaries to stay inside.

IBM describes generative AI as AI that creates content in response to a user’s prompt or request. That is why prompting sits at the center of generative AI use: without a prompt, there is no direction.

A helpful analogy is giving directions to a capable assistant. If you only say “help me write,” the destination is vague. If you say “write a polite, two-paragraph email asking to reschedule tomorrow’s meeting,” the assistant has a much clearer target.

Scenario: if you ask “What is machine learning?” you may get a broad answer. If you ask “Explain machine learning to a 12-year-old using one analogy,” you will get a very different result.

## 2) Good prompts use several kinds of guidance

Prompts work best when they include the right mix of guidance.

An instruction tells the model what to do. An example shows the pattern you want. A constraint limits the output, such as length, tone, or format. Context gives the model the background information it needs to answer well.

That mix is important because language models are flexible. They can adapt to many tasks, but they need enough direction to know which task you actually want.

**Prompt layering**: In real systems, prompts often have multiple layers:
- **Persistent instructions**: System-level rules that apply across sessions (e.g., "always cite sources")
- **Task-specific prompts**: Instructions for the current request (e.g., "summarize this article")
- **Context augmentation**: Source text, examples, or constraints added to the prompt

Scenario: “Write a project update” is vague. “Write a short project update for executives, mention the milestone, the risk, and the next step, and keep it under 100 words” is much more useful.

Think of it like briefing a contractor. A one-line request may produce something usable but generic. A request with goals, examples, and constraints is more likely to produce something that matches the job.

## 3) Zero-shot and few-shot prompting are simple patterns

Zero-shot prompting means asking the model to do a task without giving examples.

Few-shot prompting means giving a few examples first so the model can imitate the pattern. The examples can show the format, the tone, or the kind of reasoning you want.

You do not need to memorize the terminology yet. The practical idea is simple: if the first attempt is too loose, add examples.

A good example is turning rough notes into meeting minutes. If you give the model a sample of the format you want, it often follows that pattern much better than it would from instructions alone.

Scenario: if you want the model to turn messy bullet points into a polished status update, one example of a well-written status update can improve the result dramatically.

Concrete example:

- Zero-shot: “Summarize this article in three bullets for a non-technical manager.”
- Few-shot: “Here are two examples of the summary style I want... Now summarize this article in the same style.”

## 4) Prompt quality changes output quality

Prompting is not just about being polite or clever. It is about reducing ambiguity.

If the task is underspecified, the model has to guess what you want. If you clearly specify the audience, format, tone, and goal, the output usually becomes much more useful.

That is one reason modern AI feels powerful. The model is flexible enough to follow natural-language instructions, and the better you express those instructions, the better the interaction becomes.

Scenario: “Explain this issue” might produce a generic answer. “Explain this issue to a customer in simple language, avoid blame, and suggest one next step” gives the model a much clearer target.

A useful mental model is that the prompt is not only content. It is also control.

## 5) Prompt refinement is iterative

Good prompting usually comes from revision, not perfection on the first try.

You ask for a result, inspect the answer, notice what is missing or wrong, then change the prompt. Maybe you add a constraint, clarify the audience, or provide an example. That loop is the real skill.

IBM notes that prompt engineering can involve iteratively refining prompts until they consistently deliver the results you want. That is a good description of what people actually do in practice.

The MIT article also points out that as tasks get longer and more complex, context becomes increasingly important. That makes prompt iteration even more valuable, because longer tasks often need more explicit guidance.

In IBM’s broader lifecycle framing, prompting sits in the generate phase after the model has already been trained and tuned. That is why better prompts often help, but they do not replace a well-trained model.

Scenario: if a summary is too long, ask again for three bullets only. If the tone is too formal, say “make it warmer and more conversational.” If the answer misses a key point, add that point to the prompt and try again.

## 6) Prompting works best when it matches the model’s strengths

A good prompt does not fight the model. It uses the model’s strengths.

LLMs are good at rewriting, summarizing, classifying by instruction, brainstorming alternatives, and following style examples. They are weaker when the prompt is ambiguous or when the task requires exact factual recall without enough supporting context.

That is why clear prompting matters so much. You are not trying to force the model into one rigid shape. You are trying to give it enough structure that its language ability can be useful.

Scenario: a coding assistant may be excellent at rewriting a function, but if you want a very specific output format, you should show that format explicitly in the prompt.

## 7) Prompting is part of a workflow, not just a single message

Prompting is not only about one-off chat. It is the first step in a workflow.

A user may prompt a model to draft text, then refine it, then ask for a different tone, then ask for a shorter version. In other words, the prompt becomes part of a conversation with the system.

This is why prompt design matters in real products. It shapes the user experience, output quality, and reliability of the whole system.

The best prompting systems often include guardrails, which are limits that keep the model focused on trusted sources or allowed behaviors. IBM also notes that retrieval augmented generation, or RAG, can help by bringing in relevant external sources so the model has better context and more current information.

Scenario: in a support tool, a carefully designed prompt can help the model produce a polite answer, include the right policy detail, and stay within company guidelines.

## 8) Prompting and consistency are related

Generative models can produce different outputs from the same prompt. That is not always bad, but it can be a problem when a task needs stable behavior.

IBM points out that because generative models are probabilistic, the same inputs can lead to different outputs. Prompt engineering helps reduce that variation by making the prompt clearer and more structured.

This is important in customer support, compliance, and internal tooling, where people often want predictable results. In those cases, the prompt may need to specify tone, format, sources, and refusal behavior more carefully than a casual chat prompt would.

Scenario: if you want a customer-service reply to always include the next step, the prompt should say so directly instead of hoping the model remembers to include it.

## 9) Prompts can use context to unlock better answers

Context is the surrounding information the model needs in order to answer well.

A prompt with no context may be too thin. A prompt with the right context gives the model something to work with. That context can include background, previous messages, source text, or examples of the desired style.

The MIT article emphasizes that context windows matter because they determine how much information the model can consider at once. That means prompting is partly about choosing the right information to include and partly about keeping the request focused.

Scenario: if you ask a model to rewrite an email, including the email itself and the tone you want is much more effective than asking for a rewrite with no source text at all.

## 10) Prompting and context engineering are different layers

Prompting is the immediate instruction you give the model. Context engineering is the broader job of assembling the right task description, examples, source material, and constraints around that instruction.

That means some improvements come from rewriting the prompt, while others come from changing what the model is allowed to see. If the model keeps missing a detail, adding the right source text may help more than making the wording slightly nicer.

Scenario: a support reply improves when you add the actual policy excerpt, not just a more polite instruction.

## 11) When prompting is enough vs when you need more

Not every task needs an agent or complex system. Here's how to decide:

**Prompting alone works for**:
- Simple questions with clear answers
- Creative writing within known domains
- Summarization of provided text
- Classification or formatting tasks

**Add retrieval (RAG) when**:
- The model needs current information beyond its training data
- You need to ground responses in specific documents
- Accuracy on factual details is critical

**Add tools when**:
- The task requires interacting with external systems (search, databases, APIs)
- You need the system to perform actions, not just generate text
- Results depend on real-time data or state changes

**Add an agent harness when**:
- The workflow has multiple steps that depend on each other
- You need planning, iteration, and recovery from failures
- State must persist across interactions
- Safety requires sandboxing, approvals, or audit trails

Scenario: a simple summarization task needs only a prompt. A research assistant that gathers sources, compares them, drafts sections, and revises based on feedback needs an agent harness with tools and memory.

## 12) What to remember without the jargon

Prompting is simply the skill of giving the model clear, useful direction.

If you want better output, be more specific about the task, the audience, the format, the tone, and the boundaries. Then refine based on the result.

That is the beginner version of prompt engineering: clear instructions, good examples, helpful context, and steady iteration.

Context engineering is the broader task of assembling the right source material and constraints around the prompt.

## Closing summary

Prompting is the practical skill that turns a language model from a general generator into a useful tool. A prompt tells the model what to do, what style to use, and what limits to respect. When prompts are vague, outputs are usually vague. When prompts are clear and well supported, outputs are usually much better.

That is why prompting matters so much in real AI systems. It is not a trick. It is a repeatable craft that improves with practice, and it is one of the main ways users shape model behavior.

## Key takeaways

- A prompt is the input that steers the model.
- Instructions, examples, constraints, and context all affect output.
- Zero-shot means no examples; few-shot means a few examples.
- Prompt refinement is iterative.
- Guardrails and RAG can improve reliability in real systems.
- Prompting and context engineering both matter.
- Clear prompts usually produce better results.

## Quick self-check

Answer these in your own words:

1. What is a prompt?
2. Why do examples help?
3. What is the difference between zero-shot and few-shot prompting?
4. Why is prompt refinement iterative?
5. What information should a strong prompt usually include?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-04-28_What_is_generative_AI__-_IBM.md
- /home/rich/wiki/ai-research/raw/articles/2026-05-04_WhatisgenerativeAI_-IBM.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
- /home/rich/wiki/ai-research/raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
