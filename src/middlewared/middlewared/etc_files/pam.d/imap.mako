#
# $FreeBSD: head/etc/pam.d/imap 170771 2007-06-15 11:33:13Z yar $
#
# PAM configuration for the "imap" service
#

# auth
#auth		sufficient	pam_krb5.so		no_warn try_first_pass
#auth		sufficient	pam_ssh.so		no_warn try_first_pass
auth		required	pam_unix.so		no_warn try_first_pass

# account
#account	required	pam_nologin.so
account		required	pam_unix.so
