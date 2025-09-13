provider "azurerm" {
    features {}
}

resource "azurerm_resource_group" "example" {
    name     = "example-resources"
    location = "East US"
}

resource "azurerm_storage_account" "example" {
    name                     = "examplestoracc1234"
    resource_group_name      = azurerm_resource_group.example.name
    location                 = azurerm_resource_group.example.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
}

resource "azurerm_storage_share" "example" {
    name                 = "exampleshare"
    storage_account_name = azurerm_storage_account.example.name
    quota                = 50
}

output "storage_account_name" {
    value = azurerm_storage_account.example.name
}

output "storage_share_name" {
    value = azurerm_storage_share.example.name
}