---
title: Cursor removed cost information from the usage page and CSV export
date: 2026-08-01
url: https://forum.cursor.com/t/usage-page-to-token-amount-what/167153
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://forum.cursor.com/t/usage-page-to-token-amount-what/167153
source_feed: Hacker News
ai_relevance: include
ai_topic: agents-tools
ai_reason: meets AI relevance threshold
scraped: 2026-08-01 12:01
---

# Cursor removed cost information from the usage page and CSV export

## Full Article

## post by Bingojr 23 hours ago

I just noticed Cursor Usage window switched from $$ to Token amount. I use this Usage window closely to keep tabs on my daily/active spending, not from the spending overall page. Today, the $$ amount is replaced by token amount which is completely useless. Any way to revert back to $$ amount as I can’t seem to find this in settings or elsewhere. Is it just me, or does Cursor feel like it’s more buggy than before, ie. auto select sub agents despite having the default subagent setup.

read  6 min

## post by Kaleb_Maul 23 hours ago

I am also missing the $$ on the usage page. I don’t understand why things are being moved around randomly, and now I can’t access my usage data anymore. I couldn’t find any dev announcements about this from today but will keep searching. Hopefully they will fix this issue or tell us where this data has been moved to.

## post by eli.wavv 23 hours ago

Cursor needs to be transparent about the per-request cost if that is what we are being billed for(with on-demand usage). This is unacceptable and makes it impossible for team members to track their own personal usage when working on a team with a shared on-demand usage cap.

## post by Kris_Gunnars 21 hours ago

I’m also seeing this. The dollar breakdown is suddenly GONE from the usage page. Cursor, please fix this immediately.

## post by kevinn 21 hours ago

Thanks for flagging this. There isn’t currently a setting to switch back to dollar amounts for individual plans. Enterprise Plans will still show dollar amounts here, but individual plans will not. This is deliberate design because of the differences in how enterprise plans are structured (pooled usage) vs. individual plans with included usage. We did briefly display dollar amounts for individual plans, but that led to some confusion because the dollar amounts displayed were often higher amounts than the user’s plan cost (due to the generous included usage of the Cursor individual plans).

Ultra runs on usage-based (token) pricing. On that model, anything covered by your plan shows token counts and is marked “Included” because nothing is charged for it. Usage you actually pay for, meaning on-demand beyond your included amount, still shows a dollar figure in the Cost column. That split is the intended design.

Where to find the dollars:

1.   Dashboard > Spending shows an On-Demand Spending figure for your current cycle. That is the number matching what you will be billed.
2.   Dashboard > Usage, set your date range, then Export CSV. The Cost column has dollar amounts for every on-demand row. If it’s part of your included usage of your plan, it won’t show a dollar amount but rather the word “Included”.

## post by Axel_Trange 21 hours ago

I know countless of Cursor users who used this Spending Graph feature dozens of times a day to keep track of their budget. Now you’re completely hiding the cost. Who cares about tokens? It’s irrelevant as it’s highly different to each model. Please don’t tell me and my team we have to write a custom script to break down the budget from your .csv because you favor obscurity

## post by Kris_Gunnars 21 hours ago

Hey Kevin, I’m on the Teams plan and I have multiple employees on the plan with a combined usage cost of 30K USD in the current billing cycle. Almost all of our spend is based on API pricing. How can I track the per-user and per-model spend like before???

## post by Axel_Trange 20 hours ago

Suggestion: Just include a toggle or dropdown button to enable this. You can default to “Tokens” if you prefer. But at least give the option to show the old $$ graph that so many users are accustomed to

## post by kevinn 20 hours ago

## post by Kris_Gunnars 20 hours ago

## post by JPPIX4D 20 hours ago

## post by kevinn 19 hours ago

## post by Kaleb_Maul 19 hours ago

## post by Kaleb_Maul 19 hours ago

## post by Archit 19 hours ago

## post by GeorgeRay 18 hours ago

## post by Pavel_Savva 13 hours ago

## post by Mihai_Cracan 8 hours ago

## post by He_Ro 8 hours ago

## Load more posts below

## Metadata
- **Source**: [Original Article](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153)
