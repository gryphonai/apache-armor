<p align="center">
<img width="80px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
</p>

>## Under developement

# Apache Armor

This Ansible role provides an easy way to harden your Apache webserver.

You can apply it as is immediately, as the default settings are good enough to start. Tailor the hardening process to your needs by enabling further options.

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

| Setting       | Apache value | Armor value       | Applied | Description                                                                                                                       |
| ------------- | ------------ | ----------------- | :-----: | --------------------------------------------------------------------------------------------------------------------------------- |
| Etag          | test         | none              |   yes   | Gives info on running server. In production, there is no reason to give this information.                                         |
| Cookie header | ?            | $cookie; secure   |   yes   | Setting the `Secure` attribute on cookies will prevent them from being sent over insecure HTTP.                                   |
| Cookie header | ?            | $cookie; httponly |   yes   | `HttpOnly` cookies are inaccessible from JavaScript, preventing cross-site scripting (XSS) attacks from stealing session cookies. |
| Cookie header | ?            | $cookie; samesite |   yes   | The `SameSite` attribute prevents your cookies from being sent cross-site, protecting against CSRF attacks.                       |

## Test the result

You can check the result on [observatory.mozilla.org](https://observatory.mozilla.org).
