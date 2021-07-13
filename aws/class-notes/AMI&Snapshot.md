# AWS Session Class-notes
## from kahoot

Snapshot take curent copy of the EBS dsk purpuse
            --Backup
            --Copying AMI for creating multople instance with sane features
            --Creating new volume
(after you creat the instance are you be able to change the encryption of the volume (interview) answer is no becasue you need to change it on the creation time its on the add storage tub
AMI take copy of the EC2)

AWS stores snapshots in the S3 (storage) most


when we creat snapshot we have 2 options to use as source either VOLUME or INSTANCE

## from the slides

Amazone Machone Image (AMI) =====> lunch instnce in the AWS, they are template (configure OS and others softwre). with AMI you copy multiple EC2. types :
                    -public
                    -paid-
                    -private

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-snapshot.html

Data lufe manager (DLM) to creat delete the snapshot.
        --if you back up on wed and you have failure on friday you need to the back up on on tuesday.

creat instance > snapshot >AMI > EC2        

