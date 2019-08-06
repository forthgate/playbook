# Ansible playbooks
Here some playbooks for different tasks <br>
____
#### aws_playbooks
These playbooks are intended for deploying/managing AWS instances with Apache Airflow workers <br>
***aws*** role will create  ec2 instance <br>
***aws_deploy_worker*** role prepare instance for worker deploy - copying SSH keys, install necessary packages, mount NFS etc. <br>
***aws_docker_deploy*** role needs for deploying worker on current instance

Some variables in playbooks are encrypted with ansible-vault
