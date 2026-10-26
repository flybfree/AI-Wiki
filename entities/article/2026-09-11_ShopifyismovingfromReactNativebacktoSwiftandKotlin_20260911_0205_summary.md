# Summary: Shopify is moving from React Native back to Swift and Kotlin
Saved: 2026-10-25
Source: 2026-09-11_ShopifyismovingfromReactNativebacktoSwiftandKotlin.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://shopify.engineering/back-to-native)

---

## Summary
Shopify has announced a strategic decision to migrate its mobile development stack from React Native back to native Swift and Kotlin languages. This reversal is driven by significant advancements in Large Language Model (LLM) capabilities, which have drastically reduced the cost and effort required to maintain feature parity across iOS and Android platforms. By leveraging AI coding agents to handle implementation, translation, and testing tasks, Shopify determined that the historical advantages of a unified codebase no longer outweigh the benefits of native platform-specific development.

## Key Takeaways
- **AI Agents Redefine Development Costs:** The primary driver for this migration is the improved capability of LLMs since 2025. These models can now effectively translate features between iOS and Android, allowing developers to implement a feature on one platform using the other as a reference, thereby mitigating the traditional burden of building software twice.
- **Reevaluation Based on Changed Assumptions:** Shopify explicitly states that it does not cling to past decisions solely based on their previous success. The company reevaluated its 2020 decision to adopt React Native from first principles after recognizing that LLMs had altered the core assumption that maintaining two native codebases was prohibitively expensive and inefficient.
- **Native Development Becomes Viable Again:** While React Native previously offered significant benefits in terms of developer accessibility and reduced maintenance overhead, Shopify’s internal prototyping revealed that AI agents could dramatically reduce the cost of maintaining parity between platforms through shared specifications and automated review checkpoints, making native development competitive again.

## Context
This shift highlights a broader trend in software engineering where AI tools are not just assisting with code completion but are fundamentally altering architectural decisions. Shopify has been integrating LLMs into its workflow since 2021, initially for bug fixing and code review, but by late 2025, these tools had evolved to handle complex cross-platform implementation tasks. This case study serves as a concrete example of how rapid improvements in generative AI are forcing large tech companies to reconsider long-standing infrastructure choices that were previously justified by the high human cost of maintaining separate native stacks.

## Implications
The implications for the industry are significant, suggesting that the "write once, run anywhere" paradigm may lose its economic advantage as AI agents become capable of bridging the gap between disparate programming languages and platforms. For developers, this signals a potential shift back toward specialized native expertise, as AI tools lower the barrier to entry for cross-platform maintenance without requiring a unified framework. Furthermore, it demonstrates that technology stacks are increasingly dynamic, with companies willing to pivot strategies rapidly when underlying assumptions about labor costs and tooling capabilities change due to AI advancements. This could lead to a fragmentation of mobile development strategies, where some organizations may abandon cross-platform frameworks in favor of native approaches supported by AI automation.
