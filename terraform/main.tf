# example code, to practice, taken from
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloud9_environment_ec2

#####################################################################################################
# providers
#####################################################################################################
provider "aws" {
    region = "us-east-2"
}

#####################################################################################################
# resources
#####################################################################################################
resource "aws_cloud9_environment_ec2" "example" {
  instance_type = "t2.micro"
  name = "bks-c9-practice"
  automatic_stop_time_minutes = 30
}

#####################################################################################################
# data
#####################################################################################################
data "aws_instance" "cloud9_instance" {
  filter {
    name = "tag:aws:cloud9:environment"
    values = [aws_cloud9_environment_ec2.example.id]
  }
}

# get the latest amazon linux ami
data "aws_ssm_parameter" "ami" {
  name = "/aws/service/ami-amazon-linux/amzn2-ami-hvm-x86_64-gp2"
}
#####################################################################################################
# output
#####################################################################################################
# output "cloud9_url" {
#   value = "https://${var.region}.console.aws.amazon.com/cloud9/ide/${aws_cloud9_environment_ec2.example.id}"
# }