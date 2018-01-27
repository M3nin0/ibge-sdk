class IBGE():
    '''
        Classe que trata os dados do IBGE
    '''


    def __init__(self, dataframe):
        '''
            Inicializador
                - Salva o dataframe recebido como atributo
        '''
        
        self.dataframe = dataframe


    def gerar_links_estatistica(self):
        ''' 
            Gera links das páginas com os dados
        
            :return: links
            :rtype list
        '''

        _url = 'https://www.ibge.gov.br/estatisticas-novoportal/economicas/'
        urls = []

        for i in range(0, len(self.dataframe)):
            _id = self.dataframe.loc[i]['id']
            _path = self.dataframe.loc[i]['path']
            # Busca o np pois ele será substituido pelo _id
            _index = _path.find('np')
            
            temp = _path[:_index] + str(_id) + _path[_index + 2:] + '.html'
            
            urls.append(_url + temp[25:])

        return urls
