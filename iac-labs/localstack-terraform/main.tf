# 1. Tell Terraform to use a slightly older AWS provider (v4.x is much more stable with LocalStack)
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.67.0"
    }
  }
}

# 2. Configure the AWS provider for LocalStack
provider "aws" {
  region     = "us-east-1"
  access_key = "test"
  secret_key = "test"

  endpoints {
    s3  = "http://localhost:4566"
    ec2 = "http://localhost:4566"
    iam = "http://localhost:4566"
  }

  # These skips prevent Terraform from making real-AWS validation calls that LocalStack can't answer
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  skip_region_validation      = true

  # CRITICAL FIX: Forces Terraform to use http://localhost:4566/bucketname instead of http://bucketname.localhost:4566
  s3_use_path_style = true
}

# 3. Define the resource: An S3 Bucket
resource "aws_s3_bucket" "devops_learning_bucket" {
  bucket = "my-terraform-localstack-bucket"
}

# 4. Define the resource: An S3 Bucket Object (a file inside the bucket)
resource "aws_s3_object" "example_file" {
  bucket  = aws_s3_bucket.devops_learning_bucket.id
  key     = "hello.txt"
  content = "Hello from Terraform and LocalStack! 🚀"
}