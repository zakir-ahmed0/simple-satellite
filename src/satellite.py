class Satellite:
    def __init__(self, satellite_id):
        self.satellite_id = satellite_id
        self.temperature = None
        self.battery = None
        self.solar_output = None
        self.signal_strength = None
        self.status = "UNKNOWN"

    def update_telemetry(self, temperature, battery, solar_output, signal_strength):
        # Validate the telemetry data types
        if not isinstance(temperature, (int,float)) or isinstance(temperature, bool):
            raise TypeError("Temperature must be a number,")
        
        if not isinstance (battery , (int, float)) or isinstance(battery , bool):
            raise TypeError("Battery must be a number,")
        
        if not isinstance(solar_output, (int,float)) or isinstance(solar_output, bool):
            raise TypeError("Solar output must be a number,")
        
        if not isinstance(signal_strength, (int,float)) or isinstance(signal_strength, bool):
            raise TypeError("Signal Strength must be a number,")
        
        #Validate each measuremenet's range
        if not -100 <= temperature <= 150:
            raise ValueError("Temperature is outside the valid range")
        
        if not 0 <= battery <= 100:
            raise ValueError("Battery is outside the valid range")
        
        if not 0 <= solar_output <= 100:
            raise ValueError("Solar output is outside the valid range")
        
        if not 0 <= signal_strength <= 100:
            raise ValueError("Signal Strength is outside the valid range")
                
        
        
        self.temperature = temperature
        self.battery = battery
        self.solar_output = solar_output
        self.signal_strength = signal_strength

        
        