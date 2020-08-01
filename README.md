<p align="center">
<img width="100" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">

# Apache Armor
</p>
This Ansible role provides an easy and fast way to harden your Apache webserver.

The role with default values can be applied immediately, as the default settings are good.

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
The role starts by making a backup of your configuration file, so you can revert to your precedent state in case is breaks.

## Test the result
You can check the result on https://observatory.mozilla.org.
