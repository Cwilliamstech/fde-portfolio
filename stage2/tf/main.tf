terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

resource "local_file" "hello" {
  filename = "hello.txt"
  content  = "hi from terraform test file 2"
}