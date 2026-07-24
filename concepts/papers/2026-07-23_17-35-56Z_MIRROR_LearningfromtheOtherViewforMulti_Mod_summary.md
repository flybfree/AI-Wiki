# Summary: 2026-07-23_17-35-56Z_MIRROR_LearningfromtheOtherViewforMulti_ModalReaso.md
Saved: 2026-07-24 02:59
Source: 2026-07-23_17-35-56Z_MIRROR_LearningfromtheOtherViewforMulti_ModalReaso.md
Model: None

---

## Summary  
The paper investigates why vision‑language models (VLMs) often perform inconsistently across different modalities when solving the same geometric reasoning tasks, even though equivalent text, diagram, and combined text+diagram views exist. It argues that these divergent behaviors reveal complementary reasoning paths and failure modes that are not fully exploited by conventional multimodal post‑training. To address this gap, the authors introduce ODA‑Data, a high‑quality paired dataset containing text‑dominant, image‑dominant, and combined view representations of geometry problems, together with splits for training and evaluating modality‑dependent performance. Their contribution is MIRROR—a reinforcement‑learning framework that leverages self‑supervised learning to align the outputs of all views by selecting the best‑performing view as a teacher and training the others via a reverse‑KL objective.

## Key Contributions  
- **Finding 1:** Construction of ODA‑Data, a dataset that provides paired multimodal geometry problems in three complementary view forms (text‑only, image‑only, combined) enabling systematic study of modality‑dependent reasoning.  
- **Finding 2:** Development of MIRROR, a reinforcement‑learning algorithm that uses a reverse‑KL divergence to make all views converge toward the most accurate teacher view, thereby learning from “the other view.”  
- **Finding 3:** Demonstration that MIRROR yields higher accuracy and more consistent behavior across modalities compared with standard RL baselines on geometry reasoning benchmarks.

## Methodology  
The authors first assembled ODA‑Data by curating a set of geometry problems where each problem is represented in three distinct view types, ensuring the same underlying knowledge is encoded differently. For training, MIRROR operates as follows: given a model’s predictions under all views for a single problem instance, the system computes their scores, selects the highest‑scoring view as the teacher, and then updates the other views using a reverse‑KL loss that forces them to produce outputs closer to the teacher’s distribution. This self‑supervised loop is repeated across many problems, allowing the model to learn from its own multimodal representations without explicit human labels.

## Results  
Experimental results show that MIRROR improves over baseline reinforcement learning methods by a statistically significant margin on standard geometry reasoning benchmarks. The model achieves higher pass rates on both text‑only and image‑only tasks and exhibits markedly reduced disagreement between view predictions, indicating more coherent multimodal reasoning. Quantitative gains are reported as 12 % absolute increase in overall accuracy and a 30 % reduction in modality‑specific failure rates.

## Significance  
By uncovering the phenomenon of “different views elicit different behaviors,” MIRROR provides a principled way to exploit complementary information across modalities, moving beyond simple concatenation or joint embedding strategies. This work advances the field toward more robust, consistent multimodal agents that can reliably reason from any representation, which is crucial for applications requiring precise geometric understanding.

## Related Concepts  
- Multi‑modal reasoning: integrating text and visual inputs to solve complex problems.  
- Reinforcement learning: training agents via reward signals; here adapted for self‑supervised view alignment.  
- Reverse‑KL divergence: a regularization term that minimizes the KL distance between two probability distributions, used as a teacher‑student loss.  
- Self‑supervised learning: extracting useful representations without labeled supervision.  
- Geometry reasoning: logical inference over spatial and metric relationships in visual diagrams.
