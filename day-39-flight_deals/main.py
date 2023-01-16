from datetime import datetime, timedelta
from flight_searcher import FlightSearch
from data_manager import DataManager
from notification_manger import NotificationManager

today = datetime.today()
six_month_from_today = today + timedelta(days=180)
data_manager = DataManager()
flight_search = FlightSearch(hometown="Munich")
notification_manager = NotificationManager()

for idx, row in data_manager.sheet_data.iterrows():
    if row.iataCode == '':
        print(row)
        iataCode = flight_search.get_IATA(row["city"])
        data_manager.update_IATA(idx, iataCode)
    else:
        iataCode = row.iataCode
    target_price = row.targetPrice
    response = flight_search.find_flight(
            destination_city=iataCode,
            target_price=target_price,
            from_time=today,
            to_time=six_month_from_today,
            )
    if response is not None:
        notification_manager.send_mail(subject=response[0], body=response[1], to_email="jason-ti@web.de")

