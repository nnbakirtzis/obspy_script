from obspy import read
from obspy.core.event import read_events
import matplotlib.pyplot as plt
import os


# Fetches latitude and longitude from a single file
def get_lat_and_long(file_path):
    # Read the file
    catalog = read_events(file_path)

    latitude = []
    longitude = []

    # Extract latitude and longitude
    for event in catalog:
        origin = event.origins[0]
        latitude.append(origin.latitude)
        longitude.append(origin.longitude)
    
    return latitude, longitude


def main(path):
    latitudes = []
    longitudes = []

    # Handles the case where the user gives a folder instead of a single file
    # If the input is a directory, iterate through the individual files inside of it
    if os.path.isdir(path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            # Check if it is a file and ends with .qml
            if os.path.isfile(file_path) and filename.endswith('.qml'):
                latitude, longitude = get_lat_and_long(file_path)
                latitudes.extend(latitude)
                longitudes.extend(longitude)
    # If the input is a single file
    elif os.path.isfile(path):
        latitude, longitude = get_lat_and_long(path)
        latitudes.extend(latitude)
        longitudes.extend(longitude)
    # Error handling 
    else:
        print("Error: Invalid input.")
        return

    if not latitudes or not longitudes:
        print("Error: No events were found.")
        return

    # Configure matplotlib and plot the event locations
    plt.figure(figsize=(10, 6))
    plt.scatter(longitudes, latitudes, marker='.', color='red')
    plt.title("Locations of Earthquake Events")
    plt.ylabel("Latitude")
    plt.xlabel("Longitude")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    input_file_path = input("Enter the path to the file/directory: ")
    main(input_file_path)







