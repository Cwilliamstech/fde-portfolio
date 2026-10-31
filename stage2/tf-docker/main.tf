terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {
  host = "unix:///Users/conner/.docker/run/docker.sock"
}

resource "docker_network" "bank_net" {
  name = "bank-net"
}

resource "docker_image" "registry"{
  name = "registry:2"
}

resource "docker_container" "registry" {
  name = "bank-registry"
  image = docker_image.registry.image_id
  ports {
    internal = 5001
    external = 5001
  }
}

resource "docker_image" "nginx" {
  name = "nginx"
}

resource "docker_container" "nginx" {
  name = "bank-app"
  image = docker_image.nginx.image_id
  ports {
    internal = 80
    external = 8080
  }
  networks_advanced {
    name = docker_network.bank_net.name
  }
}