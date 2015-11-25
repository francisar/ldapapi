# ldapapi
python ldap管理http api

#配置说明

在ldapapi/settings.py中配置如下内容
<!--lang:python-->
    LDAP_SERVER = 'ldap://ldap.example.com'
    LDAP_BIND = 'cn=Manager,dc=example,dc=com'
    LDAP_PASS = 'pass'
    LDAP_BASE = 'dc=example,dc=com'
在ldapapi/ldapusermanage/setting.py中设置user和group的前缀dn
<!--lang:python-->
    groupdn = 'ou=Group,dc=example,dc=com'
    userdn = 'ou=People,dc=example,dc=com'


# 调用详情
目前只支持添加，删除用户，修改用户密码
