import requests

API_KEY = "5d249d90eac7954a1dd7400db935fc21"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]  # 包含未来五天的天气预报，一共40个数据，8个算一天
    nr_values = 8 * forecast_days  # 按天数获取数据
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))
