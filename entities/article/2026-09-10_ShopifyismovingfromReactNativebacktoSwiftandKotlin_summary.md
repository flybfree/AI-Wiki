# Summary: Shopify is moving from React Native back to Swift and Kotlin
Saved: 2026-10-25
Source: 2026-09-10_ShopifyismovingfromReactNativebacktoSwiftandKotlin.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://shopify.engineering/back-to-native)

---

## Summary
Shopify has announced a strategic decision to migrate its mobile development stack from React Native back to native Swift and Kotlin, reversing a major architectural shift made in 2020. This reversal is driven by the significant advancement of Large Language Models (LLMs) and coding agents, which have drastically reduced the cost and complexity of maintaining feature parity across iOS and Android platforms. The company asserts that while React Native remains an excellent framework, the core assumption that building software twice was prohibitively expensive no longer holds true in the current AI-assisted development landscape.

## Key Takeaways
- **Re-evaluation Based on Changed Assumptions:** Shopify originally adopted React Native to avoid duplicating work and enable cross-stack development. However, they are now reverting because LLMs have fundamentally altered the cost-benefit analysis of maintaining two separate codebases, making native development more feasible than previously thought.
- **LLMs as Parity Enablers:** Coding agents can now effectively translate features between iOS and Android, assist developers in working outside their primary stack, and maintain parity through shared specifications and automated testing. This capability mitigates the historical disadvantage of native development, which required significant manual effort to keep platforms synchronized.
- **Native Advantages Outweigh Framework Overheads:** While Shopify acknowledges that React Native apps can be fast and that they spent resources optimizing it, they concluded that the advantages of building natively for each platform now outweigh the benefits of a shared implementation when supported by AI agents. The "twice the work" burden has been significantly alleviated by automated assistance in implementation, translation, and review.

## Context
This decision highlights a broader industry trend where AI tools are reshaping software engineering practices and architectural choices. Shopify’s timeline is notable for its early adoption of LLMs in 2021, predating the public release of ChatGPT, demonstrating how long-term integration of these tools can lead to significant strategic pivots. The article underscores that technology decisions should not be static; when foundational assumptions about development costs change due to external technological advancements like AI, companies must be willing to revisit and reverse previous commitments. This case study serves as a practical example of how generative AI is moving beyond simple code completion to influencing high-level architectural strategy and platform selection.

## Implications
For the mobile development industry, this shift suggests that the dominance of cross-platform frameworks may face challenges from AI-enhanced native workflows. As coding agents become more capable at handling the tedious aspects of maintaining dual-platform consistency, the primary justification for using frameworks like React Native or Flutter—reducing duplication—may weaken. This could lead to a resurgence in native development expertise and tooling, as companies seek the performance and platform-specific integration benefits of Swift and Kotlin without the historical penalty of doubled maintenance costs. Furthermore, it signals that engineering teams must continuously reassess their tech stacks in light of AI capabilities, prioritizing adaptability over long-term adherence to previously successful but now outdated assumptions.
