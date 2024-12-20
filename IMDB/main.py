import concurrent.futures
from bs4 import BeautifulSoup
import time
import requests
import random
import csv

headers = {"User-Agent": "Mozilla/5.0"}
MAX_THREADS = 10


def extract_movies_details(movie_link):
    # formato: /title/tt10548174/?ref_=chtmvm_i_{n}
    time.sleep(random.uniform(0, 0.2))
    response = requests.get(movie_link, headers=headers)
    movie_soup = BeautifulSoup(response.content, "html.parser")

    if movie_soup is not None:
        title = None
        date = None

        # Section que contem as informações do filme .ipc-page-section
        page_section = movie_soup.find("section", attrs={"class": "ipc-page-section"})

        if page_section is not None:
            # verificando as divs da section
            divs = page_section.find_all("div", recursive=False)

            if len(divs) > 1:
                # segunda div contem o titulo do filme
                # o titulo esta num span dentro de um h1
                target_div = divs[1]

                title_tag = target_div.find("h1")
                if title_tag:
                    title = title_tag.find("span").get_text()

                # verificando a data de lançamento
                date_tag = target_div.find(
                    "a", href=lambda href: href and "releaseinfo" in href
                )
                if date_tag:
                    date = date_tag.get_text().strip()

                # nota do filme
                rating_tag = movie_soup.find(
                    "div",
                    attrs={"data-testid": "hero-rating-bar__aggregate-rating__score"},
                )
                rating = rating_tag.get_text() if rating_tag else None

                # sinopse do filme
                plot_tag = movie_soup.find(
                    "span", attrs={"data-testid": "plot-xs_to_m"}
                )
                plot_text = plot_tag.get_text().strip() if plot_tag else None

                with open("movies.csv", mode="a", newline="", encoding="utf-8") as file:
                    movie_writer = csv.writer(
                        file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
                    )
                    if all([title, date, rating, plot_text]):
                        print(title, date, rating, plot_text)
                        movie_writer.writerow([title, date, rating, plot_text])


def extract_movies(soup):
    # Pesquisa pela div com o atributo chart-layout-main-column no data-testid
    # dentro dessa div, existe uma ul contendo a lista dos filmes em li
    movies_table = soup.find(
        "div", attrs={"data-testid": "chart-layout-main-column"}
    ).find("ul")
    movies_table_rows = movies_table.find_all("li")
    # seleciona apenas o conteudo hfref da tag a da lista anterior
    # formato: /title/tt10548174/?ref_=chtmvm_i_{n}
    movies_links = [
        "https://imdb.com" + movie.find("a")["href"] for movie in movies_table_rows
    ]

    threads = min(MAX_THREADS, len(movies_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as exec:
        exec.map(extract_movies_details, movies_links)


def main():
    start_time = time.time()

    # 100 filmes mais populares
    popular_movies_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
    response = requests.get(popular_movies_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    extract_movies(soup)

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time}")


if __name__ == "__main__":
    main()
