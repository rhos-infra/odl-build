---
# Plugin type is provision since custom type is not supported by Infrared at the moment
plugin_type: provision
description: Build, provision or install OpenDaylight
subparsers:
    build:
        help: Build OpenDaylight from source
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: Build options
              options:
                  url:
                      type: Value
                      help: 'The url of the component'
                      required: True
                  branch:
                      type: Value
                      help: 'The branch of the component'
                      required: True
                  dist-git:
                      type: Value
                      help: 'The url of the dist-git repo'
                      required: True
    provision:
        help: OpenDaylight provisioner
        include_groups: ['Ansible options', 'Inventory', 'Common options', 'Answers file']
        groups:
            - title: OpenDaylight provisioner options
              options:
                  odl-controller-memory:
                      type: Value
                      help: 'Controller memory'
                  odl-controller-disks:
                      type: Value
                      help: 'Controller Disks size'
                  odl-controller-cpu:
                      type: Value
                      help: 'Controller CPU'
                  odl-compute-memory:
                      type: Value
                      help: 'Compute memory'
                  odl-compute-disks:
                      type: Value
                      help: 'Compute Disks size'
                  odl-compute-cpu:
                      type: Value
                      help: 'Compute CPU'
                  odl-pub-int-name:
                      type: Value
                      help: 'Public interface name'
                  odl-pub-int-addr:
                      type: Value
                      help: 'Public interface address'
                  odl-pub-int-vlan:
                      type: Value
                      help: 'Public interface vlan'
                  odl-pub-int-prefix:
                      type: Value
                      help: 'Public interface prefix'
