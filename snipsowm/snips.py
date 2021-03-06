# -*- coding: utf-8 -*-
from enum import Enum


class SnipsWeatherConditions(Enum):
    HUMID = 0
    BLIZZARD = 1
    SNOWFALL = 2
    WINDY = 3
    CLOUD = 4
    RAINY = 5
    STORMY = 6
    SUN = 7
    SNOW = 8
    FOG = 9
    DEPRESSION = 10
    STORM = 11
    RAINFALL = 12
    SNOWY = 13
    SUNNY = 14
    RAIN = 15
    HAIL = 16
    FOGGY = 17
    OVERCAST = 18
    CLOUDY = 19
    HUMIDITY = 20
    SNOWSTORM = 21
    WIND = 22
    TRENCH_COAT = 23  # TODO REMOVE WHEN INTENT 'ITEM' WILL BE INDEPENDENTLY MANAGE
    PARKA = 24
    CARDIGAN = 25
    SUMMER_CLOTHING = 26
    GAMP = 27
    BROLLY = 28
    SUNSHADE = 29
    PARASOL = 30
    UMBRELLA = 31
    OPEN_TOED_SHOES = 32
    SHORTS = 33
    SKIRT = 34
    WARM_JUMPER = 35
    WARM_SOCKS = 36
    WARM_SWEATER = 37
    SCARF = 38
    STRAW_HAT = 39
    HAT = 40
    SUNBLOCK = 41
    SUNSCREEN = 42
    SUN_CREAM = 43
    WOOLEN_SWEATER = 44
    WOOLEN_JUMPER = 45
    WOOLEN_SOCKS = 46
    WOOLEN_TIGHTS = 47
    SLEEVELESS_SUNDRESS = 48
    SUNDRESS = 49
    CHUNKY_SWEATER = 50
    SUNGLASSES = 51
    RAINCOAT = 52


