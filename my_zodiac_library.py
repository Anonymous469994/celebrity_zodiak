import re
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def fit_mounth(x):
    if x == 'января':
        return 1
    elif x == 'февраля':
        return 2
    elif x == 'марта':
        return 3
    elif x == 'апреля':
        return 4
    elif x == 'мая':
        return 5
    elif x == 'июня':
        return 6
    elif x == 'июля':
        return 7
    elif x == 'августа':
        return 8
    elif x == 'сентября':
        return 9
    elif x == 'октября':
        return 10
    elif x == 'ноября':
        return 11
    elif x == 'декабря':
        return 12
    else:
        return 
    
def find_zodiac(data):
    x = data % 10000
    if (321 <= x) and (x <= 420):
        return 'Aries'
    elif (421 <= x) and (x <= 520):
        return 'Taurus'
    elif (521 <= x) and (x <= 621):
        return 'Gemini'
    elif (622 <= x) and (x <= 722):
        return 'Cancer'
    elif (723 <= x) and (x <= 823):
        return 'Leo'
    elif (824 <= x) and (x <= 921):
        return 'Virgo'
    elif (922 <= x) and (x <= 1022):
        return 'Libra'
    elif (1023 <= x) and (x <= 1121):
        return 'Scorpio'
    elif (1122 <= x) and (x <= 1221):
        return 'Sagittarius'
    elif (1222 <= x) or (x <= 120):
        return 'Capricorn'
    elif (121 <= x) and (x <= 219):
        return 'Aquarius'
    elif (220 <= x) and (x <= 320):
        return 'Pisces'
    else:
        return 
    
def find_element(x):
    if x in {'Leo', 'Sagittarius', 'Aries'}:
        return 'fire'
    if x in {'Aquarius', 'Libra', 'Gemini'}:
        return 'air'
    if x in {'Scorpio', 'Cancer', 'Pisces'}:
        return 'water'
    if x in {'Taurus', 'Virgo', 'Capricorn'}:
        return 'earth'
    else:
        return 
    
zod_code = dict({
    'Aries': '1',
    'Taurus': '2',
    'Gemini': '3',
    'Cancer': '4',
    'Leo': '5',
    'Virgo': '6',
    'Libra': '7',
    'Scorpio': '8',
    'Sagittarius': '9',
    'Capricorn': '10',
    'Aquarius': '11',
    'Pisces': '12',
})

zod_color = dict({
    'Aries': 'brown',
    'Taurus': 'goldenrod',
    'Gemini': 'gainsboro',
    'Cancer': 'darkblue',
    'Leo': 'darkred',
    'Virgo': 'goldenrod',
    'Libra': 'lightgrey',
    'Scorpio': 'midnightblue',
    'Sagittarius': 'firebrick',
    'Capricorn': 'peru',
    'Aquarius': 'silver',
    'Pisces': 'navy',
})

elem_color = dict({
    'fire': 'indianred',
    'air': 'lightgrey',
    'water': 'royalblue',
    'earth': 'olivedrab',
})

def define_prof(x):
    prof_code = dict({
        0: 'wrtr',
        1: 'prod',
        2: 'drct',
        3: 'edtr',
        4: 'actr',
    })
    prof = np.argmax([x[8], x[9], x[10], x[11], x[12]])
    if (prof == 4 and (x[8] + x[10] + x[11] > x[12])):
        prof = np.argmax([x[8], x[9], x[10]])
    if (prof == 3):
        prof = np.argmax([x[8], x[9], x[10]])
    res_prof = prof_code[prof]    
    return res_prof

