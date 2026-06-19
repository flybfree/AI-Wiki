---
title: AI/ML Foundations Course Map
date: 2026-05-06
tags: [course-map, machine-learning, artificial-intelligence, foundations]
status: draft
source_pages:
  - ilya-sutskever-reading-list.md
  - ilya-sutskever-reading-list-study-order.md
---

## Summary

Placeholder summary — please add a concise summary.


# AI/ML Foundations Course Map



**Source**: [Original Article](https://example.com/placeholder)
Concept-first, math-light sequence for a basic understanding of machine learning and artificial intelligence.

Design principles:
- Use plain language
- Focus on concepts, not formulas
- Build from broad ideas to specific model families
- Use the Ilya Sutskever reading list as the backbone, then layer in wiki sources for context and systems thinking

## Legend
- CHAPTER = should become a core lesson in the final course
- BACKGROUND = supporting context, recap, or optional enrichment

## 1) AI, Machine Learning, and Deep Learning
Flag: CHAPTER
Goal:
- Define artificial intelligence, machine learning, and deep learning
- Explain the difference between rule-based systems and learning systems
- Place ML inside the broader AI landscape

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md
2. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md

## 2) How an ML System Works
Flag: CHAPTER
Goal:
- Describe the pipeline: data -> training -> evaluation -> deployment -> monitoring
- Understand that ML is a system, not just a model
- Recognize the major components of an ML architecture

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## 3) Data as the Foundation of Learning
Flag: CHAPTER
Goal:
- Explain why data quality matters
- Describe collection, cleaning, transformation, integration, and splitting
- Distinguish training, validation, and test data

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## 4) Supervised Learning: Learning from Labels
Flag: CHAPTER
Goal:
- Explain learning from labeled examples
- Distinguish classification from prediction/regression
- Understand how labels guide learning

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## 5) Unsupervised Learning: Finding Hidden Structure
Flag: CHAPTER
Goal:
- Explain learning without labels
- Introduce clustering, grouping, and anomaly detection
- Understand when the model is discovering structure rather than predicting known answers

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## 6) Neural Networks: The Core Building Blocks
Flag: CHAPTER
Goal:
- Understand neurons, layers, weights, and activations conceptually
- Explain why deeper networks can represent more complex patterns
- Build intuition for feature learning

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-27_Neural_Network_Architectures_-_GeeksforGeeks.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## 7) Convolutional Networks for Vision
Flag: CHAPTER
Goal:
- Explain why convolutional neural networks are good for images
- Understand filters, feature maps, and pooling conceptually
- Recognize why different data types need different architectures

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/ilya-sutskever-reading-list-study-order.md
4. /home/rich/wiki/ai-research/ilya-sutskever-reading-list.md

## 8) Recurrent Networks and LSTMs
Flag: CHAPTER
Goal:
- Explain why order matters in language, speech, and time series
- Understand recurrence and memory at a conceptual level
- Learn why LSTMs were a major step forward

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-27_Neural_Network_Architectures_-_GeeksforGeeks.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
3. /home/rich/wiki/ai-research/ilya-sutskever-reading-list-study-order.md
4. /home/rich/wiki/ai-research/raw/papers/2026-05-06_understanding_lstm_networks.md

## 9) Attention and Transformers
Flag: CHAPTER
Goal:
- Explain the problem attention solves
- Understand the conceptual shift from recurrence to attention
- Recognize why transformers became the dominant language architecture

Source order:
1. /home/rich/wiki/ai-research/ilya-sutskever-reading-list.md
2. /home/rich/wiki/ai-research/ilya-sutskever-reading-list-study-order.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
4. /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md

## 10) Generative AI: Creating New Content
Flag: CHAPTER
Goal:
- Define generative models in non-mathy terms
- Distinguish generation from classification and prediction
- Understand why generative AI is a special case of ML

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
3. /home/rich/wiki/ai-research/ilya-sutskever-reading-list.md

## 11) Large Language Models: The Modern AI Interface
Flag: CHAPTER
Goal:
- Explain what an LLM is and what it is trained to do
- Understand prompts, tokens, and context windows at a high level
- See why modern AI systems feel more capable than older chatbots

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md
3. /home/rich/wiki/ai-research/ilya-sutskever-reading-list.md
4. /home/rich/wiki/ai-research/ilya-sutskever-reading-list-study-order.md

## 12) Prompting: Guiding Model Behavior
Flag: CHAPTER
Goal:
- Explain what prompting is and why it matters
- Show how instructions, examples, constraints, and context shape model output
- Introduce prompt refinement as an iterative skill rather than a magic trick

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-28_What_is_generative_AI__-_IBM.md
2. /home/rich/wiki/ai-research/raw/articles/2026-05-04_WhatisgenerativeAI_-IBM.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
4. /home/rich/wiki/ai-research/raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md

## 13) Agents and Agentic Workflows
Flag: CHAPTER
Goal:
- Define what an AI agent is in practical terms
- Explain how tools, planning, memory, and iteration differ from plain prompting
- Recognize where agents help and where they add complexity or risk

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-26_Qwen_3_6_27B_Arrives_with_GGUF_Support_and_Local_M.md
3. /home/rich/wiki/ai-research/raw/articles/2026-05-01_GenerativeAInewsandanalysis_TechCrunch.md
4. /home/rich/wiki/ai-research/raw/summaries/SUMMARY_2026-04-29_Inaugural_Adobe_Creators__Toolkit_Report__86_Perce.md

## 14) Choosing the Right Architecture for the Task
Flag: CHAPTER
Goal:
- Match common problem types to common model families
- Explain why vision, language, time-series, clustering, and generation use different architectures
- Build task-to-architecture intuition

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-27_Neural_Network_Architectures_-_GeeksforGeeks.md
3. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
4. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md

## 15) Evaluation, Overfitting, and Limits
Flag: CHAPTER
Goal:
- Understand why models can look good in training but fail in practice
- Explain validation, testing, and monitoring in plain language
- Recognize limitations such as brittleness, hallucination, bias, and domain drift

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
4. /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md

## 16) Deployment, Scaling, and What Comes Next
Flag: CHAPTER
Goal:
- Understand that ML systems need infrastructure, monitoring, and maintenance
- Explain scaling in concept, including why bigger models need more coordination
- Introduce the idea that modern AI is moving toward longer-running, more capable systems

Source order:
1. /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
2. /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
3. /home/rich/wiki/ai-research/raw/papers/2026-05-06_gpipe_easy_scaling_with_micro_batch_pipeline_parallelism.md
4. /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
5. /home/rich/wiki/ai-research/raw/articles/2026-04-28_Generative_AI_-_Wikipedia.md

## Suggested chapter/background split
Core chapters:
- 1 through 16

Background-only support pages or sidebars:
- /home/rich/wiki/ai-research/ilya-sutskever-reading-list.md
- /home/rich/wiki/ai-research/ilya-sutskever-reading-list-study-order.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md

## Notes
- This outline intentionally avoids math-heavy treatment.
- The final lesson order is designed to move from basic concepts to modern AI systems.
- The Ilya Sutskever reading list is the backbone for the middle of the course, especially sequence models, attention, and generative systems.
