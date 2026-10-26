# Summary: Shopify moves back to Native from React Native
Saved: 2026-10-25
Source: 2026-09-10_ShopifymovesbacktoNativefromReactNative.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://shopify.engineering/back-to-native)

---

## Summary
Shopify has announced a strategic decision to migrate its mobile application development stack from React Native back to native platforms, specifically Swift and Kotlin. This reversal is driven by significant advancements in Large Language Models (LLMs) and coding agents, which have drastically reduced the cost and effort required to maintain feature parity across iOS and Android. While Shopify previously adopted React Native to avoid building features twice, they now assert that AI tools can effectively handle cross-platform implementation, translation, and testing, making native development more viable and advantageous than before.

## Key Takeaways
- **AI Changed Core Assumptions:** The primary driver for this migration is the evolution of coding agents since 2025. These tools can now implement features on one platform using the other as a reference, effectively bridging the gap that previously made cross-platform frameworks necessary to avoid duplicate work.
- **Native Advantages Outweigh Shared Implementation Costs:** Although native development inherently requires maintaining two codebases, Shopify found that AI agents dramatically reduce the burden of this duplication through shared specifications, automated tests, and review checkpoints. Consequently, the benefits of native performance and platform-specific optimization now outweigh the historical advantages of a single shared codebase.
- **Reevaluation Based on New Capabilities:** Shopify emphasizes that they do not cling to past decisions solely because they were successful. By prototyping core app components in Swift and Kotlin with AI assistance, they discovered that developers could ramp up quickly outside their primary stack, validating that the "cost of building twice" is no longer a prohibitive factor.

## Context
This shift highlights a broader trend in software engineering where AI tools are altering fundamental architectural decisions. Historically, cross-platform frameworks like React Native were adopted to solve resource constraints and ensure feature parity across mobile ecosystems. However, as LLMs become capable of handling complex code translation and maintenance tasks, the economic incentives for cross-platform abstraction diminish. This case study serves as a critical data point for the industry, demonstrating that AI is not just accelerating coding but fundamentally changing the trade-offs between unified codebases and platform-native performance.

## Implications
For the mobile development industry, Shopify’s move suggests that "write once, run anywhere" strategies may become less attractive for large-scale applications if AI can efficiently manage dual-platform maintenance. This could lead to a resurgence in native development practices, as companies seek the performance and user experience benefits of Swift and Kotlin without the traditional overhead of maintaining two separate teams or codebases. It also underscores the need for organizations to continuously reevaluate their tech stacks against emerging AI capabilities, rather than relying on static architectural decisions made years prior.
