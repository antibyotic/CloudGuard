variable "vpc_id" {
  description = "ID of the VPC these security groups belong to"
  type        = string
}

variable "my_ip" {
  description = "Your IP address in CIDR notation, for bastion SSH access"
  type        = string
}