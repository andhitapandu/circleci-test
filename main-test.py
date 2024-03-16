# Import the Add function, and assert that it works correctly.
from main import Add

def CatchPokemon(ball_type, pokemon_level):
    # Assume a regular Pokéball has a catch rate of 1.
    # Higher-level Pokémon are harder to catch.
    catch_rate = ball_type * pokemon_level
    # Generate a random number between 1 and 100.
    import random
    random_number = random.randint(1, 100)
    if random_number <= catch_rate:
        print("You caught the Pokémon!")
    else:
        print("The Pokémon broke free!")

def TestCatchPokemon():
    # We can simulate catching a level 5 Pikachu with a Great Ball.
    # The catch rate would be 2 * 5 = 10%.
    CatchPokemon(ball_type=2, pokemon_level=5)

    # We can simulate catching a level 10 Charmander with a regular Pokéball.
    # The catch rate would be 1 * 10 = 10%.
    CatchPokemon(ball_type=1, pokemon_level=10)

    # We can simulate catching a level 50 Dragonite with an Ultra Ball.
    # The catch rate would be 3 * 50 = 150%.
    # However, let's assume there's a cap of 100%.
    CatchPokemon(ball_type=3, pokemon_level=50)
    
    # Let's simulate catching a level 20 Snorlax with a Master Ball.
    # The catch rate would be 6 * 20 = 120%.
    # Since it's a Master Ball, it has a guaranteed catch rate.
    CatchPokemon(ball_type=6, pokemon_level=20)

    print("CatchPokemon Function works correctly")

if __name__ == '__main__':
    TestCatchPokemon()
