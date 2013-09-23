#!/usr/bin/env python 

import libvirt

vconn = libvirt.open('qemu:///system')
vconn.listAllDomains(0)
freedos = vconn.lookupByName('freedos1')



