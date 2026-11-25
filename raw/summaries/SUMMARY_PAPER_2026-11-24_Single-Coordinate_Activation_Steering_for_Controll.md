---
title: Single-Coordinate Activation Steering for Controllable Social Stance in Language Models
url: http://arxiv.org/abs/2611.29578v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-22_16-06-21Z_Single_CoordinateActivationSteeringforControllable.md
generated_at: 2026-11-24 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper asks whether an interpersonal stance in a language model can be controlled by steering a single neuron, without training. In Qwen3.5 4B, contrasting activations on hand-written guarded and eager replies identified neuron 7515 of layer 9 as a candidate for controlling a "distant crush" stance. Increasing this neuron's activation made character replies more distant, and changing the intervention direction between messages shifted replies between warmer and more distant styles.

## Key Takeaways
- Single-neuron steering can impose an interpersonal stance: neuron 7515 of layer 9 in Qwen3.5 4B was identified by contrasting activations on hand-written guarded versus eager replies, and increasing its activation made the character's replies more distant.
- The effect is specific rather than generic: three language models rated this change as stronger than the effects of changing randomly selected neurons, and a blind human comparison supported the finding.
- Stance can be modulated dynamically across a conversation: changing the intervention direction between messages shifted replies between warmer and more distant styles, suggesting conversational stance can be personalized without finetuning.

## Context
Steering one neuron of a small language model has been shown to impose a topic or a quirk without training, but replications indicate that many published single-neuron recipes are fragile or nonspecific. This paper extends that line of work from topics and quirks to interpersonal stance, asking whether a guarded, intermittently warm, and inconsistent chatbot character can be controlled in the same manner.

## Implications
The results suggest that conversational stance in language models can be personalized without finetuning, offering a lightweight and interpretable control mechanism for character-driven assistants. For practitioners, this points toward practical ways to tune social and emotional behavior in chatbots, while also underscoring the need for more robust and specific single-neuron recipes given prior fragility concerns.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.29578v1)
