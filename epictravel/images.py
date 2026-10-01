# Image registry: original url -> lighter WordPress-generated sizes (checked against attachment metadata).
B = 'https://epictravelmorocco.com/wp-content/uploads/'
def _r(path, ext, card='600x810', wide='1536x1024', orig=None):
    base = B + path
    return dict(card=base + '-' + card + ext, mid=base + '-750x400' + ext,
                wide=(base + '-' + wide + ext) if wide else orig, orig=orig)
IMG = {}
def add(key, path, ext, card='600x810', wide='1536x1024', scaled=True, orig=None):
    IMG[key] = _r(path, ext, card, wide, orig or (B + path + ('-scaled' if scaled else '') + ext))

add('sahara-exp', '2025/11/pexels-zakariahanif-12214734', '.jpg')
add('north-south', '2025/11/GettyImages-122137131-592426555f9b58f4c07ffd43', '.jpg', wide=None, scaled=False)
add('midelt', '2025/11/5ebbd586ece4c_midelt-ville-pomme-atlas-climat-histoire-infos-tourisme-maroc-1-1', '.webp', card='600x667', wide=None, scaled=False)
add('coast-desert', '2025/11/pexels-mographe-30949484', '.jpg', wide='1536x1021')
add('dunes-camel', '2025/11/IMG_5828', '.jpg', wide='1536x865', scaled=False)
add('marrakech', '2025/11/pexels-mographe-15360688', '.jpg', wide='1536x1063')
add('historic', '2025/11/MXLU7731', '.jpg', scaled=False)
add('chefchaouen-trip', '2025/11/WhatsApp-Image-2023-03-02-at-22.42.11', '.jpeg', wide='1536x1152', scaled=False)
add('ifrane', '2025/11/ifrane-1', '.jpg', card='600x475', wide=None, scaled=False)
add('magic', '2025/11/pexels-micklatter-18375222', '.jpg')
add('odyssey', '2025/07/IMG_5641', '.jpg', wide='1536x761', scaled=False)
add('journey', '2025/11/pexels-adthiry-18661913', '.jpg')
add('kasbah', '2025/11/pexels-henrik-le-botos-1588507-3878114', '.jpg')
add('north', '2025/11/pexels-abdel-achkouk-2861018-22717119', '.jpg')
add('authentic', '2025/11/pexels-gabriel-garcia-1263144-2404046', '.jpg')
add('hero1', '2025/08/pexels-ed-duvico-530456-29107895', '.jpg')
add('hero2', '2025/11/pexels-mographe-3581916', '.jpg')
add('taryn', '2025/11/pexels-taryn-elliott-3889826', '.jpg')
add('reyyan', '2025/11/pexels-reyyan-505450018-33429795', '.jpg')
add('piotr', '2025/11/pexels-piotr-arnoldes-7862031-6441048', '.jpg')
add('team', '2025/11/WhatsApp-Image-2023-03-27-at-22.53.18-1', '.jpeg', scaled=False)

# own photos for the gallery (shown at card size; original as fallback)
GALLERY = ['2025/11/IMG_5183.jpg', '2025/11/IMG_5469.jpg', '2025/11/VXKA2253.jpg',
           '2025/11/WhatsApp-Image-2023-03-02-at-22.42.12.jpeg', '2025/11/WhatsApp-Image-2023-03-02-at-22.42.13-1.jpeg',
           '2025/11/WhatsApp-Image-2023-03-02-at-22.42.16.jpeg', '2025/11/WhatsApp-Image-2023-03-02-at-22.48.00-2.jpeg',
           '2025/11/WhatsApp-Image-2023-03-27-at-22.53.18-1.jpeg', '2025/11/IMG_5727.jpg', '2025/11/IMG_8318.jpg']
def gal(p):
    stem, ext = p.rsplit('.', 1)
    return B + stem + '-600x810.' + ext, B + p

FLEET = {
 'van': B + '2025/11/Gemini_Generated_Image_kunskunskunskuns-2-768x655.png',
 'suv': B + '2025/11/Gemini_Generated_Image_tqr8vttqr8vttqr8-768x597.png',
 'sprinter': B + '2025/11/Gemini_Generated_Image_pelh0jpelh0jpelh-1024x796.png',
 'bus': B + '2025/11/Gemini_Generated_Image_wnw2hgwnw2hgwnw2-300x233.png',
}
FLEET_ORIG = {
 'van': B + '2025/11/Gemini_Generated_Image_kunskunskunskuns-2.png',
 'suv': B + '2025/11/Gemini_Generated_Image_tqr8vttqr8vttqr8.png',
 'sprinter': B + '2025/11/Gemini_Generated_Image_pelh0jpelh0jpelh.png',
 'bus': B + '2025/11/Gemini_Generated_Image_wnw2hgwnw2hgwnw2.png',
}
LOGO = B + '2025/08/PDF-2-1.png'
