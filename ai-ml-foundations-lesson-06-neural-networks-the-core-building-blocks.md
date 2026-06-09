---
title: AI/ML Foundations Lesson 06 - Neural Networks: The Core Building Blocks
date: 2026-05-06
status: draft
tags: [lesson, neural-networks, deep-learning, layers, activations, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-04-27_Neural_Network_Architectures_-_GeeksforGeeks.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
  - raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
---

# Lesson 6: Neural Networks: The Core Building Blocks

## Navigation
- Previous: [[ai-ml-foundations-lesson-05-unsupervised-learning-finding-hidden-structure.md|Lesson 5: Unsupervised Learning: Finding Hidden Structure]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-07-convolutional-networks-for-vision.md|Lesson 7: Convolutional Networks for Vision]]


Time budget: 90 to 120 minutes

## Lesson overview

If Lesson 4 showed how machine learning can learn from labels and Lesson 5 showed how it can discover hidden structure without labels, this lesson explains the core machinery that makes many modern ML systems work: neural networks.

The same building blocks show up later inside transformers, sequence models, and agent systems.

Neural networks are not magic, and they are not a literal copy of the human brain. They are layered models that learn by transforming input data through a sequence of small computational steps. Each step does only a little work on its own, but when many of them are stacked together, the network can learn surprisingly complex patterns.

At a high level, a neural network takes an input, pushes it through one or more hidden layers, and produces an output. During training, the network adjusts internal settings called weights and biases so its output gets closer to the correct answer.

This lesson builds intuition for the parts that make that possible: neurons, layers, activations, depth, feature learning, and the difference between the network design and the trained model. Deep learning means using neural networks with many layers so the model can learn more abstract features from simpler ones.

## Learning goals

By the end of this lesson, you should be able to:

- explain what a neural network is at a conceptual level
- describe the roles of neurons, layers, weights, biases, and activations
- distinguish a shallow network from a deep network
- explain why hidden layers matter
- build intuition for feature learning
- tell the difference between an architecture and a trained model

## 1) Why neural networks matter

Some machine learning problems are simple enough that a straight-line rule works well. Others are not. Real-world data often contains messy boundaries, overlapping patterns, and interactions between many inputs. Neural networks are useful because they can learn those more complicated relationships.

A classic single-layer perceptron, the simplest kind of neural model, can only solve very limited problems. It works well when the data is linearly separable, meaning a single straight decision boundary can separate the classes. But many real tasks are not that neat. A photo of a cat versus a dog, for example, is not something you can usually separate with one simple line through pixel space.

That is where hidden layers and nonlinear activations become important. They let the model bend and reshape the input space until the problem becomes easier to express.

Scenario: imagine trying to sort mixed puzzle pieces. If the pieces are all obviously square or round, a simple rule works. If they are similar in shape, color, and size, you need more than one rule. A neural network gives you that extra flexibility.

## 2) A neuron is a tiny transformation step

A neuron is the basic unit in a neural network. It receives one or more inputs, combines them with learned weights, adds a bias, and then passes the result through an activation function.

You can think of a neuron as a tiny filter. It does not make a full decision on its own. Instead, it asks, “How much should I care about each input, and should I pass this signal forward?”

If one input matters more than another, its weight will be larger. If the network needs a little extra shift in the decision, it uses a bias. Then the activation function decides how strongly the neuron should respond.

Scenario: in a spam filter, one neuron might pay close attention to the sender’s domain, another might care about urgent language, and another might react to suspicious links. None of them solves the whole problem alone, but together they help the network detect spam.

## 3) Weights, biases, and activations do different jobs

Weights are the knobs that control importance. A high weight means a signal matters a lot. A low weight means it matters less. Training adjusts those weights so the model learns which patterns are useful.

Biases help shift the output. If weights are the strength of each input, the bias is the network’s built-in offset. It gives the model more flexibility, especially when the data does not fit a neat pattern centered on zero.

Activation functions add nonlinearity. That is the key idea. Without nonlinearity, stacking more layers would not buy you much. The network would still behave like a very limited linear system. With activations, each layer can reshape the signal in a more interesting way.

You do not need to memorize activation formulas yet. The beginner-level idea is that activations decide how strongly a neuron fires after seeing its input.

Scenario: if a network is learning to distinguish cats from not-cats, it needs to react to many kinds of clues — edges, shapes, textures, and combinations of those clues. Activation functions make it possible for the network to combine those clues in a flexible way.

## 4) Layers let the network build complexity step by step

Neural networks are layered systems. The input layer receives the raw data. Hidden layers transform that data. The output layer produces the final prediction.

This layered structure is what makes neural networks so useful. Early layers tend to learn simple features. Later layers combine those simple features into more abstract ones. In other words, the network does not jump directly from raw input to final answer. It builds the answer in stages.

That staged processing is similar to a workshop with multiple stations. One station cuts material, another shapes it, another assembles it, and the last station finishes it. Each step is simpler than the whole, but together they produce something useful.

