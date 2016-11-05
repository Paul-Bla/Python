DaltonFilms = {'TLD': {'Year': 1987, 'IMDB': 6.7}, 'LTK': {'Year': 1989, 'IMDB': 6.6},
               'Villain': {'The Living Daylights': ['Jeroen Krabbe', 'Joe Don Baker'],
                           'Licence to Kill': 'Robert Davi'}}

# print(DaltonFilms)

# Let's try calling specific data.
#print(DaltonFilms['TLD']['Year'])
# NOW it works.
#print(DaltonFilms['Villain'])
# This works. Be careful to put text outputs in quotes. Make sure that all output is together. Otherwise --> PROBLEMS
#print(DaltonFilms['Villain']['The Living Daylights'][1])
#This calls a specific entry within the Villain nested-dictionary.

# dict of Dalton movies
# dict of movies and actors in them
BondFilms={'Connery':['Dr. No','From Russia With Love','Goldfinger', 'Thunderball', 'You Only Live Twice',
                      'Diamonds Are Forever'],
           'Lazenby':'OHMSS',
           'Moore':['Live And Let Die','The Man With The Golden Gun','The Spy Who Loved Me','Moonraker',
                    'For Your Eyes Only','Octopussy','A View To A Kill'],
           'Dalton':['The Living Daylights','Licence To Kill'],
           'Brosnan':['GoldenEye','Tomorrow Never Dies','The World Is Not Enough','Die Another Day'],
           'Craig':['Casino Royale','Quantum Of Solace','Skyfall','Spectre'],
           'Decade':{'1960s':{'Dr. No':1962, 'From Russia with Love':1963, 'Goldfinger':1964, 'Thunderball':1965,
                              'You Only Live Twice':1967,"On Her Majesty's Secret Service":1969},
                     '1970s':{'Diamonds Are Forever':1971,'Live and Let Die':1973,'The Man with the Golden Gun':1974,
                              'The Spy Who Loved Me':1977,'Moonraker':1979},
                     '1980s':{'For Your Eyes Only':1981,'Octopussy':1983,'A View to a Kill':1985,
                              'The Living Daylights':1987,'Licence to Kill':1989},
                     '1990s':{'GoldenEye':1995,'Tomorrow Never Dies':1997,'The World Is Not Enough':1999},
                     '2000s':{'Die Another Day':2002,'Casino Royale':2006,'Quantum of Solace':2008},
                     '2010s':{'Skyfall':2012,'Spectre':2015}},
           'IMDB':{'Dr. No':7.3,'From Russia with Love':7.5,'Goldfinger':7.8,'Thunderball':7.0,'You Only Live Twice':6.9,
                   "On Her Majesty's Secret Service":6.8,'Diamonds Are Forever':6.7,'Live and Let Die':6.8,
                   'The Man with the Golden Gun':6.8,'The Spy Who Loved Me':7.1,'Moonraker':6.3,'For Your Eyes Only':6.8,
                   'Octopussy':6.6,'A View to a Kill':6.3,'The Living Daylights':6.7,'Licence to Kill':6.6,'GoldenEye':7.2,
                   'Tomorrow Never Dies':6.5,'The World Is Not Enough':6.4,'Die Another Day':6.1,'Casino Royale':8.0,
                   'Quantum of Solace':6.7,'Skyfall':7.8,'Spectre':6.8},
           'AverageIMDB':{'ConneryAverage':7.2,'LazenbyAverage':6.8,'MooreAverage':6.67,'DaltonAverage':6.65,
                      'BrosnanAverage':6.55,'CraigAverage':7.3}

           }
print(BondFilms['Decade']['1970s']['Live and Let Die'])
print(BondFilms['Lazenby'])
print(BondFilms['AverageIMDB']['ConneryAverage'])
