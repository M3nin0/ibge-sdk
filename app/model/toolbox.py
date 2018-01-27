import sqlite3
import requests
import pandas as pd

class ToolBox():
    '''
        Classe de utilidades
    '''
    
    @staticmethod
    def get_dataframe(tipo_produto):
        '''
            Método para gerar o dataframe com os dados da API do IBGE
            
            :param: tipo_produto
            :type: str
            :info: Tipo do produto a ser gerado
                - Exemplo:
                    - estatisticas;
                    - geociencias;
                    - produtos.
        '''

        _url = 'https://servicodados.ibge.gov.br/api/v1/produtos/'

        if tipo_produto == 'estatisticas':
            _url += tipo_produto
        elif tipo_produto == 'geociencias':
            _url += tipo_produto

        r = requests.get(_url)

        # Transforma o conteúdo recebido em Json
        _json = r.json()

        # Retorna o DataFrame
        return pd.DataFrame(_json)


    @staticmethod
    def save_sqlite(dataframe, pathDB, nameDB, nameSchema):
        '''
            Método para salvar o dataframe em arquivo SQLite
            
            :param: dataframe
            :type: Pandas.DataFrame
            
            :param: pathDB
            :type: str
            
            :param: nameDB
            :type: str
            
            :param: nameSchema
            :type: str
        '''

        try:
            conn = sqlite3.connect(pathDB + nameDB)
        except BaseException as e:
            raise e

        # Gera um arquivo sqlite com os dados
        dataframe.to_sql(nameSchema, conn)
