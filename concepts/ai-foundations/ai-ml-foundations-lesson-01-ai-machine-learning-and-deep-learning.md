---
title: AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning
date: 2026-05-09
status: draft
tags: [lesson, ai, machine-learning, deep-learning, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/papers/1950-turing-computing-machinery-and-intelligence.md
  - raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md
  - raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
---

# Lesson 1: AI, Machine Learning, and Deep Learning

## Navigation
- Previous: AI/ML Foundations Landing Page
- Landing page: AI/ML Foundations Landing Page
- Next: Lesson 2: How an ML System Works

*Time budget: 90 to 150 minutes*

## Lesson overview

This lesson introduces the three terms that show up everywhere in modern AI discussions: artificial intelligence (AI), machine learning (ML), and deep learning. These terms are related, but they do not mean the same thing. By the end of the lesson, you should be able to tell them apart and understand how they fit together.

Modern AI products usually wrap these ideas in a larger system and interface, not just a standalone model. This lesson helps you see the building blocks beneath the interface.

A simple way to think about them is as a hierarchy. AI is the broadest term. It refers to systems that do tasks we usually associate with intelligence, such as recognizing patterns, making predictions, generating text, or planning actions. Machine learning is one way to build AI systems. Instead of writing every rule by hand, you give the system examples and let it learn patterns from data. Deep learning is a family of machine learning methods that use neural networks with many layers, which helps them learn more complex patterns.

If someone says "this is an AI system," that does not yet tell you how it works. It might be a rule-based system, a machine learning system, or a deep learning system. This lesson helps you tell the difference.

## Learning goals

By the end of this lesson, you should be able to:

- define artificial intelligence, machine learning, and deep learning in plain language
- explain how rule-based systems differ from learning systems
- describe why data matters so much in modern ML systems
- place generative AI inside the larger AI landscape
- give simple examples of when AI, ML, and deep learning are the right labels
- explain the Turing Test idea in your own words

## 1) Artificial intelligence is the umbrella term

Artificial intelligence is the broad category. It includes any system that performs a task we would normally associate with intelligent behavior. That can mean a chess engine, a fraud detector, a recommendation system, a chatbot, an image classifier, or a planning system.

The easiest way to understand AI is to think of it as the umbrella term for systems that make useful decisions, recognize patterns, or generate outputs in a way that seems intelligent. It does not mean the system is conscious or human-like. It only means the system performs a task that, if done by a person, would feel intelligent.

### A short history snapshot

AI has been around for decades. The earliest AI systems in the mid-twentieth century were rule-based. They followed explicit instructions written by humans. In 1950, Alan Turing published a paper asking "Can machines think?" He realized this question was too fuzzy to answer directly, so he proposed a practical test instead: the imitation game, later called the Turing test. He imagined a conversation where an interrogator tries to tell a human from a machine based only on written responses. If the interrogator cannot reliably tell them apart, the machine counts as "thinking" at least well enough for the purpose of the test. Turing's key insight was this: judge intelligence by behavior, not by biology. When a system produces outputs that people treat as intelligent, it is reasonable to call it intelligent for practical purposes.

### Where AI shows up around you

AI is already everywhere, though not all AI systems are powerful or flexible. Examples include:

- **Rule-based systems** that sort emails into folders based on fixed rules like "if the sender is your manager, label as Priority."
- **Search engines** that rank web pages by relevance and popularity.
- **Recommendation systems** that suggest movies, songs, or products based on your history.
- **Chatbots and writing tools** that generate text responses based on what you type.
- **Face detection** in photo apps, which finds where faces appear in a picture.
- **Navigation apps** that estimate travel time and suggest the fastest route.

Some of these rely on simple rules. Others rely on machine learning, where the system learns from data rather than following explicit instructions. Modern generative AI is a subset of machine learning. The important idea is that AI is a family of related approaches, not a single technology.

## 2) Rule-based systems versus learning systems

Older AI systems often depended on explicit rules. A developer wrote instructions like "if the email contains these words, mark it as spam." That approach works when the problem is narrow and the rules are easy to state.

But many real-world problems are messy. Spam messages change over time. Fraud patterns shift. Images vary in lighting, angle, and background. Human language is full of slang, ambiguity, and context. In these settings, a fixed rule set becomes fragile.

Machine learning solves this by learning from examples. Instead of hand-writing every decision rule, you give the system data and examples of the outcome you want. The model then finds patterns that help it make predictions on new inputs.

### A concrete contrast: spam detection

Scenario: imagine two ways to detect spam. In the rule-based version, you keep adding filters whenever a new spam trick appears. One week you block messages with "urgent account verification." The next week spammers change it to "Confirm your payment." The next week, the rules grow long, contradictory, and easy to break.

In the machine learning version, you train a model on thousands of examples of spam and non-spam messages. The model learns patterns such as unusual phrasing, suspicious links, misleading sender domains, and timing patterns that you might never notice or bother to codify. The approach works better for two reasons: it adapts automatically when new examples are added, and it captures subtle signals that are hard to express as rules.

### When rule-based systems still make sense

Rule-based systems are not obsolete. They are useful when:

- The rules are well understood and unlikely to change.
- Reliability must be absolute. You need a guarantee that a certain action will happen every time the condition is met, with zero exceptions.
- The problem is simple and predictable.

The choice between rules and learning usually comes down to whether the rules are clear and stable. If clarity and stability are missing, machine learning is usually the better path.

## 3) Machine learning is AI that learns from data

Machine learning is a subset of AI. It refers to systems that improve their performance on a task by learning patterns from data.

In practice, that means the system sees examples, adjusts its internal settings, and becomes better at making predictions or decisions. Those internal settings are often called parameters. You can think of them as the model's tunable numbers, which get updated as the model learns. The important idea is that the system is not just following a script. It is generalizing from examples, which means it is trying to apply what it learned in one set of examples to new ones.

### How the learning process works (at a high level)

There are three steps in nearly every ML project, no matter how complex:

1. **Training**: Feed the model examples of inputs and desired outputs. The model adjusts its internal settings, gradually improving its predictions.
2. **Testing**: Show the model new examples it has never seen. Check how often it gets the right answer.
3. **Use in production**: Put the tested model into a real product or service and monitor how it behaves with live data.

The cycle repeats. New data arrives. The model is updated or retrained. Performance is rechecked.

### What it means to generalize

Generalization means a model works on new examples, not just the ones it trained on. A model that only memorizes its training data will perform perfectly during training but fail in the real world. Good training avoids this by:

- Using enough examples to cover different situations.
- Testing on data that was not used during training.
- Keeping the model from memorizing noise patterns that do not reflect true signals.

Scenario: a streaming service recommends a movie. It is not just guessing randomly. It has learned from many examples of what people watched, skipped, rated, or replayed. It uses those patterns to make a prediction about what you might like next. The system cannot predict your preferences perfectly, but it gets better over time as more behavior data flows in.

## 4) Deep learning is a family of machine learning methods

Deep learning is a subset of machine learning. It uses neural networks, which are models made of connected layers. Each layer transforms the input a little more and passes it forward, so the model can build up a more useful internal representation of the data.

The word "deep" refers to the number of layers. More layers let the model build richer representations. A shallow model might notice simple patterns. A deep model can learn more abstract features by combining simpler ones.

### A layer-by-layer analogy

Think of how you recognize a face in a crowd:

- **First layers** in an image network might detect edges and corners.
- **Middle layers** might combine edges into basic shapes like circles and lines.
- **Later layers** might assemble shapes into features like eyes, noses, and mouths.
- **Final layers** might combine those features into a recognition of a specific person.

Each layer does not work alone. They pass information along, and the model learns the right way to pass it through training.

### Why "deep" changed performance

Deep learning became useful at scale when:

- **Data scales up**: More examples give deep networks something richer to learn.
- **Hardware improves**: Graphics processing units (GPUs) make training large networks affordable.
- **Algorithms mature**: Techniques like backpropagation let models learn which weights matter.

When these align, deep networks outperform simpler methods on tasks like image recognition, speech transcription, and language understanding. The key takeaway is not that deep learning is always best, but that deep networks shine when the data is rich, the task is complex, and the training resources are sufficient.

Scenario: think of a photo app that recognizes your dog. A shallow system might struggle if the dog is partly hidden, turned sideways, or sitting in different lighting. A deep learning model can learn many layers of visual features, which makes it better at recognizing the same dog across varied photos.

## 5) Why data changed everything

The modern rise of machine learning and deep learning is not only about clever algorithms. It is also about data and compute. AI and ML advanced dramatically once large-scale digital data and stronger hardware became available.

### Data as the true bottleneck

Algorithms have improved steadily for decades. The jump in performance around 2010 and beyond came mainly from two factors:

- Massive datasets became available (web text, photos, videos, sensor data).
- Cheaper computation made it possible to train on those datasets.

When a model learns from a small dataset, it mostly memorizes what it sees. When it learns from a large dataset, it picks up general patterns that apply beyond those examples. Data quality, variety, and coverage determine how well the model will behave in new situations.

### Data pipelines and version control

Modern ML systems depend on data pipelines and versioned datasets. A data pipeline is the path data follows from its source into the model. Versioned datasets are saved copies of data that let teams track what changed over time. If the data is poor, incomplete, biased, or stale, the model will struggle no matter how impressive the method looks.

Scenario: a hospital wants an AI system to help triage images. If the training data comes mostly from one type of scanner or one demographic group, the model may work well in the lab but fail in the real world. The lesson is simple: the quality of the learning system is tightly tied to the quality of the data it learns from.

## 6) Where generative AI fits

Generative AI is AI that creates new content, such as text, images, audio, video, or code. It is usually powered by machine learning, especially deep learning.

This is where the course's broader AI story becomes visible. AI is the umbrella term. ML is the learning method. Deep learning is a powerful family of ML techniques. Generative AI is one major application area built on top of those methods.

The source pages describe generative AI as relying on deep learning models that learn patterns in large datasets and then generate new content in response to prompts. A prompt is the input you give the model, such as a question, instruction, or starting phrase. Large language models, or LLMs, are a major example. An LLM is a model trained on large text datasets so it can generate and transform language. Many chatbots and writing tools are built on top of these models.

Some teams also talk about foundation models. A foundation model is a large general-purpose model that can be adapted to many tasks. You do not need that term to understand the lesson, but it helps explain why one model can be reused in different applications.

### How generative AI differs from other AI

- **Classification AI** sorts or labels input (is this image a cat or a dog?).
- **Prediction AI** forecasts a value (what will the stock price be tomorrow?).
- **Generative AI** creates new output from scratch (write an email draft based on these bullet points).

Generative AI does not merely process existing information. It produces new combinations of patterns that it learned during training. This is why the quality and diversity of the training data matter so much: a model can only generate what it has seen patterns of during training.

Scenario: if you ask a chatbot to summarize a report, draft an email, or explain a concept, it is not retrieving a fixed answer from a lookup table. It is generating a response based on learned patterns in language.

## 7) The big picture

The relationships should now be clear. AI is the broad field of building systems that behave intelligently. Machine learning is one way to build AI by learning from data instead of relying only on hard-coded rules. Deep learning is a family of machine learning methods that uses layered neural networks. Generative AI is an application area that creates new content using those learned patterns.

### The hierarchy summarized

A helpful way to remember the relationships:

- **All deep learning is machine learning**, but not all machine learning is deep learning.
- **All machine learning is AI**, but not all AI is machine learning.
- **Generative AI is an application area built on top of machine learning that creates rather than classifies or predicts.**

This hierarchy matters because people often use the terms loosely. A product can be called "AI" even when it is mostly rule-based. A model can be called "ML" even when it is actually deep learning. A chatbot can be called "generative AI" even though it is built on top of an LLM, which is itself a deep learning model.

Being precise about the terms helps you understand what a system can do, how it was built, and what its limits are.

## Closing summary

The main idea in this lesson is that AI is the umbrella term, machine learning is a way to build AI by learning from data, and deep learning is a family of machine learning methods that uses layered neural networks. Modern generative AI sits on top of that stack. If you can keep those relationships straight, the rest of the course becomes much easier to follow.

## Quick self-check

Answer these in your own words:

1. What is the difference between an AI system and a rule-based system?
2. Why did Turing propose the imitation game instead of trying to define "thinking"?
3. Why is machine learning useful when the rules are hard to write by hand?
4. What does "deep" mean in deep learning, and why does it matter?
5. How do training and testing differ, and why is generalization important?
6. Where does generative AI fit in the AI hierarchy?

## Suggested follow-up reading

- [[1950-turing-computing-machinery-and-intelligence|Computing Machinery and Intelligence (Turing, 1950)]]
- /home/rich/wiki/ai-research/raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md
- /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
