# Stage 2: Air-Gapped & VPC Deployments

## What's here
- `hello/`: a Helm chart (install, upgrade via values, rollback).
- `tf/`: first Terraform build (local provider: plan, apply, destroy).
- `tf-docker/`: Terraform with the Docker provider (private network, local registry, nginx).

## Also practiced
- Simulated an air gap with `docker --network none`; moved images with `docker save`/`load`; scanned with Trivy.
- Kubernetes deployment with 3 replicas; deleted a pod and watched it self-heal.

## Design notes
- One Helm chart per product, one values file per customer (e.g. pointing at a customer's private registry).
- Run `terraform plan` before `apply` at a customer site. In an air gap, providers must be mirrored locally.