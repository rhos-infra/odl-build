#!/bin/bash

set -x
kill -9 $(ps aux | grep -Ei "ostestr|stestr|tempest" | grep -vi grep | awk '{print $2}')
