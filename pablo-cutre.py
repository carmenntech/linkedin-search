from linkedin_api.clients.restli.client import RestliClient
from credenciales import *

restli_client = RestliClient()

response = restli_client.get(
    resource_path="/userinfo",
    access_token = ACCESS_TOKEN

  
)


print(response.entity)       

#3987802371