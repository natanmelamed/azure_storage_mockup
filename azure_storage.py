import json
from fastapi import APIRouter
from azure_storage_client import AzureStorageClient
from common.response_data_handler import ResponseDataHandler

router = APIRouter()
_response_data_handler: ResponseDataHandler = ResponseDataHandler(
    collection_name="azure_storage")


@router.get("/get_local_schemas_details")
async def get_local_schemas_details(file_name: str, file_type: str) -> dict:
    return _response_data_handler.get_responses_data_by_file_name(file_name=file_name,
                                                                  file_type=file_type)


@router.get("/get_schemas_details_cli")
async def get_schemas_details_cli(product: str, type: str, name: str) -> list:
    product_list: list = json.loads(product)
    type_list: list = json.loads(type)
    name_list: list = json.loads(name)
    schemas_details_list: list = list()
    for current_product in product_list:
        for current_type in type_list:
            for current_name in name_list:
                all_schemas_configuration: dict = _response_data_handler.get_responses_data_by_file_name(
                    file_name="all_schemas_configuration",
                    file_type="json")
                if f"{current_product}-{current_type}-{current_name}" in all_schemas_configuration:
                    schemas_details_list.append(
                        all_schemas_configuration[f"{current_product}-{current_type}-{current_name}"])
    return schemas_details_list


@router.get("/get_cli_results")
async def get_cli_results(file_name: str, remote_file_type: str) -> str:
    return f"{file_name} file uploaded as '{remote_file_type}'"


@router.get("/get_remote_schemas_details")
async def get_remote_schemas_details(file_name: str, file_type: str) -> dict:
    return AzureStorageClient().get_json_content_from_file(file_name=f"{file_name}.{file_type}")


@router.delete("/clean_remote_schemas_details")
async def clean_remote_schemas_details(file_name: str, file_type: str) -> str:
    return AzureStorageClient().clean_file_content(file_name=f"{file_name}.{file_type}",
                                                   file_type="json")
