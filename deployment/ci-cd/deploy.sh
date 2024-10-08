#!/bin/zsh
aws s3 cp function.zip s3://your-bucket/path-to-code/
aws cloudformation update-stack --stack-name VoiceToTextApi --template-body