def define_country(df):
    def fit_country(x):
        if pd.isna(x):
            return
        if x in {'малайзия'}:
            return 'malaysia'
        if re.search(r'корея', x):
            return 'korea'
        if re.search(r'аргентина', x):
            return 'argentina'
        if x in {'новая зеландия'}:
            return 'newzealand'
        if x in {'норвегия'}:
            return 'norway'
        if re.search(r'китай', x) is not None or x in {'макао'}:
            return 'china'
        if x in {'дания'}:
            return 'denmark'
        if x in {'швеция', 'uddevalla'}:
            return 'sweden'
        if re.search(r'армения', x) is not None:
            return 'armenia'
        if x in {'бразилия'}:
            return 'brazil'
        if x in {'южная африка', 'юар', 'свазиленд'}:
            return 'rsa'
        if x in {'турция', 'стамбул'}:
            return 'turkey'
        if x in {'ливан'}:
            return 'lebanon'
        if x in {'куба'}:
            return 'kuba'
        if x in {'израиль'}:
            return 'israel'
        if x in {'израиль'}:
            return 'israel'
        if x in {'уругвай'}:
            return 'uruguay'
        if re.search(r'польша', x) is not None:
            return 'poland'
        if re.search(r'сербия', x) is not None:
            return 'serbia'
        if x in {'румыния'}:
            return 'romania'
        if x in {'болгария'}:
            return 'bulgaria'
        if x in {'греция'}:
            return 'greece'
        if re.search(r'молдавия', x) is not None:
            return 'moldova'
        if re.search(r'узбекистан', x) is not None:
            return 'uzbekistan'
        if re.search(r'азербайджан', x) is not None:
            return 'azerbaijan'
        if x in {'марокко'}:
            return 'morocco'
        if re.search(r'чехия', x) is not None or x in {'прага'}:
            return 'czechia'
        if re.search(r'таджикистан', x) is not None:
            return 'tajikistan'
        if re.search(r'туркмения', x) is not None:
            return 'turkmenistan'
        if re.search(r'литва', x) is not None:
            return 'lithuania'
        if re.search(r'эстония', x) is not None:
            return 'estonia'
        if re.search(r'босния и герцеговина', x) is not None:
            return 'BiH'
        if x in {'венгрия'}:
            return 'hungary'
        if x in {'нигерия'}:
            return 'nigeria'
        if x in {'алжир'}:
            return 'algeria'
        if x in {'оман'}:
            return 'oman'
        if x in {'иран'}:
            return 'iran'
        if x in {'индонезия'}:
            return 'indonesia'
        if x in {'чили'}:
            return 'chile'
        if x in {'панама'}:
            return 'panama'
        if x in {'бенин'}:
            return 'benin'
        if x in {'гонконг'}:
            return 'hongkong'
        if x in {'таиланд'}:
            return 'thailand'
        if x in {'тайвань'}:
            return 'taiwan'
        if x in {'венесуэла'}:
            return 'venezuela'
        if x in {'швейцария'}:
            return 'switzerland'
        if x in {'колумбия'}:
            return 'colombia'
        if x in {'финляндия'}:
            return 'finland'
        if x in {'руанда'}:
            return 'rwanda'
        if x in {'эфиопия'}:
            return 'ethiopia'
        if x in {'перу'}:
            return 'peru'
        if x in {'египет'}:
            return 'egypt'
        if x in {'ливия'}:
            return 'libya'
        if x in {'тунис'}:
            return 'tunisia'
        if x in {'пакистан'}:
            return 'pakistan'
        if x in {'гватемала'}:
            return 'guatemala'
        if x in {'мальта'}:
            return 'malta'
        if x in {'вьетнам'}:
            return 'vietnam'
        if x in {'сингапур'}:
            return 'singapore'
        if x in {'исландия'}:
            return 'island'
        if x in {'тринидад и тобаго'}:
            return 'TaT'
        if x in {'syria', 'сирия'}:
            return 'syria'
        if x in {'эквадор'}:
            return 'ecuador'
        if x in {'сша', 'калифорния', 'массачусетс', 'нью-йорк', 'usa', 'пенсильвания', 'мэриленд'}:
            return 'usa'
        if x in {'пуэрто-рико'}:
            return 'puerto-rico'
        if x in {'англия', 'великобритания', 'шотландия', 'уэльс', 'нит-порт-толбот', 'северная ирландия', \
                 'графство уорвикшир', 'ленстер', 'дарем', 'дамфрис и галлоуэй', \
                 'йоркшир и хамбер', 'стейнес', 'лондон', 'хайес', 'staffordshire', 'глазго', 'norfolk'}:
            return 'gb'
        if x in {'ирландия'}:
            return 'ireland'
        if x in {'канада', 'канада.'}:
            return 'canada'
        if re.search(r'япония', x) is not None:
            return 'japon'
        if re.search(r'(россия|рсфср|липецкая|омская|ленинградская|московская|челябинская)', x) is not None or\
           re.search(r'(петродворец|белгородская|самарская|удмуртия|ярославская|чувашская)', x) is not None or\
           re.search(r'(крым|севастополь|ивановская|дагестан|ленинград|читинская|серышевский)', x) is not None or\
           re.search(r'(горьковская|погарский)', x) is not None:
            return 'russia'
        if re.search(r'беларусь', x) is not None or re.search(r'белоруссия', x) is not None:
            return 'belarus'
        if re.search(r'украина', x) is not None or x in {'киевская область'}:
            return 'ukraine'
        if re.search(r'казахстан', x) is not None:
            return 'kazakhstan'
        if re.search(r'латвия', x) is not None:
            return 'latvia'
        if x in {'австралия', 'australia', 'новый южный уэльс'}:
            return 'australia'
        if re.search(r'германия', x) is not None or x in {'верхний рейн', 'ремшейд'}:
            return 'germany'  
        if x in {'тоскана', 'тоскана', 'лацио', 'апулия', 'italy', 'неаполь'} or \
                re.search(r'италия', x) is not None:
            return 'italy'
        if x in {'испания', 'кастилия — ла-манча', 'андалусия', 'spain'}:
            return 'spain'
        if re.search(r'австрия', x) is not None:
            return 'austria'
        if x in {'бельгия'}:
            return 'belgium'
        if x in {'мексика'}:
            return 'mexico'
        if x in {'франция', 'нормандские острова', 'сен-маритим'}:
            return 'france'
        if re.search(r'(грузия|осетия)', x) is not None:
            return 'georgia'
        if x in {'нидерланды'}:
            return 'nederland'
        if x in {'индия'}:
            return 'india'
        if x in {'барбадос'}:
            return 'barbados'
        if x in {'гренландия'}:
            return 'greenland'
        if x in {'фиджи'}:
            return 'fiji'
        if x in {'коста-рика'}:
            return 'costa-rica'
        if x in {'судан'}:
            return 'sudan'
        if x in {'комарно', 'словакия'}:
            return 'slovakia'
        if x in {'гана'}:
            return 'ghana'
        if x in {'непал'}:
            return 'nepal'
        if x in {'словения'}:
            return 'slovenia'
        if x in {'ирак'}:
            return 'iraq'
        if x in {'филиппины'}:
            return 'philippines'
        if re.search('саудовская аравия', x) is not None:
            return 'saudi_arabia'
        
    def combine_country(a, b, c, d):
        if d is not None:
            return d
        elif c is not None:
            return c
        elif b is not None:
            return b
        elif a:
            return 'russia'
        return ''
   
    temp_df = df[['city', 'cntr_1', 'cntr_2', 'name']]
    temp_df.loc[:, 'ussr'] = temp_df['city'].map(lambda x: True if x == 'ссср' else False)
    temp_df.loc[:, 'country_0'] = temp_df['city'].map(fit_country)
    temp_df.loc[:, 'country_1'] = temp_df['cntr_1'].map(fit_country)
    temp_df.loc[:, 'country_2'] = temp_df['cntr_2'].map(fit_country)
    vfunc = np.vectorize(combine_country)
    return vfunc(temp_df['ussr'], temp_df['country_0'], temp_df['country_1'], temp_df['country_2'])

