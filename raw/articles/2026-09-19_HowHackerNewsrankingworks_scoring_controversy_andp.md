---
title: How Hacker News ranking works: scoring, controversy, and penalties (2013)
date: 2026-09-19
url: https://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-19 18:16
---

# How Hacker News ranking works: scoring, controversy, and penalties (2013)

## Full Article

How Hacker News ranking really works: scoring, controversy, and penalties
The basic formula for Hacker News ranking has been known
for years
, but questions remained.
Does the published code give the real algorithm?
Are rankings purely based on votes or do invisible factors come into play?
Do stories about the NSA get pushed down in the rankings? Why did that popular story suddenly disappear from the front page after you commented on it?
By carefully analyzing the top 60 HN stories for several days, I can answer those questions and more.
The published formula is mostly accurate.
There is much more tweaking of rankings than you'd expect, with 20% of front-page stories getting penalized in various ways. Anything with "NSA" in the title is penalized and drops off quickly. A "controversial" story gets severely penalized after hitting 40 comments. This article describes scoring and penalties in detail. [Edit: HN no longer penalizes NSA articles (
details
).]
How ranking works
Articles are scored based on their upvote score, the time since the article was submitted, and various penalties using the following
formula
:
[score=\frac{ \left( votes-1 \right) ^{.8}}{ \left( age _{hours} + 2 \right) ^ {1.8}} * penalties]
Because the time has a larger exponent than the votes, an article's score will eventually drop to zero, so nothing stays on the front page too long. This exponent is known as
gravity
.
You might expect that every time you visit Hacker News, the stories are scored by the above formula and sorted to determine their rankings. But for efficiency, stories are individually reranked only occasionally. When a story is upvoted, it is reranked and moved up or down the list to its appropriate spot, leaving the other stories unchanged. Thus, the amount of reranking is significantly reduced. There is, however, the possibility that a story stops getting votes and ends up stuck in a high position. To avoid this, every 30 seconds one of the top 50 stories is randomly selected and reranked. The consequence is that a story may be "wrongly" ranked for many minutes if it isn't getting votes.
In addition, pages can be cached for 90 seconds.
Raw scores and the #1 spot on a typical day
The following image shows the raw scores (excluding penalties) for the top 60 HN articles throughout the day of November 11. Each line corresponds to an article, colored according to its position on the page.
The red line shows the top article on HN. Note that because of penalties, the article with the top raw score often isn't the top article.
[Hacker News raw article scores throughout a day. Red line indicates the #1 article. Due to penalties, the #1 article does not always have the top score.]
This chart shows a few interesting things. The score for an article shoots up rapidly and then slowly drops over many hours. The scoring formula accounts for much of this: an article getting a constant rate of votes will peak quickly and then gradually descend. But the observed peak is even faster - this is because articles tend to get a lot of votes in the first hour or two, and then the voting rate drops off. Combining these two factors yields the steep curves shown.
There are a few articles each day that score much above the rest, along with a lot of articles in the middle. Some articles score very well but are unlucky and get stuck behind a more popular article. Other articles hit #1 briefly, between the fall of one and the climb of another.
Looking at the difference between the article with the top raw score (top of the graph) and the top-ranked article (red line), you can see when penalties have been applied.
The article
Getting website registration completely wrong
hit #1 early in the morning, but was penalized for controversy and rapidly dropped down the page, letting
Linux ate my RAM
briefly get the #1 spot before
Simpsons in CSS
overtook it.
A bit later, the controversy penalty was applied to
Apple Maps
shortly after it reached the #1 spot, causing it to lose its #1 spot and rapidly drop down the rankings.
The
Snapchat
article reached the top of HN but was penalized so heavily at 8:22 am that it dropped off the chart entirely.
Why you should never use MongoDB
was hugely popular and would have spent much of the day in the #1 spot, except it was rapidly penalized and languished around #7.
Severing ties with the NSA
started off with a NSA penalty but was so hugely popular it still got the #1 spot. However, it was quickly given an even bigger penalty, forcing it down the page. Finally, near the end of the day
$4.1m goes missing
was penalized. As it turns out, it would have soon lost the #1 spot to
FTL
even without the penalty.
The green triangles and text show where "controversy" penalties were applied. The blue triangles and text show where articles were penalized into oblivion, dropping off the top 60. Milder penalties are not shown here.
It's clear that the content of the #1 spot on HN isn't "natural", but results from the constant application of penalties to many articles.
It's unclear if these penalties result from HN administrators or from flagged articles.
Submissions that get automatically penalized
Some submissions get automatically penalized based on the title, and others get penalized based on the domain.
It appears that any article with
NSA
in the title gets an automatic penalty of .4. I looked for other words causing automatic penalties, such as
awesome
,
bitcoin
, and
bubble
but they do not seem to get penalized.
I observed that many websites appear to automatically get a penalty of .25 to .8:
arstechnica.com, businessinsider.com, easypost.com, github.com, imgur.com, medium.com, quora.com, qz.com, reddit.com, rt.com, stackexchange.com, theguardian.com, theregister.com, theverge.com, torrentfreak.com, youtube.com. I'm sure the actual list is longer. (This is separate from "banned" sites, which were
listed
at one point.
One
interesting theory
by eterm is that news from popular sources gets submitted in parallel by multiple people resulting in more upvotes than the article "merits". Automatically penalizing popular websites would help counteract this effect.
The impact of penalties
Using the scoring formula, the impact of a penalty can be computed. If an article gets a penalty factor of .4, this is equivalent to each vote only counting as .3 votes. Alternatively, the article will drop in ranking 66% faster than normal. A penalty factor of .1 corresponds to each vote counting as .05 votes, or the article dropping at 3.6 times the normal rate. Thus, a penalty factor of .4 has a significant impact, and .1 is very severe.
Controversy
In order to prevent flamewars on Hacker News, articles with "too many" comments will get heavily penalized as "controversial".
In the published code, the
contro-factor
function kicks in for any post with more than 20 comments and more comments than upvotes. Such an article is scaled by (votes/comments)^2. However, the actual formula is different - it is active for any post with more comments than upvotes and at least 40 comments. Based on empirical data, I suspect the exponent is 3, rather than 2 but haven't proven this. 
The controversy penalty can have a sudden and catastrophic effect on an article's ranking, causing an article to be ranked highly one minute and vanish when it hits 40 comments. If you've wondered why a popular article suddenly vanishes from the front page, controversy is a likely cause.
For example,
Why the Chromebook pundits are out of touch with reality
dropped from #5 to #22 the moment it hit 40 comments, and
Show HN: Get your health records from any doctor'
was at #17 but vanished from the top 60 entirely on hitting 40 comments.
My methodology
I crawled the
/news
and
/news2
pages every minute (staying under the 2 pages per minute
guideline
). I parsed the (somewhat ugly) HTML with
Beautiful Soup
, processed the results with a big pile of Python scripts, and graphed results with the incomprehensible but powerful
matplotlib
.
The basic idea behind the analysis is to generate raw scores using the formula and then look for anomalies. At a point in time (e.g. 11/09 8:46), we can compute the raw scores on the top 10 stories:
2.802 Pyret: A new programming language from the creators of Racket
1.407 The Big Data Brain Drain: Why Science is in Trouble
1.649 The NY Times endorsed a secretive trade agreement that the public can't read
0.785 S.F. programmers build alternative to HealthCare.gov (warning: autoplay video)
0.844 Marelle: logic programming for devops
0.738 Sprite Lamp
0.714 Why Teenagers Are Fleeing Facebook
0.659 NodeKnockout is in Full Tilt. Checkout some demos
0.805 ISO 1
0.483 Shopify accepts Bitcoin.
0.452 Show HN: Understand closures
Note that three of the top 10 articles are ranked lower than expected from their score:
The NY Times
,
Marelle
and
ISO 1
. Since
The NY Times
is ranked between articles with 1.407 and 0.785, its penalty factor can be computed as between .47 and .85. Likewise, the other penalties must be .87 to .93, and .60 to .82.
I observed that most stories are ranked according to their score, and the exceptions are consistently ranked much lower, indicating a penalty. This indicates that the scoring formula in use matches the published code. If the formula were different, for instance the gravity exponent were larger, I'd expect to see stories drift out of their "expected" ranking as their votes or age increased, but I never saw this.
This technique shows the existence of a penalty and gives a range for the penalty, but determining the exact penalty is difficult. You can look at the range over time and hope that it converges to a single value. However, several sources of error mess this up. First, the neighboring articles may also have penalties applied, or be scored differently (e.g. job postings). Second, because articles are not constantly reranked, an article may be out of place temporarily. Third, the penalty on an article may change over time. Fourth, the reported vote count may differ from the actual vote count because "bad" votes get suppressed. The result is that I've been able to determine approximate penalties, but there is a fair bit of numerical instability.
Penalties over a day
The following graph shows the calculated penalties over the course of a day. Each line shows a particular article. It should start off at 1 (no penalty), and then drop to a penalty level when a penalty is applied. The line ends when the article drops off the top 60, which can be fairly soon after the penalty is applied. There seem to be penalties of 0.2 and 0.4, as well as a lot in the 0.8-0.9 range. It looks like a lot of penalties are applied at 9am (when moderators arrive?), with more throughout the day. I'm experimenting with different algorithms to improve the graph since it is pretty noisy.
On average, about 20% of the articles on the front page have been penalized, while 38% of the articles on the second page have been penalized. (The front page rate is lower since penalized articles are less likely to be on the front page, kind of by definition.) There is a lot more penalization going on than you might expect.
Here's a list of the articles on the front page on 11/11 that were penalized. (This excludes articles that
would
have been there if they weren't penalized.) This list is much longer than I expected; scroll for the full list.
Why the Climate Corporation Sold Itself to Monsanto
,
Facebook Publications
,
Bill Gates: What I Learned in the Fight Against Polio
,
McCain says NSA chief Keith Alexander 'should resign or be fired'
,
You are not a software engineer
,
What is a y-combinator?
,
Typhoon Haiyan kills 10,000 in Philippines
,
To Persuade People, Tell Them a Story
,
Tetris and The Power Of CSS
,
Microsoft Research Publications
,
Moscow subway sells free tickets for 30 sit-ups
,
The secret world of cargo ships
,
These weeks in Rust
,
Empty-Stomach Intelligence
,
Getting website registration completely wrong
,
The Six Most Common Species Of Code
,
Amazon to Begin Sunday Deliveries, With Post Office's Help
,
Linux ate my RAM
,
Simpsons in CSS
,
Apple maps: how Google lost when everyone thought it had won
,
Docker and Go: why did we decide to write Docker in Go?
,
Amazon Code Ninjas
,
Last Doolittle Raiders make final toast
,
Linux Voice - A new Linux magazine that gives back
,
Want to download anime? Just made a program for that
,
Commit 15 minutes to explain to a stranger why you love your job.
,
Why You Should Never Use MongoDB
,
Show HN: SketchDeck - build slides faster
,
Zero to Peanut Butter Docker Time in 78 Seconds
,
NSA's Surveillance Powers Extend Far Beyond Counterterrorism
,
How Sentry's Open Source Service Was Born
,
Real World OCaml
,
Show HN: Get your health records from any doctor
,
Why the Chromebook pundits are out of touch with reality
,
Towards a More Modular Future for JavaScript Libraries
,
Why is virt-builder written in OCaml?
,
IOS: End of an Era
,
The craziest things you can plug into your iPhone's audio jack
,
RFC: Replace Java with Go in default languages
,
Show HN: Find your health plan on Health Sherpa
,
Web Latency Benchmark: A new kind of browser benchmark
,
Why are Amazon, Facebook and Yahoo copying Microsoft's stack ranking system?
,
Severing Ties with the NSA
,
Doctor performs surgery using Google Glass
,
Duplicity + S3: Easy, cheap, encrypted, automated full-disk backups
,
Bitcoin's UK future looks bleak
,
Amazon Redshift's New Features
,
You're only getting the nice feedback
,
Software is Easy, Hardware is of Medium Difficulty
,
Facebook Warns Users After Adobe Breach
,
International Space Station Infected With USB Stick Malware
,
Tidbit: Client-Side Bitcoin Mining
,
Go: "I have already used the name for *MY* programming language"
,
Multi-Modal Drone: Fly, Swim & Drive
,
The Daily Go Programming Newspaper
,
"We have no food, we need water and other things to survive."
,
Introducing the Humble Store
,
The Six Most Common Species Of Code
,
$4.1m goes missing as Chinese bitcoin trading platform GBL vanishes
,
Could Bitcoin Be More Disruptive than the Internet?
,
Apple Store is updating
.
The code for the scoring formula
The Arc source code for a version of the HN server
is available
, as well as
an updated scoring formula
:
(= gravity* 1.8 timebase* 120 front-threshold* 1
       nourl-factor* .4 lightweight-factor* .17 gag-factor* .1)

    (def frontpage-rank (s (o scorefn realscore) (o gravity gravity*))
      (* (/ (let base (- (scorefn s) 1)
              (if (> base 0) (expt base .8) base))
            (expt (/ (+ (item-age s) timebase*) 60) gravity))
         (if (no (in s!type 'story 'poll))  .8
             (blank s!url)                  nourl-factor*
             (mem 'bury s!keys)             .001
                                            (* (contro-factor s)
                                               (if (mem 'gag s!keys)
                                                    gag-factor*
                                                   (lightweight s)
                                                    lightweight-factor*
                                                   1)))))
In case you don't read Arc code, the above snippet defines several constants:
gravity* = 1.8
,
timebase* = 120
(minutes), etc. It then defines a method
frontpage-rank
that ranks a story
s
based on its upvotes (
realscore
) and age in minutes (
item-age
).
The penalty factor is defined by an
if
with several cases. If the article is not a 'story' or 'poll', the penalty factor is .8. Otherwise, if the URL field is blank (Ask HN, etc.) the factor is
nourl-factor*
. If the story has been flagged as 'bury', the scale factor is 0.001 and the article is ranked into oblivion. Finally, the default case combines the controversy factor and the gag/lightweight factor.
The controversy factor
contro-factor
is intended to suppress articles that are leading to flamewars, and is discussed more later.
The next factor hits an article flagged as a gag (joke) with a heavy value of .1, and a "lightweight" article with a factor of .17. The actual penalty system appears to be much more complex than what appears in the published code.
Conclusion
An article's position on the Hacker News home page isn't the meritocracy based on upvotes that you might expect.
By carefully examining the articles that appear on the Hacker News page, we can learn a great deal about the scoring formula in use. While upvotes are the obvious factor controlling rankings, there is also a complex "penalty" system causing articles to be ranked lower or disappear entirely. This isn't just preventing spam, but affects many very popular articles. And if an article has more comments than votes, don't add your comment to it or you may kill it off entirely!
See discussion on
Hacker News
.
Update (11/18): article on penalties is penalized
Ironically, this article was penalized on Hacker News. Minutes after reaching the front page, a heavy 0.2 penalty was applied to the article, forcing it off the front page. The black line in the graph below shows the position of this article on Hacker News. You can see the sharp drop when the penalty was applied. The gray line shows where the article would have been ranked without the penalty. Without the penalty, the article would have been in the #5 spot, but with the penalty it never made it back onto the front page (positions 1-30). The lower green line shows the raw score of this article. (11/26: I'm told that the penalty was because the "voting ring detection" triggered erroneously.)
[This article was penalized shortly after reaching the front page of Hacker News]
Email This
BlogThis!
Share to X
Share to Facebook
Share to Pinterest
Labels:
arc
,
reverse-engineering
15 comments:
Anonymous
said...
Nice analysis!  You should check for stories that involve YC companies and/or their competitors.  I've often thought that HN gives unfair advantage to stories about YC companies, beyond just the normal echo-chamber effect.
November 18, 2013 at 2:56 PM
Fabien
said...
Would you mind posting a link to the corresponding HN discussion, as it's burried and searching in HN is impractical at best?
November 19, 2013 at 4:18 AM
Cd-MaN
said...
Thank you! Very nice analysis!
November 19, 2013 at 6:40 AM
Ken Shirriff
said...
Fabien: the discussion on HN is
here
and Reddit has some discussion
here
. The Reddit discussion has some interesting links.
November 20, 2013 at 7:41 AM
Unknown
said...
I'll doing a postmortem of my article and I would be really amazed to see the graph my article i posted yesterday made on HN (What if successful startups are just lucky?).
Does your crawler still running?
I wonder if I had some penalties and what the graph looks like.
November 26, 2013 at 2:11 AM
HN Reader and Poster
said...
Awesome post! I'd love to see more about the voting ring detection penalty. At this point, every one of my posts that makes the front page gets penalized. According to PG this is due to voting ring detection. I'm certainly not organizing any voting rings. I believe this may be another inadvertent type of penalty for popular domains -- having too many friends that upvote you and set off "voting ring detection".
It's a bummer because I put a lot of time in the content and truly think it is good content. The end result is that I "set it and forget it" on Hacker News. Trying to engage there just leads to frustration when the comment thread suddenly drops from the front page.
Another observation - my posts on gender (which I no longer write about due to the personal risk) got the "flamewar" penalty, even though they were honest, noncontroversial pieces generating some really good discussion. Apparently it was too much discussion.
The algorithm probably protects us from a lot of junk but it also hurts sometimes too.
November 26, 2013 at 10:24 AM
Ken Shirriff
said...
Vianney Lecroart: unfortunately I'm note running my crawler any more, so I don't have data for your article.
HN Reader: I'd like to know more about the voting ring detection too.  Apparently that's what nailed my article. Like you, I'm definitely don't have any voting ring, so I don't know why I got hit by the detector.
November 26, 2013 at 11:38 AM
Unknown
said...
I was wondering why we* dropped off the front page so quickly... Hm.
Thanks for putting this together.
* we = Prime. We had the "Get your health records from any doctor" post.
November 26, 2013 at 12:32 PM
Rohit
said...
This article has got 705 point on HackerNews, quite an amazing feat.
How Hacker News ranking really works: scoring, controversy, and penalties (righto.com)
705 points by jseip 1 day ago | flag | 156 comments
Any guess, How much traffic it would be? I guess, over 100K page views??
November 27, 2013 at 12:40 AM
Ken Shirriff
said...
Hi Rohit! I received about 25K page views.
November 27, 2013 at 10:46 AM
Anonymous
said...
Very interesting! Two questions..
1) Any way to tell if different accounts' votes are valued differently based on karma points, age etc.?
2) What about if accounts' can be penalized rather then just certain sites? Not just being hellbanned.
January 22, 2014 at 5:36 PM
JavaUser
said...
@Anonymous, I think they should be, more trusted votes are counted more, If I am not wrong. Simple example, when a new account publish or vote its not reflected immediately.
October 3, 2015 at 6:11 PM
Robert Welain
said...
This comment has been removed by the author.
June 22, 2017 at 8:18 AM
Suresh Dasari
said...
Thanks for the article. Nice analysis.
May 24, 2020 at 11:11 PM
Shahzad Aslam
said...
very good explanation and nice analysis. Thanks for the article.
February 23, 2024 at 9:23 AM
Post a Comment
Newer Post
Older Post
Home

## Metadata
- **Source**: [Original Article](https://www.righto.com/2013/11/how-hacker-news-ranking-really-works.html)
