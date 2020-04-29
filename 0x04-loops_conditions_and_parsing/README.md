# Holberton School - System Engineering & DevOps
## 0x04 - Shell (Loops, conditions, and parsing)

### Purpose
This introductionary Shell scripting project covers
* creating SSH keys
* advantage of `#!/usr/bin/env bash` over `#!/bin/bash`
* using `while`, `until`, `for` loops
* using `if`, `else`, `elif`, `case` condition statements
* using `cut` command

### Requirements
* Ubuntu 14.04 LTS
* Shellcheck 0.3.3

### File List
| Program	  | Description						     |
| --------------- |:--------------------------------------------------------:|
| 0-RSA_public_key.pub | create an RSA key pair |
| 1-for_holberton_school    | display "Holberton School" ten times using `for`  |
| 2-while_holberton_school | display "Holberton School" ten times using `while` |
| 3-until_holberton_school | display "Holberton School" ten times using `until` |
| 4-if_9_say_hi  | display "Holberton School" ten times, plus "Hi" on nineth line |
| 5-4_bad_luck_8_is_your_chance | display "Holberton School" eight times, "bad luck" onfourth iteration, "good luck" on sixth |
| 6-superstitious_numbers | display numbers 1-20, "bad luck from China" on fourth iteration, "bad luck from Japan" on ninth, "bad luck from Italy" on seventeenth |
| 7-clock | displays time for 12h, 59m |
| 8-for_ls	  | display content of current dired |
| 9-to_file_or_not_to_file | displays information about file "holbertonschool" |
| 10-fizzbuzz | displays numbers 1 to 100, with various words inserted in-between |
| *100-read_and_cut | display content of `/etc/passwd` |
| *101-tell_the_story_of_passwd | display content of `/etc/passwd`, using `while` + IFS |
| *102-lets_parse_apache_logs | displays visitor log w/ HTTP status code from Apache log file |
| *103-dig_the_data | using above, group visitors by IP and HTTP status code |