def define_region(x):
    if pd.isna(x):
        return
    if x == '':
        return
    
    if x in {'russia'}:
        return 'RF'
    if x in {'armenia', 'georgia', 'kazakhstan', 'ukraine', 'belarus', 'lithuania', 'estonia', 'latvia'}:
        return 'CIS-RF'
    if x in {'usa'}:
        return 'USA'
    if x in {'gb', 'canada'}:
        return 'GB+CAN'
    
    if x in {'island', 'finland', 'sweden', 'denmark', 'norway', 'greenland'}:
        return 'NEurope'
    if x in {'switzerland', 'hungary', 'czechia', 'poland', 'austria', 'italy', 'germany'}:
        return 'CEurope'
    if x in {'malta', 'BiH', 'greece', 'serbia', 'spain'}:
        return 'SEurope'
    if x in {'moldova', 'bulgaria', 'romania', 'slovakia', 'slovenia'}:
        return 'EEurope'
    if x in {'nederland', 'france', 'belgium', 'ireland'}:
        return 'WEurope'
    
    if x in {'peru', 'venezuela', 'chile', 'uruguay', 'brazil', 'argentina'}:
        return 'SAmerica'
    if x in {'ecuador', 'TaT', 'guatemala', 'colombia', 'panama', \
             'kuba', 'mexico', 'puerto-rico', 'costa-rica', 'barbados'}:
        return 'CAmerica'
    
    if x in {'tunisia', 'libya', 'egypt', 'iran', 'oman', 'algeria', 'saudi_arabia', \
             'morocco', 'israel', 'lebanon', 'turkey', 'syria', 'sudan', 'iraq'}:
        return 'NearEast'
    if x in {'turkmenistan', 'tajikistan', 'azerbaijan', 'uzbekistan'}:
        return 'MiddleEast'
    
    if x in {'singapore','vietnam', 'pakistan', 'hongkong', 'indonesia', \
             'malaysia', 'fiji', 'thailand', 'philippines'}:
        return 'SEAsia'
    if x in {'taiwan', 'china', 'japon', 'korea'}:
        return 'EAsia'
    if x in {'pakistan', 'india', 'nepal'}:
        return 'SAsia'
    
    if x in {'newzealand', 'australia'}:
        return 'Oceania'
    if x in {'ethiopia', 'rwanda', 'benin', 'nigeria', 'rsa', 'ghana'}:
        return 'SSAfrica'
    return 'untitled'

