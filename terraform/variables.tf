locals {
  data_lake_bucket = "de_data_lake"
}

variable "project" {
  description = "de-bootcamp-357803"
}

variable "region" {
  description = "Region for GCP resources"
  default = "northamerica-northeast1"
  type = string
}

variable "bucket_name" {
  description = "Name of GCP storage bucket"
  default = ""
}

variable "storage_class" {
  description = "Storage class type for bucket"
  default = "STANDARD"
}

variable "BQ_DATASET" {
    description = "BigQuery Dataset that raw data will be written to"
    type = string
    default = "covid_data_all"
}

variable "TABLE_NAME" {
    description = "BigQuery Table"
    type = string
    default = "to_covid"
}