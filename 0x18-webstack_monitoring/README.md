# 0x18. Webstack monitoring

`DevOps`
`SysAdmin`
`monitoring`
-  By: Sylvain Kalache, co-founder at Holberton School
-  Weight: 1
- Project will start Feb 14, 2024 4:00 AM, must end by Feb 15, 2024 4:00 AM
- Checker was released at Feb 14, 2024 10:00 AM
- An auto review will be launched at the deadline

## Concepts

For this project, we expect you to look at these concepts:

[Monitoring](https://intranet.alxswe.com/concepts/13)
[Server](https://intranet.alxswe.com/concepts/67)

![monitoring infastructure](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

## Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

- Application monitoring: getting data about your running software and making sure it is behaving as expected
- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

![image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)

## Resources

### Read or watch:

- [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
- [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
- [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
- [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- Why is monitoring needed
- What are the 2 main area of monitoring
- What are access logs for a web server (such as Nginx)
- What are error logs for a web server (such as Nginx)

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing
