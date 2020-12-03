<p align="center">
<img width="80px" src="https://image.flaticon.com/icons/svg/1000/1000913.svg" alt="logo">
</p>

>## Under developement

# Apache Armor

This Ansible role provides an easy way to harden your Apache webserver.

You can apply it as is immediately, as the default settings are good enough to start. Tailor the hardening process to your needs by enabling further options.

- [Apache Armor](#apache-armor)
  - [Should I harden my webserver ?](#should-i-harden-my-webserver-)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Actions](#actions)

## Should I harden my webserver ?

**Yes**. Check by yourself at [observatory.mozilla.org](https://observatory.mozilla.org).

## Requirements

To launch this role, you will need :

- Ansible
- SSH access to your server (key-based authentication is better)
- root, or any user with sudo privilege :slightly_smiling_face:
- Any major Linux distribution

## Usage

The role edits a temporary copy of you configuration file, then backup and overwrite your original configuration file if changes were made.

>You can start by testing your webserver configuration on [observatory.mozilla.org](https://observatory.mozilla.org).

Install Ansible, then create the following `apache_hardening.yaml` playbook :
```yaml
- name: Hardening playbook
  hosts:
    production:
      ansible_host: www.example.org
      #ansible_user: user
      #ansible_password: user_pass

  become: yes

  roles:
    - Apache-Armor
```

You should have the following arborescence :
```bash
tree

```

Finally, launch your playbook with :
```bash
ansible-playbook apache_hardening.yaml
```

Now you can [check your webserver](https://observatory.mozilla.org) again and enjoy the result :sunglasses:.

## Actions

| Setting                     | Apache value | Armor value | Applied | Description                                                                                                                       |
| --------------------------- | ------------ | ----------- | :-----: | --------------------------------------------------------------------------------------------------------------------------------- |
| Etag                        | test         | none        |   yes   | Gives info on running server. In production, there is no reason to give this information.                                         |
| Cookie : Secure attribute   |              | secure      |   yes   | Setting the `Secure` attribute on cookies will prevent them from being sent over insecure HTTP.                                   |
| Cookie : HttpOnly attribute |              | httponly    |   yes   | `HttpOnly` cookies are inaccessible from JavaScript, preventing cross-site scripting (XSS) attacks from stealing session cookies. |
| Cookie : SameSite attribute |              | samesite    |   yes   | The `SameSite` attribute prevents your cookies from being sent cross-site, protecting against CSRF attacks.                       |
