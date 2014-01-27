# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.define :planecrash do |pc|
    pc.vm.host_name = "planecrash.local"
    pc.vm.network :private_network, ip: "10.10.10.100"
    pc.vm.network :forwarded_port, host: 8900, guest: 8900 # apache
    pc.vm.network :forwarded_port, host: 7432, guest: 5432 # apache

    pc.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "1024"]
    end
    # pc.vm.provision :puppet do |puppet|
    #   puppet.module_path = "modules"
    #   puppet.manifests_path = "manifests"
    #   puppet.manifest_file = "dev.pp"
    # end
    pc.ssh.forward_agent = true
    pc.vm.synced_folder "files/", "/etc/puppet/files"
    pc.vm.synced_folder "./", "/opt/apps/planecrash"
    # pc.vm.provision :shell do |s|
    #   s.path = "files/dev/setup.sh"
    #   s.privileged = false
    # end
  end
end
