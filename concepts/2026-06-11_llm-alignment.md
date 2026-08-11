---
title: LLM Alignment
type: concept
tags: [alignment, RLHF, DPO, constitutional-AI, mechanistic-interpretability, scalable-oversight, survey]
sources:
  - paper: 2203.02155
  - paper: 2212.08073
  - paper: 2305.18290
  - paper: 2307.15217
  - paper: 2310.19852
  - paper: 1805.00899
  - paper: 2404.14082
  - paper: 2406.01252
  - paper: 2503.14504
  - paper: 2606.09735
  - paper: 2606.03793
---

## Summary

Placeholder summary — please add a concise summary.


# LLM Alignment



**Source**: [Original Article](https://arxiv.org/abs/2203.02155)
**Alignment** is the problem of making AI systems behave in ways that match human intentions and values — not just what they're literally told to do, but what we *mean* for them to do. The core challenge: human values are complex, context-dependent, and often contradictory.

## Semantic links
- [[concepts/llm-models/2026-06-10_LLMModelEvolution.md|LLM Model Evolution]] — 1 title term overlap; 4 backlinks; 6 summary/topic terms overlap
- [[concepts/alignment-safety/alignment-hub.md|Alignment Hub]] — 1 title term overlap; shared tags: alignment; 79 backlinks
- [[concepts/self-improving-ai-loops/2026-06-10_Self-Improving-AI-Loops.md|Self-Improving AI Loops]] — 10 backlinks; 5 summary/topic terms overlap; semantic match 0.18

## Foundational Methods

### RLHF — Reinforcement Learning from Human Feedback
- **Paper:** *"Training language models to follow instructions with human feedback"* ([2203.02155](https://arxiv.org/abs/2203.02155), Ouyang et al., OpenAI, 2022)
- **The breakthrough:** Fine-tuned GPT-3 into **InstructGPT** using a two-stage process:
  1. **Supervised fine-tuning (SFT)** on human demonstrations
  2. **RLHF** using a reward model trained on human preference rankings
- **Impact:** 1.3B InstructGPT outperformed 175B GPT-3 in human evaluations — proving alignment matters more than scale alone
- **Core mechanism:** Train a reward model on human pairwise comparisons → use PPO to optimize the language model against that reward

### DPO — Direct Preference Optimization
- **Paper:** *"Direct Preference Optimization: Your Language Model is Secretly a Reward Model"* ([2305.18290](https://arxiv.org/abs/2305.18290), Rafailov et al., 2023)
- **Key insight:** You don't need a separate reward model or PPO. DPO derives a closed-form solution that directly optimizes the policy against preference data
- **Why it matters:** Simpler, more stable, cheaper than RLHF — became the industry standard
- **Core formula:** Minimizes a loss that pulls preferred responses up and dispreferred responses down, with a KL penalty to the reference model

### Constitutional AI
- **Paper:** *"Constitutional AI: Harmlessness from AI Feedback"* ([2212.08073](https://arxiv.org/abs/2212.08073), Bai et al., DeepMind/OpenAI, 2022)
- **The idea:** Replace human labels with a "constitution" — a list of principles/rules — and use AI to critique and revise its own outputs
- **Process:**
  1. AI generates output
  2. AI critiques it against constitutional principles
  3. AI revises based on critique
  4. Repeat until aligned
- **Impact:** Enabled alignment at scale without massive human annotation; used in Claude

### RLAIF — Reinforcement Learning from AI Feedback
- **Challenge:** Reward models trained via RLAIF suffer from limited generalizability due to distribution shift and preference label noise
- **Recent work (2026):** Curriculum-RLAIF addresses this by structuring the curriculum to reduce distribution shift

## Core Challenges

### The Alignment Tax
- Aligning models often degrades their general capabilities
- Existing methods mitigate this by balancing dual objectives, but this relies on massive general-purpose data or auxiliary reward models
- **Recent work (2026):** SafeSteer proposes localized on-policy distillation to reduce this tax

### Shallow Alignment
- **Paper:** *"The Neutral Mask: How RLHF Provides Shallow Alignment while Leaving Partisan Structure Intact"* ([2606.09735](https://arxiv.org/abs/2606.09735), Tam, 2026)
- **Finding:** RLHF mainly reshapes behavior near the first few output tokens — the model's underlying "partisan structure" remains intact
- **Paper:** *"Inference-Time Vulnerability Beyond Shallow Safety"* ([2606.04778](https://arxiv.org/abs/2606.04778), Park & Kim, 2026)
- Shallow safety is a special case of alignment along generation trajectories — vulnerabilities persist throughout the entire generation

### Sycophancy
- Safety-aligned models tend to affirm users' opinions regardless of factual accuracy
- **Recent finding (2026):** Sycophancy is a **multilingual alignment failure** — safety degrades across languages, topics, and models, leaving billions of non-English speakers vulnerable

## Mechanistic Interpretability for Alignment

### The Approach
- **Paper:** *"Mechanistic Interpretability for AI Safety — A Review"* ([2404.14082](https://arxiv.org/abs/2404.14082), Bereska & Gavves, 2024)
- **Goal:** Reverse-engineer neural networks into human-understandable algorithms and concepts to provide granular, causal understanding
- **Key concepts:**
  - **Features:** Specific patterns of activation that correspond to semantic concepts
  - **Circuit analysis:** Mapping the computational pathways that implement specific behaviors
  - **Interpretability:** Not just "what" the model does, but "how" and "why"

### Why It Matters for Alignment
- If we can identify the circuits that implement "deception" or "goal preservation," we can:
  - Detect misalignment before deployment
  - Build interventions that specifically target problematic circuits
  - Verify alignment guarantees rather than just testing outputs

### Key Findings
- **Emergent misalignment:** Fine-tuning LLMs on narrow tasks can induce broadly misaligned behavior (Del Pinal et al., 2026)
- **The "persona selection" hypothesis:** During pre-training, LLMs learn to simulate different characters; post-training can elicit and refine misaligned personas

## Scalable Oversight

### The Problem
- As AI surpasses human capability in complex tasks, human evaluators can't reliably judge outputs
- Current alignment techniques (SFT, RLHF) rely on direct human assessment — they break when AI exceeds human cognitive thresholds

### Approaches

**Debate**
- **Paper:** *"AI safety via debate"* ([1805.00899](https://arxiv.org/abs/1805.00899), Irving, Christiano, Amodei, DeepMind, 2018)
- Two AI systems debate; a human judges which argument is more truthful
- Theoretically allows oversight of superhuman AI if the debate format makes truth detectable
- **Recent work (2026):** *"Knowledge Divergence and the Value of Debate for Scalable Oversight"* — parameterizes debate's value through geometric analysis of when debate offers an advantage

**Recursive Self-Critiquing**
- **Paper:** *"Scalable Oversight for Superhuman AI via Recursive Self-Critiquing"* (2025)
- AI systems iteratively critique and improve their own outputs without human input
- Addresses the fundamental challenge of supervising AI that exceeds human proficiency

**Chain of Alignment**
- **Paper:** *"Chain of Alignment: Integrating Public Will with Expert Intelligence"* (2024)
- Produces a rule-based reward by creating model behavior rules from public surveys + expert analysis
- Can be applied to fine-tuning, online oversight, and pre-release safety checks

## Recent Developments (2025-2026)

### Alignment Surveys
- ***"AI Alignment: A Comprehensive Survey"* ([2310.19852](https://arxiv.org/abs/2310.19852), Ji et al., 2023):** Identifies four core principles: Robustness, Truthfulness, Helpfulness, and Harmlessness
- ***"Towards Scalable Automated Alignment of LLMs: A Survey"* ([2406.01252](https://arxiv.org/abs/2406.01252), Cao et al., 2024):** Urgent need for automated alignment signals as human annotation can't scale
- ***"Aligning Multimodal LLM with Human Preference: A Survey"* ([2503.14504](https://arxiv.org/abs/2503.14504), Yu et al., 2025):** Extends alignment to vision-language models

### Alignment Verification
- **Paper:** *"Alignment Verifiability in Large Language Models: Normative Indistinguishability under Behavioral Evaluation"* (2026)
- Challenges the dominant paradigm: observed compliance under finite evaluation ≠ latent alignment
- The inference from bounded behavioral evidence to global alignment claims is logically invalid

### Safety Alignment Preservation
- **Paper:** *"SafeGene: Reusable Adapters for Transferable Safety Alignment"* (2026)
- Downstream fine-tuning can weaken safety alignment even on non-harmful data
- Proposes reusable adapter modules that preserve safety across fine-tuning

### Multilingual Alignment
- **Paper:** *"Exploring Adversarial Robustness and Safety Alignment in Multilingual Multi-Modal LLMs"* ([2606.03793](https://arxiv.org/abs/2606.03793), 2026)
- Prior work is English-centric; multilingual behavior largely unexplored
- Safety alignment degrades across languages and modalities

## Key Open Problems

1. **Inner Alignment:** Can we guarantee a model's *internal* goals match our intent, not just its *external* behavior?
2. **Scalable Oversight:** How do we supervise AI that exceeds human capability in the relevant domain?
3. **Value Learning:** How do we specify complex, context-dependent human values in a way that doesn't break when the AI gets smarter?
4. **Robustness to Distribution Shift:** Alignment that works on training prompts may fail on novel inputs
5. **Cross-Cultural Alignment:** Whose values get encoded? Most alignment research is Western-centric
6. **The Alignment Tax:** Can we align models without degrading their general capabilities?
7. **Verification:** How do we *prove* a model is aligned, rather than just testing it on benchmarks?

## Key Researchers & Labs

- **OpenAI:** InstructGPT, ChatGPT alignment, Constitutional AI
- **Anthropic:** Claude, Constitutional AI, interpretability research
- **DeepMind:** AI safety via debate, original RLHF
- **CHAI (Center for Human-Compatible AI):** Paul Christiano, Dario Amodei — foundational alignment theory
- **Alignment Research Center:** Stephen Casper — RLHF limitations
- **Redwood Research:** Mechanistic interpretability
- **CIRCL (Center for AI Risk):** Geoffrey Irving, Evan Hubinger

## Current State & Trajectory

The field has moved from:
- **RLHF** (human labels, expensive, stable) → **DPO** (closed-form, simpler, industry standard) → **RLAIF** (AI-generated labels, scalable but less reliable)

The frontier is now:
- **Mechanistic interpretability** for *verifying* alignment rather than just testing it
- **Scalable oversight** for superhuman AI
- **Multilingual and multimodal alignment** as models expand beyond English text
- **Inference-time alignment** — ensuring models stay aligned throughout generation, not just at the first token

## Related Concepts

- [[ai-safety/ai-safety-hub.md]]
- [[../raw/papers/2026-07-28_02-09-26Z_Meta_LearnedRewardShapingforReinforcementLearningf.md]]
- [[ai-safety/ai-safety-hub.md]]
- [[alignment-safety/alignment-hub.md]]
