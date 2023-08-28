from datetime import datetime

from fastapi import HTTPException


class Validations:
    @staticmethod
    def validate_time(start_time: int, end_time: int):
        """
        This function validates the correctness of start time and end time.
        :param start_time: int, filter from where claim created time should start
        :param end_time: int, filter for where claim created time should end
        :return: No return as this if there is an error there will be an exception raised
        """
        if start_time >= end_time:
            raise HTTPException(status_code=400, detail="start_time must be before end_time")

        elif len(str(start_time)) != 14 or len(str(end_time)) != 14:
            raise HTTPException(status_code=400, detail="invalid entry for time")

    @staticmethod
    def validate_customer_id(customer_id: int, claims: list):
        """
        Validate is input customer_id is present in the customer claims data
        :param customer_id: int
        :param claims: list
        :return: No return as this if there is an error there will be an exception raised
        """
        if not any(claim['customer_id'] == customer_id for claim in claims):
            raise HTTPException(status_code=404, detail="customer_id not found")

    @staticmethod
    def format_response(claim_data: list) -> list:
        """
        Formatting the created time field from YYYYMMDDHHMMSS to 'YYYY-MM-DD HH-MM-SS'
        :param claim_data: list of unformatted claims data
        :return: list of formatted claims data
        """
        for claim in claim_data:
            claim["created_time"] = datetime.strptime(str(claim["created_time"]), '%Y%m%d%H%M%S') \
                .strftime("%Y-%m-%d %H:%M:%S")
        total_claims = {"Total Claims": len(claim_data)}  # This was not in requirements. Was added to test response counts for different query params.
        claim_data.append(total_claims)
        return claim_data
