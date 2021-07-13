# AWS Session Class-notes

Cloudformation:
    template + stack 

    you can reach cloud formation from :
                    -consol
                    -CLI
                    -API
            free you only charge for resources        

<!-- 
AWSTemplateFormatVersion: 2010-09-09 and currently the only valid one
Description: description of the template to know what it exactly does.
Metadata: details about your resources.
Parameters:Parameters let you make these inputs. to type how many instnace you want to creat from your template
Mappings:CloudFormation helps to organize parameters by named keys and corresponding values for each group
Conditions: You can set conditions if you want some resources to be created, or some properties to be set under certain situations.
Transform:  This section specifies one or more macros that AWS CloudFormation uses to process your template.
Resources: AWS resources are defined and configured here. 
Outputs: data output after your stack has been created, you can specify it here.  -->

from browswer will reach application throught tyhe load balancer target group to ato scaling 
