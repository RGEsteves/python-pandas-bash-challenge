#!/bin/bash

directory=$1
find $directory -type f -printf "%p\t%s\n"
