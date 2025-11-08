def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature >= 800 or neutrons_emitted <= 500:
        return False
    elif (temperature * neutrons_emitted) >= 500000:
        return False
    else:
        return True

def reactor_efficiency(voltage, current, theoretical_max_power):
    power_output_range = ((voltage * current)/theoretical_max_power)*100

    if power_output_range >= 80:
        return 'green'
    elif power_output_range < 80 and power_output_range >= 60:
        return 'orange'
    elif power_output_range < 60 and power_output_range >= 30:
        return 'red'
    elif power_output_range < 30:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    threshold_90 = (90 * threshold)/100
    threshold_10 = (10 * threshold)/100

    if (temperature * neutrons_produced_per_second) < threshold_90:
        return 'LOW'
    elif (threshold + threshold_10) > (temperature * neutrons_produced_per_second) > (threshold - threshold_10):
        return 'NORMAL'
    else:
        return 'DANGER'
