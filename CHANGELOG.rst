django-python3-ldap changelog
=============================


0.9.5
-----

- Fixing security vulnerability where username and password could be transmitted in plain text before starting TLS (reported by Weitzhofer Bernhard).


0.9.4
-----

- Fixing broken ldap3 dependency (@levisaya).
- Honoring LDAP_AUTH_CLEAN_USER_DATA setting (@etianen, @akaariai).


0.9.3
-----

- Fixing broken python3-ldap dependency (@ricard33).


0.9.2
-----

- Added setting for initiating TLS on connection (@saraheiting).


0.9.1
-----

- Adding ldap_promote management command.


0.9.0
-----

- First production release.
