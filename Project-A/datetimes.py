from datetime import datetime

# Ambil nama hari dalam bahasa Inggris
def Day(location):
    """
    Location  : Asia/Jakarta  or anything else
    """
    from datetime import datetime
    import pytz

    # Zona waktu Indonesia (WIB)
    zona_wib = pytz.timezone(location)

    # Ambil waktu sekarang di Jakarta
    waktu_jakarta = datetime.now(zona_wib)

    # Format hari dalam bahasa Inggris
    hari_inggris = waktu_jakarta.strftime('%A')

    # Mapping ke bahasa Indonesia
    hari_mapping = {
        'Monday': 'Senin',
        'Tuesday': 'Selasa',
        'Wednesday': 'Rabu',
        'Thursday': 'Kamis',
        'Friday': 'Jumat',
        'Saturday': 'Sabtu',
        'Sunday': 'Minggu'
    }

    # Cetak hasil
    return hari_mapping[hari_inggris]

def Dating(t1t, equation, t2t, format_ = "%I:%M %p"):
    t1 = datetime.strptime(t1t, format_)
    t2 = datetime.strptime(t2t, format_)

    if equation == ">":
        return t1 > t2
    elif equation == "<":
        return t1 < t2
    elif equation == "==":
        return t1 == t2
    else:
        raise ValueError("Invalid equation")
