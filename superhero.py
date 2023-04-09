import requests
# Код реализации задания №1
def Who_is_most_intelligence_hero(url,names):
    resp = requests.get(url+'/all.json').json()
    sp_of_heroes = {}
    for i in resp:
        if i['name'] in names:
            sp_of_heroes[i['powerstats']['intelligence']] = i['name']
    max_intelligence = sorted(list(sp_of_heroes),reverse= True)[0]
    return (f'Самый умный супергерой это - {sp_of_heroes[max_intelligence]}')

print(Who_is_most_intelligence_hero("https://akabab.github.io/superhero-api/api",['Thanos','Hulk','Captain America']))

