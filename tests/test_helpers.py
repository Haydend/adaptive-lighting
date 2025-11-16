from custom_components.adaptive_lighting.helpers import build_mqtt_message


def test_build_mqtt_message_with_brightness_and_colour_temp():
    service_data = {
        "color_temp_kelvin":4000,
        "brightness": 456
    }

    assert build_mqtt_message(service_data) == "{\"color_temp\":250,\"brightness\":456,\"state\":null}"

def test_build_mqtt_message_with_only_brightness():
    service_data = {
        "brightness": 456
    }

    assert build_mqtt_message(service_data) == "{\"brightness\":456,\"state\":null}"

def test_build_mqtt_message_with_only_colour_temp():
    service_data = {
        "color_temp_kelvin":4000,
    }

    assert build_mqtt_message(service_data) == "{\"color_temp\":250,\"state\":null}"