def define_glob_region(x):
    if pd.isna(x):
        return
    if x == '':
        return
    if x in {'RF', 'CIS-RF'}:
        return 'CIS'
    if x in {'USA'}:
        return 'USA'
    if x in {'GB+CAN', 'Oceania'}:
        return 'CoN'
    if x in {'WEurope', 'NEurope', 'EEurope', 'SEurope', 'CEurope'}:
        return 'Europe'
    if x in {'EAsia', 'SAsia', 'SEAsia'}:
        return 'Asia'
    if x in {'EAsia', 'SAsia', 'SEAsia'}:
        return 'Asia'
    if x in {'NearEast', 'MiddleEast'}:
        return 'ArabianWorld'
    if x in {'CAmerica', 'SAmerica'}:
        return 'SouthAmerica'
    if x in {'SSAfrica'}:
        return 'SSA'
    return 'untitled'



def check_df(df):
    temp_df = df[df.country == ''][['city','cntr_1', 'cntr_2', 'name']]
    temp_df = temp_df[temp_df.city != '-']
    if not temp_df.empty:
        print('error: country')
        print(temp_df)
        return
    temp_df = df[df.region == 'untitled'][['name', 'country', 'region']]
    if not temp_df.empty:
        print('error: region')
        print(temp_df)
        return
    temp_df = df[df.glob_region == 'untitled'][['name', 'country', 'region', 'glob_region']]
    if not temp_df.empty:
        print('error: glob_region')
        print(temp_df)
        return
    print('OK')
    
def preprocessing_df(df):
    df.loc[:, 'new_mounth'] = df['mounth'].map(fit_mounth)
    df.loc[:, 'new_death_mounth'] = df['dth_mounth'].map(fit_mounth)
    df['new_death_mounth'] = df['new_death_mounth'].fillna(0).astype(int)
    df['dth_year'] = df['dth_year'].fillna(0).astype(int)
    df['dth_day'] = df['dth_day'].fillna(0).astype(int)
    df.dropna(subset=['new_mounth', 'day', 'year'], inplace=True)
    df['new_mounth'] = df['new_mounth'].astype(int)
    df['year'] = df['year'].astype(int)
    df['day'] = df['day'].astype(int)
    df['date'] = df['year']*10000 + df['new_mounth']*100 + df['day']
    df['death_date'] = df['dth_year']*10000 + df['new_death_mounth']*100 + df['dth_day']
#     df['death_date'] = df['death_date'].replace(0, '', regex=False).astype(int)
    df['zodiac'] = df['date'].map(find_zodiac)
    df['element'] = df['zodiac'].map(find_element)
    df['prof'] = np.apply_along_axis(define_prof, 1, df)
    df['country'] = define_country(df)
    df['region'] = df['country'].map(define_region)
    df['glob_region'] = df['region'].map(define_glob_region)
    df['total_films'] = df['total_films'].astype(int)
    df['favors'] = df['favors'].fillna(0).astype(int)
#     df['career_start'] = df['career_start'].fillna(0).astype(int)
    df['folders'] = df['folders'].str.replace('None', '0', regex=False).astype(float).astype(int)
    df.drop(columns=['new_mounth', 'mounth', 'day', \
                     'new_death_mounth', 'dth_mounth', 'dth_day', 'dth_year'], inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['male'], inplace=True)
    return df
    
def purification_df(df):
    mask = (df.awards == False) & (\
                (df.total_films <= 2) |
                (pd.isna(df.rating)) |
                (pd.isna(df.favors)) |
                ((df.prof == 'actr') & (df.actor <= 1))\
                )
    return df[mask == False]

def draw_pies(data_names, data_values, data_color=None, pies_names=None):
    dpi = 80
    fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
    mpl.rcParams.update({'font.size': 9})
    pies = len(data_names)
    pn = []
    if pies_names is not None:
        pn = pies_names
    else:
        for i in range(pies):
            pn.append('A tasty pie')
    cls = min(2, pies)
    lns = int(1 + (pies-1) // 2)
    i = 0
    for ln in range(lns):
        for cl in range(cls):
            if i == pies:
                return
            ax = fig.add_axes([cl*0.9, ln*(-1.1), 1, 1], aspect=1)
            ax.set_title(pn[i])
            if data_color is not None:
                plt.pie(
                    data_values[i], autopct='%.1f', radius = 1.1,
                    explode = [0.15] + [0 for _ in range(len(data_names[i]) - 1)],
                    colors = data_color[i],
                    )
            else:
                plt.pie(
                    data_values[i], autopct='%.1f', radius = 1.1,
                    explode = [0.15] + [0 for _ in range(len(data_names[i]) - 1)],
                    )            
            plt.legend(
                bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
                loc = 'lower left', labels = data_names[i])
            i += 1
