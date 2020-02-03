# Flask Simple REST API Prime Numbers
----------------------------------

**Flask Simple REST API Prime Numbers**,  This is a Simple REST API which verify if a number is prime or not.


## Requirements
----------------------------------

- Ansible 2.8.4
- Vagrant 1.8.1
- Virtualbox 5.1


## Installation
---------------------------------

First, you need to install [Ansible](https://www.ansible.com/) on your machine.

```bash
DEBIAN

apt-get update
apt-get install software-properties-common
apt-add-repository ppa:ansible/ansible
apt-get update
apt-get install ansible

REHL

yum install epel-release
yum install Ansible

Mac OS

brew install ansible

With pip

pip install ansible
```

Then you need to install Vagrant.

```bash
apt-get install vagrant
```

Finally, you need to install Virtualbox 5.1
```bash
apt-get install virtualbox-5.1
```

## Usage
---------------------------------

You have to clone the project and follow the commands below.

```bash
git clone https://github.com/amine7777/flask-restapi-primenumbers
cd flask-restapi-primenumbers
vagrant up
vagrant ssh
>vagrant@localhost: cd /tmp/hello_api
>vagrant@localhost:~/tmp/hello_api$ export FLASK_APP=hello_api.py
>vagrant@localhost:~/tmp/hello_api$ export FLASK_ENV=development
>vagrant@localhost:~/tmp/hello_api$ flask run
```
You have to run another terminal to use the API.

```bash

cd flask-restapi-primenumbers
vagrant up
vagrant ssh
>vagrant@localhost: curl http://127.0.0.1:5000/prime/< choose any number>
```

If you would like to POST some json you can use this command. You need to create a database to save the POST.

```bash
>vagrant@localhost:  curl -H "Content-Type: application/json" -X POST -d "{"location":"UK"}" http://127.0.0.1:5000/
```

## Contributing
---------------------------------
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




## Next improvements
----------------------------------
- Add a database
- Secure the API

## Author
----------------------------------
- [Amine Kahlaoui](https://github.com/amine7777), DevOps engineer.
