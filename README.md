<p align="center"><img width="" src="https://t4.ftcdn.net/jpg/01/26/36/91/240_F_126369159_9j2zAeLiKONSxoEwuc3oX36IH4jhaEDa.jpg" alt="logo"></p>

# Apache-Armor
This Ansible role provide an easy and fast way to harden your Apache webserver.

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
The role starts by making a backup of your configuration file, so your can revert to your precedent state in case is breaks.

## Test the result
You can check the result on https://observatory.mozilla.org.
