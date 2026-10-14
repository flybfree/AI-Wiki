---
title: Putting Earth AI to work: Geospatial agents for our planet's biggest challenges
date: 2026-10-14
url: https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/
source_feed: Google AI Blog
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-10-14 11:37
---

# Putting Earth AI to work: Geospatial agents for our planet's biggest challenges

## Full Article

[Putting Earth AI to work: Geospatial agents for our planet's biggest challenges]
Putting Earth AI to work: Geospatial agents for our planet's biggest challenges
October 14, 2026
Shravya Shetty, Distinguished Engineer, and Luke Barrington, Product Director, Google Research
In a new technical report, we demonstrate how combining domain-specific foundation models, spatial tools, and upfront planning enables a Geospatial Reasoning agent to carry out complex spatial analysis and planetary prediction that standalone LLMs can’t. Following promising tests with partners, we’re also expanding experimental agent access via Ask Google Earth and an Agent-to-Agent (A2A) service.
Quick links
Microsite
Technical report
Interest form
Research@ top 10
News from Google collection page
Share
Copy link
×
When we introduced
Google Earth AI
, we shared a suite of geospatial foundation models — spanning remote sensing, weather, flood hydrology, and population dynamics — alongside an initial prototype showing how a Gemini-powered agent could connect those models to answer cross-modal questions.
Since then, we have evolved a Geospatial Reasoning agent from an early concept into a much more capable, experimental system built for multi-step, geospatial reasoning across planet-scale data and autonomous training of custom predictive models. Today, we are sharing three updates:
A new
technical report
on geospatial reasoning:
We present systematic evaluations across four benchmarks, including GeoKTools and GeoExpertQueries, two new benchmarks we developed and are releasing for researchers to test their own geospatial reasoning agents. Our results quantify the value of Earth AI’s specialized tools and planning over out-of-the-box LLMs.
Insights from real-world partner testing:
Over the past few months, we invited a small group of social impact and commercial partner organizations — including the
World Health Organization (WHO) Regional Office for Africa
,
People in Need
,
GiveDirectly
, the
Milken Institute
and
WPP
— to test the agent in support of their own real-world workflows, such as disease outbreak investigations, disaster preparedness, and clean energy screening.
Expanding early access on Google Earth and Google Cloud:
We are expanding experimental access for both multi-step geospatial analysis and for planetary prediction. We’re offering early access to an experimental deep research update for
Ask Google Earth
. We’re also providing early access to an agent-to-agent API for developers building custom workflows, including integration recipes for connecting to
Gemini
.
What’s new in Geospatial Reasoning
General-purpose LLMs and standard coding tools struggle with real-world spatial problems because planetary datasets are massive, with specialized map and satellite formats that require careful multi-step planning to combine accurately. To tackle complex spatial workflows in practice, our agent brings together four key capabilities:
Connected to Earth AI foundation models and planet-scale data
The agent connects Gemini to the capabilities of Earth AI’s foundation models — including
WeatherNext
,
Flood Forecasting
, the
Population Dynamics Foundation Model (PDFM)
,
AlphaEarth Foundations
and
Remote Sensing Foundations
— alongside information from
Google Maps Platform
(e.g., place information, routing, air quality, rooftop solar potential),
Google Earth Engine
,
Data Commons
and
Google Dataset Search
.
Modular skills, upfront planning and a dedicated spatial workspace
Earth AI capabilities are packaged as modular skills that the agent calls only when a user question needs them. Before running complex operations, the agent builds a step-by-step analytical plan, selects appropriate fallback datasets when local coverage is sparse, and processes large map layers in a dedicated workspace. This approach avoids overwhelming the agent context with massive amounts of spatial data, while preserving accuracy and tracking data attribution. Every response shows the agent’s plan and the data sources used so experts can check assumptions or substitute datasets.
Bring your own data
Organizations rarely rely on public data alone. Users can now input their own datasets via the Geospatial Reasoning agent API as CSV spreadsheets, custom map boundaries (
GeoJSON
), or cloud tables. Users can then ask the agent to join their private locations with Earth AI’s global models and catalogs.
From multi-step reasoning to autonomous Planetary Prediction
Beyond answering complex analytical questions, the agent also powers our recently announced
Planetary Prediction Engine
. Given a user’s local outcome data, such as regional disease rates, crop yields, or grid outages, the agent automatically selects relevant population and environmental signals, fuses our
Population Dynamics Insights
and
Custom Satellite Embeddings
(Google Maps Platform products built on PDFM and AlphaEarth Foundations, respectively) and trains validated machine learning models for spatial prediction, super-resolution downscaling, and forecasting. In our recent
public health research
, combining these population and satellite signals improved predictions of health outcomes by 12% over demographic baselines and enabled mapping at 8X finer spatial resolution.
[EarthAITechReport1_Overview]
Our Geospatial Reasoning agent responds to a user’s question by first planning a multistep workflow, then selecting key Earth AI tools, datasets and models that are relevant to the query, and finally executing each stage of the plan in a workspace outside the context window. The answer incorporates multiple Earth AI capabilities into a text, tabular and map-based report.
Evaluating a Geospatial Reasoning agent
To measure the impact of domain-specific tools and upfront planning on geospatial reasoning, our
technical report
compares four agent configurations across Gemini 3.8 Flash and Gemini 3.1 Pro: (1) a standalone LLM, (2) the LLM with basic
web search
and
maps grounding
tools, (3) the LLM with Earth AI tools (such as Remote Sensing Foundations and WeatherNext 3) but without upfront planning, and (4) the full Geospatial Reasoning agent which begins every query with a dedicated planning stage that reasons over available capabilities to assess what it can and cannot do and sets out the stages of retrieval and processing needed to reach an answer.
[EarthAITechReport2_evaluate]
We evaluate four agent configurations, from the base Gemini model, to agents progressively augmented with skills and orchestration that are optimized for geospatial reasoning.
The evaluation spans four benchmarks, covering expert-level open-ended analysis, multi-tool orchestration, and community-developed geospatial problems with deterministic answers.
CBGB
and
UnivEARTH
are two externally developed benchmarks that test geospatial code generation and question answering respectively. To test agents on challenging tasks that go beyond a single question or use case, we developed two new benchmarks.
GeoExpertQueries
introduces complex, real-world queries with expert-authored golden workflows that capture analysis best practices in domains like crisis resilience, site selection and public health.
GeoKTools
contains templated queries with verifiable answers, each requiring correct selection and use of 1 to 4 distinct geospatial tools. Together, this suite provides substantially broader coverage than prior evaluations of geospatial reasoning systems. To accelerate research and development of geospatial agents, we
release the development splits
of both our new benchmarks in full.
[EarthAITechReport1_table]
Example queries from our new GeoKTools (
left
) and GeoExpertQueries (
right
) benchmarks. GeoKTools tests an agent’s ability to select and use specific geospatial tools and datasets while GeoExpertQueries evaluates reasoning on open-ended, multi-step workflows.
Results and key takeaways
Two key takeaways stand out from our evaluation: First, domain-specific skills are essential for spatial reasoning. The agent with only basic tools (web search, maps grounding and code execution) struggles on quantitative spatial tasks. Equipping the agent with Earth AI skills drives a significant jump across GeoExpertQueries, GeoKTools, and CBGB. The only exception is UnivEARTH, where even a standalone LLM scores 93.6%, likely because the source NASA articles and answers are available on the public web.
Second, upfront planning unlocks open-ended, real-world workflows. While Earth AI skills alone are enough for narrower tasks like those in CBGB and GeoKTools, tackling open-ended problems in GeoExpertQueries requires upfront planning to keep the agent on track across multi-step analyses and prevent it from making unreliable assumptions or taking shortcuts like using web-search instead of spatial tools.
The table below shows scores across all four benchmarks using Gemini 3.8 Flash:
[EarthAITechReport1_table2]
Scores are 0–100, averaged over three runs. Each benchmark is scored differently, so compare within a row, not across rows.
The technical report also discusses limitations. GeoExpertQueries scores come from an autorater that compares the agent’s performance to expert workflows that define the steps an analysis should take, not the correct final answer. We therefore consider the agent’s output as a strong first draft for experts to review and build on, not a final answer.
Earth AI in action: Early testing with partners
To evaluate how this research translates to real-world challenges, we gave a small group of partners early access to test the experimental agent on their toughest problems. Across public health, disaster response, and infrastructure planning, below is an overview of how they are putting Earth AI into action:
World Health Organization (WHO AFRO) & DRC’s INRB
: At the start of the 2026 Ebola outbreak in the Democratic Republic of the Congo (DRC), WHO AFRO’s Emergency Preparedness and Response Hub in Dakar
used the Geospatial Reasoning agent
to map remote mining corridors where the exposure risk and human mobility are high by cross-referencing forest loss (from satellite images), mining sites (from maps and web data), and population data. In minutes, the team pinpointed 48 exposed settlements and located more than 45,500 at-risk people — a process that normally would have taken weeks. This allowed local responders to proactively deploy mobile laboratories and coordinate border surveillance. Meanwhile, the Epidemic Modeling and Intelligence Unit (UMIE) at the DRC’s
National Institute for Biomedical Research
(INRB) used the Planetary Prediction Engine to estimate the risk of Ebola spreading into uninfected zones. By combining mobility flows with historical case trends and Earth AI models and datasets, these weekly insights give coordinators critical planning time before cases arrive.
“Mobile populations like miners move faster than traditional paper surveillance can track, creating dangerous blind spots. Earth AI fills those gaps with satellite and mobility signals—moving us from reactively chasing a virus to actively forecasting where it will strike next.”
Dr Etien Koua
, HIS Program Area Manager & Hub Coordinator for WHO AFRO Emergency Preparedness and Response
(
watch the video
)
People in Need
: Geospatial reasoning helped combine natural disaster forecasts with population and imagery information, shifting analysts’ focus from data processing to providing insights:
"The experimental Geospatial Reasoning agent helped us analyze 14 historical cyclone paths to identify high-exposure villages in minutes rather than days of manual GIS work, turning prepared complex data into immediate insights and freeing up critical time for life-saving anticipatory action." -
Alonso Gonzales
, GIS and Remote Sensing Coordinator
GiveDirectly
: Teams uploaded custom map boundaries to rapidly calculate population exposure by wind-speed zones during Tropical Cyclone Maila and benchmark tornado damage in Mississippi, cutting crisis scoping from days to minutes inside a single workspace.
WPP
: used geospatial reasoning to connect Population Dynamics Insights with their proprietary data. Their case study demonstrates how Earth AI insights enhanced the performance of geospatial marketing campaigns, while preserving the privacy of their data.
Milken Institute
: Pre-development teams used the agent to combine their own lists of 1,500+ candidate buildings with
Google Maps Platform’s Solar API
and census data in order to screen locations for building community resilience hubs, taking into account rooftop solar potential, mobility data, nearby transit hubs, climate risks, and federal investment zone eligibility.
[Video preview image]
Watch the film
Link to Youtube Video
Early testing with these partners helped our evaluation and expansion of the agent’s geospatial skills, driving our recent additions of road-network routing, support for larger user-uploaded datasets, and better discovery of authoritative local data sources.
Expanding early access: Where you apply to test it
Today, we are expanding access across our Earth AI research capabilities to gather more feedback on these experimental geospatial reasoning capabilities. We are making these available to a limited group of early users:
Ask Google Earth
:
preview expanded deep analysis capabilities directly inside Ask Google Earth. This provides an interactive chat experience where you can ask complex spatial questions in natural language, analyze data — including your own — in Google Earth projects, and explore visual results directly on the map.
Geospatial Reasoning Agent API
: For developer teams that want a customizable, do-it-yourself integration to power custom workflows, we offer an experimental headless Agent-to-Agent(A2A) service. Early partners can connect the Geospatial Reasoning agent to their own custom agents and data pipelines. We provide step-by-step developer recipes for teams who want to connect the service to their
Gemini for business
environment.
Our Planetary Prediction Engine capabilities are also available for early preview — accessible both through an interactive interface for rapid, plain-language modeling and via the Agent API for custom workflows.
To express interest in getting access to these research capabilities, please
complete our interest form
. To be among the first to try out our early stage projects, you can also sign up for our
Early Access Pool
.
Labels:
Earth AI
General Science
Machine Intelligence
Quick links
Microsite
Technical report
Interest form
Research@ top 10
News from Google collection page
Share
Copy link
×
Other posts of interest
[USS0291-Google Research Anthem Film_Thumbnail4 (1)]
October 14, 2026
Research@ 2026: 10 ways we're amplifying human ingenuity
General Science
·
Generative AI
·
Health & Bioscience
[DeepReview2]
October 14, 2026
Analyzing technical documents with Deep Review
General Science
·
Machine Intelligence
·
Natural Language Processing
[Three aerial cityscape panels featuring public health dashboard cards: MMR coverage, Dengue cases forecast, and Cholera emergence zones.]
October 6, 2026
Unlocking Earth AI’s planetary geospatial foundation models for global public health
Earth AI
·
Global
·
Health & Bioscience
×
❮
❯
[EarthAITechReport1_table2]
[EarthAITechReport1_Overview]
[EarthAITechReport1_table]
[EarthAITechReport2_evaluate]

## Metadata
- **Source**: [Original Article](https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/)
