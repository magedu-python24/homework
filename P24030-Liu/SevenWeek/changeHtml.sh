#!/bin/bash
find /tmp/ -type f -name '*.htm' -print0 | xargs -0 -i mv {} {}l
