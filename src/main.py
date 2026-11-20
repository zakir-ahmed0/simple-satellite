from satellite import Satellite
from monitoring import evaluate_satellite_health
from telemetry import generate_telemetry



satellite_1 = Satellite("SAT-001")
satellite_2 = Satellite("SAT-002")
satellite_3 = Satellite("SAT-003")


satellites = [satellite_1, satellite_2, satellite_3]


for cycle in range(1, 6):

    print(f"\n{'=' * 45}")
    print(f"SIMULATON CYCLE: {cycle}")
    print(f"{'=' * 45}")

    for satellite in satellites:
        telemetry_data = generate_telemetry()
        satellite.update_telemetry(
        telemetry_data["temperature"],
        telemetry_data["battery"],
        telemetry_data["solar_output"],
        telemetry_data["signal_strength"]

        )

        health_report = evaluate_satellite_health(satellite)

        print(f"\nSatellite ID: {satellite.satellite_id}")
        print(f"Temperature: {satellite.temperature}°C")
        print(f"Battery: {satellite.battery} %")
        print(f"Solar_Output: {satellite.solar_output} W")
        print(f"Signal_Strength: {satellite.signal_strength} %")
        print(f"Status: {health_report['status']}")

        if health_report['alerts']:
            print("Alerts:")
            for alert in health_report["alerts"]:
                print(f"- {alert}")


        if health_report['fault_events']:
            print("Fault Events:")
            for event in health_report["fault_events"]:
                print(f"- {event}")

