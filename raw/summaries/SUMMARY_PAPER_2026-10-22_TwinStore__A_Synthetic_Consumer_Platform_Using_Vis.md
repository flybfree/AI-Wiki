---
title: TwinStore: A Synthetic Consumer Platform Using Vision--Language Models
url: http://arxiv.org/abs/2610.30909v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_08-31-18Z_TwinStore_ASyntheticConsumerPlatformUsingVision__L.md
generated_at: 2026-10-22 22:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TwinStore is a source-available synthetic consumer platform that leverages vision-language models to create digital twins of physical retail stores, enabling researchers and practitioners to simulate shopper behavior before changes reach the real world. The platform generates synthetic shoppers who navigate rendered aisles, evaluate product packs, price tags, and promotions, and produce receipts that closely mirror real-world household purchasing patterns. Validation across eleven public datasets demonstrates that simulated category-mix divergence (0.017–0.018) approaches natural household variation (real drift of 0.012), and price elasticities fall within empirically measured ranges.

## Key Takeaways
- TwinStore transforms a physical store into a digital twin using 82 ready-made formats, floor-plan images, or phone photos of shelves, then populates it with synthetic shoppers who plan trips, walk aisles, and make purchase decisions by visually inspecting rendered shelves containing packs, price tags, and promotion signs. Every simulated trip produces a receipt, enabling layout, pricing, packaging, and promotional changes to be tested on the same virtual shoppers before implementation in a real store.
- The platform provides an extensive analytical toolkit including 3D playback, paired comparisons, layout optimization, shopper interviews, a trade-area model, counterfactual edits of real shelf photographs, a marketing studio with eleven tools, and a natural-language assistant that converts plain sentences into drafted studies or answers grounded in a run's own numerical outputs.
- Held-out validation on eleven public datasets shows strong fidelity: category-mix divergence of 0.017–0.018 against a real drift of 0.012, price elasticities within field-measured ranges, and agreement across three independent decision models, suggesting the synthetic receipts capture genuine consumer heterogeneity rather than collapsing to a single behavioral mode.

## Context
This work sits at the intersection of vision-language model applications, agent-based simulation, and retail analytics. Prior synthetic-consumer approaches relied heavily on tabular data or hand-coded behavioral rules, limiting their ability to capture the visual and spatial dimensions of in-store decision-making. By grounding synthetic shoppers in rendered shelf imagery and leveraging VLMs for perception, TwinStore extends agent-based modeling into the visual domain, addressing a long-standing gap in how digital twins can faithfully reproduce the perceptual cues that drive real purchasing behavior. The cross-validation against eleven public datasets and agreement among three independent decision models strengthens confidence that the approach generalizes beyond a single simulated environment.

## Implications
For retail practitioners and CPG marketers, TwinStore offers a low-cost, pre-deployment sandbox where layout changes, price adjustments, pack configurations, and promotional strategies can be stress-tested against synthetic shoppers before committing capital to physical implementation, potentially reducing costly in-store trial-and-error cycles. For the AI research community, the platform demonstrates that vision-language models can serve as perceptual engines for economically grounded agent simulations, opening pathways toward more realistic digital twins in domains beyond retail, such as urban planning, logistics, and public health. The availability of installers for Windows, macOS, and Linux, along with cloud and on-device model support, lowers the barrier for academic and industry adoption, while the source-available distribution invites community-driven extension and reproducibility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.30909v1)
