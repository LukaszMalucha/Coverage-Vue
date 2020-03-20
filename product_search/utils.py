
BRAND_MAPPER = {("ansul", "ANSUL"), ("autocall", "Autocall"), ("bcpro", "BCPro"), ("cem-systems", "CEM Systems"),
                ("chemguard", "CHEMGUARD"), ("champion", "Champion"), ("coleman", "Coleman"), ("exacq", "Exacq"),
                ("fireater", "FIREATER"), ("facility-explorer", "Facility Explorer"), ("fraser-johnston", "Fraser-Johnston"),
                ("gem", "GEM"), ("hygood", "HYGOOD"), ("johnson-controls", "Johnson Controls"), ("kantech", "Kantech"),
                ("lpg", "LPG"), ("lux", "LUX"), ("luxaire", "Luxaire"), ("metasys", "Metasys"), ("neuruppin", "NEURUPPIN"),
                ("peak", "PEAK"), ("penn-controls", "PENN Controls"), ("pyro-chem", "PYRO-CHEM"), ("quantech", "Quantech"),
                ("ruskin", "Ruskin"), ("sabo-foam", "SABO FOAM"), ("skum", "SKUM"), ("sensormatic", "Sensormatic"),
                ("shoppertrak", "ShopperTrak"), ("simplex", "Simplex"), ("thorn-security", "THORN SECURITY"),
                ("tempmaster", "TempMaster"), ("triatek", "Triatek"), ("truevue", "TrueVUE"), ("tyco", "Tyco"),
                ("verasys", "Verasys"), ("williams", "WILLIAMS"), ("york", "YORK"), ("zettler", "Zettler"), ("frick", "FRICK")}


def clean_brand_list(lst):
    """Clean brand names so they can be used for urls"""
    clean_brands = []
    for element in lst:
        new_element = element.lower()
        new_element = new_element.replace(" ", "-")
        clean_brands.append(new_element)

    if "not-specified" in clean_brands:
        clean_brands.remove("not-specified")

    return clean_brands


def get_brand_name(string):
    """Find the real name of a brand - as listed on FT"""
    for element in BRAND_MAPPER:
        if string == element[0]:
            brand_string = element[1]
            return brand_string
    return string


def reverse_brand_name(string):
    """Get clean brand string"""
    for element in BRAND_MAPPER:
        if string == element[1]:
            brand_string = element[0]
            return brand_string
    return "johnson-controls"