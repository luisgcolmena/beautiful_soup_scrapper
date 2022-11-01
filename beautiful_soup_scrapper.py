from bs4 import BeautifulSoup
import requests

URL = 'https://www.pagina12.com.ar/'

try:
    r = requests.get(URL)
    if r.status_code == 200:
        s = BeautifulSoup(r.text, 'html.parser')
        sections_links = [item.a.get('href') for item in (s.find('ul', attrs = {
        'class': 'hide-on-dropdown'
        }).find_all('li'))]

except Exception as e:
    print('Ha ocurrido un error: {e}')

def scrapper(links):

    #Recorrer cada seccion de la página
    for seccion in links:
        r = requests.get(seccion)
        s = BeautifulSoup(r.text, 'html.parser')

        print(f'Sección: {s.title.text}')
        print(f'URL: {seccion}')
        

        try:
            articles_list = s.find_all('div', attrs={
                    'class':'article-item__content'
                    })

            articles_list_titles = [article.a.string for article in articles_list]
            articles_list_links = [seccion + article.a.get('href') for article in articles_list]
        
        except AttributeError:

            print('HA OCURRIDO UN ERROR')

        finally:

            print(f'\tArticles: {articles_list_titles}')
            print(f'\tLinks: {articles_list_links}')
            print('\n')

def bs_scrapper(link_section):
    
    print(f'Sección: {soup.title.text}')
        
    try:
        articles_list = soup.find_all('div', attrs={
                'class':'article-item__content'
                })

        #Busca el link de cada articulo de esa sección.
        articles_list_links = [url + article.a.get('href') for article in articles_list]
    
    except Exception as e:
        print('Ha ocurrido un error: {e}')

    return articles_list_links


def article_scrapper(article_link):
    try:
        r_article = requests.get(article_link)

        #Validar si el request fue realizado correctamente:
        if r_article.status_code == 200:
            soup_article = BeautifulSoup(r_article.text, 'html.parser')

            article_title = soup_article.find('div', attrs={'class':'col 2-col'}).h1.string
            article_subtitle = soup_article.find('div', attrs={'class':'col 2-col'}).h4.string
            article_section = soup_article.find('div', attrs={'class':'col 1-col'}).a.string
            article_date = soup_article.find('div', attrs={'class':'date modification-date'}).time.get('datetime')
            article_tags = [tag.string for tag in (soup_article.find('div', attrs={'class':'article-tags'}).find_all('a', attrs={'class':'tag'}))]

    except Exception as e:
        print('Ha ocurrido un error')
    
    finally:

        #Almacenar toda la información extraída en un diccionario
        article_data = {
            'section': article_section,
            'title': article_title,
            'subtitle': article_subtitle,
            'date': article_date,
            'tags': article_tags,
        }

    return article_data