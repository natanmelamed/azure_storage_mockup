import os
from azure.storage.blob import ContainerClient
from common.json_parser import load_data_from_json_file
from common.base_azure_storage_client import BaseAzureStorageClient
from common.data_files_handler import get_full_path_file_by_file_name


class AzureStorageClient(BaseAzureStorageClient):
    AZURE_STORAGE_CLIENT_CONF_PATH: str = get_full_path_file_by_file_name(
        "azure_storage_client_conf.json")
    RESPONSES_DATA_FOLDER: str = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                              "responses_data")

    def __init__(self):
        self.container_key: str = "container_name"
        self.connection_string_key: str = "connection_string"
        self.config_file: dict = load_data_from_json_file(self.AZURE_STORAGE_CLIENT_CONF_PATH)[
            "automation"]
        self.azure_storage_client: BaseAzureStorageClient = \
            BaseAzureStorageClient(self.config_file,
                                   self.connection_string_key,
                                   self.container_key)
        self.azure_container_client: ContainerClient = \
            self.azure_storage_client.azure_container_client
        super().__init__(self.config_file, self.connection_string_key, self.container_key)
