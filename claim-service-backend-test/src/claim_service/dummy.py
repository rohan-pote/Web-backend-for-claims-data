import json

# decision
# 0 - declined
# 1 - accepted

# claim_type
# 0 - accident
# 1 - illness
# 2 - others

def fetch_raw_claims_by_customer_id(customer_id):
    """Retrieve all the customer claims for the given customer_id.

    This should contact the external claim API to recover the listing for the
    given customer_id.

    :param customer_id: The customer id e.g. 1201

    :returns: A list of claim for the given customer.

    """
    
    # This is the dummy claim data responses from our external service
    claims = json.load(open("claim_service/dummy_claims_response.json", "r"))
    
    return [claim for claim in claims if claim["customer_id"] == customer_id]