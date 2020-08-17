<p align="center">
<img width="100px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
</p>

# (Not functional yet) Apache Armor
This Ansible role provides an easy way to harden your Apache webserver.

The role can be applied immediately, as the default settings are good enough to start.

You can enable further options to tailor the hardening process to your webserver usage.

## Requirements
- Apache2 webserver
- User with sudo privilege
- Debian 9+ or CentOS 7+

## Usage
To use the role, simply call it in your playbook:
```yaml
- name: my playbook
  hosts: webservers
  roles:
    - Apache-Armor
```
The role makes a backup of your configuration file, so you can reverts to a precedent state. To not clutter the apache directory, the backup is deleted if no change were made.

## Actions
Setting name | Apache value | Armor value | Description
-------------|--------------|-------------|------------
Etag | `test` | none | Gives info on apache. There is no particuliar reason for which you would give this info.

## Test the result
You can check the result on https://observatory.mozilla.org.
