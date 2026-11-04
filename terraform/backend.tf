terraform {
  backend "s3" {
    bucket       = "cloudguard-terraform-state-150897468812"
    key          = "cloudguard/terraform.tfstate"
    region       = "eu-central-1"
    use_lockfile = true
    encrypt      = true
  }
}
