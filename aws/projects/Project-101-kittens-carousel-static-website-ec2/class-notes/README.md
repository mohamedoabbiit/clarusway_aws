# AWS Session Class-notes

Note about the Project 101
introdcution about cloudformation:

Discrpition : to share the information about your template should be slear and more indersandable

parameters:
put the key pair here provided by user, ask for the key 

metadata: for security purpse you dont won't to share you will use mapping for 

Resource : very imporatnt part, 

use this link

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resources-section-structure.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

how to creat your own inrastructure (by emanate other stuff )

go to github and serch for cloudformation with EC2 you will find a lot samples.

Output :
t check if your application is runing or no



appli


swhen you done with your website how you will make it rununig good

first run it on dumy EC2 then put userdta on the template 

userdata
fn:Base64 :
    !sub: 
    #! /bin/bash/
    yum update -