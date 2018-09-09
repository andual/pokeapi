import requests

url="https://pokeapi.co/api/v2/pokemon/"



def siguiente(url):

    #offset={"offset":folw}
    response=requests.get(url)#, params=offset)
    jsonresponse=response.json()
    pokemonrsults=jsonresponse['results']
    nexte=jsonresponse['next']

    n=0
    for i in pokemonrsults:
        n+=1
        pokemonnames=i['name']
        print(str(n)+" "+pokemonnames)

    yon=input("¿Deseas ver los siguientes 20?(Y/N)")

    if yon=="Y":
        
        #folw=folw+20
        siguiente(nexte)
    else:
        print("el programa a finalizado")

siguiente(url)



