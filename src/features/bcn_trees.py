"""Barcelona City Council's Trees imports.

This script is aimed to define all functions required to import data regarding
trees from Barcelona's OpenData portal.
"""


import wget


def data_download(url, filename):
    """Downloads data and stores it into a file"""
    wget.download(url, 'data/raw/' + filename + '.csv')


def data_munging(df):
    """Cleans and prepares data from Barcelona City Council Opendata
    for importing trees' information into OSM, provided a dataframe.

    Parameters
    ----------
    df : DataFrame
        The Raw Dataframe we want to use import into OSM.


    Returns
    -------
    df
        A clean dataframe, ready for importing to OSM.

    """

    print('Loading...' + str(df))

    # Select columns.
    df = df[['LATITUD_WGS84',
             'LONGITUD_WGS84',
             'NOM_CIENTIFIC',
             'NOM_CASTELLA',
             'NOM_CATALA',
             'DATA_PLANTACIO',
             'CATEGORIA_ARBRAT',
             ]]
    # Rename
    df = df.rename(columns={'NOM_CIENTIFIC': 'species',
                            'NOM_CASTELLA': 'species:es',
                            'NOM_CATALA': 'species:ca',
                            'DATA_PLANTACIO': 'planted_date'})

    # @TODO: Populate leaf_cycle column according to species
    # https://wiki.openstreetmap.org/wiki/Key:leaf_cycle

    # @TODO: convert 'CATEGORIA' into height or diameter, according to city
    # council's guide: https://ajuntament.barcelona.cat/ecologiaurbana/sites/default/files/Plagestioarbratviaribcn_cat.pdf

    # @TODO: Tag tree pits for accessibility purposes.

    # @TODO: Consider importing city council's IDs for updating purposes.

    # Create a source column with "Opendata Ajuntament Barcelona"
    df['source'] = "Opendata Ajuntament de Barcelona"

    return(df)
