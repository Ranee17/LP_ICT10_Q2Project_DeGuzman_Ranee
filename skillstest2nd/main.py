from pyscript import document

non_metals = {
    "H": ("H", "Hydrogen", 1, 1.008),
    "He": ("He", "Helium", 2, 4.0026),
    "C": ("C", "Carbon", 6, 12.011),
    "N": ("N", "Nitrogen", 7, 14.007),
    "O": ("O", "Oxygen", 8, 15.999),
    "F": ("F", "Fluorine", 9, 18.998),
    "Ne": ("Ne", "Neon", 10, 20.180)
}
    
def get_element_info(event):

    document.getElementById('result').innerHTML = ""

    element1 = document.getElementById('element-input').value.strip().title()

    
    result = non_metals.get(
        element1,
        ("-", "Element not found", "-", "-")
    )

    document.getElementById('result').innerHTML = f"""
    <b>Symbol:</b> {result[0]}<br>
    <b>Element:</b> {result[1]}<br>
    <b>Atomic Number:</b> {result[2]}<br>
    <b>Atomic Mass:</b> {result[3]}
    """