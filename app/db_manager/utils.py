# JOHNSON CONTROLS BRANDS

BRANDS = {"YORK", "Johnson Controls", "Metasys", "Simplex", "PENN Controls", "Kantech",
          "Facility Explorer", "LUX", "CEM Systems", "Exacq", "Sensormatic", "Tyco",
          "BCPro", "Quantech", "PEAK", "Verasys", "Ruskin", "Autocall",
          "ShopperTrak", "Triatek", "ANSUL", "PYRO-CHEM", "WILLIAMS", "CHEMGUARD",
          "Champion", "Coleman", "Fraser-Johnston", "Luxaire", "TempMaster", "TrueVUE",
          "SKUM", "HYGOOD", "LPG", "GEM", "FIREATER", "SABO FOAM", "NEURUPPIN",
          "THORN SECURITY", "Zettler", "FRICK"}


def get_longest_string(dataset, column):
    """Find longest string in the column"""
    values_list = list(dataset[column].unique())
    try:
        longest = max(values_list, key=len)
    except Exception as e:
        longest = "N/A"
    return longest


def get_shortest_string(dataset, column):
    """Find shortest string in the column"""
    values_list = list(dataset[column].unique())
    try:
        shortest = min(values_list, key=len)
    except Exception as e:
        shortest = "N/A"
    return shortest


def get_na_count(dataset, column):
    """Count 'Not Specified' in column"""
    na_count = len(dataset[dataset[column] == "Not Specified"])
    return na_count


def get_missing_brands(dataset, column):
    """Check for incorrect/missing brands"""
    column_brands = set(list(dataset[column].unique()))
    difference = column_brands - BRANDS
    difference = ", ".join(difference)
    return difference


def describe_column(dataset, column):
    """Compile all the checks above"""
    column_dict = {}
    col_name = column.replace("_", " ")
    col_name = col_name.title()
    column_dict["name"] = col_name
    column_dict["Longest String"] = get_longest_string(dataset, column)
    column_dict["Shortest String"] = get_shortest_string(dataset, column)
    column_dict["Not Specified"] = get_na_count(dataset, column)

    return column_dict