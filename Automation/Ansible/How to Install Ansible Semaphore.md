[Install Semaphore Ansible Web UI on CentOS 7|CentOS 8 | ComputingForGeeks](https://computingforgeeks.com/how-to-install-semaphore-ansible-web-ui-on-centos-7/)

---

I am going to assume that ansible is already installed.

# Install MariaDB

```
dnf install mariadb-server
```
![[Pasted image 20231101160201.png]]

```
systemctl enable mariadb.service
systemctl enable mariadb.service
```
![[Pasted image 20231101160506.png]]

```
mariadb-secure-installation
```
![[Pasted image 20231101160817.png]]

Try and connect to the SQL server with no root password - should fail then try the password you have set
```
mysql -u root
mysql -u root -p
```
![[Pasted image 20231101161154.png]]


# Install Git
```
dnf install git
```
![[Pasted image 20231101161312.png]]

# Install Curl and Wget
```
dnf install wget curl
```
![[Pasted image 20231101161405.png]]

# Download .rpm
Navigate to - [Release v2.9.39-beta · ansible-semaphore/semaphore · GitHub](https://github.com/ansible-semaphore/semaphore/releases/tag/v2.9.39-beta)

and find the correct latest release for your system - in my case - semaphore_2.9.39-beta_linux_amd64.rpm

create a new directory for semaphore
```
mkdir /etc/ansible-semaphore
cd /etc/ansible-semaphore
```

get file
```
wget https://github.com/ansible-semaphore/semaphore/releases/download/v2.9.39-beta/semaphore_2.9.39-beta_linux_amd64.rpm
```
![[Pasted image 20231101161907.png]]

# Install Semaphore
```
rpm -Uvh semaphore_2.9.39-beta_linux_amd64.rpm
```
![[Pasted image 20231101162027.png]]

# Confirm installation
```
semaphore version
```
![[Pasted image 20231101162124.png]]

# Setup Semaphore

```
semaphore setup
```
![[Pasted image 20231101163421.png]]

I would ignore some settings in the above picutre and do the following:
```
Database - 1
db Hostname - leave default
db User - leave default
db Password - enter your MariaDB root password
db Name - leave default
Playbook Path - leave default
Public URL - the URL you will connect to - in my cause http://noc01ansible01.hilsamlabs.uk:3000/semaphore
Emaill alerts - leave default
telegram alerts - leave default
slack alerts - leave default
LDAP - leave default
ouptut directory - /etc/ansible-semaphore
```

Set default user account
![[Pasted image 20231101163534.png]]

# Open Firewall
```
firewall-cmd --add-port=3000/tcp --zone=internal --permanent
```

# Start the Server
```
semaphore server --config /etc/ansible-semaphore/config.json
```
![[Pasted image 20231101192656.png]]

# Connect to server and login with admin account
In a web browser navigate to the URL you put as your public URL. - in my case - http://noc01ansible01.hilsamlabs.uk:3000/semaphore

Using the default admin account you created earlier login to semaphore
![[Pasted image 20231101192819.png]]

Now logout of the admin account by clicking on the username in the bottom left hand of the screen and selecting sign out
![[Pasted image 20231101192917.png]]

# Configure LDAP
In your ansible sever CLI press the Ctrl+C keys to stop the server running

Open your config file
```
/etc/ansible-semaphore/config.json
```

ensure your ldap config is like the following:
```
"ldap_enable": true,
"ldap_binddn": "CN=semaphore-bind,CN=Managed Service Accounts,DC=example,DC=com",
"ldap_bindpassword": "PASSWORD",
"ldap_server": "LDAP Server IP or Hostname:389",
"ldap_searchdn": "OU=USERS,DC=example,DC=com",
"ldap_searchfilter": "(&(sAMAccountName:=%s))",
"ldap_mappings": {
       "dn": "distinguishedName",
       "mail": "userPrincipalName",
       "uid": "sAMAccountName",
       "cn": "cn"
},
"ldap_needtls": false,
```
Save the config file

start the server again and browser back to the web page - login with an LDAP user

# Set User to Admin
In my case I want my LDAP user to be an admin so once I have logged in as that use to create the profile in semaphore I will logout

Now log back in as the default admin account

Click on the account username in the bottom left hand corner and select Users
![[Pasted image 20231101193525.png]]

Find the user you want to make an admin and click the Pencil button to the right to edit
![[Pasted image 20231101193640.png]]

Tick the admin user box and then click save

Now you can sign back in as your LDAP user as an admin

# Set Server to Run as a Service
Create a systemd service unit file
```
vi /etc/systemd/system/semaphore.service
```

Add the following:
```
[Unit]
Description=Semaphore Ansible UI
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecReload=/bin/kill -HUP $MAINPID
ExecStart=/usr/bin/semaphore server --config /etc/ansible-semaphore/config.json
SyslogIdentifier=semaphore
Restart=always

[Install]
WantedBy=multi-user.target
```

Set Execute permissions
```
 chmod +x /etc/systemd/system/semaphore.service
```

```
systemctl daemon-reload
systemctl restart semaphore
systemctl status semaphore
```
![[Pasted image 20231101194426.png]]

Now we know the service can be started we can set it to start on boot

```
systemctl enable semaphore
```

