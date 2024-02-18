
# 0x19. Postmortem
`DevOps`
`SysAdmin`
 - By: Sylvain Kalache
 - Weight: 1
 - Project will start Feb 12, 2024 4:00 AM, must end by Feb 19, 2024 4:00 AM
 - Manual QA review must be done (request it when you are done with the project)

## Concepts
For this project, we expect you to look at this concept:

[On-call](https://intranet.alxswe.com/concepts/39)

## Background Context

![video](https://youtu.be/rp5cVMNmbro)

Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

## Resources

### Read or watch:

- [Incident Report, also referred to as a Postmortem](https://www.pagerduty.com/resources/learn/incident-postmortem/)
- [The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem)
- [What is an Incident Postmortem?](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)

## More Info
## Manual QA Review
It is your responsibility to request a review for your postmortem from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.


Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

Requirements:

- Issue Summary (that is often what executives will read) must contain:
duration of the outage with start and end times (including timezone)
what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
what was the root cause
- Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

when was the issue detected
how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
misleading investigation/debugging paths that were taken
which team/individuals was the incident escalated to
how the incident was resolved
- Root cause and resolution must contain:

explain in detail what was causing the issue
explain in detail how the issue was fixed
- Corrective and preventative measures must contain:

what are the things that can be improved/fixed (broadly speaking)
a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
Be brief and straight to the point, between 400 to 600 words

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

# Nginx web server Crash postmortem Report [Web stack debugging 2]

## Issue Summary

- **Duration:**  First signs of webserver not serving request was reported from 1am UTC and lasted until 1:30 am UTC
- **Impact:** It affected all the organizations web applications served by web01 causing mostly the Accounting and marketing departments to loose access to their applications about 40% of all organization users were down
- **Root cause** The root cause of the issue was port configuration conflict with Nginx server and Apache web server and the user configuration of nginx.

## Timeline

- 1am UTC: Marketing and Accounting employees started sending complain to IT and Operations department of not being able to access their departmental applications.

- 1:15am UTC: IT and Operations went directly to work and throught monitoring tools like datadog we noticed Nginx was not running on Web 01 and the network traffic for the server had reduced drastically.

- 1:17am UTC: we were able to use ssh and remotely access the web server and start the debugging process. we started our assumption that Nginx had stopped unexpectedly due to a runtime error

- 1:25am UTC: with that assumption we tried starting nginx but it kept on crashing at each instance. we proceeded to the nginx log files to see what was not going on well

- The web server down incident greatly escalated to other departments such as management and sales as they were unable to get neccesary files and information from the accounting and marketing departments

- 1:30am: we successfully resolved the issue by changing nginx configuration settings

## Root Cause and Resolution 

- Detail cause: the cause of this incident coude be tranced to conflicting configuration settings in nginx and Apache web server which both were configured to run on thesame port number meanwhile Apache was already running preventing Nginx from running.
we also noticed nginx was configure to run as root instead of nginx user which posses a security risk should in case nginx server is compromised by a malicious actor.

- Detail Fix:

  - We edited nginx configuration file to permit it to be runned as the user Nginx

  - we changed the port on which nginx listens to connextions from 80 to 8080 for all ips

  - we granted read privilleges to nginx configuration files

  - And finally we stopped apache2 server and everything was restored to proper functioning state.

## Corrective and preventative measures

- improve on privillege assignment to various processes in our system to prevent the modification of configuration files by any script or program

- Todos
  - add application level instrumentation monitoring on nginx server
  - assign privilleges to nginx config and prevent it from being modified by any unwanted processes.