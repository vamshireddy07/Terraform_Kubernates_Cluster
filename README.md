# Terraform_Kubernates_Cluster
## Terraform Installation And Setup In AWS EC2 Redhat Instnace.
##### Prerequisite
+ AWS Acccount.
+ Create Redhat EC2 Instnace.
+ Create IAM Role With Required Polocies.
   + VPCFullAccess
   + EC2FullAcces
+ Attach IAM Role to EC2 Instance.
### Create user to install Ansible & terraform
$sudo useradd ansible
$echo "ansible ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/ansible
$sudo su ansible
### Install Terraform

``` sh
$ sudo yum install wget unzip -y
$ wget https://releases.hashicorp.com/terraform/0.12.28/terraform_0.12.28_linux_amd64.zip
$ sudo unzip terraform_0.12.28_linux_amd64.zip -d /usr/local/bin/
# Export terraform binary path temporally
$ export PATH=$PATH:/usr/local/bin
# Add path permanently for current user.By Exporting path in .bashrc file at end of file.
$ vi .bashrc
   export PATH="$PATH:/usr/local/bin"
# Source .bashrc to reflect for current session
$ source ~/.bashrc   
```
####Ansible Installation
$ sudo su ansible
$ sudo yum install python3 -y
$ sudo alternatives --set python /usr/bin/python3
$ sudo yum -y install python3-pip -y
$ pip3 install ansible --user
$ pip3 install boto3 --user

#### Clone terraform scripts
``` sh
$ git clone https://github.com/vamshireddy07/Terraform_Kubernates_Cluster.git
$ cd Terraform_Kubernates_Cluster
```
#### <span style="color:orange">Update Your Key Name in variables.tf file before executing terraform script.</span>
## Infrastructure As A Code
#### Create Infrastructure(VPC,Subnets,Route Tables,EC2 Instnaces ..etc) As A Code Using Terraform Scripts
``` sh
# Initialise to install plugins
$ terraform init Terraform_Kubernates_Cluster/
# Validate teffaform scripts
$ terraform validate Terraform_Kubernates_Cluster/
# Plan terraform scripts which will list resources which is going  be created.
$ terraform plan Terraform_Kubernates_Cluster/
# Apply to create resources
$ terraform apply --auto-approve Terraform_Kubernates_Cluster/
```
###Configuration Management
##Check if Dynamicinvntry scripts works.

$ chmod =x Dynamicinvnrty.py
$ ./Dynamicinvnrty.py --list

###Kubernetes cluster Setup Using Ansible(Configuration Management)With Dynamicinvntry.
 ###Create a pem file and copy aws private key(pem) file content which you used in terraform.
 
 $ vi devops.pem
 $ chmod.400 devops.pem
 
 ##Replace<pemfile> with your pemfile path in server
   
   $ ansible-playbook -i Dynamicinvnrty.py site.yml -u ubuntu --private-key=<PemFilePath> --ssh-common-args "-o StrictHostKeyChecking=no"

##  Destroy Infrastructure  
```sh
$ terraform destroy --auto-approve Terraform_Kubernates_Cluster/
```
