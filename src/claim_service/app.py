from fastapi import FastAPI
import logging
from .fetch_raw_claims import fetch_raw_claims_by_customer_id
from .validations import Validations

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

"""
Note: For a bigger project, the endpoints would ideally be split in different files, one file for each endpoint.
This can be done by utilizing the APIRouter available from FastAPI using import: from fastapi import APIRouter   
"""


@app.get("/", status_code=200)
@app.get("/ping", status_code=200)
async def ping():
    """This is used to "ping" the web service to check if it's running.

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


@app.get("/claims/")
def get_customer_claims(customer_id: int, start_time: int, end_time: int):
    """
    This endpoint will be used to get the customer claims.
    :param customer_id:
    :param start_time:
    :param end_time:
    :return: list of customer claims
    """
    try:
        logger.info(msg="Call to get customer claims")
        Validations.validate_time(start_time=start_time, end_time=end_time)
        claim_data = fetch_raw_claims_by_customer_id(customer_id=customer_id, start_time=start_time,
                                                     end_time=end_time)
        Validations.format_response(claim_data)
        return claim_data
    except Exception as e:
        logger.error(msg="Error getting claim data", exc_info=True)
        return {"message": "Error getting claim data",
                "error details": e}
