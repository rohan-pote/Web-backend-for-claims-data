# claim service backend test solution

For project requirements please refer: https://github.com/rohan-pote/napo-challenge/blob/main/README.requirements.md

## Assumptions and approach
1. The endpoint requires all following parameters for getting the correct response. Error handling is added if any parameter is missing. 
   1. customer_id
   2. start_time
   3. end_time
2. The datetime format provided in the project is YYYYMMDDHHMMSS. The datetime in the `dummy_claims_response.json` file was not as per this format. 
   1. For eg: 1685761200000 does not provide a valid datetime format equal to `YYYYMMDDHHMMSS`. Hence, the `created_time` in the `json` has been updated to work for this project.
3. The size of the project is small requiring only one endpoint. Therefore, the `/claims` endpoint is added in the `app.py` script. Ideally for a bigger project the best practice is to add each endpoint in its own python file. This can be done by utilizing the `APIRouter` available from `FastAPI` using import: `from fastapi import APIRouter`.    

## Local Environment Setup

Checkout the code and set up the service ready for development as follows:

    # Setup your virtual environment
    python3 -m venv venv

    # Activate and use the created virtual environment
    source venv/bin/activate

    # Install all the dependencies
    pip install -r requirements.txt
    
    # Running the webapp locally and it will be automatically reloaded when changes are made:
    uvicorn src.claim_service.app:app --reload --access-log --log-level debug

## Building and running Docker container
    # cd to directory conataining Dockerfile
    
    # Build the docker image and tag the image as claim-api-service:
    docker build -t claim-api-service . 

    # Create a docker container using the built image and run it:  
    docker run --rm -it --name claim-api -p 8000:8000 claim-api-service

![Screenshot 2023-08-29 at 00 47 02](https://github.com/rohan-pote/napo-challenge/assets/34726174/83c042c0-d4c6-4430-ae23-7db8a3bbc261)

## Calling the customer claims endpoint:
      # When the app is running you can do the following curl request: 
      
      curl --location 'http://localhost:8000/claims?customer_id=1201&start_time=20230604000000&end_time=20230730000000'
      
      Query parameters: 
      customer_id = 1201
      start_time = 20230604000000
      end_time = 20230605000000

   This will give the response: 
```json
   [
       {
           "created_time": "2023-06-04 00:00:00",
           "claim_id": 3389,
           "customer_id": 1201,
           "policy_id": 5678,
           "details": {
               "claim_type": 2,
               "claim_amount": 619.16
           },
           "result": {
               "decision": 1,
               "paid_amount": 544.16
           }
       },
       {
           "Total Claims": 1
       }
   ]
```

**Note: The "Total Claims" details have been included to provide more information on how many claims are returned in the response based on the `start_time` and the `end_time` filter. This was not a requirement but I felt this give a good insight in change in claims data with respect to time filters**

## Error handling

1. Providing start_time greater than end_time will result in the 400 bad request:


      # curl --location 'http://localhost:8000/claims?customer_id=1201&start_time=20230704000000&end_time=20230605000000' 
      
      Query parameters: 
      customer_id = 1201
      start_time = 20230704000000
      end_time = 20230605000000

   ```json
   {
       "message": "Error getting claim data",
       "error details": {
           "status_code": 400,
           "detail": "start_time must be before end_time",
           "headers": null
       }
   }
   ``` 

2. Providing invalid customer_id will result in 404 error response: 


      # curl --location 'http://localhost:8000/claims?customer_id=1203&start_time=20230604000000&end_time=20230605000000' 
      
      Query parameters: 
      customer_id = 1203
      start_time = 20230604000000
      end_time = 20230605000000

   ```json
   {
       "message": "Error getting claim data",
       "error details": {
           "status_code": 404,
           "detail": "customer_id not found",
           "headers": null
       }
   }
   ``` 
3. Providing invalid format of start_time of end_time (YYYYMMDDHHMMSS) will result in a 400 bad request: 


      # curl --location 'http://localhost:8000/claims?customer_id=1201&start_time=202306040000&end_time=20230605000000' 
      
      Query parameters: 
      customer_id = 1201
      start_time  = 202306040000
      end_time    = 20230605000000

   ```json
   {
       "message": "Error getting claim data",
       "error details": {
           "status_code": 400,
           "detail": "invalid entry for time",
           "headers": null
       }
   }
   ``` 



## Running tests

1. Tests are added in the `/tests` folder
2. To run tests execute the command: 
   `pytest -sv`
