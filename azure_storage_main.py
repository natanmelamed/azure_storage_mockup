import uvicorn
import azure_storage
from fastapi import FastAPI


app = FastAPI()
base_url = "/azure_storage"
app.include_router(azure_storage.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('azure_storage_main:app', host='0.0.0.0', port=80, reload=True)
