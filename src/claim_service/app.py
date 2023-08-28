from fastapi import FastAPI
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", status_code=200)
@app.get("/ping", status_code=200)
async def ping():
    """This is used to "ping" the web service to check if its running.

    Returns:
        dict[str, str]: a status dict which the configured view will return as JSON.
        
        The dict has the form::
        dict(
            status="ok",
            name="claim-service-backend-test",
            version="<version number of service>"
        )
    """
    return dict(
            status="ok",
            name="claim-service-backend-test",
            version="1.0.0",
        )

