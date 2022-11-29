import requests
import json
import re

__all__ = ['googleSearchLib']
class googleSearchLib:

    def __remove_prefix(self,text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text  # or whatever


    def __init__(self):
        pass
    def searchImage(self,byteArray):
        
        
        base="https://lens.google.com"
        s = requests.Session()  

        #richiedo di caricare un file ( di una data dimensione )
        headers={
            'X-Goog-Upload-Command':'start',
            'Content-Type':'application/x-www-form-urlencoded',
            'X-Client-Side-Image-Upload': 'true',
            'X-Goog-Upload-Protocol': 'resumable',
            'X-Goog-Upload-Header-Content-Length': str(len(byteArray))

            }
        response = s.post(base+"/_/upload/",headers=headers)
        if(response.status_code!=200):
            raise Exception("upload url not correctly requested")

        uploadUrl= response.headers["X-Goog-Upload-Url"]



        #carico il file
        headers={
            'X-Goog-Upload-Offset': '0',
            'X-Goog-Upload-Command':'upload, finalize',
            'X-Client-Side-Image-Upload': 'true',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
            }
        response = s.post(uploadUrl, data=byteArray,headers=headers)
        y = json.loads(self.__remove_prefix(response.text,")]}'"))



        #recupero l'url per la ricerca dell'immagine
        imageSearchUrl=base+y["url"]
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36'
        }
        response = s.get(imageSearchUrl, headers=headers,params={"ucbcb":1})
        f = open('GFG.html', 'w',encoding='utf-8')
        f.write(response.text)
        f.close()



        #approvo la privacypolicy



        #TODO: per fare una ricerca occorre accettare le policy
        #in teoria il coockie "SOCS" è un id all'utente che lo identifica e da quello google capisce se hai accettato le policy
        #per il momento setto a mano ( dovrebbe durare 13 mesi...)
        #s.cookies.set("SOCS","CAISHAgCEhJnd3NfMjAyMjA5MDgtMF9SQzEaAml0IAEaBgiAyvSYBg")

        #print(imageSearchUrl)

        
        m = re.search('(https:\/\/www.google.com\/search\?tbs[^"]*)', response.text)
        stringa="[\""+m.group(0)+"\"]"
        y = json.loads(stringa)
        print( y)





        #headers={'Content-Type':'application/x-www-form-urlencoded'}
        #data = {"anchor":"","logintoken":loginToken,"username":user,"password":password}
        #response = self.s.post(url, data = data,headers=headers)


        #faccio una richiesta ad upload 
        #prendo l'upload id ( url ) 
        
        #faccio l'upload su quell'url
        
        #visualizzo il link dell'upload
        pass

