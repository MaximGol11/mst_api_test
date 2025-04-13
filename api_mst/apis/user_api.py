from restclient.client import RestClient
from api_mst.models.email_register.registration_form import (RegistrationForm)
from api_mst.models.email_register.register_by_email_successful_response import RegisterResponse


class UserApi(RestClient):
    
    def post_api_v2_register_json(self, email_registration_form: RegistrationForm):
        """
        Register a new user using the provided registration form data.

        Args:
            email_registration_form (RegistrationForm): The registration form data.

        Returns:
            Response: The response object from the request.
        """
        url = "/api/v2/register.json"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = email_registration_form.to_form()
        
        response = self.post(
            path="/api/v2/register.json",
            headers=headers,
            data=email_registration_form.to_form()
            )
        
        return RegisterResponse(**response.json())
            
        