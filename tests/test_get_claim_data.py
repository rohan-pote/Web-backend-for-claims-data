class TestClaimAPI:

    def test_get_claim_data(self, client):
        customer_id = 1201
        start_time = 20230604000000
        end_time = 20230830000000
        response = client.get("http://localhost:8000/claims",
                              params={"customer_id": customer_id, "start_time": start_time,
                                      "end_time": end_time})
        json_response = response.json()
        assert response.status_code == 200
        assert json_response[0]["customer_id"] == 1201

    def test_invalid_start_time(self, client):
        customer_id = 1201
        start_time = 20231004000000
        end_time = 20230830000000
        response = client.get("http://localhost:8000/claims",
                              params={"customer_id": customer_id, "start_time": start_time,
                                      "end_time": end_time})
        print(response.json())
        json_response = response.json()
        assert json_response["error details"]["status_code"] == 400
        assert json_response["error details"]["detail"] == "start_time must be before end_time"

    def test_invalid_customer_id(self, client):
        customer_id = 1203
        start_time = 20230604000000
        end_time = 20230830000000
        response = client.get("http://localhost:8000/claims",
                              params={"customer_id": customer_id, "start_time": start_time,
                                      "end_time": end_time})
        print(response.json())
        json_response = response.json()
        assert json_response["error details"]["status_code"] == 404
        assert json_response["error details"]["detail"] == "customer_id not found"
