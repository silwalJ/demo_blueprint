from views import about, list_of_clothes, list_of_shoes, list_of_tshirts


about.add_url_rule('/listOfClothes', 'list_of_clothes', list_of_clothes)
about.add_url_rule('/listOfShoes', 'list_of_shoes', list_of_shoes)
about.add_url_rule('/listOfTshirts', 'list_of_tshirts', list_of_tshirts)