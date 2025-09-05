targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment that can be used as part of naming resource convention')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

@description('Resource name prefix')
param resourcePrefix string = 'nap'

param resourceGroupName string = 'rg-${environmentName}'

// Tags that should be applied to all resources.
var tags = {
  'azd-env-name': environmentName
}

// Generate a unique token for use in naming resources
var resourceToken = uniqueString(subscription().id, location, environmentName)

resource rg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: resourceGroupName
  location: location
  tags: tags
}

module resources 'resources.bicep' = {
  name: 'resources-${resourceToken}'
  scope: rg
  params: {
    location: location
    environmentName: environmentName
    resourcePrefix: resourcePrefix
    resourceToken: resourceToken
    tags: tags
  }
}

output AZURE_RESOURCE_GROUP string = rg.name
output AZURE_LOCATION string = location
output RESOURCE_GROUP_ID string = rg.id
output AZURE_APP_SERVICE_NAME string = resources.outputs.APP_SERVICE_NAME
