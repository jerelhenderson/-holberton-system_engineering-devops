# Holberton School - System Engineering & DevOps
## 0x01 - Shell (Permissions)

### Purpose
This introductionary Shell scripting project covers
* `chmod`, `sudo`, `su`, `chown`, `chgrp` commands
* file permissions
* representing permissions as a single digit
* changing permissions, ownership, and group
* running commands at root
* changing user ID, becoming superuser

### Requirements
* Ubuntu 14.04 LTS

### File List
| Program	  | Description						     |
| --------------- |:--------------------------------------------------------:|
| 0-iambetty | change user ID to `betty` |
| 1-who_am_i      | prints effective userid of current user |
| 2-groups      | prints all groups current user is part of |
| 3-new_owner 	  | change owner of file `hello` to user `betty` |
| 4-empty	  | create empty file `hello` |
| 5-execute	  | add execute permission to `hello` owner |
| 6-multiple_permissions	  | add +x to `hello` owner, group... +r to `hello` others |
| 7-everybody	  | add +x to `hello` owner, group, others |
| 8-James_Bond	  | sets 007 to `hello` |
| 9-John_Doe	  | sets `hello` mode to `-rwxr-x-wx` |
| 10-mirror_permissions	  | set `hello` mode to `olleh` mode |
| 11-directories_persmissions  | add +X to all subdirectories of current directory for owner, group, others |
| 12-directory_permissions  | create a directory 751 `dir_holberton` |
| 13-change_group | change `file` group owner to `holberton` |
| 14-change_owner_and_group	   | change owner to `betty`, group owner to `holberton` for all files/directories |
| 15-symbolic_link_permissions | change owner/group owner of `_hello` to `betty`/`holberton` |
| 16-if _only   | change owner of `hello` to betty, only if owned by `guillaume` |
| 100-Star_Wars	   | script plays Star Wars VI |
| 101-man_holberton	   | create man page |