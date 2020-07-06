

# Personal Philosophy

## Designing Systems


### Simplicity
> Make things as simple as possible but no simpler - Einstein

* Simple systems have fewer failure modes.
* Always need to have fallback plans for when things fail, the final fallback being some type of manual intervention - and the more complex a system is, the harder it is to manually keep operational.


### Automation
> A man is rich in proportion to the number of things he can afford to let alone - Thoreau

* Automation provides leverage, and I like to view all software engineering efforts through the lens of automation leverage.
* We need to be careful to plan for what happens when the automation breaks down.

## Leading

### Influencing people
* Ask lots of questions and actually listen to answers. Guide people to arrive at answers themselves.
  * Why?
    * The more relevant data points a leader has, the better the decisions made are - team members share more data points when they feel their input is valued.
    * Team member realizes the answer to their question through talking through the problem. Best form of persuasion is when the person comes up with the solution themselves.
* Influence is built through reputation and trust.

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

### Turf battles
* Have to manage / preempt them otherwise it reflects poorly across teams.
* Build relationships and get multiple data points for diversity of context and insights.
* Build trust with common goal in mind.

### Building Trust
* Pick up the (grunt) work teams are unwilling / unable to do because it a) falls between team boundaries b) isn’t shiny and exciting c) people in the teams don’t have the necessary background.
* In my experience this kind of work has outsize impact because it enables smooth end to end operation across teams.
* Building trust in this manner pre-empts turf battles and opens up access to future opportunities for impact.
* **Examples**
  * [Driver Engagement team](#driver-engagement-team)
  * [DSP forecasting system](#dsp-forecasting-system)

### Identifying true needs

### Strengths
* Developed a reputation for strong analytical chops / data sense - uncommon for SWE.
  * Great at data visualization and telling a story.
  * My approach
    * Present easy to grok analysis to stakeholders and walk them through my take. Do they agree with it?
    * Get buy-in or disagree and commit.
    * Builds trust and people tend to reach out for advice.
* Distilling ambiguous requirements and designing and delivering strong technical solutions.



## Technical

* Talk about some particularly crazy/difficult bugs that you encountered
  * [Redshift cluster slowdown](#severe-redshift-cluster-slowdown)
  * [Hive cluster instability](#hive-resource-usage-dashboard)
* Roadmap planning
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
    * Feeling like I deserved to be doing "*intellectual*" work and being resentful when given grunt work as being a reflection of how my abilities were perceived. e.g. Facebook
  * I finally broke the cycle at Lyft after considerable self reflection and talking to mentors when I noticed the same loop repeating itself.
  * **Learnings**
    * No one knows or cares if I am awesome - they have plenty of their own shit to worry about. I need to establish that trust anew in every new environment.
    * Doing (impactful) grunt work nobody is willing to do is actually an amazing way to quickly build trust. Even better if I can automate it.
    * Once I build the trust and reputation, folks open up about their deep challenges and are eager to build a true partnership.
    * To dig past superficial understanding (what you can pull from a Google search or blogs) to deep and hidden insights, one needs to stick with a path through tough times and periods of doubt. This is when insights present themselves that you didn't even know existed or were important. e.g.
      * Directing and upleveling team output is higher leverage than optimizing my personal technical contributions for the most prestigious work. Much better to help the team deliver and I fill in the skill gaps to make that happen.
      * Importance of driving the problem statement process and [pre-empting stakeholder needs](#preempt-and-guide-stakeholder-needs).

### Preempt and guide stakeholder needs
* I used to think that my involvement as an engineer began once the business problem was defined by stakeholders and I was just responsible for solution design and delivery.
* This mindset was a blind spot of mine - I learned about it during one of my checkins, and I realized that it was self limiting, given all the industry experience I had.
* Showed intentional improvement with this insight in the [DSP forecasting project](#dsp-forecasting-system).
  * Socialized the importance of SLA, observability and monitoring, data quality and circuit breakers.
  * Got buy-in for these areas of focus in the project while cutting out the distractions (distributed training, real time sources)
* **Learnings**
  * Use my industry experience and technical knowledge to anticipate and communicate stakeholder needs ahead of them even being aware of them, and lay out a recommended solution. This builds trust, reduces the number of things they need to worry about and helps everyone succeed.
  * Demonstrates ownership of the business outcome.

### Validate stakeholder assumptions
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
* Set technical direction and execution pace for cross functional team (decision science, forecasting platform) that hadn't worked together before.
* Identified individual teams members' technical comparative advantages (e.g.data science, data engineering) so they could lean into their strengths and also coached them to uplevel in areas they were lacking background (e.g. defensive coding, production system troubleshooting).
* **Impact**: On schedule delivery of high impact and fully automated forecast pipeline that *just works*.

### GDPR Backend
* Context
  * Company wide effort to comply with GDPR / CCPA within 6 month timeframe.
  * Major unchartered territory in terms of requirements.
* Tech lead for analytical data export backend
  * Worked with stakeholders (privacy council) and partners (frontend, orchestration teams) to define requirements and technical roadmap.
  * Led team of 3 engineers for implementation, load testing, internal user testing and delivery of end to end solution.
* Major challenges
  * Data quality issue blew up after internal tests showed incorrect data. This caused a loss of exec trust in the project progress.
  * Despite history, took full ownership of the oversight and led a thorough data quality investigation of all data sources
  * Socialized easy to grok visual summary of investigation and recommendations to allow stakeholders to take decisions on the path forward.
  * Mitigation effort was extremely well received.
* **Impact**
  * On schedule delivery of data export service for ~2000 users per day at launch with no outages.
* **Learnings and missed opportunities**
  * During early phases of the project, the general consensus was that data quality was not important - the law just stated that we should export any data we have.
  * I could have been more critical of this assumption - what about user trust if we export visibly incorrect data? What about the impact on customer support?

### Driver Engagement team
* Context
  * Newly formed DE pod didn't have trust of stakeholder (DS) team.
  * Frequent failures and data quality issues in (poorly written) Hive pipelines.
  * Legacy Redshift pipelines that were hitting scale limits were viewed as superior
  * DS team felt DE was imposing new tech on them and taking away their ability to self serve.
* Identified lack of tracking mechanism for data issues and set up JIRA.
* Automated data quality and parity checks for every stage of ETL to fail early
* Optimize ETL for faster recovery in the event of upstream data issues.
* Coached DS team members on effective use of Hive pipelines.
* **Impact**
  * Number of reported issues dropped from 13 a month to 3 a month in just 3 months.
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


## Example questions
* What were you hired to do?
* What accomplishments are you most proud of in these roles?
* What were some low points during that job?
* Previous teams and management
	* What was it like working with them?
	* What would they say are your biggest strengths?
	  * Steady hand during tense times during technical outages.
	* What would they say were areas for improvement?
    * Evangelize and drive adoption of new solutions I have developed
* Helping a team succeed when you weren't the official leader
* How do you work individually and in a team
  * Individual contribution doesn't exist in a vacuum - either the team succeeds or fails. How do I leverage my contribution to make the team succeed?
  * My view - I have a breadth of experience and expertise and can wear multiple hats. I identify what strengths team members bring to the table and what successful project delivery needs. I help team members lean in on their strengths, and I fill in for the skill gaps.
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
