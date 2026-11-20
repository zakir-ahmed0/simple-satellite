def evaluate_satellite_health(satellite):
    status = "HEALTHY"

    alerts = []
    fault_events = []

    # Temperature monitoring
    if satellite.temperature > 40:
        alerts.append(
            f"[WARNING] {satellite.satellite_id}: "
            f"Temperature is high: {satellite.temperature}°C"
        )

        if satellite.temperature >= 45:
            status = "CRITICAL"
        else:
            status = "WARNING"

    # Battery monitoring
    if satellite.battery < 30:
        status = "CRITICAL"

        alerts.append(
            f"[CRITICAL] {satellite.satellite_id}: "
            f"Battery is low: {satellite.battery}%"
        )

        fault_events.append("LOW_BATTERY")

    # Update satellite status
    satellite.status = status

    # Return monitoring report
    return {
        "status": status,
        "alerts": alerts,
        "fault_events": fault_events
    }
