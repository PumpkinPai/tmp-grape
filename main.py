#!/usr/bin/python3

# Watches your SL user folders for changes and diplays
# changes as native notifications in UBUNTU

# For other OS's, please see:
# https://github.com/pumpkinpai/...

import os
import yaml
import xml.etree.ElementTree as etree


def getConfig():
    confFile = open('config.yaml', 'r')
    conf = yaml.load(confFile)
    confFile.close
    return conf


if __name__ == '__main__':
    conf = getConfig
    # todo- use actual user folder and file
    notifyxml = conf['SL']['notifyxml']
    print(str(notifyxml))
    tree = etree.parse(notifyxml)
    root = tree.getroot()
    print(str(tree))
    print(str(root))
    
