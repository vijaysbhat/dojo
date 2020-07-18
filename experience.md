

# Personal Philosophy

## Designing Systems


### Simplicity
> Make things as simple as possible but no simpler - Einstein

* Simple systems have fewer failure modes.
* Easier to pinpoint root causes and make improvements.
* Always need to have fallback plans for when things fail, the final fallback being some type of manual intervention - and the more simple a system is, the easier it is switch over to manual mode.


### Automation
> A man is rich in proportion to the number of things he can afford to let alone - Thoreau

* Automation provides leverage, and I like to view all software engineering efforts through the lens of automation leverage.
* We need to be careful to plan for what happens when the automation breaks down.

### Efficiency & Slack Tradeoff

* Maximizing system efficiency by definition requires cutting slack - insight from [convex optimization formulation](https://en.wikipedia.org/wiki/Convex_optimization#Lagrange_multipliers)
* Having zero slack means no cushion to handle unforeseen shocks to the system. Too much slack is wasteful.
* Important to highlight and align on assumptions and tradeoffs, and revisit periodically.
* Elastic cloud services allow having your cake and eating it too. Still have to validate configured caps.
  * Model scaling behavior with [back of the envelope calculations](#https://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf).
  * [Benchmark](#https://stackoverflow.com/questions/19863857/hardware-requirements-for-presto) and validate hypothesis.
  * Identify bottlenecks (network, disk, CPU) and maintain resource utilization with predefined cushion.

## Leading

### Influencing people
* Ask lots of questions and actually listen to answers. Guide people to arrive at answers themselves.
  * Why?
    * The more relevant data points a leader has, the better the decisions made are - team members share more data points when they feel their input is valued.
    * Team member realizes the answer to their question through talking through the problem. Best form of persuasion is when the person comes up with the solution themselves.
* Influence is built through reputation and trust.

### Establishing leadership in a new team
* Learn wide and deep as quickly as possible.
* Execute quick wins to build credibility.
* Give credit publicly to team members for impactful work.

### Driving long term roadmaps
* Brainstorm project ideas based on understanding of business priorities.
* Influence project prioritization through guidance on impact and tradeoffs (e.g.feature work vs SLA improvements)
* Examples
  * Feature backfill functionality by extending online / offline ML feature service backend.
  * Migrating dashboards to superset.
  * Build automated tool to generate and configure campaigns across ad platforms.

### Mentoring
* I find mentoring a wonderful and fulfilling way to leverage impact.
* My method:
  * First give a vaguely defined small task to measure a baseline ability.
  * Tailor the amount of support needed based on how well they do.
    * How do they clarify the requirements? Do they communicate directly with stakeholders?
    * Assess the quality of code produced e.g. defensive coding, observability and monitoring.
  * Why?
    * Too much support and team member might be demoralized or resentful.
    * Too little support and team member might be demotivated and not even ask for help.
* Examples
  * Getting stakeholder buyin and keeping them in the loop.
  * Prioritize unblocking current workstream over future implementation work.
  * Building with observability and monitoring in mind
    * Coach data scientists how to build scalable and fault tolerant pipelines.
    * Coach DE how to monitor ML feature and output quality.
  * Code optimization through profiling.
  * Helping understand system architecture decisions.

### Turf battles
* Have to manage / preempt them otherwise it reflects poorly across teams.
* Build relationships and get multiple data points for diversity of context and insights.
* Build trust with common goal in mind.

### Building trust
* Pick up the (grunt) work teams are unwilling / unable to do because it a) falls between team boundaries b) isn’t shiny and exciting c) people in the teams don’t have the necessary background.
* In my experience this kind of work has outsize impact because it enables smooth end to end operation across teams.
* Building trust in this manner pre-empts turf battles and opens up access to future opportunities for impact.
* **Examples**
  * [Driver Engagement team](#driver-engagement-team)
  * [DSP forecasting system](#dsp-forecasting-system)

### Incubating new efforts and partnerships
* Increase leverage and impact through cross team efforts.
* Build relationships with senior ICs and managers across teams.
* Important to vet true needs from stated needs.  
  * What resources are partners willing to commit?
  * What efforts have been put in so far?
  * How engaged are they in spec definition and feedback?
  * Get multiple backchannel opinions
* Examples
  * Business chat
  * [DSP forecasting system](#dsp-forecasting-system)


## Technical

* Talk about some particularly crazy/difficult bugs that you encountered
  * [Redshift cluster slowdown](#severe-redshift-cluster-slowdown)
  * [Hive cluster instability](#hive-resource-usage-dashboard)
* Roadmap planning
  * Guidelines
    * 10% exploiting previous long term investments. If it was executed well, shouldn't take more overhead than this.
    * 50% on medium term - responding to changing business requirements
    * 40% long term efforts - making future long term investments
* Rightsizing amount of process
  * Too little process - buggy code, delayed ship dates
    * How to measure
      * Number of defects
      * Number of sevs / outages
      * Ship date delays
  * Too much process - slow team velocity
    * How to measure
      * Story points completed per sprint
      * Increase in high priority backlog size

## Strengths
* Developed a reputation for strong analytical chops / data sense - uncommon for SWE.
  * Great at data visualization and telling a story.
  * My approach
    * Walk stakeholders through easy to grok data analysis and recommendation. Do they agree with it?
    * Get buy-in or disagree and commit.
    * Builds trust and people tend to reach out for advice.
* Distilling ambiguous business requirements, evaluating technical options for tradeoffs, planning and executing delivery of strong technical solutions.
* Steady hand during tense times e.g. during technical outages.
* Following through and taking things to closure.
* Full stack expertise makes me a good pinch hitter - I can quickly ramp up and contribute on cross functional projects and help take them across the finish line.
* Broad industry background.
* Owning gaps in my knowledge and knowing when to seek help.

## Improvement Areas

### Address blind spots
* Meta improvement area - blind spots are insidious because one can't see them or know they exist. It takes consistent feedback from trusted mentors and an open mind to identify and improve.
* I used to think that as an engineer, all my impact was through the technical strength of my solutions. I was not even aware of other more important aspects of impact.
* Most of the improvement areas below were blind spots of mine that I am grateful to have been made aware of.

### Impatience to see progress / giving up too early
  * Most consistent feedback I'd been receiving in the past which I've addressed with maturity in recent years.
  * I was getting stuck in a cycle of a) being all in on a shiny new path b) getting turned off by lack of progress or setbacks c) questioning whether I had made the right choice. e.g
    * Transitioning from SWE to data science (due to perceived increase in prestige) to data engineering and back to SWE.
    * Getting turned off at not being chosen for desirable projects when I thought I was best suited for them. e.g. AG
    * Feeling like I deserved to be doing "*intellectual*" work and being resentful when given grunt work and assuming that was a reflection of how my abilities were perceived. e.g. Facebook
  * I finally broke the cycle at Lyft after considerable self reflection and talking to mentors when I noticed the same loop repeating itself.
  * **Learnings**
    * No one knows or cares if I am awesome - they have plenty of their own shit to worry about. I need to establish that trust anew in every new environment.
    * Doing (impactful) grunt work nobody is willing to do is actually an amazing way to quickly build trust. Even better if I can automate it.
    * Once I build trust and reputation, folks open up about their deeper challenges and are eager to build a true partnership.
    * Awareness of surface level / tablestakes problems that are often common knowledge (i.e can be found in a Google search) is not valuable - what's valuable are the hidden challenges that arise after solving tablestakes. To earn access to those, I need to stick with a path through tough times and periods of doubt. This is when deep insights present themselves that I didn't even know existed or were important. e.g.
      * Directing and up-leveling team output provides much more leverage than me optimizing my individual technical contributions by chasing more *prestigious* work. Much better to help the team deliver and I can fill in the skill gaps needed to make that happen.
      * Importance of driving the roadmap process and [pre-empting stakeholder needs](#influence-long-term-stakeholder-roadmaps).
      * Technical example - data pipeline lineage visibility and quickly assessing downstream impact of failures is a hidden challenge that emerges after a tool like Airflow gains adoption.

### Influence long term stakeholder roadmaps
* What does this involve?
  * Ideation and alignment on charter.
  * Anticipate and guide stakeholder needs.
  * Collaborative prioritization.
  * Highlight and explain tradeoffs.
* I used to think that my role as an engineer was in solution design and delivery, *after* the business problem had been identified by stakeholders.
* This self limiting mindset was a major blind spot, given all the industry experience I had. It came to my attention during one of my checkins.
* I showed intentional improvement in the [DSP forecasting project](#dsp-forecasting-system).
  * Socialized the importance of SLA, observability and monitoring, data quality and circuit breakers.
  * Got buy-in for these areas of focus in the project while deprioritizing the distractions (distributed training, real time sources)
* **Learnings**
  * I need to lean in on my industry experience and technical expertise to anticipate and communicate stakeholder needs ahead of them even being aware of them, and lay out a recommended roadmap. This builds trust, reduces the cognitive burden for stakeholders, and helps everyone succeed.
  * Demonstrates ownership of the business outcome.

### Vet stakeholder assumptions
* Be proactive and assertive in questioning stakeholder assumptions in a collaborative way. What if the stakeholders have blind spots that could benefit from additional perspective? e.g.
  * [Hive migration timing](#driver-engagement-team)
  * [GDPR data quality](#gdpr-backend)
* Showed intentional improvement with this insight in the [DSP forecasting project](#dsp-forecasting-system).
  * Do we truly need distributed training? No, small dataset.
  * Do we truly need real time sources? No, forecasts used to inform manual decisions taken once a day.

### Drive adoption of solutions
* Socialize and drive adoption of solutions I've built, even if they are not in my core area.
  * e.g. [Hive resource usage dashboard](#hive-resource-usage-dashboard) - others picked it up and took credit for it.

### Others
* Be confident about ownership and recommendations made.
* Actively mentor junior team members.

## Stories

### DSP forecasting system
* Context
  * Existing marketplace balance models were wildly inaccurate after  COVID-19 shock.
  * Needed replacement models to inform marketplace lever (incentives / acquisition spend) budgeting decisions.
  * **My guiding insight** - a forecast model is of limited utility if it needs a lot of manual effort to operate and validate, and therefore cannot be widely used by non data scientists.
* Identified and validated core requirements (time to ship, no-touch / full automation, SLA, data quality, observability and monitoring) and non-requirements (distributed training, real time, external features)
  * Aggressively pruned the solution search space to minimize technical execution risk given the tight delivery timeline.
  * Designed end to end production system with proven components, heavy use of defensive checks, alerts, circuit breakers and visualizations to monitor / output quality.
  * Linear lasso regression model with trend seasonality decomposition.
* Set technical direction and execution pace for cross functional team (decision science, forecasting platform) that hadn't worked together before.
* Identified individual teams members' technical comparative advantages (e.g.data science, data engineering) so they could lean into their strengths and also coached them to uplevel in areas they were lacking background (e.g. defensive coding, production system troubleshooting).
* Surfaced issues early and transparently to keep stakeholders informed.
* **Impact**: On schedule delivery of high impact and fully automated forecast pipeline that *just works*.

### GDPR backend
* Context
  * Company wide effort to comply with GDPR / CCPA within 6 month timeframe.
  * Major unchartered territory in terms of requirements.
* Tech lead for analytical data export backend
  * Worked with stakeholders (privacy council) and partners (frontend, orchestration teams) to define requirements and technical roadmap.
  * Led team of 3 engineers for implementation, load testing, internal user testing and delivery of end to end solution.
* Major challenges
  * Data quality
    * Issue blew up after internal tests showed incorrect data. This caused a loss of exec trust in the project progress.
    * Took full ownership of the oversight and led a thorough data quality investigation of all data sources.
    * Socialized easy to grok analysis and follow up plan that became a key reference for stakeholders in driving critical next step discussions.
    * Mitigation effort was extremely well received.
  * Pinch hitter to recover peer team delivery timeline
    * Led defect triage and resolution effort for hundreds of distinct failure cases.
* **Impact**
  * On schedule delivery of data export service for ~2000 users per day at launch with no outages.
  * Smooth, predictable delivery with no surprises, hitting all internal and external milestones.
* **Learnings and missed opportunities**
  * During early phases of the project, the general consensus was that data quality was not important - the law just stated that we should export any data we have. I could have been more critical of this assumption - what about user trust if we export visibly incorrect data? What about the impact on customer support?

### Driver engagement team
* Context
  * Newly formed DE pod didn't have trust of stakeholder (DS) team.
  * Frequent failures and data quality issues in (poorly written incremental build) Hive pipelines. Technical challenge was reconciling data from three different systems (e.g. experimentation, payments) that had different views of incentive redemption.
  * Legacy Redshift pipelines that were hitting scale limits were viewed as superior
  * DS team felt DE was imposing new tech on them and taking away their ability to self serve.
* Identified lack of tracking mechanism for data issues and set up JIRA.
* Automated data quality and parity checks for every stage of ETL to fail early
* Optimize ETL for faster recovery in the event of upstream data issues.
* Coached DS team members on effective use of Hive pipelines.
* **Impact**
  * Number of reported issues dropped from 13 a month to 3 a month in just 3 months.
    * March - 9
    * April - 13
    * May - 6
    * June - 3
* **Learnings and missed opportunities**
  * Should have questioned aggressive Hive migration roadmap early on when stakeholder trust was so low.
  * Could have done better keeping stakeholders in the loop regarding technical challenges using less technical explanations.


### DE oncall

#### Severe Redshift cluster slowdown
* Context
  * Redshift pipelines inexplicably slowed to a crawl and were missing 9am SLAs.
  * Took over oncall after initial investigation completed over the weekend.
  * Lots of red herrings.
* Led the war room effort
  * Initial hypothesis was some tables had developed data skew due to exponential growth through duplicates in join keys.
  * Split up work across engineers to investigate potential candidates for skew.
  * Missed a clue that had already been discussed over the weekend that ultimately turned out to be the root cause.
* User permissions change scheduled job for all users (not just updates) got checked in that flushed the cluster cache on every update, causing the slowdown. These changes would be written to a separate audit log, not the main query log.
* **Impact**
  * Issue got resolved, but not after a major grind with multiple engineers and AWS support involved.

#### Hive resource usage dashboard

* Context
  * Hive jobs randomly stopped progressing and ultimately failed in the cluster and missed SLAs.
  * Individual job failure investigations yielded several red herrings, but the general pattern was of cluster instability.
* No dashboard existed that tied Hive cluster resource utilization to individual pipelines. Data existed at an individual query level.
* Envisioned and implemented a prototype that tied Hive queries to pipelines / ETL tables and visualized top resource hogs.
* **Impact**
  * Unlocked oncall's ability to quickly identify any rogue pipelines that were destabilizing cluster health.

### AG energy data platform
* When I joined - RoR app on MySQL with cron job running forecast models in R for ~10 installations.
* Architected scalable platform for processing and forecasting time series data from millions of smart meters.
* Saw early on that data platform needed to be decoupled from forecasting algorithm development.
* Envisioned and delivered *containerized* approach with:
  * Hadoop / HBase timeseries ingestion and serving backend.
  * Isolated Python containers within MapReduce environment for distributed training and forecasting.
  * Ability for data scientists to develop models locally outside the Hadoop / HBase environment.
* **Impact**
  * Successful deployment to millions of smart meters in Oklahoma.   

### Low points
* Early into Lyft
  * Lack of direction three months in after successful delivery of initial project.
  * Stakeholder team members had moved on to other teams. No immediate impactful projects were presenting themselves within the current team.
  * Wasn't getting my EM and skip's buy-in about projects I wanted to work on.
  * Felt a lack of trust after my efforts to change teams were blocked.
  * In hindsight, I hadn't been proactive about nurturing key relationships outside the team to identify, vet and incubate impactful opportunities myself. I'd assumed that was EM's role and my role was technical design and execution.
  * After the setback, I was determined this time around to get past the tough period to:
    * Prove to myself that I can do it.
    * See what new things I learn and internalize them.
  * Agreed to disagree and commit to projects my EM identified and saw them through to successful completion.
  * **Impact**
    * Broke out of my nagging self doubt that I had a habit of giving up too early.
    * Going through a few perf cycles, I got valuable feedback that helped me identify and fix blind spots that I didn't know existed or were important.

## Example questions
* What were you hired to do?
* What [accomplishments](#stories) are you most proud of in these roles?
* What were some [low points](#low-points) during that job?
* Previous teams and management
	* What was it like working with them?
	* What would they say are your biggest [strengths](#strengths)?
	* What would they say were [areas for improvement](#improvement-areas)?
* Helping a team succeed when you weren't the official leader
  * [DSP forecasting system](#dsp-forecasting-system)
  * [GDPR backend](#gdpr-backend)
* How do you work individually and in a team
  * My view is individual contribution doesn't exist in a vacuum - either the team succeeds or fails. I ask myself how do I leverage my contribution to make the team succeed?
  * I have a breadth of experience and expertise and can wear multiple hats. I identify what strengths team members bring to the table and what the project needs for successful ship. I help team members lean in on their strengths, coach their improvement areas nd I fill in for the skill gaps.
* How do you help others?
* How do you navigate ambiguity?
* How do you push yourself to grow outside of your comfort zone
* Describe two specific goals you set for yourself
  * Clear objectives
  * Reasons for those goals
  * Metrics to track progress
  * Obstacles to overcome and things learned
* Describe when you failed to meet a deadline
  * Root cause
  * How you applied what you learned in future projects
