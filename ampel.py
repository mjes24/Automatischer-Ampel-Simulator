import time

def show_signal(color, duration):
    print(f"{color} – {'STOP' if color == 'ROT' else 'BEREIT' if color == 'GELB' else 'LOS'}")
    time.sleep(duration)

def traffic_light_cycle():
    while True:
        show_signal("ROT", 3)
        show_signal("GELB", 1)
        show_signal("GRÜN", 3)
        print("---------------")

if __name__ == "__main__":
    traffic_light_cycle()
