import random



def generate_telemetry():
    temperature = round(random.uniform(20, 48), 1)
    battery = round(random.uniform(20,100), 1)
    solar_output = round(random.uniform(0,100), 1)
    signal_strength = round(random.uniform(40,100), 1)
    return {
        "temperature" : temperature,
        "battery" : battery,
        "solar_output" : solar_output,
        "signal_strength" : signal_strength
    }