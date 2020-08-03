<p align="center">
<img width="100px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
</p>

# Apache Armor
This Ansible role provides an easy way to harden your Apache webserver.

The role can be applied immediately, as the default settings are good enough to start.

You can enable further options to tailor the hardening process to your webserver usage.

## Requirements
- apache2 webserver
- Debian 10

## Usage
To use the role, simply call it in your playbook:
```yaml
- name: my playbook
  hosts: webservers
  roles:
    - Apache-Armor
```
The role starts by fetching a backup of your configuration file, so you can revert to your precedent state in case is breaks.

## Test the result
You can check the result on https://observatory.mozilla.org.
