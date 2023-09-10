# Zadanie 1 - Parkujeme

# Meno: 
# Spolupráca: 
# Použité zdroje: 
# Čas potrebný na vypracovanie: 


def load_parking_records(file_path):
    records = []
    file_path = open(file_path, 'r')

    with open(file_path, 'r') as f:
        for line in f:
                spz, start_h, start_m, end_h, end_m = line.strip().split(',')
                start_h, start_m, end_h, end_m = map(int, [start_h, start_m, end_h, end_m])

                records.append((spz, start_h, start_m, end_h, end_m))
    return records


def load_prices(file_path):
    prices = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split(': ')
            prices[key] = float(value)
    return prices


def calculate_parking_time(start_h, start_m, end_h, end_m):  # 0.5b
    time_in_minutes = (end_h - start_h) * 60 + (end_m - start_m)
    return time_in_minutes


def get_parking_fee(time_in_minutes, prices):  # 1b
    """
    Calculates and returns the price of parking for a given amount
    of time based on pricing.
    """
    price4 = 0.0
    prices3 = 0.0
 
    if(time_in_minutes < 15):
        prices3 = 0.0
    elif(time_in_minutes < 30):
        prices3 = prices["30m"]
    elif(time_in_minutes <= 60):
        prices3 = prices["1h"]
    elif(time_in_minutes <= 180):
        fullHour = int(time_in_minutes / 60)
        lastMinute = time_in_minutes % 60
        prices3 += prices["h+"] * fullHour
        # if lastMinute:
        prices3 += prices["1h"]
        price4 = prices["3h"]
        if price4 < prices3:
            prices3 = price4
    elif(time_in_minutes <= 360):
        prices3 = prices["3h"]
        time_in_minutes = time_in_minutes - 180
        fullHour = int(time_in_minutes / 60)
        lastMinute = time_in_minutes % 60
        prices3 += prices["h+"] * fullHour
        # if lastMinute:
        prices3 += prices["h+"]
        price4 = prices["6h"]
        if price4 < prices3:
            prices3 = price4
    elif(time_in_minutes <= 1440):
        prices3 = prices["6h"]
        time_in_minutes = time_in_minutes - 360
        fullHour = int(time_in_minutes / 60)
        lastMinute = time_in_minutes % 60
        prices3 += prices["h+"] * fullHour
        # if lastMinute:
        prices3 += prices["h+"]
        price4 = prices["1d"]
        if price4 < prices3:
            prices3 = price4
    return prices3


def calculate_average_parking_fee(records, prices):  # 0.5b
    total = 0.0

    for spz, start_h, start_m, end_h, end_m in records:
        time_in_minutes = calculate_parking_time(start_h, start_m, end_h, end_m)
        fee = get_parking_fee(time_in_minutes, prices)
        total += fee
    average_parking = total / len(records)
    return float(average_parking)


def calculate_average_parking_time(records):  # 0.5b
    total = 0
    # a = 2
    for spz, start_h, start_m, end_h, end_m in records:
        time_in_minutes = calculate_parking_time(start_h, start_m, end_h, end_m)
        total += time_in_minutes
    average_time = total / len(records)
    return float(average_time)


def calculate_average_stays(records):  # 0.5b
    venich = {}
    total_stays = 0
    for record in records:
        spz, _, _, _, _ = record
        # get = bool, шукає подібне 1, якщо не 0
        venich[spz] = venich.get(spz, 0) + 1
        total_stays += 1

    average_stays = total_stays / len(venich)
    return float(average_stays)


def get_most_common_region(records):  # 1b
    region_count = {}

    for record in records:
        spz, _, _, _, _ = record
        region_code = spz[:2]
        region_count[region_code] = region_count.get(region_code, 0) + 1

    total_region_code = max(region_count, key=region_count.get)
    return total_region_code


def get_busiest_hour(records):  # 0.5b
    max_count = 0
    busiest_hour = 0
    count_8 = count_9 = count_10 = count_11 = count_12 = count_13 = 0
    for record in records:
     _, start_h, _, end_h, _ = record
    # [0] - це час якій є в началі і в кінці години
    arrive_hour = int(start_h[0])
    leave_hour = int(end_h[0])

    for hour in range(arrive_hour, leave_hour + 1):
        if hour == 8:
            count_8 += 1
        elif hour == 9:
            count_9 += 1
        elif hour == 10:
            count_10 += 1
        elif hour == 11:
            count_11 += 1
        elif hour == 12:
            count_12 += 1
        elif hour == 13:
            count_13 += 1

# година є найбільш завантаженою
    if count_8 > max_count:
        max_count = count_8
        busiest_hour = 8
    if count_9 > max_count:
        max_count = count_9
        busiest_hour = 9
    if count_10 > max_count:
        max_count = count_10
        busiest_hour = 10
    if count_11 > max_count:
        max_count = count_11
        busiest_hour = 11
    if count_12 > max_count:
        max_count = count_12
        busiest_hour = 12
    if count_13 > max_count:
        max_count = count_13
        busiest_hour = 13
    return float(busiest_hour)


def get_max_number_of_cars(records):  # 2b
    """
    Returns the highest number of cars parked at the parking lot in a given
    minute.
    """
    return 0, list()


def optimize_hourly_fee(records, prices):  # 2b
    """
    Returns the fee of additional hours that will maximize income for
    the parking lot.
    """
    return 0.0
