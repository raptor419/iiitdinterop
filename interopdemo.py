import interop

client = interop.Client(url='http://127.0.0.1:8000',
                        username='testuser',
                        password='testpass')
# The following shows how to request the mission details and the current position of the obstacles.

missions = client.get_missions()
print (missions)

stationary_obstacles, moving_obstacles = client.get_obstacles()
print (stationary_obstacles, moving_obstacles)

#The following shows how to upload UAS telemetry.

telemetry = interop.Telemetry(latitude=38.145215,
                              longitude=-76.427942,
                              altitude_msl=50,
                              uas_heading=90)
client.post_telemetry(telemetry)

# The following shows how to upload a object and it's image.

odlc = interop.Odlc(type='standard',
                    latitude=38.145215,
                    longitude=-76.427942,
                    orientation='n',
                    shape='square',
                    background_color='green',
                    alphanumeric='A',
                    alphanumeric_color='white')
odlc = client.post_odlc(odlc)

with open('testimg.jpg', 'rb') as f:
    image_data = f.read()
    client.put_odlc_image(odlc.id, image_data)
