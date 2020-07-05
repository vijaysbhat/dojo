

## Personal Philosophy

### Designing Systems


#### Simplicity
> Make things as simple as possible but no simpler - Einstein

* Simple systems have fewer failure modes.
* Always need to have fallback plans for when things fail, the final fallback being some set of manual interventions - and the more complex a system is, the harder it is to operate manually.


#### Automation
> A man is rich in proportion to the number of things he can afford to let alone - Thoreau

* Automation provides leverage, and I like to view all software engineering efforts through the lens of automation leverage.
* We need to be careful to plan for what happens when the automation breaks down.

### Leading

* Influencing people
  * Ask lots of questions and actually listen to answers
    * Why?
      * The more relevant data points a leader has, the better the decisions made are - team members share more data points when they feel their input is valued.
      * Team member realizes the answer to their question through talking through the problem. Best form of persuasion is when the person comes up with the solution themselves.
* Mentoring
  * First give a vaguely defined small task to measure a baseline for ability.
  * Calibrate amount of support needed based on how well they do.
    * How do they clarify the requirements? Talk directly to stakeholders?
    * Assess the quality of code produced e.g. defensive coding, observability and monitoring.
  * Why?
    * Too much support and team member might be demoralized or resentful.
    * Too little support and team member might be demotivated and not even ask for help.
* Turf battles
  * Have to manage / preempt them otherwise it reflects poorly across teams.
  * Build relationships and get multiple data points for diversity of context and insights.
  * Build trust with common goal in mind
* Building Trust
  * Pick up the (grunt) work teams are unwilling / unable to do because it a) falls between team boundaries b) isn’t shiny and exciting c) people in the teams don’t have the necessary background.
  * In my experience this kind of work has outsize impact because it enables smooth end to end operation across teams.
  * Building trust in this manner pre-empts turf battles and opens up access to future opportunities for impact.
  * **Examples**
    * **Driver Engagement team**
      * Identified lack of tracking mechanism for data issues and set up JIRA for the data science team.
      * Automated data quality and parity checks for every stage of ETL to fail early
      * Optimize ETL for faster recovery in the event of upstream data issues.
      * **Impact**: number of reported issues dropped from 13 a month to 3 a month in just 3 months.
    * **Marketplace forecasting system**
      * Identified and validated essential requirements (time to ship, no-touch / full automation, SLA, observability and monitoring) and non-requirements (distributed training)
      * A forecast model is of limited utility if it needs a lot of manual steps to operate and validate, and therefore cannot be widely used by non data scientists.
      * Proactive with use of defensive checks, alerts and visualizations to monitor / output quality.
      * **Impact**: On schedule delivery of high impact and fully automated forecast pipeline that *just works*.

* What's my superpower?
  * Developed a strong reputation for analytical chops - uncommon for SWE.
  * Great at data visualization and telling a story.
  * Mindset - walk folks through my interpretation and recommendation, do they agree with it?
  * Get buy-in or disagree and commit.
  * Builds trust and people reach out for advice.


### Technical

* Talk about some particularly crazy/difficult bugs that you encountered
  * Severe Redshift cluster slowdown
    * Lots of red herrings
    * Led the war room effort - multiple players, took over oncall after initial investigation completed.
    * Thought it was some tables that had developed data skew due to  exponential growth on account of duplicates in join keys.
    * Missed a clue that had already been discussed over the weekend that turned out to be the root cause
    * User permissions change for everyone (not just updates) got checked in which was flushing the cache on every update. This would be visible in a separate audit log, not the main query log.
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




### Example questions
* What were you hired to do?
* What accomplishments are you most proud of in these roles?
* What were some low points during that job?
* Previous teams and management
	* What was it like working with them?
	* What would they say are your biggest strengths?
	  * Steady hand during tense back to back incidents
	* What would they say were areas for improvement?
* Helping a team succeed when you weren't the official leader
* How do you work individually and in a team
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
