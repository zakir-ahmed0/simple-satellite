from satellite import Satellite
from monitoring import evaluate_satellite_health

satellite_1 = Satellite("SAT-001")
satellite_2 = Satellite("SAT-002")
satellite_3 = Satellite("SAT-003")

satellite_1.update_telemetry(temperature = 32.5,
                         battery = 85,
                         solar_output = 76.4,
                         signal_strength = 92)

satellite_2.update_telemetry(45, 65, 60, 80)
satellite_3.update_telemetry(28, 20, 85, 55)


satellites = [satellite_1, satellite_2, satellite_3]

for satellite in satellites:
    report = evaluate_satellite_health(satellite)

    print(f"\n {'=' * 35}")
    print(f"SATELLITE: {satellite.satellite_id}")
    print(f"STATUS: {report['status']}")
    
    print("\nTELEMETRY:")
    print(f"Temperature: {satellite.temperature}°C")
    print(f"Battery: {satellite.battery}%")
    print(f"Solar Output: {satellite.solar_output}W")
    print(f"Signal Strength: {satellite.signal_strength}%")

    print("\nALERTS:")
    if report["alerts"]:
        for alert in report["alerts"]:
            print(f"- {alert}")
    else:
        print("No alerts")

    print("\nFAULT EVENTS:")
    if report["fault_events"]:
         for event in report["fault_events"]:
              print(f"- {event}")
    else:
        print("No fault events")

