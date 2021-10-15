"""Constants for stiebel_eltron_isg."""
# Base component constants
NAME = "Stiebel Eltron ISG"
ATTR_MANUFACTURER = "Stiebel Eltron"
DOMAIN = "stiebel_eltron_isg"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ISSUE_URL = "https://github.com/pail23/stiebel_eltron_isg/issues"
DEFAULT_HOST_NAME = ""
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_PORT = 502

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [SENSOR]  # [BINARY_SENSOR, SENSOR, SWITCH]

PRODUCED_HEATING_TODAY = "produced_heating_today"
PRODUCED_HEATING_TOTAL = "produced_heating_total"
PRODUCED_WATER_HEATING_TODAY = "produced_water_heating_today"
PRODUCED_WATER_HEATING_TOTAL = "produced_water_heating_total"

CONSUMED_HEATING_TODAY = "consumed_heating_today"
CONSUMED_HEATING_TOTAL = "consumed_heating_total"
CONSUMED_WATER_HEATING_TODAY = "consumed_water_heating_today"
CONSUMED_WATER_HEATING_TOTAL = "consumed_water_heating_total"


ENERGY_SENSOR_TYPES = [
    [
        "Produced Heating Today",
        PRODUCED_HEATING_TODAY,
        "kWh",
        "mdi:radiator",
    ],
    [
        "Produced Heating Total",
        PRODUCED_HEATING_TOTAL,
        "kWh",
        "mdi:radiator",
    ],
    [
        "Produced Water Heating Today",
        PRODUCED_WATER_HEATING_TODAY,
        "kWh",
        "mdi:water-boiler",
    ],
    [
        "Produced Water Heating Total",
        PRODUCED_WATER_HEATING_TOTAL,
        "kWh",
        "mdi:water-boiler",
    ],
    [
        "Consumed Heating Today",
        CONSUMED_HEATING_TODAY,
        "kWh",
        "mdi:lightning-bolt",
    ],
    [
        "Consumed Heating Total",
        CONSUMED_HEATING_TOTAL,
        "kWh",
        "mdi:lightning-bolt",
    ],
    [
        "Consumed Water Heating Today",
        CONSUMED_WATER_HEATING_TODAY,
        "kWh",
        "mdi:lightning-bolt",
    ],
    [
        "Consumed Water Heating Total",
        CONSUMED_WATER_HEATING_TOTAL,
        "kWh",
        "mdi:lightning-bolt",
    ],
]


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
