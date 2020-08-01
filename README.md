# Apache-Armor
Ansible role to easily harden your Apache web server.

This Ansible role provide an easy and fast way to harden your Apache webserver.
Default configuration is appliable as this.
You can customize the options to tailor the hardening process to your needs.

## Requirements
- apache2 webserver
- on Debian 10

## Usage
To use the role, simply call it in your playbook:
```yaml
- name: my playbook

  hosts: webservers

  roles:
    - Apache-Armor
```

## Test the result
You can check the result on [https://observatory.mozilla.com].
