---
title: Many Right Answers, One Training Example: Removing Responder Noise from GRPO for LLM Recommenders
url: http://arxiv.org/abs/2610.17771v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_05-57-20Z_ManyRightAnswers_OneTrainingExample_RemovingRespon.md
generated_at: 2026-10-14 00:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper addresses a fundamental flaw in reinforcement learning training for LLM-based recommenders: when training on Reddit threads that contain multiple valid replies naming different titles, the state-of-the-art Rank-GRPO method selects only one reply per training example, causing 85% of the advantage signal to reflect which reply happened to be drawn rather than the actual quality of the generated recommendation list. The authors propose ReMaRk, which instead scores every generated list against the union of all replies' titles and samples each request equally, effectively removing responder noise from the training signal. Across seven model backbones and three datasets, ReMaRk matches or exceeds Rank-GRPO's performance while requiring only 25–53% of the training steps, demonstrating a strictly cheaper and more principled approach to RL training with multiple valid answers.

## Key Takeaways
- Rank-GRPO's core weakness is that it treats each individual reply as a separate training example, so the policy gradient advantage is dominated by sampling noise—which specific reply was selected—accounting for 85% of its variance. This means the RL signal largely encodes "which answer was drawn" rather than "how good is the recommendation list," fundamentally corrupting the learning objective.
- ReMaRk reformulates the training unit from individual replies to entire requests: it aggregates all titles mentioned across every reply in a thread into a single ground-truth set, scores the generated list once against that union, and samples each request with equal probability. This eliminates the responder-selection variance and makes the reward signal reflect genuine list quality, while also reducing the number of RL steps needed by a factor of roughly 2 to 4.
- The approach generalizes beyond recommendation tasks: on ProtoQA, where approximately 100 humans provide answers to each question, the same joint-reward strategy improves performance, pointing to a broader principle that when multiple valid human answers exist, RL should reward the model against all of them jointly rather than against a randomly chosen subset.

## Context
Group Relative Policy Optimization (GRPO) has become a popular reinforcement learning recipe for fine-tuning large language models, particularly in domains like recommendation and question answering where human-generated ground truth is noisy and multi-valued. Prior work such as Rank-GRPO attempted to handle multiple valid answers by sampling one per training step, but this introduced a systematic bias that the authors quantify as 85% variance from responder selection. This paper sits at the intersection of RLHF methodology, recommendation systems, and the broader challenge of training generative models on crowdsourced or community-generated data, where the "correct" answer is inherently a set rather than a single string.

## Implications
For practitioners deploying LLM-based recommenders or any system trained on community-sourced ground truth, ReMaRk offers a concrete recipe that cuts GPU training costs by 47–75% while maintaining or improving accuracy, making RL fine-tuning far more accessible for smaller teams and faster iteration cycles. More broadly, the paper's central insight—that RL should train on the request and reward against the union of all valid answers—provides a simple, transferable rule for any RL pipeline dealing with multi-annotator or multi-response data, including open-domain QA, code generation with multiple valid solutions, and creative writing evaluation, potentially reshaping how the community designs reward functions for generative model training.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17771v1)
