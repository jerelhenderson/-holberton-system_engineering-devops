# Holberton School - System Engineering & DevOps
## 0x02 - Shell (Redirections)

### Purpose
This introductionary Shell scripting project covers
** I/O Redirection (`head` `tail` `find` `wc` `sort` uniq` grep` `tr`
* direct stdout to file
* get stdin from file
* send output from program to program
* combine commands and filters
** Special Characters
* white spaces, single/double quotes, backlash, comment, pipe, command separator, tilde
** Other Man Pages
* display line of text
* concatenate files and print to stdout
* reverse string
* remove sections from line of files
* `/etc/passwd` and `/etc/shadow` file and format

### Requirements
* Ubuntu 14.04 LTS

### File List
| Program	  | Description						     |
| --------------- |:--------------------------------------------------------:|
| 0-hello_world | print "Hello World" |
| 1-confused_smiley      | print `"(Ôo)'` 	 |
| 2-hellofile      | display content of `/etc/passwd` 	 |
| 3-twofiles 	  | display content of `/etc/passwd` and `/etc/`hosts` |
| 4-lastlines	  | display last ten lines of `/etc/passwd` |
| 5-firstlines	  | display first ten lines of `/etc/passwd` |
| 6-third_line	  | display third line of `icata` |
| 7-file	  | create file `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)` containing "Holberton School" |
| 8-cwd_state	  | write `ls -la` result into `ls_cwd_content` |
| 9-duplicate_last_line	  | duplicates `iacta` last line |
| 10-no_more_js	  | delete regular files w/ `.js` ext present in current dired/subfolders |
| 11-directories 		  | count direds/sub-direds in current dired |
| 12-newest_file |display ten newest files in current dired |
| 13-unique | take list of words and print words that appear once |
| 14-findthatword	   | display lines containing "root" from `/etc/passwd` |
| 15-countthatword	   | display lines containing "bin" from `/etc/passwd` |
| 16-whatsnext   | display lines containing "root" and three lines after from `/etc/passwd` |
| 17-hidethisword	   | display lines from `/etc/passwd` w/o "bin" |
| 18-letteronly	   | display all lines of /etc/ssh/sshd_config start w/ a letter |
| 19-AZ	   | replace 'A' from 'c' to 'Z' from 'e' |
| 20-hiago | remove 'c' and 'C' |
| 21-reverse | reverse input |
| 22-users_and_homes | display all users and home direds |
| 100-empty_casks | find all empty files and direds in current- and sub-direds |
| 101-gifs | list all files with `.gif` ext in current- and sub-direds |
| 102-acrostic | decodes acrostics that use first letter of each line |