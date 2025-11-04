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
      Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.

    - add_ingredient(recipe_name, ingredient):
      Aggiunge un ingrediente alla ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.

    - remove_ingredient(recipe_name, ingredient):
      Rimuove un ingrediente dalla ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

    - update_ingredient(recipe_name, old_ingredient, new_ingredient):
      Sostituisce un ingrediente con un altro nella ricetta specificata.
      Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.

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

    def __init__(self) -> None:
        self.ricettario: dict[str, list[str]] = {}

    def create_recipe(self, name: str, ingredients: list[str]) -> dict[str, list[str]] | str:
        '''
        Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
        Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
        '''
        if name not in self.ricettario:
            self.ricettario[name] = ingredients

            return {name: self.ricettario[name]}

        else:
            return "La ricetta esiste già"

    def add_ingredient(self, recipe_name: str, ingredient: str) -> list[str] | str:
        '''
        Aggiunge un ingrediente alla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
        '''
        if recipe_name in self.ricettario and ingredient not in self.ricettario[recipe_name]:
            self.ricettario[recipe_name].append(ingredient)

            return {recipe_name: self.ricettario[recipe_name]}

        else:
            return "L'ingrediente esiste già" if ingredient in self.ricettario[recipe_name] else "La ricette non esiste"

    def remove_ingredient(self, recipe_name: str, ingredient: str) -> list[str] | str:
        '''
        Rimuove un ingrediente dalla ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        '''
        if recipe_name in self.ricettario:
            lista_ingredienti: list[str] = self.ricettario[recipe_name]
            trovato_ingrediente: bool = False

            for ingrediente in lista_ingredienti:

                if ingrediente == ingredient:
                    lista_ingredienti.remove(ingrediente)
                    trovato_ingrediente = True

            if trovato_ingrediente:
                self.ricettario[recipe_name] = lista_ingredienti

                return {recipe_name: self.ricettario[recipe_name]}

            else:
                return "Ingrediente non trovato"

        else:
            return "Ricetta non trovata"

    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str) -> list[str] | str:
        '''
        Sostituisce un ingrediente con un altro nella ricetta specificata.
        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
        '''
        if recipe_name in self.ricettario:
            lista_ingredienti: list[str] = self.ricettario[recipe_name]
            trovato_ingrediente: bool = False

            for i, ingrediente in enumerate(lista_ingredienti):

                if ingrediente == old_ingredient:
                    lista_ingredienti[i] = new_ingredient
                    trovato_ingrediente = True

            if trovato_ingrediente:
                self.ricettario[recipe_name] = lista_ingredienti

                return {recipe_name: self.ricettario[recipe_name]}

            else:
                return "Ingrediente non trovato"

        else:
            return "Ricetta non trovata"

    def list_recipes(self) -> list[str]:
        '''
        Elenca tutte le ricette esistenti.
        '''
        return [r for r in self.ricettario]

    def list_ingredients(self, recipe_name: str) -> list[str] | str:
        '''
        Mostra gli ingredienti di una specifica ricetta.
        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
        '''
        if recipe_name in self.ricettario:
            return [i for i in self.ricettario[recipe_name]]

        else:
            return "La ricetta non esiste"

    def search_recipe_by_ingredient(self, ingredient) -> list[str] | str:
        '''
        Trova e restituisce tutte le ricette che contengono un determinato ingrediente.
        Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.
        '''
        trovato: bool = False
        for ricetta in self.ricettario.values():

            if ricetta in self.ricettario.values():
                trovato = True

        if trovato:
            elenco_di_ricette: dict[str, list[str]] = {}
            lista_di_ingredienti: list[str]

            for ricetta, ingredienti in self.ricettario.items():

                if ingredient in ingredienti:
                    elenco_di_ricette[ricetta] = ingredienti

            return elenco_di_ricette

        else:
            return "Nessuna ricetta contiene l'ingrediente"

if __name__ == "__main__":

    manager = RecipeManager()
    print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
    print(manager.add_ingredient("Pizza Margherita", "Basilico"))
    print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
    print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
    print(manager.list_ingredients("Pizza Margherita"))