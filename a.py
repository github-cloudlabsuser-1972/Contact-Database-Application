{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "webAppName": {
            "type": "string"
        },
        "appServicePlanName": {
            "type": "string"
        },
        "appServicePlanSku": {
            "type": "string"
        }
    },
    "resources": [
        {
            "type": "Microsoft.Web/serverfarms",
            "apiVersion": "2020-06-01",
            "name": "[parameters('appServicePlanName')]",
            "location": "[resourceGroup().location]",
            "sku": {
                "name": "[parameters('appServicePlanSku')]"
            }
        },
        {
            "type": "Microsoft.Web/sites",
            "apiVersion": "2020-06-01",
            "name": "[parameters('webAppName')]",
            "location": "[resourceGroup().location]",
            "dependsOn": [
                "[resourceId('Microsoft.Web/serverfarms', parameters('appServicePlanName'))]"
            ],
            "properties": {
                "serverFarmId": "[resourceId('Microsoft.Web/serverfarms', parameters('appServicePlanName'))]"
            }
        }
    ]
}