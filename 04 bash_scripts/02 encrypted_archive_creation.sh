#!/bin/bash

archive=$1
echo $archive

zip -r "$archive.zip" $archive

gpg -c "$archive.zip"
