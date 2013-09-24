#!/usr/bin/env python

import sys
import libvirt

vconn = libvirt.open("qemu:///system")

def listvm():
    for vm in vconn.listAllDomains(0):
        print "vm %s is %s" % (vm.name(), isrunning(vm))

def getvm(n):
    vm = vconn.lookupByName(n)
    return vm

def getvmstate(vm):
    return vm.state(0)

def startvm(vm):
    ret = vm.create(vm)
    return ret

def isrunning(vm):
    if vm.isActive() == 0:
        ret = 'down'
    elif vm.isActive() == 1:
        ret = 'running'
    else:
        ret = 'status error.'
    return ret

def shutdownvm(vm):
    ret = vm.destroy()
    return ret

def resetvm(vm):
    ret = vm.reset(0)
    return ret

def descxml(vm):
    xml = vm.XMLDesc(1)
    return xml


if __name__ == '__main__':
    # list all vm
    listvm()
    # get vm xml.
    vm = getvm('freedos')
    print descxml(vm)
