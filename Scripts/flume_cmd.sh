#!/bin/bash

flume-ng agent -n flume1 -c conf -f /root/apache-flume-1.8.0-bin/conf/flume.conf -Dflume.root.logger=INFO,console
