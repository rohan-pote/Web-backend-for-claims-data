# claim service backend test

This is the programming test for all backend candidates.

Please do not push your solution to any public repo.

# Introduction

This is a Python / FastAPI backend service to get customer claim data from our system.

# Environment setup

Checkout the code and set up the service ready for development as follows:

    # Setup your virtual environment
    python3 -m venv venv

    # Activate and use the created virtual environment
    source venv/bin/activate

    # Install all the dependencies
    pip install -r requirements.txt

    # Running the webapp locally and it will be automatically reloaded when changes are made:
    uvicorn src.claim_service.app:app --reload --access-log --log-level debug

    # Optional: Running any test you might choose to write:
    pytest -sv


# Check the service is running after setup

When the app is running you can do the following curl request:

    curl http://localhost:8000/ping
    {
      "name": "claim-service-backend-test",
      "status": "ok",
      "version": "1.0.0"
    }


# Programming test 

You are expected to complete the following tasks:
  - Design and implement a get customer claims endpoint
    - Expectations: 
      - Providing a customer_id, start_time (inclusive) and end_time (inclusive), the endpoint will return a list of claims from that specific customer within the time between start_time and end_time
      - Format of start_time and end_time is YYYYMMDDHHMMSS (e.g. 20230615132510 means 2023/06/15 13:25:10 (UTC+0))
      - Output format as illustrated in the example below
      - Always output with ascending creation_time
  - The claims data supposes to be retrieved through a third-party service. For simplicity of this test, you can use fetch_raw_claims_by_customer_id() pre-defined in dummy.py. 
  - Implement test cases (in tests/ folder) to verify the correctness of your work.
  - Build and run the FastAPI application inside a docker container and verify the endpoint is working as expected, using curl requests.
  - There isn't any strict time limit that you can spend on this task. Feel free to reorg / restructure the code if you think necessary.


After you have completed your work:
  - Clone the repo, and create a new repo in your private github account, mark the repo as private
  - Checkin your changes into your own repo
  - Add the following email as a repo collaborator: technology@napo.pet
  - tar zip your work folder (without the virtual env folder)
  - Submit it via https://forms.gle/qQcKgYGiAxiPwKB48
  - We will primarily assess your work in github, the submitted file is only for backup purpose (just in case there is issue in github).


Before the interview, we will review your work. 
If necessary, you may be asked to demonstrate your work through screen sharing, we may also ask you further questions related to your work during the interview. 


## Get customer claims endpoint behaviour

### A valid GET request

    customer_id = 1201
    start_time = 20230604000000
    end_time = 20230620000000

    Response code: 200

    Output:
    [
      {
        "created_time":"2023-06-04 07:00:00",
        "claim_id":3390,
        "customer_id":1201,
        "policy_id":9012,
        "claim_type":"others",
        "claim_amount_in_pence":61223,
        "decision":"accepted",
        "paid_amount_in_pence":59223
      },
      {
        "created_time":"2023-06-13 07:00:00",
        "claim_id":3391,
        "customer_id":1201,
        "policy_id":9012,
        "claim_type":"accident",
        "claim_amount_in_pence":83842,
        "decision":"accepted",
        "paid_amount_in_pence":81842
      },
      {
        "created_time":"2023-06-15 02:00:00",
        "claim_id":3392,
        "customer_id":1201,
        "policy_id":1234,
        "claim_type":"accident",
        "claim_amount_in_pence":67700,
        "decision":"declined",
        "paid_amount_in_pence":0
      },
      {
        "created_time":"2023-06-17 07:00:00",
        "claim_id":3393,
        "customer_id":1201,
        "policy_id":5678,
        "claim_type":"accident",
        "claim_amount_in_pence":77160,
        "decision":"declined",
        "paid_amount_in_pence":0
      }
    ]

### A bad GET request with bad input

    customer_id = 1201
    start_time = 20230620000000
    end_time = 20230604000000

    Response code: 400

    {
      "detail":"start_time must be before end_time"
    }
