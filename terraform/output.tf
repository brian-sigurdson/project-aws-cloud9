output "cloud9_url" {
  value = "https://${var.region}.console.aws.amazon.com/cloud9/ide/${aws_cloud9_environment_ec2.my-ide.id}"
}

output "id" {
  value = aws_cloud9_environment_ec2.my-ide.id
}

output "arn" {
  value = aws_cloud9_environment_ec2.my-ide.arn
}

output "tags_all" {
  value = aws_cloud9_environment_ec2.my-ide.tags_all
}

output "type" {
  value = aws_cloud9_environment_ec2.my-ide.type
}