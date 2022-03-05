#!/usr/bin/python
'''This shows how to configure and use the ADCs.
'''
from mcp2221 import MCP2221, find_devices
from mcp2221.enums import VoltageReferenceSource, VoltageReferenceValue

# opens 1st device found
mcp = MCP2221(find_devices()[0])
# reads ADC voltage reference source using property
print(mcp.adc_reference_source)
# this tells if the ADC uses VDD or the internal
# reference as a voltage reference; if the later
# is true, then we may want to read the internal
# voltage reference value that way (with property):
print(mcp.adc_voltage_reference)
# sets the ADC reference source and voltage reference
# using properties; note that setting voltage reference voltage
# when reference source is Vdd is useless, but it can be done
mcp.adc_reference_source = VoltageReferenceSource.Vdd
mcp.adc_voltage_reference = VoltageReferenceValue.Voltage2_048V
# reads adc voltage reference source and value with class methods
print(mcp.read_adc_reference_source())
print(mcp.read_adc_voltage_reference())
# writes adc voltage reference source and value with class methods
mcp.write_adc_reference_source(VoltageReferenceSource.Internal)
mcp.write_adc_voltage_reference(VoltageReferenceValue.Voltage1_024V)
# reads ADC 0 value; there are 3 ADCs (indexed as 0, 1 and 2)
print(mcp.adc0_value)
# ADC values are read-only properties
try:
    mcp.adc0_value = 10
except AttributeError as e:
    print("adcx_value properties are read-only: {}".format(e))
# reads the same ADC but using class method
print(mcp.read_adc(0))
