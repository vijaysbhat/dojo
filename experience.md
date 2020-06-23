## Personal Philosophy

### Designing Systems

* Simplicity
  * Make things as simple as possible but no simpler - Einstein
  * Why?
    * Simple systems have fewer failure modes.
    * In the spirit of always having a backup plan for when things will fail, and complex systems are hard to keep functioning manually.
* Automation
  * A man is rich in proportion to the number of things he can afford to let alone - Thoreau.
  * Automation is leverage, view all software engineering through the lens of automation leverage.
  * Plan for what happens when the automation breaks down.

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
    * Quality of code produced. Defensive coding, observability and monitoring.
  * Why?
    * Too much support and team member might be demoralized or resentful.
    * Too little support and team member might be demotivated and not even ask for help.
* Turf battles
  * Have to manage / preempt them otherwise it reflects poorly on everyone.
  * Build relationships and get multiple data points on history and motivations of teams
  * Build trust with common goal in mind
* What's my superpower?
  * Developed a strong reputation for analytical chops - uncommon for SWE
  * Great at data visualization and telling a story
  * Mindset - walk folks through my interpretation and recommendation, do they agree with it?
  * Get buy-in or disagree and commit
  * Builds trust and people reach out for advice


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
