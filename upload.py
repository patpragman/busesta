"""
This code is a series of functions to push code and content to AWS

"""

import boto3



def update_api(lambda_function_endpoints=["bus"], env="dev"):
    """
    This code updates the api by spooling up a lambda client, then for each end point selected
    uploading the associated zip file.

    notes.  The zip files have to have a specific format "deployment_package_<type of api action>.zip"
    we could probably make this more generalized later, refactor if necessary


    :param lambda_function_endpoints: the api endpoint names - for instance, <env>-post or somethign
    :param env: the other half of the api endpoint name
    :return: None - it just does it's work and then dies
    """
    lambda_client = boto3.client("lambda")
    for lambda_function_endpoint in lambda_function_endpoints:
        # iterate through post and get and update the lambda functions that handle posts and get requests on aws
        with open(f"deployment_package_{lambda_function_endpoint}.zip", "rb") as zipfile:
            lambda_client.update_function_code(
                FunctionName=f'{lambda_function_endpoint}',
                ZipFile=zipfile.read()
            )




if __name__ == "__main__":
    update_api()

