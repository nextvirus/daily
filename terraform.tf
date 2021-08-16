terraform {
  backend "remote" {
    organization = "test-zsh"

    workspaces {
      name = "testtt"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}
provider "aws" {
   access_key = "AKIA6MDLBASGTXEWEENT"
   secret_key = "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"
   region = "cn-northwest-1"
}
resource "aws_s3_bucket" "s3_bucket" {

   bucket = "my-tf-test-bucket202108161"

   acl    = "private"






}
