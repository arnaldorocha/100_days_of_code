import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "LON"


# ==================== Update the Airport Codes in Google Sheet ====================

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

# import time
# from data_manager import DataManager
# from flight_search import FlightSearch

# # ==================== Set up the Flight Search ====================

# data_manager = DataManager()
# sheet_data = data_manager.get_destination_data()
# # print(sheet_data)
# flight_search = FlightSearch()

# # ==================== Update the Airport Codes in Google Sheet ====================

# #  In main.py check if sheet_data contains any values for the "iataCode" key.
# #  If not, then the IATA Codes column is empty in the Google Sheet.
# #  In this case, pass each city name in sheet_data one-by-one
# #  to the FlightSearch class to get the corresponding IATA code
# #  for that city using the API.
# #  You should use the code you get back to update the sheet_data dictionary.

# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#         # slowing down requests to avoid rate limit
#         time.sleep(2)
# print(f"sheet_data:\n {sheet_data}")

# data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()

# # # 4. Pass the data back to the main.py file, so that you can print the data from main.py
# # from data_manager import DataManager
# # data_manager = DataManager()
# # sheet_data = data_manager.get_destination_data()
# # # print(sheet_data)

# # #  5. In main.py check if sheet_data contains any values for the "iataCode" key.
# # #  If not, then the IATA Codes column is empty in the Google Sheet.
# # #  In this case, pass each city name in sheet_data one-by-one
# # #  to the FlightSearch class to get the corresponding IATA code
# # #  for that city using the Flight Search API.
# # #  You should use the code you get back to update the sheet_data dictionary.
# # if sheet_data[0]["iataCode"] == "":
# #     from flight_search import FlightSearch
# #     flight_search = FlightSearch()
# #     for row in sheet_data:
# #         row["iataCode"] = flight_search.get_destination_code(row["city"])
# #     print(f"sheet_data:\n {sheet_data}")

# #     data_manager.destination_data = sheet_data
# #     data_manager.update_destination_codes()