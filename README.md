<p align="center">
<img width="80px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
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

The role **edits a temporary copy** of you configuration file, then keeps a **backup and overwrite** your original configuration file **if changes were made**.

## Actions

| Setting name | Apache default value | Armor default value | Description                                                                              |
| ------------ | -------------------- | ------------------- | ---------------------------------------------------------------------------------------- |
| Etag         | `test`               | none                | Gives info on apache. There is no particular reason for which you would give this info. |

## Test the result

You can check the result on https://observatory.mozilla.org.