Scenario: if the input is a photo, one layer may notice edges, another may notice corners, another may notice shapes, and a later layer may combine those signals into an object like a face or a car.

## 5) Hidden layers are where much of the learning happens

Hidden layers sit between the input and output. They are called hidden because you do not directly observe them as the answer, but they carry the internal representation the network is building.

This is one of the most important ideas in deep learning: the network can learn intermediate features on its own. You do not always have to hand-design the important features in advance. The network can discover useful representations during training.

That is why hidden layers matter. A single-layer model can only do a limited amount of work. Once you add hidden layers with nonlinear activations, the network can learn much richer mappings from input to output.

Scenario: if a network is learning house prices, early layers might notice square footage, neighborhood hints, and room counts. Later layers might combine those signals into a more useful estimate of value.

## 6) Deep networks can represent more complex patterns

A shallow network has few layers. A deep network has many. More depth gives the model more stages for transformation, which increases its expressive power.

That does not mean deeper is always better. A deeper model may be harder to train, more expensive to run, and easier to overfit if the data is not good enough. But when the task is complex, depth can be a major advantage.

The intuition is simple: some problems are easier to solve if you can break them into multiple subproblems. A deep network can do that internally.

Scenario: a voice assistant may need to process sound, turn it into words, infer meaning, and then generate a response. Those are different levels of abstraction, and a deeper model gives the system more room to represent them.

## 7) Training means adjusting the internal parameters

Training a neural network means changing its weights and biases so its predictions improve.

At a high level, the network makes a guess, compares that guess to the correct answer, and then updates itself to reduce the error. The specific mechanism that moves the error signal backward through the network is called backpropagation. Backpropagation is the learning process that tells each layer how it should change.

You do not need the algorithm details yet. The main idea is that training is not about storing answers. It is about tuning the network until its internal settings produce better outputs.

Scenario: if a vision model keeps confusing wolves and huskies, training nudges the internal settings so the model becomes less likely to repeat that mistake.

## 8) Feature learning is what makes neural networks powerful

Feature learning means the model learns which patterns matter instead of relying only on hand-crafted rules.

Before deep learning became dominant, many systems depended on humans to design features manually. Engineers would decide which measurements, shapes, or signals to feed into a model. Neural networks reduced that burden by learning useful internal features from data.

This is a big shift. The model is not just matching inputs to outputs. It is learning a representation of the problem that makes the task easier to solve.

Scenario: in an image task, a human might manually decide to measure edges or color histograms. A neural network can learn its own internal representation, often combining raw signals into a more useful set of features than a hand-built pipeline would produce.

## 9) Architecture and model are not the same thing

The architecture is the design of the network. It tells you how many layers there are, what kinds of layers they are, and how information flows through them.

The model is the trained result of that design after it has learned from data.

That distinction matters because two systems can share the same architecture but end up with different models after training on different data. The blueprint may be the same, but the finished result depends on the training experience.

Scenario: two houses can use the same floor plan but look completely different once they are furnished and lived in. The floor plan is the architecture. The lived-in house is the trained model.

## 10) Neural networks are the base family behind later architectures

Later lessons in this course build on the same core ideas.

Convolutional neural networks (CNNs) add structure that works especially well for images. Recurrent neural networks (RNNs) add a way to handle sequence and memory over time. Transformers replace recurrence with attention. All of those are specialized neural network architectures.

So this lesson is not a detour. It is the foundation. Once you understand neurons, layers, weights, biases, activations, and training, the rest of deep learning becomes much easier to place.

Scenario: learning neural networks is like learning the grammar of a language before reading different books written in that language. The books may differ, but the underlying grammar keeps showing up.

## Closing summary

Neural networks turn a simple idea into a powerful one: learn a chain of transformations, then tune that chain until it maps inputs to useful outputs. The individual parts are small, but the combination of layers, nonlinear activations, and training gives the model the flexibility to solve complicated problems.

That is why neural networks became the core building block for so many later architectures. CNNs, RNNs, and transformers all inherit the same basic idea of learning useful internal representations, even though they arrange the pieces differently.

## Key takeaways

- Neural networks are layered models that learn from data.
- Neurons combine inputs using weights, biases, and activations.
- Hidden layers let the network learn intermediate representations.
- Deeper networks can represent more complex patterns, but depth is not automatically better.
- Training adjusts internal parameters, usually with backpropagation.
- Architecture is the design; the model is the trained instance.
- CNNs, RNNs, and transformers all build on the same core neural network ideas.

## Quick self-check

Answer these in your own words:

1. What is a neural network trying to do?
2. What do weights, biases, and activation functions each contribute?
3. Why are hidden layers important?
4. What is the difference between shallow and deep networks?
5. What is backpropagation in plain language?
6. How is an architecture different from a trained model?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-04-27_Neural_Network_Architectures_-_GeeksforGeeks.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
