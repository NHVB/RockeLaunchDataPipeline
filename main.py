from rocket_launch.fetch_api_response import fetch_api



if __name__ == "__main__":
    url = "https://api.spacexdata.com/v5/launches/latest"
    response = fetch_api(url)
    print(response)