## Explaining of the Ansible automation part
First, I installed Vagrant and the additional plugin `vagrant-disksize`

* I create a pub key on my own computer
* I launched the ubuntu VM on vagrant
* The file inventory contains the address of different hosts of the solution.
* The file playbook contains the list of runs to do in order to install the docker tool, pull my image and run it with the sample 
of the text to check. 

* from my own computer I launched with the following command:


```shell script
ansible-playbook playbook.yml -i inventory.yml --user vagrant 
```
* I also use the AWS EC2 to deploy the solution. 
To test it, I add the key timesaver.pem in the project, you can run 
to test it.
I will remove the server in one week. (So if you check after one week, the server will be unreachable )
```shell script
ansible-playbook playbook.yml -i inventory.yml --user ubuntu --key-file timesaver.pem
```
