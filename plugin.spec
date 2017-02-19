---
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
