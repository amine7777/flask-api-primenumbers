Vagrant.configure("2") do |config|
  config.vm.box = "bento/centos-7.5"
  config.vm.network "forwarded_port", guest: 5000, host: 5000

   ####### Ansible provisioner #######
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "provisioner/deploy_api.yaml"
    ansible.verbose = true
  end
end
