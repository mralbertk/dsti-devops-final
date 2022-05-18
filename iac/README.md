# Infrastructure as Code
This directory contains a deployment of the simple web application using a _Infrastructure as Code_ approach with 
Vagrant and Ansible.

## Installation 
1. Clone this repository: ```$ git clone mralbertk/dsti-devops-final```
2. Install Virtualbox: [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
3. Install Vagrant: [Installing Vagrant](https://www.vagrantup.com/docs/installation)

## Run 
```shell
# Navigate to the iac directory
cd your/local/repository/iac

# Create & provision VM with Vagrant & Ansible 
vagrant up
```

## Use 
- The API is accessible on `localhost:3000`
- For more information, refer to top-level [documentation](../README.md)

## Cleanup 
- To pause the virtual machine: `vagrant halt`
- To destroy the virtual machine: `vagrant destroy`