mappings = {
    SnipsWeatherConditions.HUMID: {
        'fr_FR': [u'humide'],
        'en_US': [u'humid'],
        'es_ES': [u'húmedo']
    },
    SnipsWeatherConditions.BLIZZARD: {
        'fr_FR': [u'blizzard'],
        'en_US': [u'blizzard'],
        'es_ES': [u'ventisca']
    },
    SnipsWeatherConditions.SNOWFALL: {
        'fr_FR': [u'chutes de neige'],
        'en_US': [u'snowfall'],
        'es_ES': [u'nieve']
    },
    SnipsWeatherConditions.WINDY: {
        'fr_FR': [u'venteux'],
        'en_US': [u'windy'],
        'es_ES': [u'viento']
    },
    SnipsWeatherConditions.CLOUD: {
        'fr_FR': [u'nuage', u'nuages'],
        'en_US': [u'cloud', u'clouds'],
        'es_ES': [u'nuboso']
    },
    SnipsWeatherConditions.RAINY: {
        'fr_FR': [u'pluvieux'],
        'en_US': [u'rainy'],
        'es_ES': [u'lluvioso']
    },
    SnipsWeatherConditions.STORMY: {
        'fr_FR': [u'orageux'],
        'en_US': [u'stormy'],
        'es_ES': [u'tormentoso']
    },
    SnipsWeatherConditions.SUN: {
        'fr_FR': [u'soleil'],
        'en_US': [u'sun'],
        'es_ES': [u'soleado']
    },
    SnipsWeatherConditions.SNOW: {
        'fr_FR': [u'neige', u'neiger', u'neigera'],
        'en_US': [u'snow'],
        'es_ES': [u'nieve']
    },
    SnipsWeatherConditions.FOG: {
        'fr_FR': [u'brouillard'],
        'en_US': [u'fog'],
        'es_ES': [u'niebla']
    }, SnipsWeatherConditions.DEPRESSION: {
        'fr_FR': [u'dépression'],
        'en_US': [u'depression'],
        'es_ES': [u'depresión']
    },
    SnipsWeatherConditions.STORM: {
        'fr_FR': [u'tempête'],
        'en_US': [u'storm'],
        'es_ES': [u'tormenta']
    },
    SnipsWeatherConditions.RAINFALL: {
        'fr_FR': [u'précipitations'],
        'en_US': [u'rainfall'],
        'es_ES': [u'precipitaciones']
    },
    SnipsWeatherConditions.SNOWY: {
        'fr_FR': [u'neigeux'],
        'en_US': [u'snowy'],
        'es_ES': [u'nevada']
    },
    SnipsWeatherConditions.SUNNY: {
        'fr_FR': [u'ensoleillé'],
        'en_US': [u'sunny'],
        'es_ES': [u'soleado']
    },
    SnipsWeatherConditions.RAIN: {
        'fr_FR': [u'pluie'],
        'en_US': [u'rain'],
        'es_ES': [u'lluvia']
    },
    SnipsWeatherConditions.HAIL: {
        'fr_FR': [u'grêle'],
        'en_US': [u'hail'],
        'es_ES': [u'granizo']
    },
    SnipsWeatherConditions.FOGGY: {
        'fr_FR': [u'brumeux'],
        'en_US': [u'foggy'],
        'es_ES': [u'nebuloso']
    },
    SnipsWeatherConditions.OVERCAST: {
        'fr_FR': [u'couvert'],
        'en_US': [u'overcast'],
        'es_ES': [u'cubierto']
    },
    SnipsWeatherConditions.CLOUDY: {
        'fr_FR': [u'nuageux'],
        'en_US': [u'cloudy'],
        'es_ES': [u'nublado']
    },
    SnipsWeatherConditions.HUMIDITY: {
        'fr_FR': [u'humidité'],
        'en_US': [u'humidity'],
        'es_ES': [u'humedad']
    }, SnipsWeatherConditions.SNOWSTORM: {
        'fr_FR': [u'tempête de neige'],
        'en_US': [u'snowstorm'],
        'es_ES': [u'tormenta de nieve']
    },
    SnipsWeatherConditions.WIND: {
        'fr_FR': [u'vent'],
        'en_US': [u'wind'],
        'es_ES': [u'viento']
    },
    SnipsWeatherConditions.TRENCH_COAT: {
        'fr_FR': [u'trench'],
        'en_US': [u'trench coat'],
        'es_ES': [u'gabardina']
    },
    SnipsWeatherConditions.PARKA: {
        'fr_FR': [u'parka'],
        'en_US': [u'parka'],
        'es_ES': [u'anorak']
    },
    SnipsWeatherConditions.CARDIGAN: {
        'fr_FR': [u'cardigan'],
        'en_US': [u'cardigan'],
        'es_ES': [u'chaqueta']
    },
    SnipsWeatherConditions.SUMMER_CLOTHING: {
        'fr_FR': [u'légé'],
        'en_US': [u'summer clothing'],
        'es_ES': [u'ropa de verano']
    },
    SnipsWeatherConditions.GAMP: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'gamp'],
        'es_ES': [u'paraguas']
    },
    SnipsWeatherConditions.BROLLY: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'brolly'],
        'es_ES': [u'paraguas']
    },
    SnipsWeatherConditions.SUNSHADE: {
        'fr_FR': [u'parasol'],
        'en_US': [u'sunshade'],
        'es_ES': [u'sombrilla']
    },
    SnipsWeatherConditions.PARASOL: {
        'fr_FR': [u'parasol'],
        'en_US': [u'parasol'],
        'es_ES': [u'sombrilla']
    },
    SnipsWeatherConditions.UMBRELLA: {
        'fr_FR': [u'parapluie'],
        'en_US': [u'umbrella'],
        'es_ES': [u'paraguas']
    }, SnipsWeatherConditions.OPEN_TOED_SHOES: {
        'fr_FR': [u'sandales'],
        'en_US': [u'open toed shoes'],
        'es_ES': [u'sandalias']
    },
    SnipsWeatherConditions.SHORTS: {
        'fr_FR': [u'short'],
        'en_US': [u'shorts'],
        'es_ES': [u'pantalones cortos']
    },
    SnipsWeatherConditions.SKIRT: {
        'fr_FR': [u'jupe'],
        'en_US': [u'skirt'],
        'es_ES': [u'falda']
    },
    SnipsWeatherConditions.WARM_JUMPER: {
        'fr_FR': [u'jupe courte'],
        'en_US': [u'warm jumper'],
        'es_ES': [u'jersey cálido']
    },
    SnipsWeatherConditions.WARM_SOCKS: {
        'fr_FR': [u'chausettes chaudes'],
        'en_US': [u'warm socks'],
        'es_ES': [u'calcetines cálidos']
    },
    SnipsWeatherConditions.WARM_SWEATER: {
        'fr_FR': [u'pull'],
        'en_US': [u'warm sweater'],
        'es_ES': [u'jersey cálido']
    },
    SnipsWeatherConditions.SCARF: {
        'fr_FR': [u'écharpe'],
        'en_US': [u'scarf'],
        'es_ES': [u'bufanda']
    },
    SnipsWeatherConditions.STRAW_HAT: {
        'fr_FR': [u'chapeau de paille'],
        'en_US': [u'straw hat'],
        'es_ES': [u'sombero de paja']
    },
    SnipsWeatherConditions.HAT: {
        'fr_FR': [u'chapeau'],
        'en_US': [u'hat'],
        'es_ES': [u'sombrero']
    },
    SnipsWeatherConditions.SUNBLOCK: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sunblock'],
        'es_ES': [u'crema solar']
    },
    SnipsWeatherConditions.SUNSCREEN: {
        'fr_FR': [u'écran solaire'],
        'en_US': [u'sunscreen'],
        'es_ES': [u'protector solar']
    }, SnipsWeatherConditions.SUN_CREAM: {
        'fr_FR': [u'crème solaire'],
        'en_US': [u'sun cream'],
        'es_ES': [u'crema solar']
    },
    SnipsWeatherConditions.WOOLEN_SWEATER: {
        'fr_FR': [u'pull en laine'],
        'en_US': [u'woolen sweater'],
        'es_ES': [u'jersey de lana']
    },
    SnipsWeatherConditions.WOOLEN_JUMPER: {
        'fr_FR': [u'pull en laine'],
        'en_US': [u'woolen jumper'],
        'es_ES': [u'jersey de lana']
    },
    SnipsWeatherConditions.WOOLEN_TIGHTS: {
        'fr_FR': [u'collants en laine'],
        'en_US': [u'woolen tights'],
        'es_ES': [u'medias de lana']
    },
    SnipsWeatherConditions.SLEEVELESS_SUNDRESS: {
        'fr_FR': [u'robe d\'été'],
        'en_US': [u'sleeveless sundress'],
        'es_ES': [u'vestido sin mangas']
    },
    SnipsWeatherConditions.SUNDRESS: {
        'fr_FR': [u'robe d\'été'],
        'en_US': [u'sundress'],
        'es_ES': [u'vestido de verano']
    },
    SnipsWeatherConditions.CHUNKY_SWEATER: {
        'fr_FR': [u'gros pull'],
        'en_US': [u'chunky sweater'],
        'es_ES': [u'jersey grueso']
    },
    SnipsWeatherConditions.SUNGLASSES: {
        'fr_FR': [u'lunettes de soleil'],
        'en_US': [u'sunglasses'],
        'es_ES': [u'gafas de sol']
    },
    SnipsWeatherConditions.RAINCOAT: {
        'fr_FR': [u'manteau pour la pluie'],
        'en_US': [u'raincoat'],
        'es_ES': [u'impermeable']
    },
    SnipsWeatherConditions.WOOLEN_SOCKS: {
        'fr_FR': [u'chaussettes en laine'],
        'en_US': [u'woolen socks'],
        'es_ES': [u'calcetines de lana']
    }
}
