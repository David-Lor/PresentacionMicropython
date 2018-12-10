import network

def connect():
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        with open("WIFI_SSID.txt","r") as f:
            ssid = f.read().strip()
        with open("WIFI_PASSWORD.txt","r") as f:
            password = f.read().strip()
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass

    print('network config:', sta_if.ifconfig())

    network.WLAN(network.AP_IF).active(False)

