


"""
Website : streamtape.com | streamtape.xyz | streamtape.to

Regex: https?://(streamtape\.(com|to|xyz)/)\S+

Example: https://streamtape.com/v/O1j7DBkmleiGwm/

Note: Bypassed url only open/download with the ip of machine you are working on
( for indian region  change the streamtape.com to streamtape.to)

"""
import requests
import re
import time

def streamtape_bypass(url: str) -> tuple:
    while True:
        # Hacer la solicitud GET a la URL proporcionada
        response = requests.get(url)
        
        # Extraer el valor de content de <meta name="og:title" content="...">
        meta_content_match = re.search(r'<meta name="og:title" content="([^"]+)"', response.text)
        if meta_content_match:
            meta_content = meta_content_match.group(1)
        else:
            print("Meta tag 'og:title' no encontrada.")
            return None
        
        # Extraer el enlace de video usando regex
        if (videolink := re.findall(r"document.*((?=id\=)[^\"']+)", response.text)):
            nexturl = "https://streamtape.com/get_video?" + videolink[-1]
            
            # Verificar si el token cumple con el requisito de 12 caracteres
            match = re.search(r"token=([A-Za-z0-9]{12})", nexturl)
            if match:
                # Si el token es correcto, devolver nexturl y meta_content
                return nexturl, meta_content
            else:
                # Si no cumple, esperar 5 segundos antes de reintentar
                # print("Token incorrecto, reintentando en 5 segundos...")
                time.sleep(5)
        else:
            print("No se encontró el videolink en la respuesta.")
            return None
