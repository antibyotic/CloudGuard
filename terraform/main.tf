module "vpc" {
  source       = "./modules/vpc"
  vpc_cidr     = "10.0.0.0/16"
  project_name = "cloudguard"
  azs          = ["eu-central-1a", "eu-central-1b"]
}

module "security" {
  source = "./modules/security"
  vpc_id = module.vpc.vpc_id
  my_ip  = "134.102.8.152/32"
}