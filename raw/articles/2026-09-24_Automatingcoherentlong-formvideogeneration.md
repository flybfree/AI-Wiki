---
title: Automating coherent long-form video generation
date: 2026-09-24
url: https://research.google/blog/coherent-long-form-video-generation/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/coherent-long-form-video-generation/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-24 14:54
---

# Automating coherent long-form video generation

## Full Article

[A man and woman sit at a table looking at a glowing blue 3D holographic projection of a house emerging from a blueprint.]
Automating coherent long-form video generation
September 24, 2026
Yale Song and Yiwen Song, Research Scientists, Google
We introduce a unified multi-agent framework that autonomously generates temporally consistent, long-form video narratives, overcoming the identity drift and cascading failures of current linear AI pipelines.
Quick links
AI video co-director
CANVAS
A²RD
VQQA
Share
Copy link
×
Recent advancements in video diffusion
demonstrate remarkable high-fidelity generation with models that can render realistic scenes in seconds. However, while diffusion models generate high-fidelity video clips, transforming them into coherent long storytelling engines remains challenging.
Most existing agentic pipelines automate this process via chained modules but suffer from
semantic drift
(subtle shifts in character attire or scenery across shots) and
cascading failures
(e.g., an upstream asset artifact corrupting downstream video synthesis) due to independent, handcrafted prompting. Because early errors propagate and break long-horizon consistency, the process often requires exhaustive manual intervention. From a structural perspective, this reflects the classical credit assignment problem, as terminal failures are difficult to trace back to specific prompts. Furthermore, existing methods suffer from
feature drift
, where entities and environments gradually change unintentionally, or
content collapse
, where narratives fail to progress meaningfully.
Today, we introduce our research on an AI video co-director, a unified, multi-agent framework that explicitly plans visual continuity in multi-shot narratives. Built as an orchestration layer on top of
Gemini
and
Veo
, this framework natively inherits safety mechanisms like
SynthID watermarking
. By treating long-form generation as a global optimization and world-state tracking problem, we have developed a suite of frameworks —
Co-Director
(to appear at
COLM 2026
),
CANVAS
(to appear at
EMNLP 2026
),
A²RD
, and
VQQA
—that translate high-level human creative specification into execution by automating repetitive orchestration tasks, from multi-model prompting and shot chaining to closed-loop visual refinement.
We designed these frameworks to act as responsive creative partners that abstract away the burdens of maintaining visual continuity, freeing users to concentrate on the art of storytelling. This architecture decouples creative synthesis from consistency by modeling quality as a test-time objective. Across comprehensive evaluations, our framework demonstrates substantial gains in multi-shot narrative consistency and character persistence, successfully generating minutes-long videos while mitigating visual drift and pipeline error propagation.
How it works
To solve the multi-faceted problem of long-horizon video, we broke the research down into four foundational pillars, each addressing a specific bottleneck in the generative pipeline.
1. Orchestrating creative intent with AI video co-director
To ensure semantic coherence across an entire video, we present
AI video co-director
, a hierarchical multi-agent framework formalizing video storytelling as a global optimization problem. Rather than relying on rigid, linear prompt chains, we introduce hierarchical parameterization: a
multi-armed bandit
(MAB) globally identifies promising creative directions.
This formalizes the creative process as a search for the optimal balance between exploration of novel narrative strategies with the exploitation of effective creative configurations. The system samples abstract creative trajectories — such as combining an informational strategy with a vignette narrative mode and a specific aesthetic archetype — and dynamically injects these into the system prompts of sub-agents. This top-down steering guarantees that the entire pipeline operates under a unified vision. Because our AI video co-director framework operates as an orchestration layer, it achieves this vision by feeding these structured prompts directly into the foundational Gemini and Veo models (though its model-agnostic architecture allows it to sit on top of any foundation generative model). This architecture ensures that all generated images, video, and audio inherently carry native safety protections, including SynthID watermarking. For production, additional safety classifiers can be applied across the final video to safeguard against unintended contextual interactions between individually safe clips.
The pipeline executes global optimization through two interconnected loops: strategic steering and multi-stage production. First, the Orchestrator Agent evaluates the inputs using a MAB algorithm to select a creative configuration across three dimensions: (1) Creative Strategy (intent), (2) Narrative Mode (story structure), and (3) Aesthetic Archetype (visual tone and cinematography). This configuration drives the production hierarchy. The Pre-Production Agent synthesizes a brief scene-by-scene storyline and visual assets into a unified storyboard. The Production Agent then translates this storyboard into concrete audiovisual media using specialized sub-agents: the Keyframe Agent anchors character and scene visuals, the Video Agent adds motion, and the Audio Agent layers in matching voiceover and score.
Finally, a
multimodal LLM
(MLLM) Judge critiques the compiled cut across the three designated dimensions, feeding a factored reward signal back to the MAB to iteratively refine and optimize choices across successive generation loops.
[A flowchart illustrating an AI video co-director pipeline consisting of orchestrator, pre-production, production, and post-production agents.]
AI video co-director multi-agent pipeline. Top:
The Orchestrator Agent utilizes MAB to navigate a factored creative action space.
Bottom:
The Pre-Production Agent synthesizes a creative brief, storyline, and visual assets to establish a consistent storyboard, which the Production Agent translates into synchronized keyframes, video clips, and audio. An MLLM Judge evaluates the final video to generate a factored reward signal which is propagated back to the MAB to iteratively refine the creative configuration over optimization loops.
2. Visual storyboarding with CANVAS
Even with a unified script, generating long sequential shots often leads to character drift and unstable environments. To address this, we introduce
Continuity-Aware Narratives via Visual Agentic Storyboarding
(CANVAS), a multi-agent framework that explicitly plans visual continuity in multi-shot narratives.
CANVAS enforces coherence by maintaining structured representations of characters, locations, and object states as the narrative evolves. Built as an orchestration layer on top of Gemini, it relies on a persistent visual memory. By retrieving visual anchors from memory or initializing new ones when needed, CANVAS ensures smooth transitions within the same setting. This explicit world-state modeling ensures that characters retain their identity and environments preserve their spatial structure when revisited.
To see these in action, the figure below showcases a multi-shot museum heist sequence, comparing CANVAS against representative baselines: direct generation using the underlying base model (
Gemini-3.1-Pro
) and an alternative multi-agent framework (
AutoStudio
). The prompts at the bottom of the figure highlight recurring elements — e.g., the thief, the exhibit hall, and the gemstone — that must maintain identical visual traits. Notice how each method handles consecutive transitions (e.g., the character’s clothing) versus non-consecutive transitions (e.g., when the camera returns to the main hall after a detour). Generation with
Gemini-3.1-Pro
alone exhibits prop inconsistency (the artifact changes) and background drift (the room layout shifts), showing the limits of unguided generation.
AutoStudio
also degrades across cuts, resulting in character drift (the thief’s cap disappears) and background inconsistency. In contrast, CANVAS's persistent visual memory ensures that characters, spatial geometry, and object states remain perfectly coherent across the entire narrative.
[A storyboard comparing video generation consistency for a museum heist scene across Auto Studio, Gemini, and Canvas platforms.]
Visual storyboard comparison on a museum heist sequence from HardContinuityBench, contrasting CANVAS against
AutoStudio
and Gemini-3.1-Pro baselines.
3. Scaling temporal dynamics with A²RD
To translate storyboards into actual minutes-long video, we developed
A²RD
, an agentic autoregressive video generation architecture. A²RD features segment-by-segment generation augmented with a multimodal video memory that tracks segment contexts and dynamics.
For each segment, it operates in a retrieve-synthesize-refine-update loop. A critical part of this loop is how the agent adaptively determines the segment generation mode. It smoothly switches between extrapolation — to allow for natural narrative progression — and interpolation, which anchors segments to existing entities and environments. This effectively balances the need for the story to move forward with the necessity of maintaining the physical reality of the scene.
To test this system, the ten-minute movie below showcases a long-form generation, which demands consistent narrative progression across minutes-long temporal gaps. The video highlights how the system dynamically shifts between its two operational modes: using extrapolation to push the plot into new narrative beats, and interpolation to anchor returning characters and environments to their original designs. While standard video generators suffer from severe visual decay — where characters mutate and locations morph — A²RD continuously queries its multimodal video memory to maintain character identity, costume details, and structural geometry from the opening shot to the final frame.
[Video preview image]
Watch the film
Link to Youtube Video
Long-form video demonstrating A²RD's ability to maintain strict visual consistency and narrative progression over a continuous ten-minute duration.
4. Closed-loop refinement with VQQA
Finally, we needed a way for the system to autonomously identify and fix visual artifacts. Existing test-time optimization methods are typically either
computationally expensive
or
require white-box access to model internals
. To address this, we developed
Video Quality Question Answering
(VQQA), a unified, multi-agent framework generalizable across diverse input modalities and video generation tasks.
VQQA dynamically generates visual questions tailored to the specific prompt and uses the resulting
Vision-Language Model
(VLM) critiques as semantic gradients (provides natural language directional feedback to guide iterative refinement, analogous to numerical gradients in backpropagation). This replaces traditional, passive evaluation metrics with human-interpretable, actionable feedback. The system can then execute a highly efficient, iterative feedback loop (where the model generates a video, evaluates it via visual questions, and refines the text prompt based on the critique) via a natural language interface. To prevent semantic drift during this refinement, VQQA employs a
Global Selection
mechanism: rather than blindly taking the final iteration's output, a global VLM rater evaluates every video generated across the optimization trajectory against the original, unedited prompt. The system then selects the highest-scoring candidate, ensuring localized corrections do not compromise the broader context.
In practice, VQQA operates as a black-box prompt optimizer rather than a pixel-level editor. Instead of modifying pixels directly, it iteratively refines the text prompt to correct high-level compositional defects like attribute binding errors or inconsistent character attributes. This updated prompt guides the generator to sample a new path in its latent space. In the examples below, VQQA does not mask or paint over the original frames; rather, it resolves the model’s material binding struggle by rendering a realistic mylar balloon texture onto a strict cuboid geometry, and fixes a chaotic mid-performance instrument change by keeping the violinist and pianist consistently anchored to their respective instruments across cuts.
play silent looping video
pause silent looping video
unmute video
mute video
Resolving attribute binding errors.
Prompt: "A cuboid balloon drifts past a circular window, sunlight streaming through the glass panes." While the vanilla generation (
left
) fails to capture the properties of a balloon by rendering a rigid, textureless cube, VQQA (
right
) successfully enforces the intended cuboid shape while maintaining the texture and material properties of an inflated balloon. By leveraging iterative visual feedback, the optimized prompt guides the generator to render a distinct, box-shaped mylar balloon with defined edges and seams drifting smoothly past the sunlit window.
play silent looping video
pause silent looping video
unmute video
mute video
Resolving temporal inconsistency.
Prompt: "Violinist and pianist captivate with harmonious duet performance." The vanilla generation (
left
) suffers from a severe continuity break across shot transitions, showing a female pianist and a male violinist initially but suddenly depicting the woman playing the violin after the cut. VQQA (
right
) maintains strict semantic consistency throughout the performance, keeping the female pianist and male violinist anchored continuously to their respective instruments.
Key results & benchmarks
To rigorously evaluate our frameworks, we developed three specialized benchmarks designed to mirror the challenges of professional video production.
GenAD-Bench
:
Uses a human-in-the-loop pipeline that pairs Gemini 3 Pro with specialized image models to construct 50 fictional brands containing four distinct products each. Across 400 unique scenarios, it tests exact marketing constraints without relying on copyright conflicts or training priors.
HardContinuityBench
:
Designed to evaluate spatial and environmental continuity. Generated using intricate GPT-5.2 multi-shot narrative storyboards, this benchmark challenges models with massive gaps between scene reappearances, frequent costume and accessory changes for actors, and complex state changes for interactive props.
LVBench-C
:
Addresses long-horizon temporal dynamics. This dataset contains 120 text-only scenarios grouped into evolving character states, changing object properties, and progressive environmental revelations, maintaining a strict gap rule where critical visual assets must disappear for at least 10 segments before returning with realistic, narrative-driven changes.
Our evaluations demonstrate measurable performance improvements over existing video generation architectures. By navigating the creative strategy search space, AI video co-director achieves a peak quality score of 81.4 on
GenAD-Bench
and enhanced story consistency on
ViStoryBench
. CANVAS leverages structured visual memory to mitigate scene drift, yielding significant continuity gains across scene reappearances on
ST-Bench
and HardContinuityBench. For long-duration temporal dynamics, A²RD minimizes layout drift to improve character and environment consistency over continuous multi-minute runs on
VBench-Long and
LVBench-C. Finally, VQQA's closed-loop prompt optimization resolves physical and compositional inconsistencies, delivering notable absolute quality gains across
T2V-CompBench
,
VBench2
, and
VBench-I2V
. Please consult the individual papers for comprehensive details on our model architectures, training configurations, and baseline evaluations.
[A data table comparing the evaluation benchmarks, key performance metrics, and baseline improvements of four AI video generation frameworks: AI video co-director, CANVAS, A²RD, and VQQA.]
Future directions
These frameworks represent a foundational step toward unlocking coherent, long-horizon visual storytelling for creators. As we continue to refine these agentic architectures, we are exploring how to integrate human-in-the-loop workflows. Our ultimate goal is not to replace human storytelling but to empower creators by abstracting away the tedious complexities of temporal consistency and world-state tracking, ensuring they remain the control of creative direction and narrative design.
Acknowledgements
This work was made possible by the dedicated efforts of our broader research teams across Google. We would like to thank Andrew Pan, Brett Slatkin, Burak Gokturk, Carina Claassen, Daniel Vlasic, Do Xuan Long, Ishani Mondal, Jasmine Leon, Jingyun Liu, Joe Timmons, Jordan Boyd-Graber, Khanh G. LeViet, Kuang Su, Long T Le, Mihir Parmar, Min-Yen Kan, Nathan Hodson, Nick Losier, Palash Goyal, Rhyard Zhu, Sebastian Ko, Scott Penberthy, Yan Xu, Yang Li, Ye Jin, and Tomas Pfister for their invaluable contributions to this suite of research.
Labels:
Generative AI
Machine Intelligence
Quick links
AI video co-director
CANVAS
A²RD
VQQA
Share
Copy link
×
Other posts of interest
[A screenshot of an interactive learning module library interface, showing a sidebar with subjects and a main grid displaying eight vetted educational activity cards.]
September 17, 2026
The future of practice: Enabling teachers to create learning interactives with generative UI
Education Innovation
·
Generative AI
·
Machine Intelligence
[A conceptual diagram illustrating a system retrieving various camping gear items based on a user's text query.]
September 15, 2026
Bypassing inference bottlenecks: Accelerating complex AI search with Retrieve-for-Train
Algorithms & Theory
·
Data Mining & Modeling
·
Generative AI
[A diagram showing ToolGrad's sequential API mini-batch method achieving a high annotation pass rate compared to failing prior art.]
September 10, 2026
ToolGrad: Efficient tool-use dataset generation with textual "gradients"
Machine Intelligence
·
Natural Language Processing
×
❮
❯
[AI-video-co-director2_VisualStoryBoard]
A storyboard comparing video generation consistency for a museum heist scene across Auto Studio, Gemini, and Canvas platforms.
[AI-video-co-director1_Pipeline]
A flowchart illustrating an AI video co-director pipeline consisting of orchestrator, pre-production, production, and post-production agents.
[AI-video-co-director5_evaluation]
A data table comparing the evaluation benchmarks, key performance metrics, and baseline improvements of four AI video generation frameworks: AI video co-director, CANVAS, A²RD, and VQQA.

## Metadata
- **Source**: [Original Article](https://research.google/blog/coherent-long-form-video-generation/)
