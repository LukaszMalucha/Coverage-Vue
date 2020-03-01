
BRAND_MAPPER = {('ansul', 'ANSUL'), ('autocall', 'Autocall'), ('bcpro', 'BCPro'), ('cem-systems', 'CEM Systems'),
                ('chemguard', 'CHEMGUARD'), ('champion', 'Champion'), ('coleman', 'Coleman'), ('exacq', 'Exacq'),
                ('fireater', 'FIREATER'), ('facility-explorer', 'Facility Explorer'), ('fraser-johnston', 'Fraser-Johnston'),
                ('gem', 'GEM'), ('hygood', 'HYGOOD'), ('johnson-controls', 'Johnson Controls'), ('kantech', 'Kantech'),
                ('lpg', 'LPG'), ('lux', 'LUX'), ('luxaire', 'Luxaire'), ('metasys', 'Metasys'), ('neuruppin', 'NEURUPPIN'),
                ('peak', 'PEAK'), ('penn-controls', 'PENN Controls'), ('pyro-chem', 'PYRO-CHEM'), ('quantech', 'Quantech'),
                ('ruskin', 'Ruskin'), ('sabo-foam', 'SABO FOAM'), ('skum', 'SKUM'), ('sensormatic', 'Sensormatic'),
                ('shoppertrak', 'ShopperTrak'), ('simplex', 'Simplex'), ('thorn-security', 'THORN SECURITY'),
                ('tempmaster', 'TempMaster'), ('triatek', 'Triatek'), ('truevue', 'TrueVUE'), ('tyco', 'Tyco'),
                ('verasys', 'Verasys'), ('williams', 'WILLIAMS'), ('york', 'YORK')}


def clean_brand_list(lst):
    clean_brands = []
    for element in lst:
        new_element = element.lower()
        new_element = new_element.replace(" ", "-")
        clean_brands.append(new_element)

    clean_brands.remove("not-specified")

    return clean_brands


def get_brand_name(string):

    for element in BRAND_MAPPER:
        if string == element[0]:
          brand_string = element[1]

    return brand_string