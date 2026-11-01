---
title: I built an AI Tamagotchi before Meta could
date: 2026-10-31
url: https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Meta Muse
scraped: 2026-10-31 21:07
---

# I built an AI Tamagotchi before Meta could

## Full Article

Gadgets
AI
Tech
I built an AI Tamagotchi before Meta could
We have Muse Charm at home.
by
Sean Hollister
Oct 31, 2026, 4:05 PM UTC
Link
Share
Gift
[verge-sean-hollister-muse-gadget-331A2564-01-3]
[verge-sean-hollister-muse-gadget-331A2564-01-3]
Photo by Sean Hollister / The Verge
Gadgets
AI
Tech
I built an AI Tamagotchi before Meta could
We have Muse Charm at home.
by
Sean Hollister
Oct 31, 2026, 4:05 PM UTC
Link
Share
Gift
Part Of
Today I’m toying with
see all updates
[Sean Hollister]
Sean Hollister
is a senior editor and founding member of The Verge who covers gadgets, games, and toys. He spent 15 years editing the likes of CNET, Gizmodo, and Engadget.
Mark Zuckerberg’s Meta
made AI look so stinking cute
by giving it a squishy little face — and this holiday season, he wants to sell you
a Muse Charm
so you can carry your jolly AI helper around like a Tamagotchi.
But I won’t be buying one, because
we have Muse Charm at home
. It cost just $50, and I’ve decided the learning experience was worth it.
My version doesn’t
sport cameras or a 5G cellular radio
, but it really talks to Muse and has cute avatars, too! It doubles as a pocket watch and a remote camera viewfinder, and it can (theoretically) control my smart home.
Or at least it can if you inject a lot of extra vibe code.
Weeks ago, I paid $50 to get a 1.75-inch touchscreen computer pendant drop-shipped from China — specifically the
Waveshare ESP32-S3 1.75C
. Not only does the push-to-talk AI devkit look a
lot
like the Muse Charm, but it’s officially sanctioned by Meta. It’s one of the company’s first suggestions if you want to build
a “Muse Gadget,”
a device that uses Meta’s open-source code and tokens to directly connect to its Muse AI cloud.
When the silver metal pocket watch arrived, it felt pretty useless to start. Setup was easy enough — I just plugged it into my PC and pointed Claude at Meta’s GitHub, then paired it to the Muse phone app. But even after I put Meta’s keys on the device, Muse originally thought I was sending it audio clips
to transcribe
rather than commands. After I cleared that up, Muse’s responses were still slow, and it didn’t answer me out loud. It was hard to tell what it was saying since it only showed a few words onscreen at a time, with no place to read full messages unless I whipped out my phone with its own Muse app.
Meta’s build also only came with a single Jolly avatar that mostly just sat there and looked cute, and it wouldn’t automatically discover smart home gadgets like Amazon Echo or Google Home devices do. (This gadget really didn’t do
anything
useful after my initial install.) And though Meta AI software engineers Anant Narayanan and Jeremy Payne include
a neat sample app
showing how Muse Gadgets can stream video from your phone camera, the lack of a remote shutter button made it not so useful for taking photos.
Photo by Sean Hollister / The Verge
But a few sessions of Claude Code filled in almost all those holes. All I had to do was plug the Waveshare back into my PC, then ask Claude to reprogram each thing I wanted.
When I complained to Claude that I couldn’t properly read or hear Muse’s replies to my asks,
issues that others
have
mentioned as well
, Claude built a conversation history page so I can swipe right to read what it said, and I plugged in a British AI voice from ElevenLabs that speaks its answers out loud. (The voice was the least soul-sucking of the ones in ElevenLabs’ free tier, my wife and I agree, even if it doesn’t match the Muse avatars’ cuddly vibe at all.)
Photo by Sean Hollister / The Verge
Thanks to Claude, I can now press a button to make my phone take a picture from across the room with a high-quality live preview, and my phone’s front-facing camera no longer displays upside down. Claude made fairly short work of adding a low-quality camera preview over Bluetooth, too, so I don’t need to be on home Wi-Fi to get photos from creative angles.
When I hit this button on my new remote viewfinder…
Photo by Sean Hollister / The Verge
…my phone takes a photo.
Photo by Sean Hollister / The Verge
I asked Claude to make a whole batch of different avatars like the ones Meta showed off during Meta Connect, and to add a Tamagotchi-like minigame where they need food, play, sleep, and a bath. When the game seemed too simple to capture any attention, I had it add four different levels of hunger, boredom, and dirt. I decided treats should make a crunchy mess and get avatars dirtier when they eat them, and that too much play should tire out a pet. My wish was Claude’s command.
When I noticed I was accidentally letting go of the push-to-talk button too soon and making Muse choke on almost-empty audio, vibe coding fixed it minutes later by sending only audio over one second in length. The only obvious lag I’m seeing now is from Meta’s own servers — sometimes they’re responsive, sometimes they lag quite a bit.
Photo by Sean Hollister / The Verge
It was so easy to let Claude reprogram the pendant that I asked it to build a few features specifically for this video in this story, including a working pocket watch face with three hands that actually tells the time. (That took it 15 minutes; now, when I say the hardware looks like a pocket watch, you can see what I mean!) It even found, downloaded, trimmed, and loaded video clips of Zuck introducing the Muse Charm and installed a video player so I could play those clips on the Waveshare.
I want you to understand I have no coding experience, and so I have no idea if any of this code is good. It might be fatally flawed. Nor do I trust Meta or its Muse agent with my email or my home network, particularly after hearing
how it leaked one reviewer’s home address
. (I put it on guest Wi-Fi from the get-go as a precaution.)
Related
Your secrets aren’t safe with cute robot toy Eiliko
That means I don’t
really
know how useful a Muse Charm may or may not be for those who
do
know how to code and
are
willing to take a bigger leap of faith. But after nearly dropping a bulky little silver pendant a couple of times, one with no more Muse functionality than my phone (and quite a bit less without additional code), I’m thinking Muse itself isn’t the reason to buy a dedicated compute pocket watch.
The reason to have a dedicated piece of hardware is to do things you
can’t
do on the phone that’s already in your pocket, like coding the entire gadget to do whatever you want. Which makes me wonder: Will the actual Muse Charm be this freely programmable, or would the kind of people who’d buy one be better off with a development kit? I guess we’ll see when it ships.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Sean Hollister
AI
Anthropic
Gadgets
Meta
Tech
More in:
Today I’m toying with
The gadget giveaway pile is shrinking — should I restock it?
Sean Hollister
Oct 29
Antigravity just halved the price of its drone — by swapping its headset for wristwatch control
Sean Hollister
Oct 20
Here’s the magnetic USB-C port that Microsoft built.
Sean Hollister
Oct 7
Most Popular
Most Popular
Sam Altman says it’s better for RAM to be in a data center than on your desk
The Apple Pencil turned the Duo into my new favorite notebook
Sam Altman sympathizes with mathematicians, but says OpenAI’s math onslaught won’t stop
I built an AI Tamagotchi before Meta could
The HomeView and Echo Show 16 could be the family computers I’ve been asking for
The Verge Daily
A free daily digest of the news that matters most.
Email (required)
Sign Up
By providing your information, you agree to our
Terms of Use
and our
Privacy Policy
. We use vendors that may also process your information to help provide our services. This site is protected by reCAPTCHA and the Google
Privacy Policy
and
Terms of Service
apply.
Advertiser Content From
[Sponsor Logo]
This is the title for the native ad
[Sponsor thumbnail]

## Metadata
- **Source**: [Original Article](https://www.theverge.com/gadgets/1013375/muse-charm-gadgets-preview-waveshare-esp32-claude-vibe-code)
