def length_converter(value, from_unit, to_unit):
    units = {
        'm': 1,
        'meter': 1,
        'cm': 0.01,
        'centimeter': 0.01,
        'mm': 0.001,
        'millimeter': 0.001,
        'km': 1000,
        'kilometer': 1000,
        'mile': 1609.34,
        'foot': 0.3048,
    }
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported units! Choose from m, cm, mm, km, meter, kilometer, mile, or foot.")
    
    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]

    return converted_value

if __name__ == "__main__":
    print("\n--------- Simple length Converter ---------\n")
    value = float(input("Enter a value to convert: "))
    from_unit = input("Enter the unit to convert from (m, cm, mm, km, meter, kilometer, mile, foot): ")
    to_unit = input("Enter the unit to convert to (m, cm, mm, km, meter, kilometer, mile, foot): ")

    try:
        result = length_converter(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}\n")
    except ValueError as e:
        print(e)
