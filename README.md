<p align="center">
<img width="80px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
</p>

>## Under developement

# Apache Armor

This Ansible role provides an easy way to harden your Apache webserver.

You can apply it as is immediately, as the default settings are good enough to start.

Tailor the hardening process to your needs by enabling further options.

- [Apache Armor](#apache-armor)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Actions](#actions)
  - [Test the result](#test-the-result)

## Requirements

To launch this role, you will need :

- an Apache2 webserver
- a user with sudo privilege
- Debian 9+ or CentOS 7+

## Usage

To use the role, simply call it in your playbook :
```yaml
- name: my playbook
  hosts: webservers
  become: yes

  roles:
    - Apache-Armor
```

The role edits a temporary copy of you configuration file, then backup and overwrite your original configuration file if changes were made.

## Actions

| Setting name | Apache default value | Armor default value | Applied by default | Description                                                                                            |
| ------------ | -------------------- | ------------------- | :----------------: | ------------------------------------------------------------------------------------------------------ |
| Etag         | test                 | none                |        [x]         | Gives info on apache. In production, there is no particular reason for which you would give this info. |

## Test the result

You can check the result on [observatory.mozilla.org](https://observatory.mozilla.org).
