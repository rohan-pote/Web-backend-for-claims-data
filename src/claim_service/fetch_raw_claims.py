import json
import os
from .validations import Validations


# decision
# 0 - declined
# 1 - accepted

# claim_type
# 0 - accident
# 1 - illness
# 2 - others

def fetch_raw_claims_by_customer_id(customer_id: int, start_time: int, end_time: int):
    """Retrieve all the customer claims for the given customer_id.

    This should contact the external claim API to recover the listing for the
    given customer_id.

    :param end_time:
    :param start_time:
    :param customer_id: The customer id e.g. 1201

    :returns: A list of claim for the given customer.

    """
    # This is the dummy claim data responses from our external service

    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'dummy_claims_response.json')

    claim_data = open(filename, 'r')
    claims = json.load(claim_data)

    Validations.validate_customer_id(customer_id=customer_id, claims=claims)

    return [claim for claim in claims
            if (claim["customer_id"] == customer_id) and
            (claim["created_time"] >= start_time) and
            (claim["created_time"] <= end_time)]
