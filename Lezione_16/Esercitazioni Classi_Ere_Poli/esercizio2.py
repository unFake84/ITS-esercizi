'''
Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di
creare, modificare, e cercare ricette basate sugli ingredienti.
Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.

Classe:
- RecipeManager:
    Gestisce tutte le operazioni legate alle ricette.

    Metodi:
    - create_recipe(name, ingredients):
      Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
      Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore
      se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient):
      Aggiunge un ingrediente alla ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se
      l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient):
      Rimuove un ingrediente dalla ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o
      la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient):
      Sostituisce un ingrediente con un altro nella ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o
      la ricetta non esiste.

    - list_recipes():
      Elenca tutte le ricette esistenti.

    - list_ingredients(recipe_name):
      Mostra gli ingredienti di una specifica ricetta.
      Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

    - search_recipe_by_ingredient(ingredient):
      Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
      Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

'''

class RecipeManager:
    '''Gestisce tutte le operazioni legate alle ricette'''

    collezione_di_ricette: dict[str, list[str]]

    def __init__(self, name: str|None = None, ingredients: list[str]|None = None) -> None:
        self.collezione_di_ricette = {}

        if name is not None and ingredients is not None:
            self.collezione_di_ricette = {
                name: ingredients
                }

    def create_recipe(self, name: str, ingredients: list[str]) -> None|str:
        '''
        Crea una nuova ricetta con il nome specificato e una lista di ingredienti.<br>
        Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore<br>
        se la ricetta esiste già.
        '''

        if name not in self.collezione_di_ricette:
            self.collezione_di_ricette[name] = ingredients
            
            return self.collezione_di_ricette

        else:
            raise ValueError("La ricetta esiste già")

    def add_ingredient(self, recipe_name: str, ingredient: str|list[str]) -> dict[str, list[str]]|str:
        '''
        Aggiunge un (o più) ingrediente alla ricetta specificata.<br>
        Restituisce la ricetta aggiornata o un messaggio di errore se<br>
        l'ingrediente esiste già o la ricetta non esiste.
        '''

        if recipe_name not in self.collezione_di_ricette:
            return "La ricetta non esiste"

        ingredienti_esistenti: list[str] = [i for i in self.collezione_di_ricette[recipe_name]]

        if isinstance(ingredient, str):
            if ingredient not in ingredienti_esistenti:

                ingredienti_esistenti.append(ingredient)
                self.collezione_di_ricette[recipe_name] = ingredienti_esistenti

                return self.collezione_di_ricette

        if isinstance(ingredient, list):
            for ingrediente_da_aggiungere in ingredient:

                if ingrediente_da_aggiungere not in ingredienti_esistenti:
                    ingredienti_esistenti.append(ingrediente_da_aggiungere)
                    self.collezione_di_ricette[recipe_name] = ingredienti_esistenti

                    return self.collezione_di_ricette

    def remove_ingredient(self, recipe_name: str, ingredient: str|list[str]) -> None:
        '''
        Rimuove un (o più) ingrediente dalla ricetta specificata.<br>
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o<br>
        la ricetta non esiste.
        '''

        if recipe_name not in self.collezione_di_ricette:
            return "La ricetta non esiste"

        lista_ingredienti: list[str] = [i for i in self.collezione_di_ricette[recipe_name]]

        if isinstance(ingredient, str):
            if ingredient in lista_ingredienti:
                lista_ingredienti.remove(ingredient)
                self.collezione_di_ricette[recipe_name] = lista_ingredienti
                
                return self.collezione_di_ricette

            else:
                return f"L' ingrediente {ingredient} non è presente nella ricetta {recipe_name}"

        if isinstance(ingredient, list):
            trovati: bool = False
            for ingrediente_da_rimuovere in ingredient:

                if ingrediente_da_rimuovere in lista_ingredienti:
                    trovati = True
                    lista_ingredienti.remove(ingrediente_da_rimuovere)
                    self.collezione_di_ricette[recipe_name] = lista_ingredienti

                    return self.collezine_di_ricette

            if not trovati:
                return f"Non sono stati trovati i seguenti ingredienti nella ricetta {recipe_name}:\n{', '.join(lista_ingredienti)}"

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> None|str:
        '''
        Sostituisce un ingrediente con un altro nella ricetta specificata.<br>
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o<br>
        la ricetta non esiste.
        '''

        if recipe_name not in self.collezione_di_ricette:
            return "La ricetta non esiste"

        lista_ingredienti: list[str] = [i for i in self.collezione_di_ricette[recipe_name]]
        trovato: bool = False

        for i, ingrediente_da_modificare in enumerate(lista_ingredienti):

            if old_ingredient == ingrediente_da_modificare:
                trovato = True
                lista_ingredienti[i] = new_ingredient
                self.collezione_di_ricette[recipe_name] = lista_ingredienti
                
                return self.collezione_di_ricette
        

        return f"Ingrediente {old_ingredient} non trovato"

    def list_recipes(self) -> list[str]:
        '''
        Elenca tutte le ricette esistenti.
        '''

        lista_di_ricette: list[str] = [r for r in self.collezione_di_ricette]
        return lista_di_ricette

    def list_ingredients(self, recipe_name: str) -> None|str:
        '''
        Mostra gli ingredienti di una specifica ricetta.<br>
        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
        '''

        if recipe_name not in self.collezione_di_ricette:
            return "La ricetta non esiste"

        lista_ingredienti: list[str] = [i for i in self.collezione_di_ricette[recipe_name]]
        return lista_ingredienti

    def search_recipe_by_ingredient(self, ingredient: str) -> str:
        '''
        Trova e restituisce tutte le ricette che contengono un determinato ingrediente.<br>
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
        '''

        for ricetta, ingredienti in self.collezione_di_ricette.items():

            for ingrediente in ingredienti:

                if ingredient == ingrediente:
                    return self.collezione_di_ricette

        return "Nessuna ricetta trovata"